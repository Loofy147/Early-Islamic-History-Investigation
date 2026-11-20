# Data dictionary

## Source register
One row per textual, documentary, material or scholarly source. A source record describes what the source is and what has been inspected. It does not encode the truth of its contents.

## Claim register
One row per atomic proposition. A source-content claim (e.g. “Theophanes reports X”) must remain distinct from an event claim (e.g. “X happened”).

## Event register
One row per historical event or separately attested narrative episode. Similar names do not justify merging records. If identity is uncertain, create separate events and link them through a disputed identity claim.

## Hypothesis register
One row per causal or interpretive explanation. Include mechanism, scope, observable predictions, supporting/contrary claims and conditions that would weaken it.

## Identifiers
Use stable IDs:
- SRC-#### for sources
- CLM-#### or CLM-[CASE]-### for claims
- EVT-#### for events
- H-[CASE]-# for hypotheses
- CASE-### for case studies

Never reuse an ID. Do not change an ID because wording changes; record the change in the decision log.

## CSV rules
- UTF-8.
- Quote text cells containing commas, quotes or line breaks.
- Keep the same number of fields in every row.
- Use semicolon-delimited IDs for multiple references.
- Empty cells mean unknown/not entered; they do not mean false.
