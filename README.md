<p align="center">
  <img src="assets/airbnb_logo.png" alt="Airbnb Logo" width="80"/>
</p>

<h1 align="center">Airbnb & Hospitality Bookings Analysis</h1>

<p align="center">
  <strong>End-to-end data analytics project analyzing 999 Airbnb bookings to uncover revenue drivers, guest behavior, and seasonal trends across European hospitality markets.</strong>
</p>

<p align="center">
  <a href="https://public.tableau.com/views/AirbnbBookingsAnalysis_17822935752310/DetailedAnalysis?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">
    <img src="https://img.shields.io/badge/📊_Tableau-View_Live_Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Tableau Dashboard"/>
  </a>
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Complete-00C853?style=for-the-badge" alt="Status"/>
  &nbsp;
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"/>
</p>

---

## 📊 Dashboard Preview

<p align="center">
  <a href="https://public.tableau.com/views/AirbnbBookingsAnalysis_17822935752310/DetailedAnalysis?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">
    <img src="assets/dashboard_preview.png" alt="Dashboard Preview" width="800"/>
  </a>
</p>

<p align="center"><em>Click the image to explore the interactive dashboard on Tableau Public →</em></p>

---

## 🎯 Project Overview

### Objective
Analyze Airbnb booking patterns across European hospitality markets to identify **revenue optimization opportunities**, **seasonal demand patterns**, and **high-value guest segments** — enabling data-driven pricing and marketing decisions.

### Key Questions Answered
- Which countries generate the highest revenue vs. booking volume?
- What seasonal patterns drive demand and pricing?
- How do room types differ in performance and profitability?
- What does the guest composition and booking behavior look like?
- Where are the biggest opportunities for revenue growth?

---

## 📈 Key Findings at a Glance

<table>
<tr>
<td align="center"><h3>$91K</h3><sub>Total Revenue</sub></td>
<td align="center"><h3>$91</h3><sub>Avg. Daily Rate</sub></td>
<td align="center"><h3>999</h3><sub>Total Bookings</sub></td>
<td align="center"><h3>1.5%</h3><sub>Cancellation Rate</sub></td>
</tr>
</table>

### 🌍 Geographic Insights
| Rank | Country | Bookings | Revenue | Avg ADR | Insight |
|------|---------|----------|---------|---------|---------|
| 1 | 🇵🇹 Portugal | 324 (32%) | $25,804 | $79.64 | High-volume, below-avg ADR |
| 2 | 🇪🇸 Spain | 182 (18%) | $13,854 | $76.12 | Price-sensitive segment |
| 3 | 🇫🇷 France | 110 (11%) | $10,326 | $93.88 | Balanced volume & value |
| 4 | 🇬🇧 United Kingdom | 65 (7%) | $7,227 | $111.18 | **High-value segment** |
| 5 | 🇮🇹 Italy | 36 (4%) | $4,816 | $133.76 | **Highest ADR — premium guests** |

> **Insight**: Portugal + Spain account for **50.6% of bookings** but only **43.5% of revenue**. Italy and UK guests pay **47–67% higher ADR** — targeted marketing toward these segments could significantly boost revenue per booking.

### 📅 Seasonal Revenue Trends
```
Sep  ████████████████████████████████████████████████  $46K (50.5%) ← PEAK MONTH
Oct  ████████████████████████                          $20K (22.2%)
Aug  ████████████                                      $11K (11.6%)
Nov  █████████                                          $8K  (8.5%)
Dec  ███████                                            $6K  (6.8%)
Jul  █                                                 $0.3K (0.4%)
```

### 🏡 Room Type Performance
| Room Type | Bookings | Share | Avg ADR | Revenue |
|-----------|----------|-------|---------|---------|
| Entire Place | 797 | 79.7% | $91.00 | $72,523 |
| Private Room | 84 | 8.4% | $97.07 | $8,154 |
| Treehouse | 50 | 5.0% | $85.17 | $4,259 |
| Shared Room | 32 | 3.2% | $98.19 | $3,142 |
| Tiny Room | 16 | 1.6% | $108.18 | $1,731 |
| Cabin | 8 | 0.8% | $96.51 | $772 |

---

## 🗂️ Data Architecture

### Star Schema Design

```
                    ┌──────────────┐
                    │  dim_budget  │
                    │──────────────│
                    │ CountryName  │
                    │ Budget       │
                    └──────┬───────┘
                           │
┌──────────────┐   ┌───────┴────────────┐   ┌──────────────┐
│  dim_owner   │───│  airbnb_bookings   │───│   dim_room   │
│──────────────│   │  (FACT TABLE)      │   │──────────────│
│ OwnerID      │   │────────────────────│   │ RoomCode     │
│ OwnerName    │   │ 999 rows × 32 cols │   │ RoomInfo     │
│ Phone        │   │ Bookings, Revenue, │   └──────────────┘
│ ImageURL     │   │ Guests, Dates ...  │
└──────────────┘   └────────────────────┘
```

### Data Sources

| File | Records | Description |
|------|---------|-------------|
| [`data/airbnb_bookings.csv`](data/airbnb_bookings.csv) | 999 rows × 32 cols | Core fact table with booking transactions |
| [`data/dim_budget.csv`](data/dim_budget.csv) | 19 rows | Marketing budget allocation by country |
| [`data/dim_owner.csv`](data/dim_owner.csv) | 36 rows | Property owner profiles with contact info |
| [`data/dim_room.csv`](data/dim_room.csv) | 9 rows | Room type reference mapping (A–K) |

---

## 📋 Data Dictionary

<details>
<summary><strong>Click to expand full data dictionary (32 columns)</strong></summary>

| Column | Type | Description |
|--------|------|-------------|
| `ArrivalDateYear` | int | Year of arrival (2015) |
| `ArrivalDateMonth` | str | Month of arrival (July–December) |
| `ArrivalDateDayOfMonth` | int | Day of month (1–31) |
| `ArrivalDateWeekNumber` | int | ISO week number (28–53) |
| `Owner` | int | Foreign key to dim_owner (property owner ID) |
| `AssignedRoomType` | str | Room type code (A–K), maps to dim_room |
| `Company` | int | Company ID for corporate bookings (sparse) |
| `Country` | str | Guest country — ISO 3166-1 alpha-3 code |
| `CountryName` | str | Guest country — full name |
| `CustomerType` | str | Contract / Transient / Transient-Party |
| `DepositType` | str | Deposit type (No Deposit / Non Refund / Refundable) |
| `DistributionChannel` | str | Booking channel (TA/TO, Direct, Corporate) |
| `AirBnBType` | str | Property location quality (Prime / Non-Prime) |
| `MarketSegment` | str | Market segment (Online TA, Groups, Direct, etc.) |
| `Meal` | str | Meal package code (BB, HB, FB, SC) |
| `Mealgroup` | str | Meal package description |
| `ReservationStatus` | str | Final status (Check-Out, Canceled, No-Show) |
| `ReservationStatusDate` | str | Date of last status update |
| `ReservedRoomType` | str | Originally reserved room type |
| `AmountPaid` | float | Total amount paid per booking (ADR proxy) |
| `Adults` | int | Number of adult guests |
| `Children` | int | Number of children |
| `Babies` | int | Number of babies |
| `BookingChanges` | int | Number of modifications to the booking |
| `DaysInWL` | int | Days the booking spent on waiting list |
| `IsCanceled` | int | Cancellation flag (0/1) |
| `IsRepeatedGuest` | int | Repeat guest flag (0/1) |
| `LeadTime` | int | Days between booking and arrival |
| `PreviousBookingsNC` | int | Previous non-canceled bookings by guest |
| `PreviousCancellations` | int | Previous cancellations by guest |
| `RequiredCarParkingSpaces` | int | Parking spaces requested |
| `StaysWeekNights` | int | Number of weeknight stays |
| `StaysWeekendNights` | int | Number of weekend night stays |
| `Special Requests` | int | Number of special requests (0–4) |
| `Reviews` | int | Guest review rating (1–5) |

</details>

---

## 🛠️ Tools & Technologies

<table>
<tr>
<td align="center"><img src="https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white" alt="Tableau"/><br><sub>Dashboard & Viz</sub></td>
<td align="center"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/><br><sub>Data Processing</sub></td>
<td align="center"><img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/><br><sub>Data Analysis</sub></td>
<td align="center"><img src="https://img.shields.io/badge/AWS_Redshift-FF9900?style=flat-square&logo=amazonaws&logoColor=white" alt="Redshift"/><br><sub>Cloud Data Warehouse</sub></td>
<td align="center"><img src="https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white" alt="Excel"/><br><sub>Data Preparation</sub></td>
</tr>
</table>

---

## 🔍 Methodology

```
1. Data Collection        → Acquired raw booking data (999 records, 32 attributes)
         ↓
2. Data Cleaning          → Handled nulls, standardized column names, validated types
         ↓
3. Schema Design          → Built star schema with 1 fact table + 3 dimension tables
         ↓
4. Exploratory Analysis   → Statistical profiling, distribution analysis, outlier detection
         ↓
5. Dashboard Development  → Built interactive Tableau dashboard with filters & drill-downs
         ↓
6. Insight Generation     → Synthesized findings into actionable business recommendations
```

---

## 💡 Actionable Recommendations

| Priority | Recommendation | Expected Impact |
|----------|---------------|-----------------|
| 🔴 High | **Target UK & Italy markets** — guests pay 47–67% higher ADR | +15–20% revenue per booking |
| 🔴 High | **Implement guest retention program** — 0% repeat guest rate | Reduce acquisition costs, boost LTV |
| 🟡 Medium | **Optimize September pricing** — peak demand supports premium rates | +8–12% peak season revenue |
| 🟡 Medium | **Increase direct bookings** — 89.5% via TA/TO incurs commissions | Reduce 15–20% commission costs |
| 🟢 Low | **Investigate Tiny Room pricing** — highest ADR ($108) with low supply | Potential for inventory expansion |

---

## 📁 Repository Structure

```
airbnb-hospitality-analysis/
├── 📊 assets/
│   ├── airbnb_logo.png          # Brand assets
│   └── dashboard_preview.png    # Dashboard screenshot
├── 📁 data/
│   ├── airbnb_bookings.csv      # Fact table (999 bookings)
│   ├── dim_budget.csv           # Country budget dimension
│   ├── dim_owner.csv            # Property owner dimension
│   └── dim_room.csv             # Room type dimension
├── 🐍 scripts/
│   ├── csv_to_redshift.py       # ETL: CSV → AWS Redshift loader
│   └── fake_data_generator.py   # Synthetic data generation utility
├── 📄 docs/
│   └── DATA_DICTIONARY.md       # Detailed column documentation
├── 📄 README.md                 # Project documentation (this file)
├── 📄 LICENSE                   # MIT License
└── 📄 .gitignore                # Git ignore rules
```

---

## 🚀 Getting Started

### Prerequisites
- [Tableau Public](https://public.tableau.com/) (for dashboard viewing)
- Python 3.x (for running scripts)
- `pip install pandas faker sqlalchemy psycopg2-binary`

### Quick Start
```bash
# Clone the repository
git clone https://github.com/whyabhiiiii/airbnb-hospitality-analysis.git
cd airbnb-hospitality-analysis

# Install dependencies
pip install pandas faker

# Generate synthetic owner data
python scripts/fake_data_generator.py

# View the live dashboard
open "https://public.tableau.com/views/AirbnbBookingsAnalysis_17822935752310/DetailedAnalysis"
```

---

## 📬 Connect

**Abhishek Kumar** — Data Analyst

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/whyabhiiiii/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/whyabhiiiii)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=flat-square&logo=gmail)](mailto:workwithabhi19@gmail.com)

---

<p align="center">
  <sub>⭐ Star this repo if you found the analysis useful!</sub>
</p>
