# A.8.28 — Secure programming

## Purpose

Secure programming ensures that code, configurations, scripts and automations do not systematically create avoidable vulnerabilities. It is not about perfect freedom from errors, but about a robust routine for secure patterns, reviews, tool signals, developer enablement and handling of findings.

The core is: teams know which error classes are relevant for their technologies, what secure implementation looks like, which checks apply before merge or release and how deviations are decided.

## Control objective in repository language

The organization operates a secure coding routine that connects development guidelines, code reviews, automated checks, dependency and secret checks, secure framework use, developer enablement and finding treatment. Security-relevant code decisions become traceable, testable and improvable.

## Typical risks

- If developers do not know secure patterns, recurring errors arise in inputs, outputs, authentication, authorization, sessions, error handling or cryptography.
- If code reviews check only functionality, security-relevant logic errors remain undiscovered.
- If secrets, tokens or credentials end up in repositories, systems and data can be compromised.
- If dependencies are included without review, vulnerable or unmaintainable components arise.
- If security tools produce many findings but nobody triages them, critical signals are ignored.
- If AI-supported code is adopted without review, insecure patterns, license or quality problems can enter products.

## Triggers

- new code, merge request, pull request, release or hotfix.
- new library, framework, container image, build tool or code generator.
- security finding from SAST, DAST, SCA, secret scan, code review, test or incident.
- new error class, vulnerability notification or recurring finding pattern.
- onboarding of new developers, external development team or technology change.
- change to authentication, authorizations, input validation, cryptography, logging or data access.
- review of coding guidelines and tool gates.

## Roles and responsibilities

- **Development team:** implements secure patterns, performs peer reviews and handles findings.
- **Tech Lead:** responsible for coding standards, review quality, technical decisions and training needs in the team.
- **Security/AppSec role:** defines security-relevant review areas, supports triage and improves guidelines.
- **Product Owner:** prioritizes security work in the backlog and decides business impacts.
- **DevOps/platform team:** operates build, scan, secret and dependency checks in the pipeline.
- **ISMS Owner:** connects coding findings with risk register, actions and management review.
- **Procurement / Supplier management:** includes external development and delivery evidence.
- **Management:** decides on resource shortages, tooling, recurring critical debt or accepted residual risks.

## Implementation

### Minimum start

Objective: the most common avoidable code and repository risks become visible and are handled.

1. Owners and responsible teams are named for active repositories.
2. A short secure coding checklist is created for the technologies used.
3. Changes to security-relevant functions require peer review.
4. Secret scanning and dependency checking are introduced at least for critical repositories.
5. Critical findings are recorded as tickets with owner, priority, deadline and decision.
6. Developers receive short, practical guidance on recurring errors.

Minimum evidence:

- repository list with owners,
- coding checklist or team standard,
- pull/merge request reviews,
- scan or review evidence,
- finding tickets with treatment,
- exception decision for open critical findings.

### Solid practice

Objective: secure programming becomes part of the daily development flow.

1. Coding guidelines are technology-specific and contain secure examples for relevant error classes.
2. Review criteria consider input validation, authorization logic, error handling, logging, secrets, dependencies and secure framework use.
3. SAST, SCA, secret scanning and selected linter signals run in the pipeline with defined triage.
4. Tool findings are assessed by risk, exploitability, code path and asset criticality.
5. Critical or recurring findings lead to pairing, training, pattern change or architecture handoff.
6. External developers use the same minimum standards and provide appropriate evidence.
7. AI-supported code suggestions are reviewed and tested like other code and are not adopted without review.

Strong evidence:

- technology-specific coding guidelines,
- review checklists and pull/merge request history,
- pipeline scan results with triage,
- finding backlog with owner, deadline and status,
- evidence of remediated secrets or vulnerable dependencies,
- training or team learning evidence,
- supplier evidence for external development.

### Advanced practice

Objective: coding security is measurably improved and embedded in platforms.

1. Secure templates, framework configurations and internal libraries reduce insecure individual decisions.
2. Pipeline gates are risk-based: critical findings block, lower findings are steered instead of blindly blocking.
3. Findings are analyzed by cause: knowledge gap, insecure framework pattern, missing platform function, architecture problem or time pressure.
4. Security Champions or comparable roles support teams directly in everyday development.
5. Relevant metrics show repeated errors, remediation times, false-positive burden and critical technical debt.
6. Coding lessons learned from incidents and tests change guidelines, templates and training.

## Routine flow

1. **Code change arises:** feature, bugfix, infrastructure code, script, automation or hotfix.
2. **Check security relevance:** does the change affect data access, roles, inputs, secrets, cryptography, logging, interfaces or dependencies?
3. **Apply secure patterns:** use team standard, framework functions and reviewed building blocks.
4. **Run checks:** perform peer review, automated scans and relevant tests.
5. **Triage findings:** distinguish real risks, false positives and technical debt.
6. **Treat:** change code, update dependency, rotate secret, add test or define compensation.
7. **Decide:** accept, block or escalate open critical findings before merge or release.
8. **Learn:** feed recurring patterns back into guidelines, templates, training or architecture.

## Decisions

- Which repositories and code types are critical for the start?
- Which findings block merge or release?
- Who may accept a deviation and for how long?
- Which tool signals are used, which create too much noise?
- Which recurring errors need training, template or architecture change?
- How is AI-supported code reviewed and documented?

## Evidence

### Strong evidence

- repository and owner overview,
- secure coding guidelines with technology reference,
- pull/merge request reviews with security comments,
- scan results with traceable triage,
- tickets for remediated findings,
- secret rotation or dependency update evidence,
- exception decisions with expiry date,
- evidence of team learnings or guideline updates.

### Weak evidence

- general secure-coding PDF without use in the team,
- tool dashboard without triage or remediation,
- code review as pure formal approval,
- long finding list without prioritization,
- statement “framework prevents this” without review evidence,
- training participation without relation to recurring errors.

### Evidence gaps

- active repositories without owner,
- critical findings without ticket or decision,
- secrets in the repository without rotation evidence,
- external development without review or scan evidence,
- no treatment of recurring error classes,
- AI-generated code without review and test trail.

## Effectiveness review

Review questions:

- Do critical repositories have owners, review obligations and appropriate checks?
- Are security-relevant code changes reviewed before merge or release?
- Are tool findings triaged and treated on a risk basis?
- Is repetition of known error classes decreasing?
- Are secrets and vulnerable dependencies treated quickly?
- Are external and AI-supported code contributions included in a controlled way?

Possible metrics:

- share of critical repositories with active checks,
- open critical code or dependency findings,
- mean remediation time by criticality,
- false-positive rate of relevant tools,
- recurring error classes per team,
- findings without owner or deadline,
- blocked releases due to critical coding findings.

## BSIG/NIS2 connection point

Secure programming is a connection point for NIS2-oriented topics such as secure development, vulnerability treatment, cyber hygiene, risk management, supply chain security and protection of digital services. The concrete relationship should be assessed in an organization-specific way through requirements registers, development processes and risk decisions.

This artifact does not replace legal assessment, data protection review or a security guarantee.

## Boundaries

- This artifact is not a complete secure-coding handbook for all programming languages.
- It does not replace code review, security testing or architecture review in individual cases.
- It does not guarantee error-free or secure software.
- It contains no ISO 27002 texts and no confidential code examples.
- It makes no legal, license or data protection assessment of concrete code.

## Handoffs

- **SDLC handoff:** coding standards must be included in development process, Definition of Done and release gates.
- **Architecture handoff:** recurring code errors that arise from design or platform boundaries.
- **Security testing handoff:** critical code areas, authentication, authorizations, inputs or interfaces need targeted tests.
- **Incident handoff:** secret leak, active exploitation, suspected compromise or critical vulnerable dependency.
- **Supplier handoff:** external development, third-party repositories, non-reviewable components or missing scan evidence.
- **Data protection/legal handoff:** code affects personal logging, tracking, data exports, licenses or contractual commitments.
- **Management handoff:** tooling, resources, recurring critical debt or accepted release risks.

## Typical mistakes

- Secure coding is treated as one-off training instead of as a review and improvement routine.
- Tools are introduced, but findings are not owned.
- Code reviews check style, but not security logic.
- Secrets are removed but not rotated.
- Dependency updates are applied without test and operations coordination or are permanently deferred.
- External development delivers code without shared minimum standards.
- AI code is adopted because it looks plausible, but was not reviewed.

## Fictional mini example

A fictional development team maintains an API for partner access. In a merge request, the secret scan detects an accidentally committed test token. The merge is stopped, the token is rotated, the repository is checked and a ticket is created to improve the local developer environment. In addition, the Tech Lead adds API tokens and logging of sensitive values to the team checklist. The next review checks whether similar findings occur again.

Evidence:

- merge request with blocked secret finding,
- rotation evidence for the token,
- ticket for environment improvement,
- updated coding checklist,
- review note on recurrence check.
