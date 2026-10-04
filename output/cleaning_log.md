# Cleaning log

Data pulled 2026-10-04T15:33:33.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 39,816 from 782 committees
- Raw e-file feed rows from filings received in the last 7 days: 2,946

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 233 | $15,041,516 |
| 1a. E-file rows added (filings not yet in processed data) | SLF | 9 | $199,364 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **242** | **$15,240,880** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 57 | $1,833,374 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **57** | **$1,833,374** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 1,476 | $102,514,357 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 209 | $23,248,483 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **1,685** | **$125,762,840** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 1,634 | $8,017,590,819 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 2 | $2,060 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **1,636** | **$8,017,592,879** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 11,518 | $792,755,257 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 34 | $12,470,398 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 88 | $6,442,043 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 35 | $2,535,973 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 6 | $930,876 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 19 | $260,031 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **11,700** | **$815,394,577** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 465 | $1,001,116,987 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **468** | **$1,001,147,893** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 74 | $2,189,921 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **74** | **$2,189,921** |
| 5. Dropped: not 2026 general (other) | All other committees | 32 | $1,003,179,171 |
| 5. Dropped: not 2026 general (other) | **All** | **32** | **$1,003,179,171** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,764 | $1,707,039,761 |
| 5. Dropped: not 2026 general (primary) | SLF | 83 | $6,844,268 |
| 5. Dropped: not 2026 general (primary) | WinSenate | 6 | $1,488,396 |
| 5. Dropped: not 2026 general (primary) | North Star | 2 | $1,010,128 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **12,876** | **$1,716,646,793** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 691 | $63,664,591 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **693** | **$64,492,302** |
| 5. Dropped: not 2026 general (special) | All other committees | 662 | $24,367,342 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **701** | **$27,006,480** |

Final cleaned general-election independent expenditure rows: **10,079**, $1,148,804,187.

Coordinated party expenditure rows added (Schedule F): **267**, $62,898,456.
- NRSC filing 2014360: 54 Schedule F rows read from the raw filing because the API had not loaded them

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-06-30; SLF 2026-06-30; Texas PAC none filed; Cornhusker Majority none filed; The Maine Standard none filed; MAGA Inc. 2026-08-31; No Going Back PAC none filed; Safety & Affordability PAC none filed; HMP 2026-08-31; SMP 2026-06-30; WinSenate 2026-08-31; Texas Forever none filed; North Star none filed; The Georgia Way 2026-06-30. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

42 rows, $1,000,283,203. These are left out of the tables and charts.

| Race | Candidate | Party | Support/oppose | Rows | Amount |
|---|---|---|---|---|---|
| FL-SEN | BETTIS, SHAWN STEFAN | nan | S | 1 | $1,000,000,000 |
| IA-01 | BRIDGFORD, MICHAEL | IND | S | 6 | $158,561 |
| NY-23 | LANGWORTHY, NICK | nan | S | 1 | $95,900 |
| IA-03 | BALDACCI, JOHN ELIAS | nan | O | 9 | $15,923 |
| TX-03 | SELF, KEITH ALAN MR | nan | S | 12 | $9,613 |
| TX-28 | CUELLER, ENRIQUE ROBERTO | nan | S | 1 | $2,058 |
| WI-04 | BURKS, ARTHUR | nan | S | 5 | $856 |
| IN-03 | STUTZMAN, MARLIN | nan | S | 5 | $178 |
| OH-13 | SKYES, EMILIA | nan | S | 1 | $105 |
| NY-18 | RYAN, PATRICK | nan | S | 1 | $10 |

89 rows ($4,871,269) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

## Reconciliation against FEC aggregates

The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour notices. The comparison below therefore uses the regular-report rows in this dataset, across all election types, for the named committees. Spending after the coverage end date, and spending by the other committees, has no FEC aggregate checked here.

| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |
|---|---|---|---|---|---|
| CLF | $264,240 | $264,240 | -0.0% | $264,240 (2026-06-30) | -0.0% |
| NRCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| SLF | $6,450,360 | $5,770,959 | +10.5% **(over 2%)** | $6,450,360 (2026-06-30) | +0.0% |
| Texas PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| Cornhusker Majority | $0 | $0 | n/a | $0 (n/a) | n/a |
| The Maine Standard | $0 | $0 | n/a | $0 (n/a) | n/a |
| NRSC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| MAGA Inc. | $2,535,973 | $2,535,973 | +0.0% | $2,535,973 (2026-08-31) | +0.0% |
| No Going Back PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| Safety & Affordability PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| HMP | $961,782 | $961,782 | +0.0% | $961,782 (2026-08-31) | +0.0% |
| DCCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| SMP | $0 | $0 | n/a | $0 (2026-06-30) | n/a |
| WinSenate | $12,464,041 | $12,464,041 | +0.0% | $12,464,041 (2026-08-31) | +0.0% |
| Texas Forever | $0 | $0 | n/a | $0 (n/a) | n/a |
| North Star | $0 | $0 | n/a | $0 (n/a) | n/a |
| The Georgia Way | $0 | $0 | n/a | $0 (2026-06-30) | n/a |
| DSCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |

### Coordinated party expenditures

| Committee | Schedule F rows here (House and Senate) | FEC committee-total coordinated expenditures (through) | Gap |
|---|---|---|---|
| NRCC | $8,311,565 | $8,311,579 (2026-08-31) | -0.0% |
| NRSC | $48,146,800 | $48,146,800 (2026-08-31) | +0.0% |
| DCCC | $5,243,971 | $5,243,985 (2026-08-31) | -0.0% |
| DSCC | $1,196,120 | $1,196,131 (2026-08-31) | -0.0% |

### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)

| Committee | Race | Regular-report rows here | FEC by_candidate |
|---|---|---|---|
| SLF | MI-SEN | $1,078,706 | $747,656 |
| SLF | NH-SEN | $239,116 | $11,166 |
| SLF | OH-SEN | $1,154,416 | $1,034,015 |

## Expenditures not mapped to a race

7 general-election rows, $12,000,000,300, had no usable state or House district. Largest:

| Committee | Candidate | Office | State | District | Amount | Date | Filing |
|---|---|---|---|---|---|---|---|
| None | BETTIS, SHAWN STEFAN | H | FL | None | $9,000,000,000 | 2026-04-03 | 1957531 |
| None | BETTIS, SHAWN STEFAN | H | CA | None | $1,000,000,000 | 2026-05-15 | 1975315 |
| None | BETTIS, SHAWN STEFAN | H | CA | None | $1,000,000,000 | 2026-05-14 | 1975235 |
| None | BETTIS, SHAWN STEFAN | H | FL | None | $1,000,000,000 | 2026-04-22 | 1970917 |
| None | BETTIS, SHAWN STEFAN | H | FL | None | $100 | 2026-07-06 | 1989236 |
| None | BETTIS, SHAWN STEFAN | H | None | None | $100 | 2026-06-25 | 1986763 |
| None | BETTIS, SHAWN STEFAN | H | CA | None | $100 | 2026-05-26 | 1979441 |

## Most recent transaction per spender

| Spender | Latest date in cleaned data | Latest filing received | Rows | Total |
|---|---|---|---|---|
| CLF | 2026-10-01 | 2026-10-03 | 285 | $67,748,035 |
| NRCC | 2026-08-31 | n/a | 67 | $8,311,565 |
| SLF | 2026-10-02 | 2026-10-04 | 287 | $167,150,488 |
| Texas PAC | 2026-10-01 | 2026-10-02 | 36 | $131,564,652 |
| Cornhusker Majority | 2026-09-30 | 2026-10-02 | 15 | $4,745,568 |
| The Maine Standard | 2026-09-30 | 2026-10-02 | 5 | $3,748,587 |
| NRSC | 2026-08-31 | n/a | 67 | $48,146,800 |
| MAGA Inc. | 2026-10-03 | 2026-10-03 | 6 | $25,000,000 |
| No Going Back PAC | 2026-10-02 | 2026-10-03 | 786 | $128,265,960 |
| Safety & Affordability PAC | 2026-09-30 | 2026-10-01 | 3 | $1,281,250 |
| Other R | 2026-10-04 | 2026-10-04 | 3,664 | $243,364,408 |
| HMP | 2026-10-02 | 2026-10-02 | 446 | $47,992,734 |
| DCCC | 2026-08-31 | n/a | 100 | $5,243,971 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-09-30 | 2026-10-02 | 172 | $103,150,097 |
| Texas Forever | 2026-09-29 | 2026-10-01 | 2 | $2,113,210 |
| North Star | 2026-09-30 | 2026-10-02 | 24 | $6,350,418 |
| The Georgia Way | 2026-09-29 | 2026-10-01 | 7 | $6,100,125 |
| DSCC | 2026-08-31 | n/a | 33 | $1,196,120 |
| Other D | 2026-10-04 | 2026-10-04 | 4,252 | $205,357,385 |
