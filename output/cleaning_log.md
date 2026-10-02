# Cleaning log

## Rows pulled

| Committee | Processed rows (cycle 2026) | E-file feed rows | Pulled at |
|---|---|---|---|
| CLF | 249 | 263 | 2026-10-02T12:12:10 |
| NRCC | 0 | 0 | 2026-10-02T12:12:14 |
| SLF | 430 | 323 | 2026-10-02T12:12:31 |
| Texas PAC | 35 | 35 | 2026-10-02T12:28:54 |
| NRSC | 0 | 0 | 2026-10-02T12:12:36 |
| MAGA Inc. | 75 | 9 | 2026-10-02T12:12:46 |
| No Going Back PAC | 746 | 746 | 2026-10-02T12:14:11 |
| Safety & Affordability PAC | 3 | 3 | 2026-10-02T12:14:25 |
| HMP | 442 | 599 | 2026-10-02T12:14:45 |
| DCCC | 0 | 0 | 2026-10-02T12:14:49 |
| SMP | 0 | 0 | 2026-10-02T12:14:54 |
| WinSenate | 189 | 207 | 2026-10-02T12:17:00 |
| DSCC | 0 | 0 | 2026-10-02T12:14:59 |

## Rows added and dropped at each step

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | HMP | 86 | $9,049,935 |
| 1a. E-file rows added (filings not yet in processed data) | WinSenate | 29 | $40,114,334 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **115** | **$49,164,269** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | HMP | 86 | $9,049,935 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | CLF | 14 | $249,920 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **100** | **$9,299,855** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 95 | $11,781,920 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **95** | **$11,781,920** |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 2 | $2,060 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **2** | **$2,060** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 6 | $930,876 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 19 | $260,031 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 88 | $6,442,043 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 34 | $12,470,398 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 35 | $2,535,973 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **182** | **$22,639,321** |
| 5. Dropped: not 2026 general (G2024) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (G2024) | **All** | **3** | **$30,906** |
| 5. Dropped: not 2026 general (P2026) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (P2026) | SLF | 83 | $6,844,268 |
| 5. Dropped: not 2026 general (P2026) | WinSenate | 6 | $1,488,396 |
| 5. Dropped: not 2026 general (P2026) | **All** | **110** | **$8,596,904** |
| 5. Dropped: not 2026 general (R2026) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (R2026) | **All** | **2** | **$827,711** |
| 5. Dropped: not 2026 general (S2025) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (S2025) | MAGA Inc. | 31 | $1,690,361 |
| 5. Dropped: not 2026 general (S2025) | **All** | **37** | **$2,621,237** |
| 5. Dropped: not 2026 general (S2026) | MAGA Inc. | 2 | $17,901 |
| 5. Dropped: not 2026 general (S2026) | **All** | **2** | **$17,901** |

Final cleaned general-election rows: **1851**, $631,682,451.

Latest regular-report coverage end date used for the notice cut-off: CLF 2026-06-30; NRCC 2026-08-31; SLF 2026-06-30; Texas PAC none filed; NRSC 2026-08-31; MAGA Inc. 2026-08-31; No Going Back PAC none filed; Safety & Affordability PAC none filed; HMP 2026-08-31; DCCC 2026-08-31; SMP 2026-06-30; WinSenate 2026-08-31; DSCC 2026-08-31.

## Reconciliation against FEC aggregates

The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour notices. The comparison below therefore uses the regular-report rows in this dataset, across all election types. Spending after the coverage end date has no FEC aggregate to check against.

| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |
|---|---|---|---|---|---|
| CLF | $264,240 | $264,240 | -0.0% | $264,240 (2026-06-30) | -0.0% |
| NRCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| SLF | $6,450,360 | $5,770,959 | +10.5% **(over 2%)** | $6,450,360 (2026-06-30) | +0.0% |
| Texas PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| NRSC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| MAGA Inc. | $2,535,973 | $2,535,973 | +0.0% | $2,535,973 (2026-08-31) | +0.0% |
| No Going Back PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| Safety & Affordability PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| HMP | $961,782 | $961,782 | +0.0% | $961,782 (2026-08-31) | +0.0% |
| DCCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| SMP | $0 | $0 | n/a | $0 (2026-06-30) | n/a |
| WinSenate | $12,464,041 | $12,464,041 | +0.0% | $12,464,041 (2026-08-31) | +0.0% |
| DSCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |

### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)

| Committee | Race | Regular-report rows here | FEC by_candidate |
|---|---|---|---|
| SLF | MI-SEN | $1,078,706 | $747,656 |
| SLF | NH-SEN | $239,116 | $11,166 |
| SLF | OH-SEN | $1,154,416 | $1,034,015 |

## Expenditures not mapped to a race

None. Every general-election row carried an office, state and (for House) district.

## Most recent transaction per committee

| Committee | Latest date in cleaned general-election data | Latest filing received | Rows | Total |
|---|---|---|---|---|
| CLF | 2026-09-29 | 2026-10-01 | 209 | $42,731,086 |
| NRCC | no general-election IEs | n/a | 0 | $0 |
| SLF | 2026-09-30 | 2026-10-01 | 257 | $143,884,822 |
| Texas PAC | 2026-10-01 | 2026-09-30 | 35 | $131,529,652 |
| NRSC | no general-election IEs | n/a | 0 | $0 |
| MAGA Inc. | 2026-09-26 | 2026-09-26 | 5 | $20,000,000 |
| No Going Back PAC | 2026-10-01 | 2026-10-01 | 746 | $127,370,892 |
| Safety & Affordability PAC | 2026-09-30 | 2026-10-01 | 3 | $1,281,250 |
| HMP | 2026-09-29 | 2026-10-01 | 418 | $45,576,106 |
| DCCC | no general-election IEs | n/a | 0 | $0 |
| SMP | no general-election IEs | n/a | 0 | $0 |
| WinSenate | 2026-09-29 | 2026-10-01 | 178 | $119,308,644 |
| DSCC | no general-election IEs | n/a | 0 | $0 |
