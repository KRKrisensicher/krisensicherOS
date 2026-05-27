# Setup entry point for krisensicherOS

## Core message

krisensicherOS requires approved AI usage.

Without an approved AI environment, krisensicherOS is not a meaningful operating mode. Organizations can prepare AI usage approval, but they cannot work productively with krisensicherOS.

## First: clarify AI usage approval

Use `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`) to define at least:

- which data classes may be processed,
- which AI environment is approved,
- which content is prohibited,
- who reviews outputs,
- which human gates apply.

If these points are not clarified: stop, prepare approval, no productive use.

## Which guide should I open?

| Approved environment | Entry point |
| --- | --- |
| ChatGPT is approved for suitable data classes | `chatgpt-lokale-ide.md` (`chatgpt-lokale-ide.md`) |
| Microsoft 365 Copilot is approved tenant-side | `m365-copilot.md` (`m365-copilot.md`) |
| Claude Code is to be used for repo work | `claude-code.md` (`claude-code.md`) |
| Local AI without cloud transmission is approved or is to be technically piloted | `lokale-ki.md` (`lokale-ki.md`) |
| Compare multiple maturity levels or team setup | `ki-setups-bedienungsanleitung.md` (`ki-setups-bedienungsanleitung.md`) |

## 15-minute decision

1. Start with `../getting-started/minimaler-nis2-start-in-5-artefakten.md` (`../getting-started/minimaler-nis2-start-in-5-artefakten.md`).
2. Check AI usage approval with `../../templates/ki-nutzungsfreigabe-matrix.md` (`../../07-ai-governance-agents/templates/ki-nutzungsfreigabe-matrix.md`).
3. Select exactly one setup document for the pilot.
4. Always review outputs through human gates before they are decided internally or shared externally.

## Common rules for all setups

- No legal advice, data protection advice, compliance, certification, or security assurance.
- No management decision or risk acceptance by AI or agents.
- No confidential, personal, customer-specific, contractual, or licensed content in AI environments that have not been approved.
- Use licensed standards only as metadata, references, or your own summaries.
- Redaction tools are support layers, not an anonymization guarantee and not compliance evidence.

## Windows-first note

The setup documents are primarily described for Windows workstations. macOS/Linux are mentioned only where they are relevant for developer or local AI setups.
