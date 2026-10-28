# Cleaning log

Data pulled 2026-10-28T14:35:38.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 60,713 from 979 committees
- Raw e-file feed rows from filings received in the last 7 days: 13,555 distinct transactions (27,110 rows returned across overlapping pages)

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 6,505 | $391,545,369 |
| 1a. E-file rows added (filings not yet in processed data) | HMP | 462 | $78,994,806 |
| 1a. E-file rows added (filings not yet in processed data) | SLF | 140 | $75,040,242 |
| 1a. E-file rows added (filings not yet in processed data) | CLF | 239 | $70,152,247 |
| 1a. E-file rows added (filings not yet in processed data) | WinSenate | 99 | $62,956,711 |
| 1a. E-file rows added (filings not yet in processed data) | Texas PAC | 11 | $16,781,793 |
| 1a. E-file rows added (filings not yet in processed data) | Texas Forever | 6 | $8,738,910 |
| 1a. E-file rows added (filings not yet in processed data) | North Star | 18 | $4,625,403 |
| 1a. E-file rows added (filings not yet in processed data) | The Maine Standard | 10 | $3,048,046 |
| 1a. E-file rows added (filings not yet in processed data) | Cornhusker Majority | 10 | $2,333,681 |
| 1a. E-file rows added (filings not yet in processed data) | No Going Back PAC | 44 | $1,581,832 |
| 1a. E-file rows added (filings not yet in processed data) | The Georgia Way | 2 | $1,021,945 |
| 1a. E-file rows added (filings not yet in processed data) | Safety & Affordability PAC | 2 | $596,723 |
| 1a. E-file rows added (filings not yet in processed data) | MAGA Inc. | 15 | $325,000 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **7,563** | **$717,742,708** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | All other committees | 105 | $9,873,631 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **105** | **$9,873,631** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 65 | $6,913,881 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **65** | **$6,913,881** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 2,994 | $155,778,178 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 304 | $35,042,403 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **3,298** | **$190,820,581** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 2,898 | $8,047,621,643 |
| 3. Dropped: memo / memoed-subtotal rows | HMP | 278 | $7,711,075 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 4 | $39,110 |
| 3. Dropped: memo / memoed-subtotal rows | North Star | 1 | $2,520 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **3,181** | **$8,055,374,348** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 21,822 | $1,592,341,381 |
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
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **25,439** | **$2,696,785,690** |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | CLF | 3 | $17,000 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | **All** | **3** | **$17,000** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 468 | $1,001,249,726 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **471** | **$1,001,280,632** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 101 | $215,117 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **101** | **$215,117** |
| 5. Dropped: not 2026 general (other) | All other committees | 15 | $1,000,812,617 |
| 5. Dropped: not 2026 general (other) | **All** | **15** | **$1,000,812,617** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,683 | $1,701,381,122 |
| 5. Dropped: not 2026 general (primary) | SLF | 76 | $5,269,976 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **12,780** | **$1,706,915,338** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 708 | $60,445,148 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **710** | **$61,272,859** |
| 5. Dropped: not 2026 general (special) | All other committees | 678 | $25,892,950 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **717** | **$28,532,088** |

Final cleaned general-election independent expenditure rows: **21,255**, $1,630,790,211.

Coordinated party expenditure rows added (Schedule F): **1,335**, $270,313,810.
- NRCC filing 2039287: 213 Schedule F rows read from the raw filing because the API had not loaded them
- NRCC filing 2033415: 339 Schedule F rows read from the raw filing because the API had not loaded them
- NRSC filing 2032982: 35 Schedule F rows read from the raw filing because the API had not loaded them
- NRSC filing 2038496: 11 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2033299: 139 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2040710: 5 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2038977: 111 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2028658: 27 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2038862: 61 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2033001: 164 Schedule F rows read from the raw filing because the API had not loaded them

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-10-14; SLF 2026-10-14; Texas PAC 2026-10-14; Cornhusker Majority 2026-10-14; The Maine Standard 2026-10-14; MAGA Inc. 2026-10-14; No Going Back PAC 2026-10-14; Safety & Affordability PAC 2026-10-14; HMP 2026-10-14; SMP 2026-10-14; WinSenate 2026-10-14; Texas Forever 2026-10-14; North Star 2026-10-14; The Georgia Way 2026-10-14. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

226 rows, $1,004,776,200. These are left out of the tables and charts.

| Race | Candidate | Party | Support/oppose | Rows | Amount |
|---|---|---|---|---|---|
| FL-SEN | BETTIS, SHAWN STEFAN | nan | S | 1 | $1,000,000,000 |
| OH-SEN | REDPATH, WILLIAM | LIB | S | 9 | $1,677,884 |
| OH-SEN | LEVY, GREGORY LEE | IND | S | 7 | $912,287 |
| OH-SEN | LEVY, GREGORY | IND | S | 3 | $578,418 |
| IA-SEN | LAEHN, THOMAS RAYMOND DR. | LIB | S | 8 | $427,602 |
| KS-SEN | GRAHAM, DAVID C. | LIB | S | 5 | $187,867 |
| NH-SEN | LAPLANTE, EDMOND | RNC | S | 4 | $105,736 |
| NY-23 | LANGWORTHY, NICK | nan | S | 1 | $95,900 |
| KY-06 | BOWMAN, JAY | nan | S | 6 | $94,602 |
| IA-02 | STEWART, RICK | nan | S | 6 | $73,616 |
| MI-04 | BARNETT, SHAFINA CHE | GRE | S | 4 | $65,475 |
| VA-02 | BAKER, MATTHEW | IND | S | 4 | $57,867 |
| TX-34 | ROYAL, CHRIS B. | LIB | S | 5 | $54,218 |
| NE-06 | HARDING, BRINKER | nan | O | 17 | $40,637 |
| OH-10 | MCMASTERS, THOMAS | LIB | S | 5 | $40,605 |
| SC-01 | REESIDE, WILLIAM OLIVER JR. | LIB | S | 2 | $40,108 |
| MT-01 | SHEEDY, NICK | nan | S | 5 | $38,419 |
| OH-13 | SKYES, EMILIA | nan | S | 2 | $35,029 |
| OH-13 | COLEMAN, CAREY | REP | nan | 1 | $34,924 |
| CO-08 | WOOD, DAVE | nan | S | 6 | $31,324 |
| CA-46 | PAN, DAVID | nan | S | 1 | $30,295 |
| SC-01 | ANDREWS, ANNIE DR. | nan | S | 7 | $28,425 |
| AZ-06 | JUAN, CISCOMANI | REP | nan | 1 | $20,000 |
| WI-03 | STEIL, BRYAN REP. | nan | S | 2 | $13,114 |
| NJ-07 | JR., THOMAS KEAN | nan | O | 2 | $12,940 |

Plus 50 smaller groups totalling $78,908.

3 rows ($33,590) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

## Reconciliation against FEC aggregates

The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour notices. The comparison below therefore uses the regular-report rows in this dataset, across all election types, for the named committees. Spending after the coverage end date, and spending by the other committees, has no FEC aggregate checked here.

| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |
|---|---|---|---|---|---|
| CLF | $138,050,966 | $67,698,719 | +51.0% **(over 2%)** | $138,051,007 (2026-10-14) | -0.0% |
| NRCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| SLF | $81,428,552 | $5,770,959 | +92.9% **(over 2%)** | $248,237,806 (2026-10-14) | -67.2% **(over 2%)** |
| Texas PAC | $16,781,793 | $0 | +100.0% **(over 2%)** | $148,311,446 (2026-10-14) | -88.7% **(over 2%)** |
| Cornhusker Majority | $2,333,681 | $0 | +100.0% **(over 2%)** | $7,079,253 (2026-10-14) | -67.0% **(over 2%)** |
| The Maine Standard | $3,048,046 | $0 | +100.0% **(over 2%)** | $6,796,637 (2026-10-14) | -55.2% **(over 2%)** |
| NRSC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| MAGA Inc. | $2,535,973 | $2,535,973 | +0.0% | $36,291,873 (2026-10-14) | -93.0% **(over 2%)** |
| No Going Back PAC | $0 | $0 | n/a | $187,807,636 (2026-10-14) | -100.0% **(over 2%)** |
| Safety & Affordability PAC | $0 | $0 | n/a | $16,216,833 (2026-10-14) | -100.0% **(over 2%)** |
| HMP | $118,107,458 | $44,661,964 | +62.2% **(over 2%)** | $118,107,483 (2026-10-14) | -0.0% |
| DCCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| SMP | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| WinSenate | $75,420,752 | $12,464,041 | +83.5% **(over 2%)** | $167,312,018 (2026-10-14) | -54.9% **(over 2%)** |
| Texas Forever | $8,738,910 | $0 | +100.0% **(over 2%)** | $10,852,121 (2026-10-14) | -19.5% **(over 2%)** |
| North Star | $4,622,883 | $0 | +100.0% **(over 2%)** | $11,933,434 (2026-10-14) | -61.3% **(over 2%)** |
| The Georgia Way | $1,021,945 | $0 | +100.0% **(over 2%)** | $7,080,603 (2026-10-14) | -85.6% **(over 2%)** |
| DSCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |

### Coordinated party expenditures

| Committee | Schedule F rows here (House and Senate) | FEC committee-total coordinated expenditures (through) | Gap |
|---|---|---|---|
| NRCC | $84,028,433 | $84,028,447 (2026-10-14) | -0.0% |
| NRSC | $86,953,589 | $86,953,603 (2026-10-14) | -0.0% |
| DCCC | $60,946,873 | $60,946,887 (2026-10-14) | -0.0% |
| DSCC | $38,384,915 | $38,384,917 (2026-10-14) | -0.0% |

### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)

| Committee | Race | Regular-report rows here | FEC by_candidate |
|---|---|---|---|
| HMP | AK-AL | $1,612,218 | $607,154 |
| HMP | AZ-01 | $2,378,090 | $794,162 |
| HMP | AZ-02 | $475,200 | $0 |
| HMP | AZ-06 | $2,656,544 | $1,974,609 |
| HMP | CA-13 | $539,483 | $0 |
| HMP | CA-22 | $4,338,215 | $2,456,775 |
| HMP | CA-48 | $4,127,879 | $2,736,000 |
| HMP | CO-05 | $375,842 | $232,472 |
| HMP | CO-08 | $4,196,372 | $2,276,246 |
| HMP | FL-13 | $1,568,260 | $133,832 |
| HMP | FL-14 | $3,268,200 | $608,160 |
| HMP | FL-22 | $4,832,695 | $54,931 |
| HMP | FL-25 | $6,804,160 | $879,053 |
| HMP | IA-01 | $147,606 | $96,657 |
| HMP | IA-02 | $2,292,264 | $1,471,746 |
| HMP | IA-03 | $1,327,910 | $753,924 |
| HMP | KY-06 | $343,060 | $0 |
| HMP | ME-02 | $5,000,082 | $2,114,989 |
| HMP | MI-04 | $2,842,204 | $1,764,059 |
| HMP | MI-07 | $4,633,245 | $2,186,932 |
| HMP | MI-10 | $3,695,214 | $350,776 |
| HMP | MT-01 | $633,963 | $0 |
| HMP | NC-01 | $5,629,154 | $2,862,865 |
| HMP | NC-11 | $2,474,848 | $1,399,255 |
| HMP | NE-02 | $1,477,246 | $1,367,378 |
| HMP | NJ-07 | $1,828,251 | $0 |
| HMP | NM-02 | $250,000 | $204,000 |
| HMP | NY-04 | $268,192 | $0 |
| HMP | NY-17 | $1,011,615 | $473,783 |
| HMP | OH-01 | $785,413 | $0 |
| HMP | OH-07 | $3,298,220 | $0 |
| HMP | OH-09 | $2,984,887 | $1,916,560 |
| HMP | OH-10 | $1,716,374 | $0 |
| HMP | OH-15 | $782,478 | $173,470 |
| HMP | PA-01 | $2,794,609 | $422,451 |
| HMP | PA-07 | $3,498,983 | $586,541 |
| HMP | PA-08 | $2,506,196 | $1,231,378 |
| HMP | PA-10 | $2,111,446 | $765,555 |
| HMP | TX-15 | $3,123,130 | $1,860,298 |
| HMP | TX-28 | $3,059,196 | $645,473 |
| HMP | TX-34 | $4,628,474 | $2,892,888 |
| HMP | TX-35 | $1,333,955 | $39,392 |
| HMP | VA-01 | $3,218,112 | $1,743,334 |
| HMP | VA-02 | $1,852,167 | $1,307,847 |
| HMP | WA-03 | $2,994,696 | $472,336 |
| HMP | WI-01 | $1,337,740 | $0 |
| HMP | WI-03 | $4,095,841 | $1,847,153 |
| CLF | AK-AL | $653,000 | $0 |
| CLF | AZ-01 | $5,378,446 | $3,144,812 |
| CLF | AZ-06 | $3,476,100 | $2,276,828 |
| CLF | CA-13 | $4,890,007 | $2,823,287 |
| CLF | CA-22 | $6,447,874 | $3,712,430 |
| CLF | CO-08 | $5,964,256 | $3,719,482 |
| CLF | FL-14 | $4,292,293 | $1,430,344 |
| CLF | FL-22 | $792,378 | $0 |
| CLF | FL-25 | $6,129,428 | $0 |
| CLF | IA-01 | $5,058,094 | $4,233,693 |
| CLF | IA-02 | $1,010,170 | $0 |
| CLF | IA-03 | $3,694,717 | $2,252,301 |
| CLF | ME-02 | $4,042,073 | $2,240,689 |
| CLF | MI-04 | $825,135 | $0 |
| CLF | MI-07 | $7,220,078 | $2,772,860 |
| CLF | MI-08 | $1,959,736 | $1,602,759 |
| CLF | MI-10 | $6,445,130 | $2,659,833 |
| CLF | NC-01 | $8,131,901 | $3,905,714 |
| CLF | NJ-07 | $2,104,640 | $0 |
| CLF | NM-02 | $3,783,551 | $1,867,098 |
| CLF | NY-03 | $432,570 | $210,035 |
| CLF | NY-17 | $6,467,984 | $3,086,233 |
| CLF | OH-01 | $2,410,043 | $1,566,117 |
| CLF | OH-07 | $3,372,090 | $1,126,781 |
| CLF | OH-09 | $4,412,067 | $2,906,425 |
| CLF | PA-01 | $1,358,750 | $0 |
| CLF | PA-07 | $5,016,844 | $2,310,916 |
| CLF | PA-08 | $3,805,316 | $2,364,142 |
| CLF | PA-10 | $2,439,083 | $1,923,013 |
| CLF | SC-01 | $749,574 | $0 |
| CLF | TX-15 | $792,730 | $0 |
| CLF | TX-28 | $4,042,765 | $2,903,034 |
| CLF | TX-34 | $5,551,453 | $3,142,538 |
| CLF | VA-01 | $437,092 | $0 |
| CLF | VA-02 | $3,072,472 | $1,662,892 |
| CLF | WA-03 | $4,803,726 | $2,602,385 |
| CLF | WI-01 | $1,067,500 | $0 |
| CLF | WI-03 | $4,091,832 | $1,834,010 |
| SLF | AK-SEN | $4,314,756 | $410,002 |
| SLF | GA-SEN | $2,287,906 | $313,600 |
| SLF | IA-SEN | $12,050,435 | $654,590 |
| SLF | KS-SEN | $5,739,230 | $0 |
| SLF | ME-SEN | $9,888,862 | $875,939 |
| SLF | MI-SEN | $10,463,858 | $747,656 |
| SLF | NE-SEN | $1,583,356 | $256,667 |
| SLF | NH-SEN | $3,359,569 | $11,166 |
| SLF | OH-SEN | $26,635,890 | $1,034,015 |
| SLF | SC-SEN | $3,637,366 | $0 |
| WinSenate | AK-SEN | $1,147,130 | $0 |
| WinSenate | IA-SEN | $16,710,464 | $1,786,417 |
| WinSenate | KS-SEN | $3,345,621 | $0 |
| WinSenate | ME-SEN | $10,037,559 | $3,026 |
| WinSenate | MI-SEN | $14,968,947 | $1,892,820 |
| WinSenate | NH-SEN | $5,056,838 | $0 |
| WinSenate | OH-SEN | $15,359,890 | $5,625 |
| WinSenate | TX-SEN | $10,900 | $0 |
| The Georgia Way | GA-SEN | $1,021,945 | $0 |
| North Star | AK-SEN | $4,622,883 | $0 |
| Texas PAC | TX-SEN | $16,781,793 | $0 |
| Cornhusker Majority | NE-SEN | $2,333,681 | $0 |
| The Maine Standard | ME-SEN | $3,048,046 | $0 |
| Texas Forever | TX-SEN | $8,738,910 | $0 |

## Rows moved to a different race

These rows were filed under a state or district that disagrees with the candidate's other filings, so they were moved to the candidate's race.

| Committee | Candidate | Reported as | Moved to | Rows | Amount |
|---|---|---|---|---|---|
| ACTIVATE AMERICA | CALVERT, KEN | CA-41 | CA-40 | 9 | $3,516 |
| ACTIVATE AMERICA | KIM, YOUNG | CA-39 | CA-40 | 1 | $1,732 |
| ACTIVATE AMERICA | VALADAO, DAVID | CA-21 | CA-22 | 6 | $2,987 |
| BUILDING A STRONG AMERICA | ECHOLS, MICHAEL CHARLES | LA-06 | LA-05 | 1 | $85,000 |
| CENTER FORWARD COMMITTEE | JAMES, LINDSAY | IA-08 | IA-02 | 1 | $200,000 |
| CITIZENS FOR A MORE AFFORDABLE FLORIDA | MOSKOWITZ, JARED | FL-23 | FL-25 | 2 | $67,658 |
| CLUB FOR GROWTH PAC | MIGUEZ, BLAKE | LA-05 | LA-06 | 2 | $4,017 |
| DCCC | MOSKOWITZ, JARED | FL-23 | FL-25 | 6 | $2,785,000 |
| FREEDOM CAUCUS FUND | BOEBERT, LAUREN | CO-03 | CO-04 | 12 | $364,596 |
| FREEDOM CAUCUS FUND | LAUBACHER, EILEEN | CO-03 | CO-04 | 1 | $79,028 |
| GROWING ECONOMIC OPPORTUNITIES | BENNETT, REBECCA | NE-07 | NJ-07 | 1 | $100 |
| INDIGO PAC | GRAY, ADAM | OH-09 | CA-13 | 1 | $95 |
| JOBS & PROSPERITY PAC | POINDEXTER, BRIAN | OH-AL | OH-07 | 1 | $25,000 |
| LATINOS FOR CONSERVATIVE VALUES | CAMMACK, KAT | FL-13 | FL-03 | 2 | $30,870 |
| LATINOS FOR CONSERVATIVE VALUES | PAULINA LUNA, ANNA | FL-03 | FL-13 | 1 | $3,000 |
| LGBTQ CONNECTION PAC | HARDING, BRINKER | NE-06 | NE-02 | 20 | $16,120 |
| MAHA PAC | KILEY, KEVIN REP. | CA-03 | CA-06 | 1 | $4,723 |
| NATIONAL ASSOCIATION OF REALTORS POLITICAL ACTION COMMITTEE | MOSKOWITZ, JARED | FL-23 | FL-25 | 4 | $76,073 |
| NEBRASKA APPLESEED ACTION FUND | OSBORN, DAN | NB-SEN | NE-SEN | 2 | $31,680 |
| NEBRASKA APPLESEED ACTION FUND | POWELL, DENISE | NB-02 | NE-02 | 4 | $66,680 |
| PROGRESSIVE TURNOUT PROJECT | MOSKOWITZ, JARED | FL-23 | FL-25 | 6 | $461,115 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | ASKAR, CASEY | FL-19 | FL-22 | 1 | $11,705 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | BALDACCI, JOHN ELIAS | IA-03 | ME-02 | 1 | $249 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | EL-SAYED, ABDUL | MN-SEN | MI-SEN | 1 | $1 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | KIGGANS, JENNIFER | FL-22 | VA-02 | 1 | $14,000 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | MANZUR, KARISHMA | NC-SEN | NH-SEN | 2 | $166 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | OSBORN, DAN | NV-SEN | NE-SEN | 1 | $92 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | PAPPAS, CHRIS | NC-SEN | NH-SEN | 2 | $166 |
| TOGETHER FOR WORKING PEOPLE | BAUMGARTNER, MICHAEL JAMES | WA-03 | WA-05 | 1 | $47,081 |
| TOGETHER WE ELECT PAC | JACKSON, TROY DALE | MP-SEN | ME-SEN | 1 | $10 |
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
| CLF | 2026-10-24 | 2026-10-25 | 686 | $181,424,913 |
| NRCC | 2026-10-14 | n/a | 619 | $84,028,433 |
| SLF | 2026-10-25 | 2026-10-26 | 334 | $127,775,233 |
| Texas PAC | 2026-10-25 | 2026-10-26 | 20 | $50,104,421 |
| Cornhusker Majority | 2026-10-09 | 2026-10-22 | 10 | $2,333,681 |
| The Maine Standard | 2026-10-21 | 2026-10-22 | 13 | $4,463,083 |
| NRSC | 2026-10-14 | n/a | 113 | $86,953,589 |
| MAGA Inc. | 2026-10-26 | 2026-10-26 | 17 | $7,725,000 |
| No Going Back PAC | 2026-10-26 | 2026-10-26 | 418 | $48,585,912 |
| Safety & Affordability PAC | 2026-10-25 | 2026-10-26 | 41 | $27,894,177 |
| Other R | 2026-10-31 | 2026-10-26 | 6,608 | $351,763,255 |
| HMP | 2026-10-25 | 2026-10-26 | 983 | $183,950,815 |
| DCCC | 2026-10-13 | n/a | 345 | $60,946,873 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-10-24 | 2026-10-25 | 234 | $128,995,041 |
| Texas Forever | 2026-10-22 | 2026-10-23 | 16 | $17,285,064 |
| North Star | 2026-10-24 | 2026-10-25 | 30 | $6,898,636 |
| The Georgia Way | 2026-10-06 | 2026-10-22 | 2 | $1,021,945 |
| DSCC | 2026-10-14 | n/a | 258 | $38,384,915 |
| Other D | 2026-11-01 | 2026-10-26 | 11,840 | $490,535,444 |
