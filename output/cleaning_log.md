# Cleaning log

Data pulled 2026-10-16T12:32:33.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 47,680 from 869 committees
- Raw e-file feed rows from filings received in the last 7 days: 14,700 distinct transactions (29,400 rows returned across overlapping pages)

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 9,771 | $339,715,413 |
| 1a. E-file rows added (filings not yet in processed data) | SLF | 282 | $171,581,970 |
| 1a. E-file rows added (filings not yet in processed data) | Texas PAC | 35 | $131,529,643 |
| 1a. E-file rows added (filings not yet in processed data) | CLF | 272 | $67,635,432 |
| 1a. E-file rows added (filings not yet in processed data) | HMP | 203 | $49,877,781 |
| 1a. E-file rows added (filings not yet in processed data) | WinSenate | 20 | $29,729,323 |
| 1a. E-file rows added (filings not yet in processed data) | No Going Back PAC | 71 | $21,881,911 |
| 1a. E-file rows added (filings not yet in processed data) | North Star | 30 | $9,025,140 |
| 1a. E-file rows added (filings not yet in processed data) | Texas Forever | 3 | $7,113,210 |
| 1a. E-file rows added (filings not yet in processed data) | The Georgia Way | 7 | $6,058,653 |
| 1a. E-file rows added (filings not yet in processed data) | Cornhusker Majority | 15 | $4,745,563 |
| 1a. E-file rows added (filings not yet in processed data) | The Maine Standard | 5 | $3,748,584 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **10,714** | **$842,642,623** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | All other committees | 78 | $5,412,624 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **78** | **$5,412,624** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 620 | $12,157,795 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **620** | **$12,157,795** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 2,271 | $132,742,053 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 304 | $35,042,403 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **2,575** | **$167,784,456** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 2,703 | $8,028,875,619 |
| 3. Dropped: memo / memoed-subtotal rows | North Star | 1 | $50,000 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 2 | $2,060 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **2,706** | **$8,028,927,679** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 17,638 | $1,112,948,942 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 356 | $173,251,256 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Texas PAC | 34 | $130,816,730 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 34 | $12,470,398 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Cornhusker Majority | 15 | $4,745,568 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | The Maine Standard | 5 | $3,748,587 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 35 | $2,535,973 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 6 | $930,876 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 19 | $260,031 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **18,142** | **$1,441,708,361** |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | CLF | 172 | $20,604,062 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | Texas Forever | 2 | $2,113,210 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | North Star | 1 | $28,000 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | **All** | **175** | **$22,745,272** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 465 | $1,001,082,436 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **468** | **$1,001,113,343** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 1,835 | $36,734,980 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **1,835** | **$36,734,980** |
| 5. Dropped: not 2026 general (other) | All other committees | 5 | $1,000,148,900 |
| 5. Dropped: not 2026 general (other) | No Going Back PAC | 2 | $5,151,145 |
| 5. Dropped: not 2026 general (other) | MAGA Inc. | 1 | $230,270 |
| 5. Dropped: not 2026 general (other) | **All** | **8** | **$1,005,530,315** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,249 | $1,677,298,143 |
| 5. Dropped: not 2026 general (primary) | SLF | 76 | $5,269,976 |
| 5. Dropped: not 2026 general (primary) | WinSenate | 6 | $1,488,396 |
| 5. Dropped: not 2026 general (primary) | North Star | 2 | $1,010,128 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **12,354** | **$1,685,330,884** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 636 | $56,409,371 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **638** | **$57,237,082** |
| 5. Dropped: not 2026 general (special) | All other committees | 639 | $22,584,258 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **678** | **$25,223,396** |

Final cleaned general-election independent expenditure rows: **18,112**, $1,865,567,591.

Coordinated party expenditure rows added (Schedule F): **267**, $62,898,441.

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-06-30; SLF 2026-09-30; Texas PAC 2026-09-30; Cornhusker Majority 2026-09-30; The Maine Standard 2026-09-30; MAGA Inc. 2026-08-31; No Going Back PAC none filed; Safety & Affordability PAC none filed; HMP 2026-08-31; SMP 2026-06-30; WinSenate 2026-08-31; Texas Forever none filed; North Star none filed; The Georgia Way 2026-06-30. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

68 rows, $1,001,041,349. These are left out of the tables and charts.

| Race | Candidate | Party | Support/oppose | Rows | Amount |
|---|---|---|---|---|---|
| FL-SEN | BETTIS, SHAWN STEFAN | nan | S | 1 | $1,000,000,000 |
| OH-SEN | LEVY, GREGORY LEE | IND | S | 3 | $578,420 |
| IA-01 | BRIDGFORD, MICHAEL | IND | S | 6 | $158,561 |
| NY-23 | LANGWORTHY, NICK | nan | S | 1 | $95,900 |
| NE-06 | HARDING, BRINKER | nan | O | 17 | $40,637 |
| NM-03 | VASQUEZ, GABE REP. | nan | S | 4 | $38,216 |
| OH-13 | SKYES, EMILIA | nan | S | 2 | $35,095 |
| OH-13 | COLEMAN, CAREY | REP | nan | 1 | $34,924 |
| AZ-06 | JUAN, CISCOMANI | REP | nan | 1 | $20,000 |
| NJ-07 | JR., THOMAS KEAN | nan | O | 1 | $10,000 |
| WI-03 | STEIL, BRYAN | nan | O | 1 | $9,000 |
| WI-03 | BERMAN, MITCHELL | nan | S | 1 | $9,000 |
| ME-SEN | COLLLINS, SUSAN | nan | O | 1 | $3,000 |
| TX-28 | CUELLER, ENRIQUE ROBERTO | nan | S | 1 | $2,058 |
| SC-SEN | NORMAN, RALPH | nan | nan | 1 | $1,000 |
| MI-SEN | BOUCHARD, MICHAEL | nan | O | 2 | $940 |
| WI-04 | BURKS, ARTHUR | nan | S | 5 | $856 |
| WA-08 | SCHRIER, KIM | nan | S | 1 | $537 |
| WA-04 | DURESKY, JOHN | nan | S | 1 | $480 |
| WA-02 | LARSEN, RICK | nan | S | 1 | $424 |
| WA-01 | DELBENE, SUZAN | nan | S | 1 | $424 |
| WA-06 | RANDALL, EMILY | nan | S | 1 | $395 |
| WA-09 | SMITH, ADAM | nan | S | 1 | $367 |
| WA-10 | STRICKLAND, MARILYN | nan | S | 1 | $367 |
| WA-07 | JAYAPAL, PRAMILA | nan | S | 1 | $339 |

Plus 6 smaller groups totalling $410.

68 rows ($4,087,062) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

## Reconciliation against FEC aggregates

The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour notices. The comparison below therefore uses the regular-report rows in this dataset, across all election types, for the named committees. Spending after the coverage end date, and spending by the other committees, has no FEC aggregate checked here.

| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |
|---|---|---|---|---|---|
| CLF | $67,898,672 | $264,240 | +99.6% **(over 2%)** | $264,240 (2026-06-30) | +99.6% **(over 2%)** |
| NRCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| SLF | $173,259,505 | $5,770,959 | +96.7% **(over 2%)** | $173,259,573 (2026-09-30) | -0.0% |
| Texas PAC | $131,529,643 | $0 | +100.0% **(over 2%)** | $131,529,652 (2026-09-30) | -0.0% |
| Cornhusker Majority | $4,745,563 | $0 | +100.0% **(over 2%)** | $4,745,568 (2026-09-30) | -0.0% |
| The Maine Standard | $3,748,584 | $0 | +100.0% **(over 2%)** | $3,748,587 (2026-09-30) | -0.0% |
| NRSC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| MAGA Inc. | $2,535,973 | $2,535,973 | +0.0% | $2,535,973 (2026-08-31) | +0.0% |
| No Going Back PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| Safety & Affordability PAC | $0 | $0 | n/a | $0 (n/a) | n/a |
| HMP | $961,782 | $961,782 | +0.0% | $961,782 (2026-08-31) | +0.0% |
| DCCC | $0 | $0 | n/a | $0 (2026-08-31) | n/a |
| SMP | $0 | $0 | n/a | $0 (2026-06-30) | n/a |
| WinSenate | $12,464,041 | $12,464,041 | +0.0% | $12,464,041 (2026-08-31) | +0.0% |
| Texas Forever | $2,113,210 | $0 | +100.0% **(over 2%)** | $0 (n/a) | +100.0% **(over 2%)** |
| North Star | $7,310,538 | $0 | +100.0% **(over 2%)** | $0 (n/a) | +100.0% **(over 2%)** |
| The Georgia Way | $6,058,653 | $0 | +100.0% **(over 2%)** | $0 (2026-06-30) | +100.0% **(over 2%)** |
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
| CLF | AK-AL | $200,000 | $0 |
| CLF | AZ-01 | $3,144,811 | $0 |
| CLF | AZ-06 | $2,276,825 | $0 |
| CLF | CA-13 | $2,823,286 | $44,696 |
| CLF | CA-22 | $3,712,429 | $219,544 |
| CLF | CO-08 | $3,719,480 | $0 |
| CLF | FL-14 | $1,430,344 | $0 |
| CLF | IA-01 | $4,233,690 | $0 |
| CLF | IA-03 | $2,252,296 | $0 |
| CLF | ME-02 | $2,240,687 | $0 |
| CLF | MI-07 | $2,772,857 | $0 |
| CLF | MI-08 | $1,602,758 | $0 |
| CLF | MI-10 | $2,659,832 | $0 |
| CLF | NC-01 | $3,905,713 | $0 |
| CLF | NE-02 | $1,418,067 | $0 |
| CLF | NM-02 | $1,867,095 | $0 |
| CLF | NY-03 | $210,035 | $0 |
| CLF | NY-17 | $3,086,233 | $0 |
| CLF | OH-01 | $1,566,117 | $0 |
| CLF | OH-07 | $1,126,780 | $0 |
| CLF | OH-09 | $2,906,421 | $0 |
| CLF | PA-07 | $2,310,915 | $0 |
| CLF | PA-08 | $2,364,140 | $0 |
| CLF | PA-10 | $1,923,011 | $0 |
| CLF | TX-28 | $2,903,032 | $0 |
| CLF | TX-34 | $3,142,536 | $0 |
| CLF | VA-02 | $1,662,890 | $0 |
| CLF | WA-03 | $2,602,383 | $0 |
| CLF | WI-03 | $1,834,009 | $0 |
| SLF | AK-SEN | $10,116,340 | $410,002 |
| SLF | FL-SEN | $280,000 | $250,000 |
| SLF | GA-SEN | $9,850,689 | $313,600 |
| SLF | IA-SEN | $23,893,249 | $654,590 |
| SLF | ME-SEN | $20,826,547 | $875,939 |
| SLF | MI-SEN | $28,167,292 | $747,656 |
| SLF | NC-SEN | $30,889,798 | $1,217,325 |
| SLF | NH-SEN | $6,298,481 | $11,166 |
| SLF | OH-SEN | $42,680,443 | $1,034,015 |
| The Georgia Way | GA-SEN | $6,058,653 | $0 |
| North Star | AK-SEN | $7,310,538 | $0 |
| Texas PAC | TX-SEN | $131,529,643 | $0 |
| Cornhusker Majority | NE-SEN | $4,745,563 | $0 |
| The Maine Standard | ME-SEN | $3,748,584 | $0 |
| Texas Forever | TX-SEN | $2,113,210 | $0 |

## Rows moved to a different race

These rows were filed under a state or district that disagrees with the candidate's other filings, so they were moved to the candidate's race.

| Committee | Candidate | Reported as | Moved to | Rows | Amount |
|---|---|---|---|---|---|
| ACTIVATE AMERICA | CALVERT, KEN | CA-41 | CA-40 | 9 | $3,516 |
| ACTIVATE AMERICA | KIM, YOUNG | CA-39 | CA-40 | 1 | $1,732 |
| ACTIVATE AMERICA | VALADAO, DAVID | CA-21 | CA-22 | 6 | $2,987 |
| CLUB FOR GROWTH PAC | MIGUEZ, BLAKE | LA-05 | LA-06 | 2 | $4,017 |
| FREEDOM CAUCUS FUND | BOEBERT, LAUREN | CO-03 | CO-04 | 11 | $601,497 |
| FREEDOM CAUCUS FUND | LAUBACHER, EILEEN | CO-03 | CO-04 | 2 | $158,055 |
| GROWING ECONOMIC OPPORTUNITIES | BENNETT, REBECCA | NE-07 | NJ-07 | 1 | $100 |
| INDIGO PAC | GRAY, ADAM | OH-09 | CA-13 | 1 | $95 |
| JOBS & PROSPERITY PAC | POINDEXTER, BRIAN | OH-AL | OH-07 | 1 | $25,000 |
| LATINOS FOR CONSERVATIVE VALUES | CAMMACK, KAT | FL-13 | FL-03 | 2 | $30,870 |
| LATINOS FOR CONSERVATIVE VALUES | PAULINA LUNA, ANNA | FL-03 | FL-13 | 1 | $3,000 |
| LGBTQ CONNECTION PAC | HARDING, BRINKER | NE-06 | NE-02 | 20 | $16,120 |
| NEBRASKA APPLESEED ACTION FUND | OSBORN, DAN | NB-SEN | NE-SEN | 2 | $31,680 |
| NEBRASKA APPLESEED ACTION FUND | POWELL, DENISE | NB-02 | NE-02 | 4 | $66,680 |
| PROGRESSIVE TURNOUT PROJECT | MOSKOWITZ, JARED | FL-23 | FL-25 | 4 | $243,524 |
| STRATEGIC MAJORITY PAC | FITZPATRICK, BRIAN | CA-22 | PA-01 | 1 | $22,910 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | ASKAR, CASEY | FL-19 | FL-22 | 1 | $11,705 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | BALDACCI, JOHN ELIAS | IA-03 | ME-02 | 4 | $11,785 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | EL-SAYED, ABDUL | MN-SEN | MI-SEN | 1 | $1 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | GARRIOTT, SARAH TRONE | CA-13 | IA-03 | 4 | $11,785 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | GRAY, ADAM C. | ME-02 | CA-13 | 4 | $11,785 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | KIGGANS, JENNIFER | FL-22 | VA-02 | 1 | $14,000 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | MANZUR, KARISHMA | NC-SEN | NH-SEN | 2 | $165 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | OSBORN, DAN | NV-SEN | NE-SEN | 1 | $91 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | PAPPAS, CHRIS | NC-SEN | NH-SEN | 2 | $165 |
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
| CLF | 2026-10-13 | 2026-10-15 | 505 | $149,680,722 |
| NRCC | 2026-08-31 | n/a | 67 | $8,311,565 |
| SLF | 2026-10-13 | 2026-10-15 | 385 | $209,923,962 |
| Texas PAC | 2026-10-14 | 2026-10-15 | 47 | $149,024,359 |
| Cornhusker Majority | 2026-10-09 | 2026-10-15 | 25 | $7,079,247 |
| The Maine Standard | 2026-10-08 | 2026-10-15 | 13 | $5,256,890 |
| NRSC | 2026-08-31 | n/a | 67 | $48,146,785 |
| MAGA Inc. | 2026-10-12 | 2026-10-14 | 72 | $33,525,630 |
| No Going Back PAC | 2026-10-14 | 2026-10-15 | 1,144 | $178,634,688 |
| Safety & Affordability PAC | 2026-10-09 | 2026-10-10 | 10 | $4,259,478 |
| Other R | 2026-10-18 | 2026-10-16 | 5,731 | $392,826,127 |
| HMP | 2026-10-13 | 2026-10-15 | 864 | $123,600,753 |
| DCCC | 2026-08-31 | n/a | 100 | $5,243,971 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-10-13 | 2026-10-15 | 264 | $165,551,433 |
| Texas Forever | 2026-10-13 | 2026-10-15 | 8 | $10,852,121 |
| North Star | 2026-10-13 | 2026-10-15 | 63 | $18,121,595 |
| The Georgia Way | 2026-10-06 | 2026-10-15 | 16 | $13,178,724 |
| DSCC | 2026-08-31 | n/a | 33 | $1,196,120 |
| Other D | 2026-10-18 | 2026-10-16 | 8,897 | $399,964,800 |
