# AGX-14 — Market Intelligence

## Purpose
Licensed price, demand, trade, logistics and buyer data.

## Functional requirements
- AGX-14-FR-001: Register provider/license/commodity/grade/market/currency/unit/cadence
- AGX-14-FR-002: preserve publication/event/ingestion time
- AGX-14-FR-003: normalize grade/unit/currency with provenance
- AGX-14-FR-004: stale/missing/revised/anomaly flags
- AGX-14-FR-005: distinguish transaction/quote/forecast
- AGX-14-FR-006: explain horizon/assumptions/uncertainty
- AGX-14-FR-007: honor redistribution/retention
- AGX-14-FR-008: avoid guaranteed-return claims.

## Data ownership and interfaces
Own MarketObservation, CommodityProfile, PriceForecast, BuyerOffer; consumes licensed sources and harvest lots.

## Acceptance, safety and security
Replay/revision and currency/unit conversion tests. No price certainty.
