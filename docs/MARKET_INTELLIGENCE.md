# Global Production and Market Intelligence
## Data
FAOSTAT (global production/trade); USDA PSD and WASDE (commodity balance); AMIS; World Bank commodity prices; UN Comtrade; India AGMARKNET, data.gov.in, e-NAM, IMD and ICAR; Copernicus/NASA/USGS Earth observation.

## Pipeline
Global production/trade → national/state/district supply → crop condition/weather → market arrivals and prices → local harvest windows → storage/transport/buyer requirements → farm-level crop/sale scenarios.

## Features
Commodity taxonomy; area/yield history; stocks/import/export; regional crop calendars; mandi arrivals and price series; weather shocks; harvest overlap; grading; storage shelf-life; processing/logistics costs; buyer demand; forward contract records.

## Models
Start with seasonal naive baselines, moving averages, ETS/ARIMA and gradient boosting; only add complex neural forecasting when backtests show value. Use rolling-origin evaluation, MAE/RMSE/MASE, quantile loss and prediction-interval calibration.

## Farm economics
Revenue scenarios = marketable yield × expected price. Subtract seed, fertilizer, crop protection, water, energy, labor, machinery, finance, packaging, storage, transport, commissions and losses. Include downside risk, perishability and cash-flow timing.

## Guardrails
Show source date/freshness, forecast horizon, confidence interval, backtest and limitations. Historical prices, official estimates, vendor forecasts and AgriNex predictions must be labeled separately. Never guarantee a price or encourage market manipulation.
