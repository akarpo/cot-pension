"""
Compute Troy pension returns FY2008-FY2025 by combining:
  - FY2008-FY2010: simple return on combined ERS trust (pension + OPEB)
    [pre-GASB-67 era; only data available]
  - FY2012-FY2013: simple return on pension-only portion of ERS trust
  - FY2014-FY2025: official money-weighted return from GASB 67 Schedule of Investment Returns
  - FY2011: skipped (scanned/OCR-only ACFR; trust composition changed)

Plus S&P 500 Total Return for fiscal years ending June 30.
"""

import yfinance as yf
import pandas as pd
import json

# ============ TROY PENSION RETURNS ============

# FY2008-FY2010: combined ERS trust (pension + OPEB)
# Source: pdf-extracted Statements of Changes in Fund Net Assets
# Approach: Total Investment Earnings / Beginning Total Net Assets Held in Trust
fy2008_inv = -8_820_252      # Total investment earnings (Employees' Retirement System)
fy2008_begin = 181_108_878   # Total net assets held in trust, beginning
fy2008 = fy2008_inv / fy2008_begin * 100

fy2009_inv = -22_149_960
fy2009_begin = 164_732_973
fy2009 = fy2009_inv / fy2009_begin * 100

fy2010_inv = 19_192_408
fy2010_begin = 140_910_654
fy2010 = fy2010_inv / fy2010_begin * 100

# FY2012-FY2013: pension trust only (split from OPEB)
# FY2012 ACFR: Pension trust began $146,670,307; investment income $(1,469,333)
fy2012_inv = -1_469_333
fy2012_begin = 146_670_307
fy2012 = fy2012_inv / fy2012_begin * 100

# FY2013 ACFR: Pension trust began $146,047,162; investment income $26,026,986
fy2013_inv = 26_026_986
fy2013_begin = 146_047_162
fy2013 = fy2013_inv / fy2013_begin * 100

# Optional cross-check: FY2014 same methodology
# FY2014 ACFR: Pension trust began $163,316,531; investment income $35,667,991
fy2014_check = 35_667_991 / 163_316_531 * 100  # ~21.84%
# Official GASB-67 money-weighted: 22.23% — close enough to validate the simple method

# FY2014-FY2025: official money-weighted returns from GASB 67 schedules
official = {
    2014: 22.23, 2015: 3.29, 2016: -0.23, 2017: 13.79, 2018: 10.56, 2019: 8.12,
    2020: 3.86, 2021: 30.32, 2022: -12.34, 2023: 12.55, 2024: 12.39, 2025: 13.18
}

# Combine
troy_returns = {
    2008: round(fy2008, 2),
    2009: round(fy2009, 2),
    2010: round(fy2010, 2),
    # 2011 skipped
    2012: round(fy2012, 2),
    2013: round(fy2013, 2),
    **official
}

print(f"FY2014 sanity check: simple method gives {fy2014_check:.2f}%, official is 22.23% ✓\n")
print("Troy pension returns:")
for y in sorted(troy_returns.keys()):
    method = "money-weighted (GASB 67)" if y >= 2014 else "simple return on beginning trust assets"
    print(f"  FY{y}: {troy_returns[y]:+.2f}%   [{method}]")

# ============ S&P 500 TOTAL RETURN FY (July-June) ============

data = yf.download("^SP500TR", start="2007-06-15", end="2025-07-15",
                    interval="1d", progress=False, auto_adjust=False)
data.columns = data.columns.get_level_values(0)
data = data[['Close']].copy()
data.index = pd.to_datetime(data.index)

june_ends = {}
for year in range(2007, 2026):
    june = data[(data.index.year == year) & (data.index.month == 6)]
    if len(june) > 0:
        june_ends[year] = float(june['Close'].iloc[-1])

print("\nS&P 500 fiscal-year total returns (July X-1 → June X):")
sp_returns = {}
prev = None
for y in sorted(june_ends.keys()):
    if prev is not None:
        ret = (june_ends[y] / june_ends[prev] - 1) * 100
        sp_returns[y] = round(ret, 2)
        print(f"  FY{y}: {ret:+.2f}%")
    prev = y

# ============ COMBINE FOR OUTPUT ============

print("\n=== Final dataset for webpage ===")
print(f"{'FY':<6}{'Troy':>12}{'S&P 500 TR':>14}{'Diff':>10}")
output = []
for y in sorted(troy_returns.keys()):
    t = troy_returns[y]
    s = sp_returns.get(y)
    diff = t - s if s is not None else None
    print(f"{y:<6}{t:>11.2f}%{s:>13.2f}%{diff:>9.2f}%")
    output.append({"fy": y, "troy": t, "sp500": s, "diff": round(diff, 2)})

# Cumulative growth of $1
years_in_order = sorted(troy_returns.keys())
def growth(rates):
    val = 1.0
    series = [(years_in_order[0]-1, 1.0)]
    for y, r in zip(years_in_order, rates):
        val *= (1 + r/100)
        series.append((y, val))
    return series, val

troy_series, troy_final = growth([troy_returns[y] for y in years_in_order])
sp_series, sp_final = growth([sp_returns[y] for y in years_in_order])

n_years = len(years_in_order)
print(f"\nNumber of years included: {n_years} (FY2011 excluded)")
print(f"Troy cumulative: {(troy_final-1)*100:.2f}%   annualized: {(troy_final**(1/n_years)-1)*100:.2f}%")
print(f"S&P 500 cumulative: {(sp_final-1)*100:.2f}%   annualized: {(sp_final**(1/n_years)-1)*100:.2f}%")

# Save as JSON for webpage
result = {
    "annual": output,
    "growth_of_1_dollar": {
        "troy": [{"fy": y, "value": round(v, 4)} for y, v in troy_series],
        "sp500": [{"fy": y, "value": round(v, 4)} for y, v in sp_series],
    },
    "summary": {
        "years_count": n_years,
        "troy_cumulative_pct": round((troy_final-1)*100, 2),
        "sp500_cumulative_pct": round((sp_final-1)*100, 2),
        "troy_annualized_pct": round((troy_final**(1/n_years)-1)*100, 2),
        "sp500_annualized_pct": round((sp_final**(1/n_years)-1)*100, 2),
    }
}

with open("/home/claude/pension_data.json", "w") as f:
    json.dump(result, f, indent=2)

print("\nSaved to /home/claude/pension_data.json")
