// City of Troy Pension Performance Data
// Sources: Annual Comprehensive Financial Reports (FY2008-FY2025) + S&P 500 Total Return Index
// See README.md and the methodology footer on index.html for full source details

const PENSION_DATA = {
  "annual": [
    { "fy": 2008, "troy":  -4.87, "sp500": -13.12, "diff":   8.25 },
    { "fy": 2009, "troy": -13.45, "sp500": -26.21, "diff":  12.76 },
    { "fy": 2010, "troy":  13.62, "sp500":  14.43, "diff":  -0.81 },
    // FY2011 omitted — scanned ACFR, trust restructuring
    { "fy": 2012, "troy":  -1.00, "sp500":   5.45, "diff":  -6.45 },
    { "fy": 2013, "troy":  17.82, "sp500":  20.60, "diff":  -2.78 },
    { "fy": 2014, "troy":  22.23, "sp500":  24.61, "diff":  -2.38 },
    { "fy": 2015, "troy":   3.29, "sp500":   7.42, "diff":  -4.13 },
    { "fy": 2016, "troy":  -0.23, "sp500":   3.99, "diff":  -4.22 },
    { "fy": 2017, "troy":  13.79, "sp500":  17.90, "diff":  -4.11 },
    { "fy": 2018, "troy":  10.56, "sp500":  14.37, "diff":  -3.81 },
    { "fy": 2019, "troy":   8.12, "sp500":  10.42, "diff":  -2.30 },
    { "fy": 2020, "troy":   3.86, "sp500":   7.51, "diff":  -3.65 },
    { "fy": 2021, "troy":  30.32, "sp500":  40.79, "diff": -10.47 },
    { "fy": 2022, "troy": -12.34, "sp500": -10.62, "diff":  -1.72 },
    { "fy": 2023, "troy":  12.55, "sp500":  19.59, "diff":  -7.04 },
    { "fy": 2024, "troy":  12.39, "sp500":  24.56, "diff": -12.17 },
    { "fy": 2025, "troy":  13.18, "sp500":  15.16, "diff":  -1.98 }
  ],
  "growth_of_1_dollar": {
    "troy": [
      { "fy": 2007, "value": 1.0000 },
      { "fy": 2008, "value": 0.9513 },
      { "fy": 2009, "value": 0.8233 },
      { "fy": 2010, "value": 0.9355 },
      { "fy": 2012, "value": 0.9261 },
      { "fy": 2013, "value": 1.0911 },
      { "fy": 2014, "value": 1.3336 },
      { "fy": 2015, "value": 1.3775 },
      { "fy": 2016, "value": 1.3743 },
      { "fy": 2017, "value": 1.5638 },
      { "fy": 2018, "value": 1.7290 },
      { "fy": 2019, "value": 1.8694 },
      { "fy": 2020, "value": 1.9416 },
      { "fy": 2021, "value": 2.5303 },
      { "fy": 2022, "value": 2.2181 },
      { "fy": 2023, "value": 2.4965 },
      { "fy": 2024, "value": 2.8058 },
      { "fy": 2025, "value": 3.1755 }
    ],
    "sp500": [
      { "fy": 2007, "value": 1.0000 },
      { "fy": 2008, "value": 0.8688 },
      { "fy": 2009, "value": 0.6411 },
      { "fy": 2010, "value": 0.7336 },
      { "fy": 2012, "value": 0.7736 },
      { "fy": 2013, "value": 0.9329 },
      { "fy": 2014, "value": 1.1625 },
      { "fy": 2015, "value": 1.2487 },
      { "fy": 2016, "value": 1.2985 },
      { "fy": 2017, "value": 1.5310 },
      { "fy": 2018, "value": 1.7510 },
      { "fy": 2019, "value": 1.9335 },
      { "fy": 2020, "value": 2.0787 },
      { "fy": 2021, "value": 2.9266 },
      { "fy": 2022, "value": 2.6157 },
      { "fy": 2023, "value": 3.1281 },
      { "fy": 2024, "value": 3.8962 },
      { "fy": 2025, "value": 4.4868 }
    ]
  },
  "summary": {
    "years_count": 17,
    "fy_start": 2008,
    "fy_end": 2025,
    "troy_cumulative_pct": 217.55,
    "sp500_cumulative_pct": 348.68,
    "troy_annualized_pct": 7.03,
    "sp500_annualized_pct": 9.23
  }
};
