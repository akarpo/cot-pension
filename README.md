# cot-pension

Independent analysis of the City of Troy, Michigan Employees Retirement System investment performance vs. the S&P 500 Total Return Index, FY2008–FY2025.

## Start here

→ **[ANALYSIS.md](./ANALYSIS.md)** — full analysis, methodology, findings, and reproducibility notes.

## Quick navigation

| What | Where |
|---|---|
| The full written analysis | `ANALYSIS.md` |
| Deployable static webpage | `webpage/index.html` + `webpage/data.js` |
| Data pipeline (reproducible) | `scripts/build_dataset.py` |
| Source ACFRs (City of Troy public records) | `source-data/*.pdf` |
| Your scratch space | `analysis/` |

## Headline numbers

| | Annualized return, FY2008–FY2025 |
|---|---:|
| Troy pension fund | **7.03%** |
| S&P 500 Total Return | **9.23%** |
| Gap | −2.20 pp |

Troy's pension is **152% funded** as of FY2025 and is among the best-funded municipal plans in Michigan. The performance gap vs. the S&P is the expected result of a diversified pension portfolio holding bonds, real estate, and private equity alongside stocks. A 60/40 portfolio would be a fairer benchmark.

## Working with this in Claude Code

```bash
cd cot-pension
claude  # or your preferred Claude Code command
```

Then ask Claude things like:

- "Read ANALYSIS.md and propose three additional sections that would strengthen the comparison."
- "Rebuild the dataset with the FY2026 ACFR once it's published."
- "Add a 60/40 benchmark line to the growth chart in webpage/index.html."
- "Extract the pension expense and contribution figures from source-data/Troy_ACFR_FY2025.pdf and add a 'cost to taxpayers' section."

## Disclaimer

Independent analysis of public records. Not affiliated with the City of Troy or its Retirement System Board of Trustees. Not financial advice.
