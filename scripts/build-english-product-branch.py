#!/usr/bin/env python3
# kso:product-relevance
# repo-scope: product
# classification: product-release-automation
# decision: keep
# review-required-on-change: true
# criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness

"""Build a generated English krisensicherOS product branch.

This script exports product-scoped files, translates user-facing prose with the
configured OpenClaw model gateway, and creates a clean English branch such as
en/main.

The script intentionally does not store credentials. For pushes to protected
remotes, provide credentials through the surrounding Git environment, for example
an approved GIT_ASKPASS wrapper.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable, Iterator

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".txt"}
SKIP_TRANSLATION_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}
PRIVATE_PATTERNS = (
    "memory/",
    ".openclaw/",
    ".learnings/",
    "exports/",
    "projects/",
    ".git/",
)
PRIVATE_EXACT = {
    "TOOLS.md",
    "USER.md",
    "SOUL.md",
    "IDENTITY.md",
    "HEARTBEAT.md",
    "MEMORY.md",
    "CONSTRAINTS.yaml",
    "DREAMS.md",
}
UNSAFE_ENGLISH_CLAIMS = (
    "guaranteed compliant",
    "legal certainty",
    "certification-ready",
    "audit passed",
    "compliance guaranteed",
)


def run(cmd: list[str], cwd: Path | None = None, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=check,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


def extract_tag(text: str) -> str:
    idx = text.find("kso:product-relevance")
    if idx == -1:
        return ""
    before = text.rfind("<!--", 0, idx)
    after = text.find("-->", idx)
    if before != -1 and after != -1:
        return text[before : after + 3]
    lines = text[idx:].splitlines()
    tag_lines: list[str] = []
    for line in lines:
        if tag_lines and not line.strip():
            break
        tag_lines.append(line)
    return "\n".join(tag_lines)


def product_files(repo: Path) -> list[Path]:
    raw = run(["bash", "-lc", "{ git ls-files; git ls-files --others --exclude-standard; }"], cwd=repo, capture=True).stdout
    out: list[Path] = []
    for name in sorted(set(raw.splitlines())):
        if not name or name in PRIVATE_EXACT or any(name.startswith(p) for p in PRIVATE_PATTERNS):
            continue
        p = repo / name
        if not p.is_file():
            continue
        try:
            text = p.read_text(errors="ignore")
        except UnicodeDecodeError:
            continue
        tag = extract_tag(text)
        if "repo-scope: product" in tag:
            out.append(Path(name))
    return out


def load_glossary(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_metadata(text: str) -> tuple[str, str]:
    idx = text.find("kso:product-relevance")
    if idx == -1:
        return "", text
    before = text.rfind("<!--", 0, idx)
    after = text.find("-->", idx)
    if before != -1 and after != -1 and before < 50:
        return text[: after + 3], text[after + 3 :]
    if idx < 50:
        lines = text.splitlines(keepends=True)
        cut = 0
        for i, line in enumerate(lines):
            cut += len(line)
            if i > 0 and not line.strip():
                break
        return text[:cut].rstrip(), text[cut:]
    return "", text


def cache_key(path: Path, text: str, glossary: str) -> str:
    digest = hashlib.sha256()
    digest.update(path.as_posix().encode())
    digest.update(b"\0")
    digest.update(text.encode())
    digest.update(b"\0")
    digest.update(glossary.encode())
    return digest.hexdigest()


def translate_text(path: Path, text: str, glossary: str, model: str | None, dry_run: bool, cache_dir: Path | None, retries: int) -> str:
    if dry_run:
        return text
    cached = None
    if cache_dir:
        cache_dir.mkdir(parents=True, exist_ok=True)
        cached = cache_dir / f"{cache_key(path, text, glossary)}.txt"
        if cached.exists():
            return cached.read_text(encoding="utf-8")
    metadata, body = split_metadata(text)
    if not body.strip():
        return text
    prompt = f"""Translate this krisensicherOS product file from German to English.

Strict rules:
- Output only the translated file content, no commentary.
- Preserve Markdown structure, links, file paths, anchors, tables and code blocks.
- Preserve YAML keys, identifiers, file paths, agent IDs, workflow IDs and source URLs.
- Preserve the product relevance metadata exactly as provided if present.
- Apply the fixed glossary below consistently.
- Keep the tone clear, operational and concise.
- Do not create legal advice, data protection advice, compliance guarantees, certification claims or audit-passed claims.
- Keep fictional examples fictional and public-safe.

Fixed glossary:
```yaml
{glossary}
```

Path: {path.as_posix()}

File content:
```text
{text}
```
"""
    cmd = ["openclaw", "infer", "model", "run", "--gateway", "--json", "--prompt", prompt]
    if model:
        cmd[5:5] = ["--model", model]
    last_error = ""
    translated = ""
    for attempt in range(1, retries + 2):
        proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode == 0:
            try:
                payload = json.loads(proc.stdout)
                translated = payload["outputs"][0]["text"]
                break
            except Exception as exc:  # noqa: BLE001
                last_error = f"Could not parse translation output: {exc}; stdout={proc.stdout[:500]}"
        else:
            last_error = f"model command failed rc={proc.returncode}; stderr={proc.stderr[:700]}; stdout={proc.stdout[:500]}"
        if attempt <= retries:
            print(f"WARN: translation failed for {path} (attempt {attempt}/{retries + 1}); retrying", file=sys.stderr, flush=True)
            time.sleep(min(2 * attempt, 10))
    else:
        raise RuntimeError(f"Translation failed for {path}: {last_error}")
    if not translated:
        raise RuntimeError(f"Translation failed for {path}: {last_error}")
    translated = translated.strip() + "\n"
    if metadata and "kso:product-relevance" not in translated[:500]:
        translated = metadata.rstrip() + "\n" + translated
    if cache_dir:
        cached.write_text(translated, encoding="utf-8")
    return translated


def copy_or_translate(src: Path, dst: Path, rel: Path, glossary: str, model: str | None, dry_run: bool, cache_dir: Path | None, retries: int) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix.lower() in SKIP_TRANSLATION_SUFFIXES or src.suffix.lower() not in TEXT_SUFFIXES:
        shutil.copy2(src, dst)
        return
    text = src.read_text(encoding="utf-8", errors="ignore")
    translated = translate_text(rel, text, glossary, model, dry_run, cache_dir, retries)
    dst.write_text(translated, encoding="utf-8")


def scan_generated(root: Path) -> list[str]:
    findings: list[str] = []
    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        rel = p.relative_to(root).as_posix()
        if rel in PRIVATE_EXACT or any(rel.startswith(prefix) for prefix in PRIVATE_PATTERNS):
            findings.append(f"private file in generated branch: {rel}")
            continue
        text = p.read_text(errors="ignore")
        if "repo-scope: workrepo" in text[:600]:
            findings.append(f"workrepo-scoped file in generated branch: {rel}")
        if ("governance:" + "constraints:start") in text or ("Active Governance " + "Constraints") in text:
            findings.append(f"runtime marker in generated branch: {rel}")
        if rel not in {"scripts/build-english-product-branch.py", "i18n/en/glossary.yaml"}:
            for line_no, line in enumerate(text.splitlines(), 1):
                lowered = line.lower()
                anti_claim_context = any(marker in lowered for marker in (
                    "do not", "must not", "may not", "cannot", "avoid", "no ",
                    "not ", "without", "prohibit", "forbidden", "exclude",
                    "does not provide", "is not", "are not",
                ))
                for claim in UNSAFE_ENGLISH_CLAIMS:
                    if claim in lowered and not anti_claim_context:
                        findings.append(f"unsafe claim phrase '{claim}' in {rel}:{line_no}")
    return findings


@contextmanager
def output_workspace(path: str | None) -> Iterator[Path]:
    if path:
        out = Path(path).resolve()
        out.mkdir(parents=True, exist_ok=True)
        yield out
    else:
        with tempfile.TemporaryDirectory(prefix="kso-en-product-") as tmp:
            yield Path(tmp)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="source worktree")
    parser.add_argument("--glossary", default="i18n/en/glossary.yaml")
    parser.add_argument("--remote", default="https://git.kr.int/krisensicher/krisensicher-os.git")
    parser.add_argument("--branch", default="en/main")
    parser.add_argument("--message", default="Generate English product branch")
    parser.add_argument("--model", default=None, help="optional model override for openclaw infer model run")
    parser.add_argument("--dry-run", action="store_true", help="copy product files without model translation")
    parser.add_argument("--push", action="store_true", help="push generated branch to remote")
    parser.add_argument("--cache-dir", default=None, help="optional translation cache directory outside the product branch")
    parser.add_argument("--output-dir", default=None, help="keep generated branch worktree at this path for review/QS")
    parser.add_argument("--retries", type=int, default=2, help="model retries per file")
    args = parser.parse_args(list(argv) if argv is not None else None)

    repo = Path(args.repo).resolve()
    glossary_path = (repo / args.glossary).resolve() if not Path(args.glossary).is_absolute() else Path(args.glossary)
    glossary = load_glossary(glossary_path)
    cache_dir = Path(args.cache_dir).resolve() if args.cache_dir else None
    files = product_files(repo)
    if not files:
        raise SystemExit("No product-scoped files found")

    with output_workspace(args.output_dir) as out:
        if (out / ".git").exists():
            pass
        else:
            run(["git", "init", "-q"], cwd=out)
        if run(["git", "remote", "get-url", "origin"], cwd=out, check=False, capture=True).returncode != 0:
            run(["git", "remote", "add", "origin", args.remote], cwd=out)
        else:
            run(["git", "remote", "set-url", "origin", args.remote], cwd=out)
        run(["git", "fetch", "origin", args.branch], cwd=out, check=False)
        if run(["git", "show-ref", "--verify", "--quiet", f"refs/remotes/origin/{args.branch}"], cwd=out, check=False).returncode == 0:
            run(["git", "checkout", "-q", "-B", args.branch, f"origin/{args.branch}"], cwd=out)
        else:
            run(["git", "checkout", "-q", "--orphan", args.branch], cwd=out)
        for item in out.iterdir():
            if item.name != ".git":
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
        for rel in files:
            print(f"translate {rel.as_posix()}", flush=True)
            copy_or_translate(repo / rel, out / rel, rel, glossary, args.model, args.dry_run, cache_dir, args.retries)
        findings = scan_generated(out)
        if findings:
            print("\n".join(findings), file=sys.stderr)
            raise SystemExit("Generated branch safety scan failed")
        run(["git", "add", "-A"], cwd=out)
        run(["git", "-c", "user.name=AI Dev Bot", "-c", "user.email=ai_dev_bot@git.kr.int", "commit", "-m", args.message], cwd=out, check=False)
        commit = run(["git", "rev-parse", "--short", "HEAD"], cwd=out, capture=True).stdout.strip()
        print(f"generated_branch={args.branch}")
        print(f"generated_commit={commit}")
        if args.push:
            run(["git", "push", "origin", f"HEAD:{args.branch}"], cwd=out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
