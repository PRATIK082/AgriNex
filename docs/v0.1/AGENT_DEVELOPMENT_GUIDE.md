# Vibe-Coding and Coding-Agent Rules
Work one bounded module or issue at a time. Before editing, read system architecture, module spec, common data model, ADRs, existing code/tests and licenses. Analyze impact and reuse existing utilities first. Never invent interfaces or alter shared contracts without compatibility review.

Every PR includes requirement IDs, assumptions, changed files, schema/API impact, tests, risks, migration/rollback, docs and known gaps. Do not mark requirements complete without test evidence. Do not fabricate agronomic facts, regulatory compliance or safety certification. Do not expose secrets or private farm data to unapproved model providers.

For physical functions: simulation first, then SIL, HIL and supervised field validation. LLM output is advisory. Local E-stop/interlocks/watchdogs cannot be overridden by software agents.
