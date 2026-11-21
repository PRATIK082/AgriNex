# Global Production and Market Intelligence
## Data sources
FAOSTAT; USDA PSD/WASDE; AMIS; World Bank Commodity Markets; UN Comtrade; India AGMARKNET, data.gov.in, e-NAM, IMD, ICAR; Copernicus, NASA and USGS Earth observation.

## Pipeline
Global production/trade → national/state/district supply → crop condition/weather → market arrivals/prices → harvest windows → storage/transport/buyer requirements → farm-level crop and sale scenarios.

## Features
Commodity taxonomy; area/yield history; stocks/import/export; regional crop calendars; mandi arrivals and prices; weather shocks; harvest overlap; grading; storage shelf-life; processing/logistics costs; buyer demand and contract records.

## Models
Start with seasonal naive baselines, moving averages, ETS/ARIMA and gradient boosting. Add complex neural forecasting only when backtests demonstrate value. Use rolling-origin evaluation, MAE/RMSE/MASE, quantile loss and interval calibration.

## Farm economics
Revenue scenarios = marketable yield × expected price. Subtract seed, fertilizer, crop protection, water, energy, labor, machinery, finance, packaging, storage, transport, commissions and losses. Include downside risk, perishability and cash-flow timing.

Show source date/freshness, horizon, interval, backtest and limitations. Label historical observations, official estimates, vendor forecasts and AgriNex predictions separately. Never guarantee price or encourage market manipulation.
