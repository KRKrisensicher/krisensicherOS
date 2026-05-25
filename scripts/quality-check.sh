#!/usr/bin/env bash
# kso:product-relevance
# repo-scope: product
# classification: product-quality-gate
# decision: keep
# review-required-on-change: true
# criteria: public-safe; ai-assisted-governance; human-gate-aware; product-safety; release-readiness

set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

fail=0
section() { printf '\n== %s ==\n' "$1"; }

ALL_FILES_TMP="$(mktemp)"
PRODUCT_FILES_TMP="$(mktemp)"
trap 'rm -f "$ALL_FILES_TMP" "$PRODUCT_FILES_TMP"' EXIT

build_file_sets() {
  python3 - "$ALL_FILES_TMP" "$PRODUCT_FILES_TMP" <<'PY'
from pathlib import Path
import subprocess, sys
all_out = Path(sys.argv[1])
product_out = Path(sys.argv[2])
def extract_tag(text: str) -> str:
    idx = text.find('kso:product-relevance')
    if idx == -1:
        return ''
    before = text.rfind('<!--', 0, idx)
    after = text.find('-->', idx)
    if before != -1 and after != -1:
        return text[before:after+3]
    lines = text[idx:].splitlines()
    tag_lines = []
    for line in lines:
        if tag_lines and not line.strip():
            break
        tag_lines.append(line)
    return '\n'.join(tag_lines)
cmd = "{ git ls-files; git ls-files --others --exclude-standard; } | grep -vE '^(memory/|\\.openclaw/|\\.learnings/|exports/|projects/|\\.git/|tmp_)'"
files = []
for name in subprocess.check_output(['bash','-lc', cmd], text=True).splitlines():
    p = Path(name)
    if p.is_file():
        files.append(name)
all_out.write_text('\n'.join(sorted(set(files))) + ('\n' if files else ''))
product = []
for name in sorted(set(files)):
    tag = extract_tag(Path(name).read_text(errors='ignore'))
    if 'repo-scope: product' in tag:
        product.append(name)
product_out.write_text('\n'.join(product) + ('\n' if product else ''))
PY
}

build_file_sets

all_files() { cat "$ALL_FILES_TMP"; }
product_files() { cat "$PRODUCT_FILES_TMP"; }

section "Whitespace / patch"
git diff --check
echo "ok: git diff --check"

section "Private/runtime files in tracked/unignored set"
private_present=$(
  all_files | grep -E '^(memory/|\.openclaw/|\.learnings/|projects/|exports/|TOOLS\.md$|USER\.md$|SOUL\.md$|IDENTITY\.md$|HEARTBEAT\.md$|MEMORY\.md$|CONSTRAINTS\.yaml$|DREAMS\.md$)' || true
)
if [ -n "$private_present" ]; then
  echo "$private_present"
  echo "FAIL: private/runtime files are tracked or unignored"
  fail=1
else
  echo "ok: no private runtime files in tracked/unignored set"
fi

section "Product relevance tags"
tag_errors=$(python3 - "$ALL_FILES_TMP" <<'PY'
from pathlib import Path
import sys
files = Path(sys.argv[1]).read_text().splitlines()
def extract_tag(text: str) -> str:
    idx = text.find('kso:product-relevance')
    if idx == -1:
        return ''
    before = text.rfind('<!--', 0, idx)
    after = text.find('-->', idx)
    if before != -1 and after != -1:
        return text[before:after+3]
    lines = text[idx:].splitlines()
    tag_lines = []
    for line in lines:
        if tag_lines and not line.strip():
            break
        tag_lines.append(line)
    return '\n'.join(tag_lines)
errors = []
for name in files:
    p = Path(name)
    text = p.read_text(errors='ignore')
    tag = extract_tag(text)
    if not tag:
        errors.append(f'{name}: missing kso:product-relevance tag')
        continue
    common = ['classification:', 'decision:', 'review-required-on-change: true', 'criteria:']
    for field in common:
        if field not in tag:
            errors.append(f'{name}: missing tag field {field}')
    has_product = 'repo-scope: product' in tag
    has_workrepo = 'repo-scope: workrepo' in tag
    if has_product == has_workrepo:
        errors.append(f'{name}: tag must contain exactly one repo-scope: product|workrepo')
    if has_product and 'decision: keep' not in tag:
        errors.append(f'{name}: product file must use decision: keep')
    if has_workrepo and not any(x in tag for x in ['decision: move-to-workrepo', 'decision: keep-in-workrepo']):
        errors.append(f'{name}: workrepo file must use decision: move-to-workrepo or keep-in-workrepo')
print('\n'.join(errors))
PY
)
if [ -n "$tag_errors" ]; then
  echo "$tag_errors"
  echo "FAIL: product relevance tagging incomplete"
  fail=1
else
  echo "ok: all tracked/unignored files carry valid product relevance tags"
fi

section "Internal work artefacts scoped to workrepo"
internal_errors=$(python3 - "$ALL_FILES_TMP" <<'PY'
from pathlib import Path
import sys
files = Path(sys.argv[1]).read_text().splitlines()
prefixes = ('agent-vault-source/','docs/briefings/','docs/changes/','docs/personas/','docs/reviews/','docs/roadmap/','docs/release/','tasks/')
exact = {
 'agents/agent-team-operating-model.md','agents/agentic-governance-delivery-architect.md','agents/ciso-workload-anthropologist.md',
 'agents/krisensicher-os-lead.md','agents/nis2-isms-domain-architect.md','agents/positioning-and-goto-market-lead.md',
 'agents/security-governance-architect.md','agents/source-map.md','docs/arbeitsmodus-repo-erstellung-v0.1.md',
 'docs/autonome-repo-erstellung-planungsplan-v0.1.md','docs/autonome-repo-erstellung-v1.0-plan.md',
 'docs/autonome-umsetzung-v1.0-detailplan.md','docs/repo-konzeption-v0.1.md','docs/repo-struktur-agenten-best-practices-2026-05-23.md',
 'docs/setup/no-ai-pfad.md','docs/standards/agent-profile-standard-v0.2.md','scripts/push-product-main-to-internal.sh'
}
errors=[]
count=0
for name in files:
    if name in exact or name.startswith(prefixes):
        count += 1
        text = Path(name).read_text(errors='ignore')
        idx = text.find('kso:product-relevance')
        tag = text[idx:text.find('\n\n', idx) if idx != -1 and text.find('\n\n', idx) != -1 else idx+400] if idx != -1 else ''
        if 'repo-scope: workrepo' not in tag:
            errors.append(f'{name}: internal artefact must be repo-scope: workrepo')
print('\n'.join(errors) if errors else f'ok: {count} internal artefacts are workrepo-scoped')
PY
)
if echo "$internal_errors" | grep -q '^ok:'; then
  echo "$internal_errors"
else
  echo "$internal_errors"
  echo "FAIL: internal artefact scope mismatch"
  fail=1
fi

section "Runtime-injected constraint markers in product files"
constraint_hits=$(product_files | grep -v '^scripts/quality-check\.sh$' | xargs -r grep -InE '(governance:constraints:start|Active Governance Constraints|Injected at:|OpenClaw runtime context|sourceSession=agent:)' || true)
if [ -n "$constraint_hits" ]; then
  echo "$constraint_hits"
  echo "FAIL: runtime/session markers found in product-scoped files"
  fail=1
else
  echo "ok: no runtime/session markers in product-scoped files"
fi

section "Secret indicators"
secret_hits=$(all_files | xargs -r grep -InE '(BEGIN (RSA|OPENSSH|EC|DSA|PRIVATE) KEY|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{30,}|glpat-[A-Za-z0-9_-]{20,}|xox[baprs]-|api[_-]?key\s*[:=]|secret\s*[:=]|password\s*[:=]|token\s*[:=])' || true)
if [ -n "$secret_hits" ]; then
  echo "$secret_hits"
  echo "FAIL: possible secret indicators found"
  fail=1
else
  echo "ok: no obvious secret indicators"
fi

section "No-AI product-path indicators"
no_ai_hits=$(product_files | grep -v '^scripts/quality-check\.sh$' | xargs -r grep -InE '(No-AI|no-ai-pfad|auch ohne KI|KI ist optional|kein Pflichtbestandteil|ohne KI-Freigabe nutzbar)' || true)
if [ -n "$no_ai_hits" ]; then
  echo "$no_ai_hits"
  echo "FAIL: No-AI fallback/product-path indicators found in product-scoped files"
  fail=1
else
  echo "ok: no No-AI fallback/product-path indicators in product-scoped files"
fi

section "Normtext / confidentiality indicators in product files"
norm_hits=$(product_files | xargs -r grep -InE '(Annex A|Anhang A|ISO/IEC 27001.*shall|ISO/IEC 27002.*shall|Normtext|gekaufte PDF|Kundendaten|vertraulich[eern]* Vertragsinhalt)' || true)
if [ -n "$norm_hits" ]; then
  echo "$norm_hits"
  echo "WARN: review norm/confidentiality indicators manually"
else
  echo "ok: no obvious normtext/confidentiality indicators"
fi

section "Claim-safety indicators in product files"
claim_hits=$(product_files | xargs -r grep -InE '(rechtssicher|garantiert konform|zertifizierungsfähig|Audit bestanden|NIS2-konform|ISO[- ]?27001[- ]?konform|Compliance garantiert)' || true)
if [ -n "$claim_hits" ]; then
  echo "$claim_hits"
  echo "WARN: claim indicators found; review whether they are prohibited examples/anti-claims or unsafe promises"
else
  echo "ok: no unsafe claim indicators"
fi

section "YAML syntax"
python3 - <<'PY'
from pathlib import Path
import subprocess, sys
try:
    import yaml
except Exception as exc:
    print(f"WARN: PyYAML unavailable: {exc}")
    sys.exit(0)
cmd = "{ git ls-files '*.yaml'; git ls-files --others --exclude-standard '*.yaml'; }"
for name in sorted(set(subprocess.check_output(['bash','-lc', cmd], text=True).splitlines())):
    p = Path(name)
    if not p.exists():
        continue
    if any(part in {'.git','memory','.openclaw','.learnings','exports','projects'} for part in p.parts):
        continue
    with p.open() as f:
        yaml.safe_load(f)
    print(f"yaml_ok {p}")
PY

section "Markdown local links in product files"
python3 - "$PRODUCT_FILES_TMP" <<'PY'
from pathlib import Path
import re, sys
files = Path(sys.argv[1]).read_text().splitlines()
missing = []
link_re = re.compile(r'(?<!\\)!?\[[^\]]*\]\(([^)]+)\)')
root = Path('.').resolve()
for name in files:
    p = Path(name)
    if p.suffix.lower() != '.md' or not p.exists():
        continue
    text = p.read_text(errors='ignore')
    for raw in link_re.findall(text):
        target = raw.split()[0].strip('<>')
        if not target or re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('mailto:') or target.startswith('#'):
            continue
        target_path = target.split('#',1)[0]
        if not target_path:
            continue
        resolved = (p.parent / target_path).resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            continue
        if not resolved.exists():
            missing.append(f"{p}: missing link target {target}")
if missing:
    print('\n'.join(missing))
    sys.exit(1)
print('ok: local markdown links resolve')
PY

section "Required product artefacts"
for path in \
  README.md LICENSE SECURITY.md CONTRIBUTING.md CHANGELOG.md AGENTS.md CLAUDE.md \
  docs/README.md docs/getting-started/minimaler-nis2-start-in-5-artefakten.md \
  docs/getting-started/30-60-90-minuten-nutzungspfad.md \
  docs/product/was-wir-bewusst-nicht-bauen.md \
  docs/setup/README.md templates/ki-nutzungsfreigabe-matrix.md \
  governance/product-relevance-process.md \
  agents/public/role-model.md agents/manifest.yaml \
  governance/disclaimer.md governance/quality-rules.md governance/review-process.md; do
  if [ ! -e "$path" ]; then
    echo "FAIL: missing $path"
    fail=1
  else
    echo "exists $path"
  fi
done

exit "$fail"
