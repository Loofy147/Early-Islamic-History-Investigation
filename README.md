# Early Islamic History Investigation

**A source-critical, multi-disciplinary research project (c. 629–661 CE).**

مشروع لإعادة بناء الوقائع العسكرية والسياسية المبكرة وتفسيرها بالأدلة، دون افتراض نتيجة مسبقة مثل «الغزو» أو «الفتح» أو «الدفاع».

## Purpose

Investigate how military and political processes transferred the authority of the nascent Islamic polity beyond Arabia into territories associated with the Byzantine and Sasanian empires. Distinguish reported motives, immediate triggers, strategic objectives, operational actions, political outcomes and longer-term consequences.

## Research principles

- A source is evidence to examine, not an authority to obey.
- Separate source-content claims from historical-event claims.
- No source is automatically neutral or independent.
- Repetition is not independent corroboration.
- Do not infer intention from outcome alone.
- Record contrary evidence, unknowns and the limits of search.
- Treat “conquest”, “opening”, “raid” and “occupation” as terms to define or attribute, not preset verdicts.
- Separate religious change, political sovereignty, military control, taxation, administration and migration.

## Start here

1. [Project charter](PROJECT_CHARTER.md)
2. [Agent instructions](AGENTS.md)
3. [Research protocol](docs/RESEARCH_PROTOCOL.md)
4. [Claim and evidence policy](docs/CLAIM_AND_EVIDENCE_POLICY.md)
5. [Source criticism checklist](docs/SOURCE_CRITICISM.md)
6. [Quality gates](docs/QUALITY_GATES.md)
7. [Current progress](docs/RESEARCH_PROGRESS.md)
8. [Research backlog](docs/RESEARCH_BACKLOG.md)

## Registers

- [Source register](data/sources/source_register.csv)
- [Claim register](data/claims/claim_register.csv)
- [Event register](data/events/event_register.csv)
- [Hypothesis register](data/hypotheses/hypothesis_register.csv)

## Case studies

- [001 — Mu'ta / Mothous](cases/001-mutah/CASE.md) — active; event identity and chronology disputed.
- [002 — Tabuk](cases/002-tabuk/CASE.md)
- [003 — Usama expedition](cases/003-usama/CASE.md)
- [004 — Ridda campaigns](cases/004-ridda/CASE.md)
- [005 — Iraq](cases/005-iraq/CASE.md)
- [006 — Syria and Palestine](cases/006-syria/CASE.md)
- [007 — Egypt](cases/007-egypt/CASE.md)
- [008 — Iran](cases/008-iran/CASE.md)

## Research status

The first active dossier separates the Islamic narrative of Mu'ta from Theophanes' account of an engagement at Mothous. The translated Theophanes text places Mothous under AM 6123 [AD 630/1], but the editor's note says the site's identification is unclear and lists alternative locations. The dossier does not treat this as independent confirmation of Mu'ta.

See [initial findings](cases/001-mutah/INITIAL_FINDINGS.md) and [open questions](docs/OPEN_QUESTIONS.md).

## Validation

Run:

```bash
python tools/validate_research_data.py
```

The validator checks CSV structure, row widths, identifiers and claim-state values. It does **not** verify historical truth or source authenticity. GitHub Actions runs the same structural check.

## Rights and license

The repository license is not yet selected. Do not upload complete copyrighted books, modern translations or scans. Record metadata, stable links, short necessary quotations and original analysis.
