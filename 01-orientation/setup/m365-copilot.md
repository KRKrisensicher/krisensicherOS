<!-- kso:product-relevance
repo-scope: product
classification: setup-guidance
decision: keep
review-required-on-change: true
criteria: public-safe; ai-assisted-governance; human-gate-aware; reusable-guidance; claim-safe
-->

# Setup: Microsoft 365 Copilot

Status: 2026-05-23

## Purpose

This setup is for organizations that work with Microsoft 365 and use Copilot with tenant-side administration.

Copilot is only suitable if permissions, Sensitivity Labels, DLP, SharePoint/OneDrive structures, and user approvals have been reviewed.

## Suitable for

- Word, Excel, PowerPoint, Teams, Outlook, and SharePoint work,
- management review notes,
- structuring governance documents,
- audit questions and action lists,
- organizations with existing M365 governance.

## Prerequisites

- Microsoft 365 Copilot license or approved Copilot variant,
- admin configuration in the Microsoft 365 Admin Center,
- responsible admin/owner role,
- reviewed SharePoint/Teams permissions,
- Sensitivity Labels and DLP rules,
- clear rule defining which krisensicherOS artifacts Copilot may process.

## Recommended SharePoint structure

```text
krisensicherOS/
├── 01 Orientation
├── 02 Compliance Register
├── 03 Audit and Evidence
├── 04 Management Review
├── 05 Dokumente in Arbeit
├── 06 Review and Approval
└── 99 Archiv
```

## Step by step

1. Check tenant and license approval.
2. Clean up permissions: no unnecessarily broad SharePoint/Teams access.
3. Check Sensitivity Labels and DLP rules.
4. Create krisensicherOS working library.
5. Upload only approved artifacts.
6. Document working rule:

```text
Copilot may summarize krisensicherOS artifacts, derive questions, and prepare drafts.
Copilot must not provide legal advice, data protection assessment, risk acceptance, or management decisions.
Confidential sources and licensed standards are used only as metadata or internal summaries.
```

## Example prompt for Word

```text
Create a structured governance document draft from these notes.

Use this structure:
1. Purpose
2. Scope and non-scope
3. Roles
4. Process / routine
5. Evidence
6. Review
7. Boundaries
8. Open decisions

Mark assumptions and gaps. Do not provide legal advice or compliance assurance.
```

## Example prompt for Teams

```text
Summarize this meeting as a governance review note.

Output:
- Decisions
- Open questions
- Risks
- Actions with owner and deadline
- Required evidence
- Items for management review

Mark where human approval is required.
```

## Tenant, role, and scenario check

Clarify before an M365 Copilot pilot:

| Check field | Minimum clarification |
| --- | --- |
| Activation | Is Copilot activated tenant-wide or group-based? |
| Scenarios | Which apps/scenarios are approved: Word, Excel, Teams, Outlook, SharePoint? |
| Pilot group | Which user groups may use Copilot for krisensicherOS? |
| Admin roles | AI Administrator, SharePoint Admin, Compliance Admin, Security Admin, or equivalent roles involved? |
| Business owner | Who has business responsibility for the krisensicherOS working library? |
| Human Gate | IT system owner, CISO/information security officer, and for sensitive data legal/data protection approve. |

## Check data access before Copilot pilot

Copilot amplifies existing permissions. Before upload or prompting, check:

- no unreviewed confidential areas within Copilot reach,
- no broad default groups such as “Everyone except external users” on governance/evidence libraries,
- check guest access and external sharing,
- clean up inherited permissions and old Teams/libraries,
- do not use OneDrive sharing and personal storage as governance storage,
- use a separate library for approved krisensicherOS artifacts,
- no production incident, customer, HR, or contract data in the pilot without explicit approval.

## Data class and upload gate

Before uploading to SharePoint, the [`../../templates/ki-nutzungsfreigabe-matrix.md`](../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md) or an equivalent internal rule must be clarified for each artifact or artifact group.

Stop/Human Gate for:

- personal data,
- secrets,
- confidential customer or contract data,
- licensed standard texts,
- unclear data class,
- unclear permission situation.

M365-specific additional questions before upload:

| Check field | Minimum clarification |
| --- | --- |
| Storage location | Which SharePoint site, library, or Teams structure is used? |
| Guests / external sharing | Have guests and external links been reviewed or disabled? |
| Broad groups | Are groups such as “Everyone except external users” excluded? |
| Copilot/Graph reach | Which content can Copilot find through permissions? |
| Retention / Audit Logging | Have retention and audit logging for the pilot been clarified? |

## DLP/Sensitivity minimum evidence

Document before the pilot:

| Evidence | Minimum content |
| --- | --- |
| Label configuration | Which Sensitivity Label applies to the working library or artifact group? |
| Policy Scope | Does the DLP/compliance policy apply to SharePoint, Teams, and OneDrive in the pilot scope? |
| Mode | Block, warn, or audit mode clarified? |
| Evidence location | Screenshot, export, or admin note stored in the review folder `06 Review and Approval`? |
| Owner approval | IT system owner and business owner confirmed the review in the decision log? |

## Human Gates in the M365 path

| Point in time | Gate |
| --- | --- |
| Before upload | Data class, owner, and permitted AI environment checked |
| Before Copilot use | Permissions, Sensitivity Labels, and DLP checked |
| Before internal sharing | Output reviewed by the responsible business role |
| Before management decision | Responsible role decides, not Copilot |
| Before external use | Explicit approval documented |

## Practical Windows/Office workflow

1. Have the owner create the SharePoint site or library.
2. Set owner group and editor group separately.
3. Check inherited permissions, external sharing, and broad groups.
4. Apply Sensitivity Label and document DLP/policy scope.
5. Upload only approved starting artifacts.
6. Upload a non-confidential test file.
7. Test the pilot in Word or Teams with an example prompt.
8. Store the result in `06 Review and Approval`.
9. Transfer decision, assumption, gap, or handoff to [`../../templates/decision-log.md`](../../02-governance-operating-model/templates/decision-log.md) or a review note.
