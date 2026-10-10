# Cleaning log

Data pulled 2026-10-10T13:15:01.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 44,548 from 819 committees
- Raw e-file feed rows from filings received in the last 7 days: 6,534 distinct transactions (13,068 rows returned across overlapping pages)

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | CLF | 69 | $32,788,021 |
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 1,017 | $28,694,895 |
| 1a. E-file rows added (filings not yet in processed data) | WinSenate | 10 | $6,405,182 |
| 1a. E-file rows added (filings not yet in processed data) | Cornhusker Majority | 4 | $1,928,738 |
| 1a. E-file rows added (filings not yet in processed data) | HMP | 27 | $1,880,196 |
| 1a. E-file rows added (filings not yet in processed data) | The Maine Standard | 4 | $1,327,668 |
| 1a. E-file rows added (filings not yet in processed data) | SLF | 2 | $414,282 |
| 1a. E-file rows added (filings not yet in processed data) | Texas Forever | 1 | $21,507 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **1,134** | **$73,460,489** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | All other committees | 264 | $708,786 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **264** | **$708,786** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 157 | $11,980,068 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **157** | **$11,980,068** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 1,982 | $117,406,144 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 304 | $35,042,403 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **2,286** | **$152,448,547** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 1,709 | $8,016,665,228 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 2 | $2,060 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **1,711** | **$8,016,667,288** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 12,070 | $802,695,329 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 34 | $12,470,398 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 88 | $6,442,043 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 35 | $2,535,973 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 6 | $930,876 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 19 | $260,031 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **12,252** | **$825,334,650** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 465 | $1,001,116,987 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **468** | **$1,001,147,893** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 148 | $1,069,055 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **148** | **$1,069,055** |
| 5. Dropped: not 2026 general (other) | All other committees | 29 | $1,002,979,171 |
| 5. Dropped: not 2026 general (other) | No Going Back PAC | 2 | $5,151,145 |
| 5. Dropped: not 2026 general (other) | **All** | **31** | **$1,008,130,316** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,746 | $1,706,498,622 |
| 5. Dropped: not 2026 general (primary) | SLF | 83 | $6,844,268 |
| 5. Dropped: not 2026 general (primary) | WinSenate | 6 | $1,488,396 |
| 5. Dropped: not 2026 general (primary) | North Star | 2 | $1,010,128 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **12,858** | **$1,716,105,654** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 686 | $63,330,933 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **688** | **$64,158,644** |
| 5. Dropped: not 2026 general (special) | All other committees | 662 | $24,367,342 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **701** | **$27,006,480** |

Final cleaned general-election independent expenditure rows: **14,306**, $1,498,607,304.

Coordinated party expenditure rows added (Schedule F): **267**, $62,898,441.

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-06-30; SLF 2026-06-30; Texas PAC none filed; Cornhusker Majority none filed; The Maine Standard none filed; MAGA Inc. 2026-08-31; No Going Back PAC none filed; Safety & Affordability PAC none filed; HMP 2026-08-31; SMP 2026-06-30; WinSenate 2026-08-31; Texas Forever none filed; North Star none filed; The Georgia Way 2026-06-30. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

61 rows, $1,000,584,795. These are left out of the tables and charts.

| Race | Candidate | Party | Support/oppose | Rows | Amount |
|---|---|---|---|---|---|
| FL-SEN | BETTIS, SHAWN STEFAN | nan | S | 1 | $1,000,000,000 |
| OH-SEN | LEVY, GREGORY LEE | IND | S | 1 | $198,520 |
| IA-01 | BRIDGFORD, MICHAEL | IND | S | 6 | $158,561 |
| NY-23 | LANGWORTHY, NICK | nan | S | 1 | $95,900 |
| NE-06 | HARDING, BRINKER | nan | O | 17 | $40,637 |
| NM-03 | VASQUEZ, GABE REP. | nan | S | 4 | $38,216 |
| AZ-06 | JUAN, CISCOMANI | REP | nan | 1 | $20,000 |
| TX-03 | SELF, KEITH ALAN MR | nan | S | 12 | $9,613 |
| WI-03 | BERMAN, MITCHELL | nan | S | 1 | $9,000 |
| WI-03 | STEIL, BRYAN | nan | O | 1 | $9,000 |
| ME-SEN | COLLLINS, SUSAN | nan | O | 1 | $3,000 |
| SC-SEN | NORMAN, RALPH | nan | nan | 1 | $1,000 |
| WI-04 | BURKS, ARTHUR | nan | S | 5 | $856 |
| IN-03 | STUTZMAN, MARLIN | nan | S | 5 | $178 |
| OH-13 | SKYES, EMILIA | nan | S | 1 | $105 |
| NJ-07 | BENNET, REBECCA | nan | S | 1 | $100 |
| NJ-78 | BENNETT, REBECCA | nan | S | 1 | $100 |
| NY-18 | RYAN, PATRICK | nan | S | 1 | $10 |

96 rows ($9,860,515) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

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
| NRSC | $48,146,785 | $48,146,800 (2026-08-31) | -0.0% |
| DCCC | $5,243,971 | $5,243,985 (2026-08-31) | -0.0% |
| DSCC | $1,196,120 | $1,196,131 (2026-08-31) | -0.0% |

### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)

| Committee | Race | Regular-report rows here | FEC by_candidate |
|---|---|---|---|
| SLF | MI-SEN | $1,078,706 | $747,656 |
| SLF | NH-SEN | $239,116 | $11,166 |
| SLF | OH-SEN | $1,154,416 | $1,034,015 |

## Rows moved to a different race

These rows were filed under a state or district that disagrees with the candidate's other filings, so they were moved to the candidate's race.

| Committee | Candidate | Reported as | Moved to | Rows | Amount |
|---|---|---|---|---|---|
| ACTIVATE AMERICA | CALVERT, KEN | CA-41 | CA-40 | 9 | $3,516 |
| ACTIVATE AMERICA | KIM, YOUNG | CA-39 | CA-40 | 1 | $1,732 |
| ACTIVATE AMERICA | VALADAO, DAVID | CA-21 | CA-22 | 6 | $2,987 |
| CLUB FOR GROWTH PAC | MIGUEZ, BLAKE | LA-05 | LA-06 | 2 | $4,017 |
| FREEDOM CAUCUS FUND | BOEBERT, LAUREN | CO-03 | CO-04 | 9 | $364,238 |
| FREEDOM CAUCUS FUND | LAUBACHER, EILEEN | CO-03 | CO-04 | 1 | $79,028 |
| GROWING ECONOMIC OPPORTUNITIES | BENNETT, REBECCA | NE-07 | NJ-07 | 1 | $100 |
| INDIGO PAC | GRAY, ADAM | OH-09 | CA-13 | 1 | $95 |
| JOBS & PROSPERITY PAC | POINDEXTER, BRIAN | OH-AL | OH-07 | 1 | $25,000 |
| LATINOS FOR CONSERVATIVE VALUES | PAULINA LUNA, ANNA | FL-03 | FL-13 | 1 | $3,000 |
| LGBTQ CONNECTION PAC | HARDING, BRINKER | NE-06 | NE-02 | 20 | $16,120 |
| NEBRASKA APPLESEED ACTION FUND | OSBORN, DAN | NB-SEN | NE-SEN | 2 | $31,680 |
| NEBRASKA APPLESEED ACTION FUND | POWELL, DENISE | NB-02 | NE-02 | 4 | $66,680 |
| PROGRESSIVE TURNOUT PROJECT | MOSKOWITZ, JARED | FL-23 | FL-25 | 3 | $130,300 |
| STRATEGIC MAJORITY PAC | FITZPATRICK, BRIAN | CA-22 | PA-01 | 1 | $22,910 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | BALDACCI, JOHN ELIAS | IA-03 | ME-02 | 1 | $249 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | EL-SAYED, ABDUL | MN-SEN | MI-SEN | 1 | $1 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | MANZUR, KARISHMA | NC-SEN | NH-SEN | 2 | $166 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | OSBORN, DAN | NV-SEN | NE-SEN | 1 | $92 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | PAPPAS, CHRIS | NC-SEN | NH-SEN | 2 | $166 |
| WHEEL DOG PAC | HILL, BILL | AZ-AL | AK-AL | 1 | $417,562 |

## Expenditures not mapped to a race

7 general-election rows, $12,000,000,300, had no usable state or House district. Largest:

| Committee | Candidate | Office | State | District | Amount | Date | Filing |
|---|---|---|---|---|---|---|---|
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $9,000,000,000 | 2026-04-03 | 1957531 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $1,000,000,000 | 2026-05-15 | 1975315 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $1,000,000,000 | 2026-05-14 | 1975235 |
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $1,000,000,000 | 2026-04-22 | 1970917 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $100 | 2026-05-26 | 1979441 |
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $100 | 2026-07-06 | 1989236 |
| nan | BETTIS, SHAWN STEFAN | H | nan | nan | $100 | 2026-06-25 | 1986763 |

## Most recent transaction per spender

| Spender | Latest date in cleaned data | Latest filing received | Rows | Total |
|---|---|---|---|---|
| CLF | 2026-10-07 | 2026-10-09 | 384 | $101,483,652 |
| NRCC | 2026-08-31 | n/a | 67 | $8,311,565 |
| SLF | 2026-10-08 | 2026-10-10 | 336 | $201,394,576 |
| Texas PAC | 2026-10-07 | 2026-10-09 | 42 | $139,478,790 |
| Cornhusker Majority | 2026-10-07 | 2026-10-09 | 23 | $6,943,097 |
| The Maine Standard | 2026-10-07 | 2026-10-09 | 12 | $5,106,890 |
| NRSC | 2026-08-31 | n/a | 67 | $48,146,785 |
| MAGA Inc. | 2026-10-03 | 2026-10-03 | 6 | $25,000,000 |
| No Going Back PAC | 2026-10-07 | 2026-10-08 | 946 | $149,485,489 |
| Safety & Affordability PAC | 2026-10-07 | 2026-10-09 | 9 | $4,009,025 |
| Other R | 2026-10-10 | 2026-10-10 | 4,986 | $326,269,465 |
| HMP | 2026-10-08 | 2026-10-09 | 634 | $72,481,132 |
| DCCC | 2026-08-31 | n/a | 100 | $5,243,971 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-10-07 | 2026-10-09 | 210 | $133,155,679 |
| Texas Forever | 2026-10-07 | 2026-10-09 | 6 | $5,837,093 |
| North Star | 2026-10-06 | 2026-10-08 | 33 | $9,037,518 |
| The Georgia Way | 2026-10-06 | 2026-10-08 | 9 | $7,120,071 |
| DSCC | 2026-08-31 | n/a | 33 | $1,196,120 |
| Other D | 2026-10-10 | 2026-10-10 | 6,574 | $301,944,311 |
