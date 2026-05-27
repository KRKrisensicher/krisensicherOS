# A.8.23 — Web filtering and access to external content

## Purpose

Web filtering and controlled access to external content reduce risks from malicious websites, unsuitable downloads, phishing targets, fraudulent services, and unapproved cloud/AI or exchange platforms. The routine connects technical filtering with a clear decision: What is blocked, what is allowed, who decides exceptions, and how are hits used?

## Control objective in repository language

The organization operates a traceable routine for web access and external content. Categories, protection mechanisms, exceptions, logging, data protection boundaries, user communication, incident handoffs, and reviews are regulated without broadly blocking ability to work or legitimate research.

## Typical risks

- If malicious or fraudulent websites remain reachable, malware, credential leakage, or social engineering can be facilitated.
- If downloads from unknown sources occur without review, endpoints, servers, or development environments can be compromised.
- If shadow cloud services or unapproved AI/file exchange services are used, information can leak in an uncontrolled way.
- If web filters are only technically active but exceptions and reviews are missing, bypasses or permanent incorrect approvals arise.
- If web logs are evaluated with personal reference without data protection clarification, additional governance and trust problems arise.

## Triggers

- introduction or change of proxy, DNS filter, secure web gateway, browser policy, EDR web protection, or cloud access security.
- new external web service, cloud service, AI service, download source, or business application.
- phishing wave, malware finding, incident, suspicious web access, or threat intelligence notice.
- user request for unblocking, blocking complaint, or business need for external content.
- change to data classes, working models, development processes, or supplier channels.
- periodic review of categories, exceptions, logs, and effectiveness.

## Roles and responsibilities

- **IT/security operations:** operates filter technology, categories, policies, technical exceptions, and monitoring.
- **Service owner / business function:** justifies legitimate business needs and assesses impacts of blocking.
- **ISMS owner / security role:** defines risk logic, exception process, review, and handoff into incident response.
- **Data protection / legal:** review personal log evaluation, content inspection, employee reference, and usage rules.
- **HR / communication:** supports clear user information and training reference where required.
- **Management:** decides on conflicts between ability to work, security level, data protection boundaries, and resources.

## Implementation

### Minimum start

Goal: reduce risky web access and make exceptions controllable.

1. The organization defines which protection mechanisms apply to standard endpoints and critical user groups.
2. Risk categories are defined, for example known malware/phishing targets, newly registered domains, unwanted downloads, or unapproved data exchange services.
3. There is a simple approval process for blocked sites or services: request, justification, owner, duration, decision.
4. Critical hits are handed over to incident triage or security operations.
5. Users receive understandable information on why blocking happens and how they can request legitimate approvals.
6. Data protection boundaries for log evaluations are clarified before personal analyses.

Minimum evidence:

- web filtering/browser policy or operating requirement,
- list of active categories or protection rules,
- exception and approval tickets,
- evidence of user information,
- incident tickets from critical hits,
- data protection/legal review point for log evaluations.

### Solid practice

Goal: web access is controlled on a risk basis, traceably, and with incident capability.

1. Filter categories are differentiated by risk, work need, and user groups.
2. Exceptions are time-limited, justified by business need, and reviewed regularly.
3. Downloads, macros, scripts, browser extensions, or developer sources are considered separately when they create increased risk.
4. Security notifications from web filters feed into incident triage, awareness, and vulnerability management.
5. New cloud, AI, or file exchange services are reviewed with data class, access protection, and supplier reference.
6. Reporting shows patterns, blocked risk categories, exception quality, and open decisions, not individual persons without clarified basis.

Strong evidence:

- documented category and exception logic,
- approval tickets with purpose, duration, and decision,
- review records for exceptions and false blocks,
- incident or alert evidence from critical hits,
- communication or awareness evidence,
- data protection clarification for personal or content-adjacent evaluations.

### Advanced practice

Goal: web filtering is connected with risk, data, and detection logic.

1. Web access is correlated with endpoint, identity, email, DNS, and cloud signals where permissible and proportionate.
2. High-risk groups or privileged roles receive stronger protection profiles and stricter exception review.
3. Unapproved cloud/AI services are moved through a regulated approval process into safe usage alternatives.
4. Threat intelligence and incident lessons learned update categories and block lists.
5. Management receives decision-ready metrics on exception rate, critical hits, shadow IT patterns, false blocks, and data protection/acceptance topics.

## Routine flow

1. **Signal or need arises:** blocking, approval request, threat notice, incident, or new service.
2. **Classify:** assess URL/service, category, user group, data class, business need, and risk.
3. **Decide:** block, allow, time-limit, offer alternative solution, or escalate.
4. **Implement technically:** adjust category, policy, exception, browser rule, or DNS/proxy configuration.
5. **Communicate:** inform requester or affected group about decision, justification, and duration.
6. **Monitor:** give critical hits to incident triage and review patterns.
7. **Review:** regularly assess exceptions, false blocks, new risk categories, and shadow IT signals.
8. **Improve:** adapt policies, awareness, tooling, or approved alternatives.

## Decisions

- Which categories are blocked by default and which are only monitored?
- Which roles or systems need stricter web protection profiles?
- Who may approve exceptions and for what duration?
- When is an approval a security, data protection, procurement, or management topic?
- Which log evaluations are permissible and necessary?
- How are ability to work, freedom to research, data protection, and security level balanced?

## Evidence

### Strong evidence

- web filtering or browser security requirement with owner and review date,
- active category/policy overview,
- exception decisions with purpose, duration, and business owner,
- review record for exceptions, false blocks, and risk hits,
- incident tickets or alerts from web protection signals,
- evidence of user communication and reporting path,
- data protection/legal clarification for personal evaluations.

### Weak evidence

- screenshot of a filter dashboard without decision logic,
- broad block list without business reference,
- exception list without expiry date,
- high number of blocks without evaluation or measures,
- user information without approval or escalation path.

### Evidence gaps

- no owners for categories or exceptions,
- unclear treatment of unapproved cloud/AI services,
- critical web hits without incident handoff,
- personal log analysis without data protection clarification,
- local browser or developer bypasses without review,
- permanent whitelists without follow-up date.

## Effectiveness review

Review questions:

- Are web protection profiles active for relevant user groups and endpoints?
- Are exceptions justified by business need, time-limited, and reviewed?
- Do critical hits lead to incident triage or other measures?
- Are false blocks and ability-to-work problems visibly handled?
- Are data protection boundaries for logging and evaluation clarified?
- Is there a way to handle shadow cloud, AI, and download risks?

Possible metrics:

- number of critical web protection hits by category,
- exception rate and overdue exceptions,
- time to decision on approval requests,
- repeated hits on phishing/malware categories,
- false block rate or complaints,
- unapproved cloud/AI services in review.

## BSIG/NIS2 connection point

Web filtering and controlled access to external content are a connection point for NIS2-oriented topics such as cyber hygiene, malware and phishing prevention, incident handling, access protection, data leakage risks, training, and secure use of external services. The specific classification should be performed organization-specifically in the requirements register and data protection/risk review.

This artifact does not replace legal, employment law, or data protection assessment.

## Boundaries

- Web filtering does not replace awareness, email security, endpoint protection, patch management, or DLP governance.
- Content inspection and personal log evaluation can be legally and data-protection sensitive.
- Overly strict blocking can promote bypasses and shadow IT.
- This artifact is not a recommendation for specific filtering products or category providers.
- No certification promise and no adoption of licensed standard text.

## Handoffs

- **Incident handoff:** malware/phishing hits, suspected credential leakage, suspicious download or C2 patterns.
- **Data protection/legal handoff:** personal logs, content inspection, employee reference, usage rule, or monitoring.
- **Procurement/supplier handoff:** new cloud, AI, download, or exchange service with business need.
- **Awareness handoff:** repeated phishing clicks, unsafe download patterns, unclear user communication.
- **Change handoff:** new filter profiles, browser policies, proxy/DNS changes.
- **Management handoff:** conflict between ability to work, data protection, security level, and cost.
- **Audit/evidence handoff:** missing exception evidence, unclear reviews, or non-traceable log evaluations.

## Typical mistakes

- Filtering technology is switched on, but nobody decides categories and exceptions.
- Whitelists grow permanently and are never cleaned up.
- Web logs are evaluated with personal reference without prior clarification.
- Blocks create frustration because a legitimate approval process is missing.
- Critical hits remain in the tool and do not reach incident response.
- Unapproved cloud or AI services are only blocked without clarifying safe alternatives.
- Reporting counts blocks but shows no risk or decision effect.

## Fictional mini example

A fictional project area wants to use an external file exchange service. The web filter blocks the service because of unclear data processing. The business function submits an approval request with purpose and data class. Data protection and procurement review the service; management decides to use an already approved platform instead. The exception is not granted, and the user information is updated with the secure alternative path.

Evidence:

- blocking and approval ticket,
- documented data class assessment,
- data protection/procurement handoff,
- management decision on the alternative,
- updated user information.
