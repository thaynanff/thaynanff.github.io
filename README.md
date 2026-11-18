[![author](https://img.shields.io/badge/author-thaynanff-blue)](https://www.linkedin.com/in/thaynanffreitas/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

<p align="center">
  <img src="https://github.com/thaynanff/thaynanff.github.io/blob/main/bannerv2.png?raw=true" >
</p>


# Thaynan Freitas
<sub> Data Analyst </sub>

<p align="justify">Data Analyst in Sydney with seven years of experience turning ERP and CRM data into reports and dashboards for finance, operations and sales teams.</p>

<p align="justify">At Shore Hire, now part of United Rentals, I automated 10+ ETL pipelines integrating APIs across Salesforce, Dynamics and Tableau, including a Python pipeline that saved 130+ hours of manual work. I built 10+ Tableau workbooks with 30+ dashboards and improved database performance by 60% by optimising legacy queries. Before moving to Australia, I spent five years at ArcelorMittal Brasil, where I reported 600+ strategic KPIs to C-level executives in Power BI, cut fleet costs by 20% and reduced invoice issuing time by up to 85% with SAP Scripting and VBA.</p>

**Tools:** SQL (Snowflake, SQL Server, IBM Db2), Python, Tableau, Power BI, Excel, Power Query.

**Links:**
* [LinkedIn](https://www.linkedin.com/in/thaynanffreitas/)
* [Kaggle](https://www.kaggle.com/thaynanff/code)

---
# Case studies

Problems from real jobs, rebuilt with fictional or anonymised data. Each one covers the problem, what I built, the result and the tools.

## 1. Split Addresses: standardising 10,000+ customer addresses

**Problem.** Customer addresses for 10,000+ customers were stored in one free-text field, typed by users. The business needed them in separate fields (street number, street name, street type, suburb, state, postcode), and the source system kept the free-text field, so the split had to keep running as addresses changed.

**Approach.** A Python script that picks up only the addresses changed since the last run (from the audit table), parses each one with rules and regular expressions, and matches suburb and postcode against a reference list. When there is no exact match, three fuzzy matching steps (80% similarity threshold) try again: first with the same number of words, then allowing a different number of words, then using the state. Addresses that still can't be fixed go to an error report with the reason, and every run is logged.

**Result.** More than 90% of addresses were split automatically, saving 130+ hours of manual work.

**Tools.** Python (pandas, regex, fuzzywuzzy), SQL Server, pyodbc.

[Notebook](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/10.%20Split%20Addresses/Split%20Address%20Script.ipynb)

## 2. Salesforce to SQL Server sync for Tableau

**Problem.** Tableau reports needed Salesforce data combined across objects, but Salesforce does not allow complex joins between objects, which made some analysis hard to build.

**Approach.** A Python script that queries the Salesforce API, compares the result with a SQL Server table and applies the difference: inserts new records, updates changed columns and deletes records removed in Salesforce. Credentials sit in an external file, so a password change does not mean rebuilding the job. The script runs as a scheduled EXE several times a day and logs each run.

**Result.** Salesforce data refreshed in SQL Server on a schedule, ready to be joined and reported in Tableau.

**Tools.** Python (simple_salesforce, pandas), Salesforce API, SQL Server, Tableau.

[Notebook](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/09.%20Salesforce%20API%20Extraction/Salesforce%20-%20Incremental%20Inserts%20and%20Updates%20-%20Calls.ipynb)

## 3. Fleet Management Dashboard

**Problem.** A fleet of 80+ vehicles needed one place to control fuel, maintenance and cost KPIs.

**Approach.** A Power BI dashboard covering fuel spend, spend per establishment, price per litre and per km, km per litre, distance travelled, infraction alerts, maintenance spend and lead time, and preventive versus corrective spend.

**Result.** Used to manage the fleet, contributing to a 20% reduction in fleet costs. The public version is translated, with real names and licence plates replaced.

**Tools.** Power BI.

[Power BI report](https://app.powerbi.com/view?r=eyJrIjoiYjhmYzFmNzEtNWM3Zi00MThjLTg5MDQtZTA1MTZjOTczOTY3IiwidCI6IjcyNmE2MjA3LTUwZjYtNDlkNS1iMGQ0LTFhNGYwNmRiYjM4OSJ9)

---
# Other projects

| Project | Description | Links |
| --- | --- | --- |
| Stock Data Scraper | Python engine that collects multi-year financial data for ASX-listed companies and scores them on growth, profitability, financial strength, cash flow and valuation. | [Notebook](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/11.%20Stock%20Analyser/Stock%20Data%20Scrapper.ipynb) |
| Stock Scoring and Financial Analysis | Power BI report on top of the scraper: scorecards by pillar, year-over-year heatmap, statements and ratios. | [Power BI report](https://app.powerbi.com/view?r=eyJrIjoiNmVkYWRmZGMtMGY0Ny00YTVlLWFiYWMtYTc5ZWEwNzI1N2YxIiwidCI6IjcyNmE2MjA3LTUwZjYtNDlkNS1iMGQ0LTFhNGYwNmRiYjM4OSJ9), [files](https://github.com/thaynanff/thaynanff.github.io/tree/main/Power%20BI%20Dashboards/4.%20Investment%20Analyser) |
| Alderman's Analyzer | Python web scraping of the Indaial City Hall website into SQL Server with incremental updates, feeding a Power BI dashboard on aldermen's propositions. | [Notebook](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/07.%20Alderman's%20Analyzer/Alderman's%20Analyzer%20-%20Python%20Web%20Scraping.ipynb), [Power BI report](https://app.powerbi.com/view?r=eyJrIjoiZDVkNGM0NTEtZmRkYi00N2FhLTkwY2YtYzIxODc5NWJjNTJjIiwidCI6IjcyNmE2MjA3LTUwZjYtNDlkNS1iMGQ0LTFhNGYwNmRiYjM4OSJ9) |
| Australian Automotive Market | Descriptive analysis of the Australian car market to find the best car for a set of criteria. | [Notebook](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/08.%20Australian%20Automotive%20Market/Australian%20Automotive%20Market.ipynb) |
| Expenses of Brazilian Politicians | Power BI analysis of Brazilian politicians' expenses from 2018 to mid 2020. | [Power BI report](https://app.powerbi.com/view?r=eyJrIjoiNGZjNDdhMWUtNzMwZi00YzBmLThjOTgtYTU2MGE1ODg4NDg4IiwidCI6IjcyNmE2MjA3LTUwZjYtNDlkNS1iMGQ0LTFhNGYwNmRiYjM4OSJ9) |
| Western Australia Weather | Rainfall and temperature patterns from the Perth Airport weather station. | [Kaggle](https://www.kaggle.com/code/thaynanff/western-australia-weather-data-analysis/notebook) |

---
# Learning

Courses, tutorials and practice exercises.

- **Python:** [Python Challenges](https://github.com/thaynanff/Python-Challenges) (CodeWars and HackerRank), [Python Projects](https://github.com/thaynanff/Projects)
- **SQL and data modelling:** [Databases and SQL](https://github.com/thaynanff/Databases-and-SQL) (DIO Database Experience Bootcamp: e-commerce and mechanical workshop models)
- **freeCodeCamp data analysis:** [Medical Data Visualizer](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/06.%20Medical%20Data%20Visualizer/Medical%20Data%20Visualizer.ipynb), [Sea Level Predictor](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/05.%20Sea%20Level%20Predictor/Sea%20Level%20Predictor.ipynb), [Page View Time Series Visualizer](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/04.%20Page%20View%20Time%20Series%20Visualizer/Page%20View%20Time%20Series%20Visualizer.ipynb), [Demographic Data Analyzer](https://github.com/thaynanff/thaynanff.github.io/blob/main/Data%20Science%20and%20Analytics/03.%20Demographic%20Data%20Analyzer/Demographic%20Data%20Analyzer.ipynb)
- **Kaggle:** [Titanic: Machine Learning from Disaster](https://www.kaggle.com/code/thaynanff/titanic-machine-learning-from-disaster-v1), [Customers Personality Analysis](https://app.powerbi.com/view?r=eyJrIjoiMzNiNWIzOWItMGZhYi00MmZlLTk1MjMtZGVmMjZlNzljZTExIiwidCI6IjcyNmE2MjA3LTUwZjYtNDlkNS1iMGQ0LTFhNGYwNmRiYjM4OSJ9) (Power BI)
