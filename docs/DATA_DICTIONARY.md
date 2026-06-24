# 📖 Data Dictionary

## Overview

This project uses a **star schema** with 1 fact table and 3 dimension tables to model Airbnb hospitality booking data.

---

## Fact Table: `airbnb_bookings.csv`

**999 booking records** from July–December 2015 across 19 countries.

### Date & Time Attributes

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `ArrivalDateYear` | INT | 2015 | Year of guest arrival |
| `ArrivalDateMonth` | STRING | Jul–Dec | Month name of arrival |
| `ArrivalDateDayOfMonth` | INT | 1–31 | Day of the month |
| `ArrivalDateWeekNumber` | INT | 28–53 | ISO week number |

### Property Attributes

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `Owner` | INT | 1–314 | FK → `dim_owner.OwnerID` |
| `AssignedRoomType` | CHAR | A–K | FK → `dim_room.AssignedRoomType` |
| `AirBnBType` | STRING | 2 values | Prime Location / Non-Prime Location |
| `Company` | INT | — | Corporate booking company ID (99.3% null) |

### Guest Attributes

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `Country` | STRING | 19 values | Guest's country of origin (ISO 3166-1 alpha-3) |
| `CountryName` | STRING | 19 values | Full country name |
| `CustomerType` | STRING | 3 values | Contract / Transient / Transient-Party |
| `Adults` | INT | 0–3 | Number of adult guests |
| `Children` | INT | 0–3 | Number of child guests |
| `Babies` | INT | 0–1 | Number of infant guests |
| `IsRepeatedGuest` | INT | 0 | Whether the guest has stayed before |

### Booking Attributes

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `LeadTime` | INT | 0–256 | Days between booking creation and arrival |
| `DepositType` | STRING | 1 value | Deposit category (all "No Deposit") |
| `DistributionChannel` | STRING | 3 values | TA/TO, Direct, Corporate |
| `MarketSegment` | STRING | 6 values | Online TA, Groups, Offline TA/TO, Direct, Complementary, Corporate |
| `BookingChanges` | INT | 0–20 | Number of modifications post-booking |
| `DaysInWL` | INT | 0–89 | Days spent on waiting list |
| `PreviousBookingsNC` | INT | 0 | Guest's prior non-canceled bookings |
| `PreviousCancellations` | INT | 0 | Guest's prior cancellations |

### Stay Attributes

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `StaysWeekNights` | INT | 0–20 | Number of weeknight stays (Mon–Fri) |
| `StaysWeekendNights` | INT | 0–9 | Number of weekend night stays (Sat–Sun) |
| `Meal` | STRING | 4 values | BB (Bed & Breakfast), HB (Half Board), FB (Full Board), SC (Self-Catering) |
| `Mealgroup` | STRING | — | Meal type description |
| `RequiredCarParkingSpaces` | INT | 0–1 | Parking spaces requested |
| `Special Requests` | INT | 0–4 | Number of special requests made |

### Outcome Attributes

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `ReservationStatus` | STRING | 3 values | Check-Out (98.5%), Canceled (1.4%), No-Show (0.1%) |
| `ReservationStatusDate` | STRING | — | Date of last status change |
| `ReservedRoomType` | STRING | 7 values | Originally requested room type |
| `AmountPaid` | FLOAT | 0–212 | Total amount paid for the stay |
| `IsCanceled` | INT | 0–1 | Binary cancellation flag |
| `Reviews` | INT | 1–5 | Guest satisfaction rating |

---

## Dimension Table: `dim_owner.csv`

**36 property owner profiles.**

| Column | Type | Description |
|--------|------|-------------|
| `Owner Id` | INT (PK) | Unique owner identifier |
| `Owner Name` | STRING | Owner's full name |
| `Owner Phone` | STRING | Contact phone number (+91 format) |
| `Owner Image` | URL | Profile picture from randomuser.me |

---

## Dimension Table: `dim_room.csv`

**9 room type classifications.**

| Column | Type | Description |
|--------|------|-------------|
| `Assigned Room Type` | CHAR (PK) | Room code (A, B, C, D, E, F, G, H, K) |
| `Room Information` | STRING | Room type name |

### Room Type Mapping

| Code | Type | Description |
|------|------|-------------|
| A | Entire Place | Full property rental |
| B | Treehouse | Unique stay — treehouse |
| C | Luxury Room | Premium room category |
| D | Private Room | Private room in shared property |
| E | Shared Room | Shared dormitory-style room |
| F | Tiny Room | Compact/micro room |
| G | Cabin | Cabin-style accommodation |
| H | Studio Room | Studio apartment |
| K | Yurt | Unique stay — yurt/tent |

---

## Dimension Table: `dim_budget.csv`

**19 country-level marketing budget allocations.**

| Column | Type | Description |
|--------|------|-------------|
| `Country Name` | STRING (PK) | Country name (matches fact table) |
| `Budget` | BIGINT | Allocated marketing budget |

---

## Data Quality Notes

| Issue | Severity | Affected Column(s) |
|-------|----------|-------------------|
| 66 null values (~6.6%) | Medium | `Owner`, `Country`, `CountryName` |
| 993 null values (99.3%) | High | `Company` |
| Zero variance (constant) | Low | `DepositType`, `IsRepeatedGuest`, `PreviousBookingsNC`, `PreviousCancellations` |
| Only H2 2015 data | Medium | `ArrivalDateYear`, `ArrivalDateMonth` |
| Yurt rooms show $0 revenue | High | `AmountPaid` where `AssignedRoomType = K` |
