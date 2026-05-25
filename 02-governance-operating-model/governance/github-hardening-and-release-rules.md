<!-- kso:product-relevance
repo-scope: product
classification: product-governance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; release-readiness; security-gate
-->

# GitHub hardening and release rules

This document describes the technical minimum rules for the public GitHub repository of krisensicherOS.

## Branches

- `de/main` is the default branch.
- `en/main` is the maintained English language branch.
- `main` is not used and must not be recreated.

## Protection rules

GitHub Branch Protection or Rulesets should be active for `de/main` and `en/main`:

- Force pushes prohibited.
- Branch deletion prohibited.
- Pull request or explicit human review before merge.
- Required status check: `quality-check`.
- Administrators should not routinely bypass protection rules.

## Quality gate

Before publication or merge, at least the following must run:

- GitHub Actions workflow `krisensicherOS quality gate`,
- `git diff --check`,
- runtime/session marker check,
- secret and unsafe compliance/certification claim checks.

## Identity and push paths

- Pushes to `git.kr.int` are performed exclusively with the AI Dev Bot.
- Pushes to GitHub are performed exclusively with the GitHub token of `KRKerstan`.
- Commits should be visible as `Rico Kerstan` / `KRKerstan`, not as a GitLab, runtime, or KI-Kumpel identity.

## Security features

GitHub Security Features should be enabled where the plan and permissions allow:

- Dependabot Alerts,
- Dependabot Security Updates,
- Secret Scanning,
- Code Scanning only lightweight and appropriate for the primarily Markdown/YAML-based repository.

## Boundaries

These rules do not replace professional review. Legal interpretation, data protection assessment, risk acceptance, external communication, and publication remain human gates.
