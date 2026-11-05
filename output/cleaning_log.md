# Cleaning log

Data pulled 2026-11-05T15:15:33.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 73,195 from 1,045 committees
- Raw e-file feed rows from filings received in the last 7 days: 9,248 distinct transactions (18,496 rows returned across overlapping pages)

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 893 | $11,632,925 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **893** | **$11,632,925** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | All other committees | 77 | $22,568 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **77** | **$22,568** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 354 | $1,250,977 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **354** | **$1,250,977** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 3,881 | $189,272,425 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 304 | $35,042,403 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **4,185** | **$224,314,827** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 2,654 | $8,026,898,681 |
| 3. Dropped: memo / memoed-subtotal rows | HMP | 18 | $1,103,316 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 2 | $2,060 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **2,674** | **$8,028,004,057** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 14,690 | $944,240,910 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 494 | $248,266,539 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | No Going Back PAC | 1,146 | $183,785,844 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 279 | $167,602,079 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Texas PAC | 46 | $148,311,446 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 526 | $138,029,798 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 891 | $125,766,887 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 108 | $36,291,873 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Safety & Affordability PAC | 26 | $12,555,808 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | North Star | 44 | $11,985,954 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Texas Forever | 8 | $10,852,121 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | The Georgia Way | 9 | $7,120,071 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Cornhusker Majority | 25 | $7,079,253 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | The Maine Standard | 15 | $6,796,637 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **18,307** | **$2,048,685,220** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 470 | $1,001,329,488 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **473** | **$1,001,360,394** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 10 | $559,006 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **10** | **$559,006** |
| 5. Dropped: not 2026 general (other) | All other committees | 15 | $1,001,260,726 |
| 5. Dropped: not 2026 general (other) | No Going Back PAC | 2 | $903,000 |
| 5. Dropped: not 2026 general (other) | MAGA Inc. | 7 | $45,000 |
| 5. Dropped: not 2026 general (other) | **All** | **24** | **$1,002,208,726** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,951 | $1,706,365,270 |
| 5. Dropped: not 2026 general (primary) | SLF | 76 | $5,269,976 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **13,048** | **$1,711,899,487** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 700 | $63,851,860 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **702** | **$64,679,571** |
| 5. Dropped: not 2026 general (special) | All other committees | 711 | $27,505,002 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **750** | **$30,144,140** |

Final cleaned general-election independent expenditure rows: **32,893**, $2,258,323,038.

Coordinated party expenditure rows added (Schedule F): **1,335**, $270,313,802.
- NRCC filing 2039287: 213 Schedule F rows read from the raw filing because the API had not loaded them
- NRCC filing 2033415: 339 Schedule F rows read from the raw filing because the API had not loaded them
- NRSC filing 2038496: 11 Schedule F rows read from the raw filing because the API had not loaded them
- NRSC filing 2032982: 35 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2033299: 139 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2040710: 5 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2038977: 111 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2033001: 164 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2038862: 61 Schedule F rows read from the raw filing because the API had not loaded them

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-10-14; SLF 2026-10-14; Texas PAC 2026-10-14; Cornhusker Majority 2026-10-14; The Maine Standard 2026-10-14; MAGA Inc. 2026-10-14; No Going Back PAC 2026-10-14; Safety & Affordability PAC 2026-10-14; HMP 2026-10-14; SMP 2026-10-14; WinSenate 2026-10-14; Texas Forever 2026-10-14; North Star 2026-10-14; The Georgia Way 2026-10-14. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

653 rows, $1,011,200,759. These are left out of the tables and charts.

| Race | Candidate | Party | Support/oppose | Rows | Amount |
|---|---|---|---|---|---|
| FL-SEN | BETTIS, SHAWN STEFAN | nan | S | 1 | $1,000,000,000 |
| OH-SEN | REDPATH, WILLIAM | LIB | S | 11 | $1,971,068 |
| OH-SEN | LEVY, GREGORY LEE | IND | S | 15 | $1,763,982 |
| IA-SEN | LAEHN, THOMAS RAYMOND DR. | LIB | S | 24 | $943,098 |
| CA-48 | WILPERT, MARNI VON | nan | S | 31 | $864,579 |
| SC-SEN | HACKETT, MARK | nan | S | 18 | $608,467 |
| KS-SEN | GRAHAM, DAVID C. | LIB | S | 18 | $606,260 |
| VA-02 | BAKER, MATTHEW | IND | S | 19 | $301,987 |
| MI-04 | BARNETT, SHAFINA CHE | GRE | S | 11 | $263,974 |
| KY-06 | BOWMAN, JAY | nan | S | 19 | $217,504 |
| IA-01 | BRIDGFORD, MICHAEL | IND | S | 19 | $198,882 |
| NV-02 | CHAPMAN, LYNN | IAP | S | 19 | $192,741 |
| WI-03 | PROVANCE, RUSTIN LEVEM | NNE | S | 13 | $187,782 |
| OH-10 | MCMASTERS, THOMAS | LIB | S | 20 | $181,609 |
| MN-SEN | WHITING, REBECCA | LIB | S | 13 | $174,789 |
| SC-01 | REESIDE, WILLIAM OLIVER JR. | LIB | S | 16 | $163,888 |
| IA-02 | STEWART, RICK | nan | S | 20 | $163,583 |
| TX-34 | ROYAL, CHRIS B. | LIB | S | 17 | $138,211 |
| NC-01 | BAILEY, TOM | LIB | S | 7 | $134,231 |
| MT-01 | SHEEDY, NICK | nan | S | 16 | $133,902 |
| LA-SEN | DAVIS, JAMIE | nan | S | 1 | $128,619 |
| OH-15 | BARRINGTON, BRENNAN | LIB | S | 13 | $117,631 |
| NH-SEN | LAPLANTE, EDMOND | RNC | S | 7 | $115,799 |
| IA-SEN | LAEHN, THOMAS DR. | LIB | O | 1 | $101,120 |
| AZ-01 | ALPONTE, MONICA MARIA | LIB | S | 14 | $98,844 |

Plus 77 smaller groups totalling $1,428,208.

4 rows ($45,461) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

## Reconciliation against FEC aggregates

The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour notices. The comparison below therefore uses the regular-report rows in this dataset, across all election types, for the named committees. Spending after the coverage end date, and spending by the other committees, has no FEC aggregate checked here.

| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |
|---|---|---|---|---|---|
| CLF | $67,898,719 | $67,698,719 | +0.3% | $138,051,007 (2026-10-14) | -50.8% **(over 2%)** |
| NRCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| SLF | $6,450,360 | $5,770,959 | +10.5% **(over 2%)** | $248,237,806 (2026-10-14) | -97.4% **(over 2%)** |
| Texas PAC | $0 | $0 | n/a | $148,311,446 (2026-10-14) | -100.0% **(over 2%)** |
| Cornhusker Majority | $0 | $0 | n/a | $7,079,253 (2026-10-14) | -100.0% **(over 2%)** |
| The Maine Standard | $0 | $0 | n/a | $6,796,637 (2026-10-14) | -100.0% **(over 2%)** |
| NRSC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| MAGA Inc. | $2,535,973 | $2,535,973 | +0.0% | $36,291,873 (2026-10-14) | -93.0% **(over 2%)** |
| No Going Back PAC | $0 | $0 | n/a | $187,807,636 (2026-10-14) | -100.0% **(over 2%)** |
| Safety & Affordability PAC | $0 | $0 | n/a | $16,216,833 (2026-10-14) | -100.0% **(over 2%)** |
| HMP | $45,720,411 | $44,661,964 | +2.3% **(over 2%)** | $118,107,483 (2026-10-14) | -61.3% **(over 2%)** |
| DCCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| SMP | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| WinSenate | $12,464,041 | $12,464,041 | +0.0% | $167,312,018 (2026-10-14) | -92.6% **(over 2%)** |
| Texas Forever | $0 | $0 | n/a | $10,852,121 (2026-10-14) | -100.0% **(over 2%)** |
| North Star | $0 | $0 | n/a | $11,933,434 (2026-10-14) | -100.0% **(over 2%)** |
| The Georgia Way | $0 | $0 | n/a | $7,080,603 (2026-10-14) | -100.0% **(over 2%)** |
| DSCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |

### Coordinated party expenditures

| Committee | Schedule F rows here (House and Senate) | FEC committee-total coordinated expenditures (through) | Gap |
|---|---|---|---|
| NRCC | $84,028,433 | $84,028,447 (2026-10-14) | -0.0% |
| NRSC | $86,953,589 | $86,953,603 (2026-10-14) | -0.0% |
| DCCC | $60,946,873 | $60,946,887 (2026-10-14) | -0.0% |
| DSCC | $38,384,907 | $38,384,917 (2026-10-14) | -0.0% |

### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)

| Committee | Race | Regular-report rows here | FEC by_candidate |
|---|---|---|---|
| HMP | NJ-07 | $1,058,447 | $0 |
| CLF | AK-AL | $200,000 | $0 |
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
| BLACK VOTERS MATTER ACTION PAC | COLOM, SCOTT | FL-SEN | MS-SEN | 1 | $11,000 |
| BUILDING A STRONG AMERICA | ECHOLS, MICHAEL CHARLES | LA-06 | LA-05 | 1 | $85,000 |
| CENTER FORWARD COMMITTEE | JAMES, LINDSAY | IA-08 | IA-02 | 1 | $200,000 |
| CITIZENS FOR A MORE AFFORDABLE FLORIDA | MOSKOWITZ, JARED | FL-23 | FL-25 | 2 | $67,658 |
| CLEAN WAVE | EL-SAYED, ABDUL | MN-SEN | MI-SEN | 1 | $2,150 |
| CLUB FOR GROWTH PAC | MIGUEZ, BLAKE | LA-05 | LA-06 | 2 | $4,017 |
| DCCC | MOSKOWITZ, JARED | FL-23 | FL-25 | 6 | $2,785,000 |
| FREEDOM CAUCUS FUND | BOEBERT, LAUREN | CO-03 | CO-04 | 13 | $389,491 |
| FREEDOM CAUCUS FUND | LAUBACHER, EILEEN | CO-03 | CO-04 | 2 | $154,028 |
| GROWING ECONOMIC OPPORTUNITIES | BENNETT, REBECCA | NE-07 | NJ-07 | 1 | $100 |
| INDIGO PAC | GRAY, ADAM | OH-09 | CA-13 | 1 | $95 |
| JOBS & PROSPERITY PAC | POINDEXTER, BRIAN | OH-AL | OH-07 | 1 | $25,000 |
| LATINOS FOR CONSERVATIVE VALUES | CAMMACK, KAT | FL-13 | FL-03 | 2 | $30,870 |
| LATINOS FOR CONSERVATIVE VALUES | PAULINA LUNA, ANNA | FL-03 | FL-13 | 1 | $3,000 |
| LGBTQ CONNECTION PAC | HARDING, BRINKER | NE-06 | NE-02 | 20 | $16,120 |
| MAHA PAC | KILEY, KEVIN REP. | CA-03 | CA-06 | 5 | $39,864 |
| MAKE THE ROAD ACTION POLITICAL COMMITTEE | COGNETTI, PAIGE | PA-01 | PA-08 | 1 | $4,410 |
| NEBRASKA APPLESEED ACTION FUND | OSBORN, DAN | NB-SEN | NE-SEN | 2 | $31,680 |
| NEBRASKA APPLESEED ACTION FUND | POWELL, DENISE | NB-02 | NE-02 | 4 | $66,680 |
| OHIO CITIZEN ACTION | LANDSMAN, GREG | OH-15 | OH-01 | 1 | $4,692 |
| OUR HERITAGE MATTERS | GROO, TRAVIS | NC-01 | NC-11 | 1 | $641 |
| PROGRESSIVE TURNOUT PROJECT | MOSKOWITZ, JARED | FL-23 | FL-25 | 6 | $461,116 |
| STRATEGIC MAJORITY PAC | FITZPATRICK, BRIAN | CA-22 | PA-01 | 1 | $22,910 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | ASKAR, CASEY | FL-19 | FL-22 | 1 | $11,705 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | BALDACCI, JOHN ELIAS | IA-03 | ME-02 | 4 | $11,787 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | EL-SAYED, ABDUL | MN-SEN | MI-SEN | 1 | $1 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | GARRIOTT, SARAH TRONE | CA-13 | IA-03 | 4 | $11,787 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | GRAY, ADAM C. | ME-02 | CA-13 | 4 | $11,787 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | KIGGANS, JENNIFER | FL-22 | VA-02 | 1 | $14,000 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | KIGGANS, JENNIFER | VA-97 | VA-02 | 1 | $2,000 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | MANZUR, KARISHMA | NC-SEN | NH-SEN | 2 | $166 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | OSBORN, DAN | NV-SEN | NE-SEN | 1 | $92 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | PAPPAS, CHRIS | NC-SEN | NH-SEN | 2 | $166 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | POINDEXTER, BRIAN | TX-07 | OH-07 | 1 | $2,600 |
| TOGETHER FOR WORKING PEOPLE | BAUMGARTNER, MICHAEL JAMES | WA-03 | WA-05 | 1 | $47,081 |
| VOTERS OF TOMORROW PAC | PERRIELLO, THOMAS STUART PRICE | CA-22 | VA-05 | 1 | $128 |
| VOTERS OF TOMORROW PAC | PERRIELLO, THOMAS STUART PRICE | MT-01 | VA-05 | 1 | $857 |
| VOTERS OF TOMORROW PAC | VILLEGAS, RANDY | CA-48 | CA-22 | 1 | $138 |
| WHEEL DOG PAC | HILL, BILL | AZ-AL | AK-AL | 2 | $438,412 |

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
| CLF | 2026-11-01 | 2026-11-02 | 561 | $152,662,197 |
| NRCC | 2026-10-14 | n/a | 619 | $84,028,433 |
| SLF | 2026-11-03 | 2026-11-03 | 366 | $105,564,313 |
| Texas PAC | 2026-10-27 | 2026-10-29 | 10 | $33,538,779 |
| Cornhusker Majority | no general-election spending | n/a | 0 | $0 |
| The Maine Standard | 2026-10-28 | 2026-10-29 | 5 | $3,117,462 |
| NRSC | 2026-10-14 | n/a | 113 | $86,953,589 |
| MAGA Inc. | 2026-10-28 | 2026-10-29 | 34 | $7,760,000 |
| No Going Back PAC | 2026-11-03 | 2026-11-03 | 601 | $88,818,515 |
| Safety & Affordability PAC | 2026-10-30 | 2026-10-30 | 74 | $50,653,712 |
| Other R | 2026-11-03 | 2026-11-04 | 10,083 | $667,491,025 |
| HMP | 2026-10-31 | 2026-11-01 | 1,051 | $201,877,784 |
| DCCC | 2026-10-13 | n/a | 345 | $60,946,873 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-11-01 | 2026-11-02 | 216 | $127,223,313 |
| Texas Forever | 2026-10-28 | 2026-10-29 | 18 | $16,609,041 |
| North Star | 2026-10-30 | 2026-10-31 | 19 | $4,152,647 |
| The Georgia Way | no general-election spending | n/a | 0 | $0 |
| DSCC | 2026-10-14 | n/a | 258 | $38,384,907 |
| Other D | 2026-11-03 | 2026-11-04 | 19,851 | $798,808,788 |
