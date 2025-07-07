# 📊 ASX Power BI Stock Analytics Dashboard

This Power BI project delivers a **fundamental analytics platform for ASX-listed companies**, supporting in-depth financial analysis, historical performance tracking, and automated scoring across key investment pillars.

---

## 🧩 Project Structure & Pages

### 1. 📈 Scorecard
Consolidated view of each company's scores across the main financial pillars:

- **Growth**
- **Profitability**
- **Financial Strength**
- **Cash Flow**

Each metric is:
- Scored on a 0–10 scale
- Weighted by sector/industry importance
- Aggregated into a total score

Used to **rank companies** within their industry or across sectors.

---

### 2. 📊 Summary
Highlights the most critical metrics over time, enabling side-by-side year comparisons.

Features:
- **Color-coded matrix** (Green/Red) for year-over-year (YoY) variation:
  - ✅ Green = Positive movement
  - ❌ Red = Deterioration
- Visual snapshot of improvements, stability, or declines.

---

### 3. 🧾 Financial Info
Displays full historical data by company:

- **Income Statement**: Revenue, EBITDA, EPS, etc.
- **Balance Sheet**: Assets, Liabilities, Equity
- **Cash Flow Statement**

Perfect for **bottom-up fundamental analysis**.

---

### 4. 📐 Ratios
Comprehensive set of investment and operational ratios:

- Valuation: P/E, P/B, EV/EBITDA
- Profitability: ROE, ROA, ROIC
- Liquidity: Current Ratio, Quick Ratio
- Leverage: Debt/Equity, Interest Coverage

Also includes **YoY delta heatmaps** to track improvements and deterioration.

---

### 5. 🧠 Metric Tooltip
Interactive reference page that defines every financial metric used.

- Friendly descriptions
- Interpretation guidance (what’s good vs bad)
- Helps both beginner and expert users understand key indicators.

---

## 🧠 Data Model – Architecture & Logic

The project uses a **star-schema data model** optimized for performance, cross-filtering, and dynamic metric interpretation across industries.

Supports **score calculation**, **sector-adjusted benchmarking**, and visual storytelling.

---

### 🔧 Key Tables & Relationships

#### 🔸 `Sheet1` (Fact Table)
Core table with financial data for each **Company-Year**.
Includes:
- Company identifiers
- Sector / Industry info
- All financial metrics
- 5Y / 10Y averages

#### 🔸 `DIM_SectorIndustry`
Contains unique `Sector + Industry` keys.
Used as a bridge table to prevent **many-to-many** relationships.

#### 🔸 `DIM_SectoralPillars`
Defines **pillar weightings** (Growth, Profitability, etc.) for each Sector/Industry pair.

- Adjusts how each metric contributes to final company score.
- Enables relevance-based scoring.

#### 🔸 `DIM_Metrics`
Catalog of all metrics evaluated in the Scorecard.
Includes:
- Assigned Pillar
- Min/Max value bands
- 5 scoring tiers (0–6)
- Explanation field (what the metric means)

#### 🔸 `DIM_Metrics_Link`
Connects metrics to industry context.
Allows dynamic filtering and sector-adjusted interpretations.

#### 🔸 `MetricSentiment`
Indicates whether higher metric values are **positive** or **negative**.
Used to drive **green/red heatmap logic** across visuals.

#### 🔸 `MetricDesc`
Short, friendly descriptions of each metric.
Used on the **Metric Tooltip** page and in tooltips.

#### 🔸 `MetricSortingOrder`
Controls how metrics appear in visualizations.
Ensures correct order and groupings in matrix-style visuals.

#### 🔸 `_Measures`
Contains custom DAX logic:
- Final scores
- Weighted calculations
- YoY % deltas
- Company rankings

---

## ⚙️ Functional Logic

### 🧮 Scoring Engine
Each metric is scored between **0 and 10**, based on predefined industry benchmarks from `DIM_Metrics`.

- Scores are **weighted per pillar** based on `DIM_SectoralPillars`
- Final score is the **sum of weighted metrics**, used for ranking

### 🎨 Heatmap Coloring
Color coding uses **YoY change** in each metric:

- Sentiment from `MetricSentiment` determines whether an increase is good or bad
- Green = favorable shift
- Red = unfavorable shift

Helps quickly spot deteriorations or improvements.

---

## 🎯 Use Case

Ideal for:
- Long-term investors
- Portfolio builders
- Equity analysts
- Financial educators

Use it to:
- Screen for high-quality companies
- Benchmark competitors
- Validate long-term trends
- Train new analysts using real company data

---

## 📈 Current Status

- ✅ Multi-sector support with dynamic pillar weighting
- ✅ Historical financial data & YoY variation
- ✅ Visual scoring breakdowns

### 🔜 Planned Features
- API integration for live financial data
- Integration with technical analysis indicators
- Export to PDF for automated investment reports

---
