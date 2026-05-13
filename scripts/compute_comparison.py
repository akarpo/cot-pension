import yfinance as yf
import pandas as pd

# Daily data for last trading day of June each year
data = yf.download("^SP500TR", start="2014-06-15", end="2024-07-15", interval="1d", progress=False, auto_adjust=False)
data.columns = data.columns.get_level_values(0)  # flatten
data = data[['Close']].copy()
data.index = pd.to_datetime(data.index)

# Get last trading day of June for each year 2014-2024
june_ends = {}
for year in range(2014, 2025):
    june = data[(data.index.year == year) & (data.index.month == 6)]
    if len(june) > 0:
        june_ends[year] = float(june['Close'].iloc[-1])

print("S&P 500 Total Return Index values at end of June:")
for y, v in sorted(june_ends.items()):
    print(f"  June {y}: {v:,.2f}")

print("\nFiscal Year (July X-1 to June X) S&P 500 Total Returns:")
fy_returns = {}
prev = None
for y in sorted(june_ends.keys()):
    if prev is not None:
        ret = (june_ends[y] / june_ends[prev] - 1) * 100
        fy_returns[y] = ret
        print(f"  FY{y} (Jul {y-1}-Jun {y}): {ret:+.2f}%")
    prev = y

# Troy pension returns
troy_pension = {
    2015: 3.29, 2016: -0.23, 2017: 13.79, 2018: 10.56, 2019: 8.12,
    2020: 3.86, 2021: 30.32, 2022: -12.34, 2023: 12.55, 2024: 12.39
}

print("\n=== COMPARISON: Troy Pension vs S&P 500 TR (FY ending June 30) ===")
print(f"{'FY':<6}{'Troy':>10}{'S&P 500 TR':>14}{'Difference':>14}")
for y in range(2015, 2025):
    t = troy_pension[y]
    s = fy_returns[y]
    print(f"{y:<6}{t:>9.2f}%{s:>13.2f}%{t-s:>+13.2f}%")

# Compute compound returns
def compound(rates):
    val = 1.0
    for r in rates:
        val *= (1 + r/100)
    return val

years = list(range(2015, 2025))
troy_cumulative = compound([troy_pension[y] for y in years])
sp_cumulative = compound([fy_returns[y] for y in years])

# Annualized
troy_ann = (troy_cumulative ** (1/10) - 1) * 100
sp_ann = (sp_cumulative ** (1/10) - 1) * 100

print(f"\n10-Year cumulative (FY2015-FY2024, $1 invested):")
print(f"  Troy pension: ${troy_cumulative:.3f}  (annualized: {troy_ann:.2f}%)")
print(f"  S&P 500 TR:   ${sp_cumulative:.3f}  (annualized: {sp_ann:.2f}%)")
print(f"  Difference (annualized): {troy_ann - sp_ann:+.2f}%")

# Growth of $1M
print(f"\nGrowth of $1,000,000 invested at start of FY2015:")
print(f"  Troy pension allocation: ${troy_cumulative*1000000:,.0f}")
print(f"  S&P 500 (100% equities):  ${sp_cumulative*1000000:,.0f}")
print(f"  Gap: ${(sp_cumulative-troy_cumulative)*1000000:,.0f}")

# Save data for visualization
import json
result = {
    "years": years,
    "troy": [troy_pension[y] for y in years],
    "sp500": [round(fy_returns[y], 2) for y in years],
    "troy_cumulative": round((troy_cumulative-1)*100, 2),
    "sp500_cumulative": round((sp_cumulative-1)*100, 2),
    "troy_annualized": round(troy_ann, 2),
    "sp500_annualized": round(sp_ann, 2),
}
with open("comparison_data.json", "w") as f:
    json.dump(result, f, indent=2)
print("\nSaved to comparison_data.json")
