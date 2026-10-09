# Cleaning log

Data pulled 2026-10-09T09:57:29.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 42,995 from 807 committees
- Raw e-file feed rows from filings received in the last 7 days: 5,752 distinct transactions (11,504 rows returned across overlapping pages)

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 939 | $35,010,860 |
| 1a. E-file rows added (filings not yet in processed data) | HMP | 241 | $33,722,089 |
| 1a. E-file rows added (filings not yet in processed data) | CLF | 6 | $126,868 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **1,186** | **$68,859,817** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | All other committees | 175 | $523,393 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **175** | **$523,393** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | HMP | 190 | $23,575,839 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 142 | $17,149,962 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **332** | **$40,725,801** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 1,881 | $106,404,739 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 114 | $11,466,564 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **1,995** | **$117,871,302** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 1,651 | $8,016,926,015 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 2 | $2,060 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **1,653** | **$8,016,928,075** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 11,882 | $801,080,673 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 34 | $12,470,398 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 88 | $6,442,043 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 35 | $2,535,973 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 6 | $930,876 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 19 | $260,031 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **12,064** | **$823,719,994** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 465 | $1,001,116,987 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **468** | **$1,001,147,893** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 123 | $341,653 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **123** | **$341,653** |
| 5. Dropped: not 2026 general (other) | All other committees | 32 | $1,003,179,171 |
| 5. Dropped: not 2026 general (other) | No Going Back PAC | 2 | $5,151,145 |
| 5. Dropped: not 2026 general (other) | **All** | **34** | **$1,008,330,316** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,782 | $1,707,563,675 |
| 5. Dropped: not 2026 general (primary) | SLF | 83 | $6,844,268 |
| 5. Dropped: not 2026 general (primary) | WinSenate | 6 | $1,488,396 |
| 5. Dropped: not 2026 general (primary) | North Star | 2 | $1,010,128 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **12,894** | **$1,717,170,707** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 686 | $63,330,933 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **688** | **$64,158,644** |
| 5. Dropped: not 2026 general (special) | All other committees | 662 | $24,367,342 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **701** | **$27,006,480** |

Final cleaned general-election independent expenditure rows: **13,154**, $1,384,858,885.

Coordinated party expenditure rows added (Schedule F): **267**, $62,898,441.

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-06-30; SLF 2026-06-30; Texas PAC none filed; Cornhusker Majority none filed; The Maine Standard none filed; MAGA Inc. 2026-08-31; No Going Back PAC none filed; Safety & Affordability PAC none filed; HMP 2026-08-31; SMP 2026-06-30; WinSenate 2026-08-31; Texas Forever none filed; North Star none filed; The Georgia Way 2026-06-30. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

60 rows, $1,000,581,795. These are left out of the tables and charts.

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
| WI-03 | STEIL, BRYAN | nan | O | 1 | $9,000 |
| WI-03 | BERMAN, MITCHELL | nan | S | 1 | $9,000 |
| SC-SEN | NORMAN, RALPH | nan | nan | 1 | $1,000 |
| WI-04 | BURKS, ARTHUR | nan | S | 5 | $856 |
| IN-03 | STUTZMAN, MARLIN | nan | S | 5 | $178 |
| OH-13 | SKYES, EMILIA | nan | S | 1 | $105 |
| NJ-78 | BENNETT, REBECCA | nan | S | 1 | $100 |
| NJ-07 | BENNET, REBECCA | nan | S | 1 | $100 |
| NY-18 | RYAN, PATRICK | nan | S | 1 | $10 |

67 rows ($5,901,474) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

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
| INDIGO PAC | GRAY, ADAM | OH-09 | CA-13 | 1 | $95 |
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
| CLF | 2026-10-06 | 2026-10-08 | 315 | $68,695,630 |
| NRCC | 2026-08-31 | n/a | 67 | $8,311,565 |
| SLF | 2026-10-06 | 2026-10-08 | 306 | $174,950,958 |
| Texas PAC | 2026-10-06 | 2026-10-08 | 40 | $138,730,868 |
| Cornhusker Majority | 2026-10-06 | 2026-10-08 | 19 | $5,014,359 |
| The Maine Standard | 2026-10-06 | 2026-10-08 | 8 | $3,779,222 |
| NRSC | 2026-08-31 | n/a | 67 | $48,146,785 |
| MAGA Inc. | 2026-10-03 | 2026-10-03 | 6 | $25,000,000 |
| No Going Back PAC | 2026-10-07 | 2026-10-08 | 946 | $149,485,489 |
| Safety & Affordability PAC | 2026-09-30 | 2026-10-01 | 3 | $1,281,250 |
| Other R | 2026-10-10 | 2026-10-09 | 4,666 | $311,101,224 |
| HMP | 2026-10-06 | 2026-10-08 | 607 | $70,600,895 |
| DCCC | 2026-08-31 | n/a | 100 | $5,243,971 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-10-06 | 2026-10-08 | 200 | $126,750,497 |
| Texas Forever | 2026-10-06 | 2026-10-08 | 5 | $5,815,586 |
| North Star | 2026-10-06 | 2026-10-08 | 33 | $9,037,518 |
| The Georgia Way | 2026-10-06 | 2026-10-08 | 9 | $7,120,071 |
| DSCC | 2026-08-31 | n/a | 33 | $1,196,120 |
| Other D | 2026-10-10 | 2026-10-09 | 5,924 | $281,593,844 |
