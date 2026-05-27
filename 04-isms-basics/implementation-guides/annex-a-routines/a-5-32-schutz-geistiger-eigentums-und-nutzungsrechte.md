# A.5.32 — Protection of intellectual property and usage rights

## Purpose

This routine ensures that intellectual property, licensed content, software, source code, brands, templates, training material, databases, and contractually governed usage rights are not accidentally infringed, lost, used without authorization, or passed on unclearly.

The core is not a detailed legal review by the ISMS, but robust operating logic: Which rights and restrictions are known, who may use what, where does evidence arise, and when are Legal, Procurement, or Management decisions needed?

## Control objective in repository language

The organization operates a traceable routine through which relevant protection and usage rights are identified, documented, communicated, considered in procurement and operations, and reviewed when changes occur. Uncertain legal questions are not decided by Security, but handed over to responsible human roles.

## Typical risks

- If licensed software, content, or data is used without clear usage rights, contract breaches, costs, shutdowns, or reputational damage can arise.
- If internally developed work, concepts, or templates are shared without protection and publication logic, valuable know-how can flow out uncontrolled.
- If open-source components enter products without license and origin checks, legal, supply-chain, and maintenance risks arise.
- If service providers deliver work products, source code, or documentation without clear rights rules, it remains unclear who may change, pass on, or operate them.
- If employees use third-party materials in presentations, training, marketing, or AI workflows, usage limits can be overlooked.

## Triggers

- new product, new service, new software, new data source, or new content asset.
- procurement, renewal, or termination of software, data, media, or consulting contracts.
- use of open source, third-party libraries, templates, images, training material, or external knowledge sources.
- publication, customer handover, repository release, or external communication.
- security event, source-code leakage, unclear data sharing, or supplier change.
- audit finding, customer question, license review, or internal legal/procurement request.
- planned review of critical assets, software inventory, or supplier deliverables.

## Roles and responsibilities

- **Asset Owner / Product Owner:** knows purpose, protection need, and usage context of the affected asset.
- **Procurement / Vendor Management:** tracks contracts, license models, usage scope, and renewals.
- **Legal:** assesses rights, licenses, publications, contract clauses, and disputed interpretations.
- **IT / Platform Owner:** maintains software and tool inventory, technical use, and access.
- **Development / Engineering:** checks open-source, dependency, and code origin in the development process.
- **Marketing / Communications / Training:** uses content only with clarified origin, approval, and usage boundary.
- **ISMS owner:** ensures minimum logic, evidence capability, risk linkage, and handoffs.
- **Management:** decides in cases of high residual risk, resource need, disputes, or strategic publications.

## Implementation

### Minimum start

Goal: make critical rights and usage limits visible.

1. The most important categories are named: software, source code, documents, designs, data, training material, brands, external content.
2. An owner is defined for critical assets.
3. Procurement or use of new external content follows a simple check: origin, purpose, usage scope, storage location, approval.
4. Publications and customer handovers receive a Legal/Owner check when rights or confidentiality are unclear.
5. Open-source and third-party components are recorded traceably at least in a list or development tool.
6. Unclear cases are stopped until Legal, Procurement, or Management has decided.

Minimum evidence:

- list of critical assets and software with owner,
- license or contract reference,
- approval for use or publication,
- dependency/open-source list for relevant products,
- documented clarification for exceptions or uncertainty.

### Solid practice

Goal: rights clarification becomes part of procurement, development, content creation, and handovers.

1. Usage rights are maintained in the asset, software, or contract register with owner, scope, term, and restrictions.
2. Procurement, development, and publication processes contain clear checkpoints.
3. Open-source components are assessed by license type, origin, maintenance status, and product relation.
4. Service provider contracts clarify rights to work products, source code, documentation, configurations, and reuse.
5. Training or a short guide explains which third-party content must not simply be reused.
6. Deviations, unclear rights, or missing evidence are tracked as a risk or action.
7. Critical inventories are reviewed regularly, for example at contract renewal or product release.

Strong evidence:

- rights/license register with owners,
- procurement or contract checklists,
- open-source and dependency analyses,
- approvals before publication or customer handover,
- documented clarifications with Legal/Procurement,
- action log for unclear or expired rights.

### Advanced practice

Goal: rights and usage protection is integrated into tooling, product governance, and governance.

1. Software inventory, contract register, SBOM/dependency tools, and release process are connected.
2. License or origin risks create tickets, blocks, or mandatory reviews before productive use.
3. Critical internal assets are classified and connected with access, confidentiality, and publication rules.
4. Use of AI tools, external knowledge sources, and content platforms is governed through data class, rights, and approval paths.
5. Metrics show unclear rights, overdue license reviews, unassignable software, and open third-party component risks.
6. Management decides on strategic publications, open-source releases, or accepted residual risks.

## Routine flow

1. **New or changed asset arises:** software, content, code, data source, template, service provider deliverable, or publication.
2. **Determine owner:** clarify professional responsibility and usage context.
3. **Record origin and rights:** document source, contract, license, purpose of use, term, and restrictions.
4. **Assess risk:** classify confidentiality, sharing, product relation, customer impact, and legal uncertainty.
5. **Approve or escalate:** confirm normal use, set restrictions, or involve Legal/Procurement/Management.
6. **Implement technically and organizationally:** storage, access, labeling, dependency management, contract reference, or publication approval.
7. **Store evidence:** decision, source, scope, and review date remain traceable.
8. **Conduct review:** at release, contract change, supplier change, audit finding, or planned interval.

## Decisions

- Which asset categories are critical enough for the start?
- Which uses need Legal, Procurement, or Management approval?
- Which open-source license types, content sources, or platforms are allowed, restricted, or prohibited?
- How is unclear origin, missing contracts, or expired licenses handled?
- Which internal materials may be published externally, shared, or processed in AI tools?
- Who accepts residual risks if clarification is not possible in time?

## Evidence

### Strong evidence

- current software, asset, or rights inventory with owner,
- contract or license references with usage scope,
- approval records for releases, publications, or customer handovers,
- open-source/dependency list with assessment,
- evidence of removed, replaced, or clarified components,
- documented exceptions with term, risk, and follow-up date,
- management decision for strategic publication or accepted residual risk.

### Weak evidence

- general copyright policy without operational checks,
- software list without license or owner relation,
- screenshots from tools without assessment,
- blanket statement “Legal checks when needed” without trigger,
- outdated contract repository without relation to actually used assets.

### Evidence gaps

- external content without evidence of origin,
- product dependencies without license or maintenance status,
- service provider work products without rights clarification,
- publications without approval,
- expired or exceeded license use without decision,
- use of sensitive internal content in AI or cloud tools without approval.

## Effectiveness review

Review questions:

- Can it be traced for critical software, content, and work products who may use them and why?
- Are open-source and third-party components visible and assessed before release?
- Are publications, customer handovers, and AI uses stopped or escalated when rights are unclear?
- Are contracts, licenses, and actual use connected with each other?
- Do findings lead to corrections, replacement, license adjustment, or management decision?
- Do relevant roles understand when Legal or Procurement must be involved?

Possible metrics:

- share of critical assets with owner and rights reference,
- open unclear license or origin cases,
- releases with dependency/license check,
- overdue contract or license reviews,
- exceptions with expired follow-up date,
- unassignable software installations.

## BSIG/NIS2 connection point

The protection of intellectual property and usage rights is connectable to NIS2-oriented governance, supply-chain security, secure procurement, asset management, secure development, and protection of business-critical information. The specific connection should be assessed in an organization-specific way in the requirements register, contract management, and risk register.

This artifact does not replace legal advice or a binding assessment of copyright, trademark, license, or contract questions.

## Boundaries

- No legal advice, license assessment, or contractual interpretation by this artifact.
- No certification, conformity, or security commitment.
- No adoption of licensed standards text.
- No use of real contract, customer, personal, or secret data in public examples.
- No replacement for software asset management, SBOM program, or legal review.

## Handoffs

- **Legal handoff:** unclear rights, license terms, publications, trademarks, disputes, open-source questions with product impact.
- **Procurement/Vendor handoff:** procurement, contract term, usage scope, supplier deliverables, audit or evidence requests.
- **Development handoff:** open source, dependencies, source-code origin, release approvals.
- **Communications/Marketing handoff:** external content, images, texts, presentations, public assets.
- **Data Protection handoff:** databases, training data, AI use, or personal information in content.
- **Management handoff:** strategic publication, accepted residual risk, licensing or replacement costs.
- **Audit/Evidence handoff:** missing evidence, unclear inventories, or approvals that cannot be reviewed.

## Typical mistakes

- Rights questions are asked only shortly before publication or customer handover.
- Open-source components are managed technically but not assessed for license and origin.
- Service providers deliver code or documents without clearly documented usage rights.
- Internal templates are shared externally although confidentiality or rights are unclear.
- License register and actual tool use diverge.
- Unclear cases remain resolved verbally and cannot be reviewed later.

## Fictional mini example

A fictional software team wants to include a new library in a customer portal. The Product Owner records purpose and product relation, Engineering documents origin and version, and Legal checks the license for usage limits. The library is approved, but with a review before every major update. In parallel, an older component is replaced because its origin cannot be traced.

Evidence:

- dependency entry with owner and purpose,
- documented license clarification,
- release approval,
- ticket to replace the unclear component,
- review date for major updates.
