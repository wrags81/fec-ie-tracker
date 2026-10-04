# Cleaning log

## Rows pulled

| Committee | Processed rows (cycle 2026) | E-file feed rows | Pulled at |
|---|---|---|---|
| CLF | 325 | 309 | 2026-10-04T18:51:28 |
| NRCC | 0 | 0 | 2026-10-04T18:51:31 |
| SLF | 451 | 352 | 2026-10-04T18:51:41 |
| Texas PAC | 36 | 36 | 2026-10-04T18:51:44 |
| NRSC | 0 | 0 | 2026-10-04T18:51:48 |
| MAGA Inc. | 76 | 10 | 2026-10-04T18:51:53 |
| No Going Back PAC | 786 | 786 | 2026-10-04T18:52:07 |
| Safety & Affordability PAC | 3 | 3 | 2026-10-04T18:52:10 |
| HMP | 670 | 655 | 2026-10-04T18:52:25 |
| DCCC | 0 | 0 | 2026-10-04T18:52:29 |
| SMP | 0 | 0 | 2026-10-04T18:53:33 |
| WinSenate | 212 | 214 | 2026-10-04T18:53:41 |
| DSCC | 0 | 0 | 2026-10-04T18:53:45 |

## Rows added and dropped at each step

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | SLF | 8 | $196,304 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **8** | **$196,304** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 209 | $23,248,483 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **209** | **$23,248,483** |
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

Final cleaned general-election rows: **2020**, $672,150,157.

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
| CLF | 2026-10-01 | 2026-10-03 | 285 | $67,748,035 |
| NRCC | no general-election IEs | n/a | 0 | $0 |
| SLF | 2026-10-02 | 2026-10-04 | 286 | $167,147,428 |
| Texas PAC | 2026-10-01 | 2026-10-02 | 36 | $131,564,652 |
| NRSC | no general-election IEs | n/a | 0 | $0 |
| MAGA Inc. | 2026-10-03 | 2026-10-03 | 6 | $25,000,000 |
| No Going Back PAC | 2026-10-02 | 2026-10-03 | 786 | $128,265,960 |
| Safety & Affordability PAC | 2026-09-30 | 2026-10-01 | 3 | $1,281,250 |
| HMP | 2026-10-02 | 2026-10-02 | 446 | $47,992,734 |
| DCCC | no general-election IEs | n/a | 0 | $0 |
| SMP | no general-election IEs | n/a | 0 | $0 |
| WinSenate | 2026-09-30 | 2026-10-02 | 172 | $103,150,097 |
| DSCC | no general-election IEs | n/a | 0 | $0 |
