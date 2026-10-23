# Cleaning log

Data pulled 2026-10-23T13:05:30.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 56,639 from 950 committees
- Raw e-file feed rows from filings received in the last 7 days: 20,095 distinct transactions (40,190 rows returned across overlapping pages)

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 9,807 | $556,753,568 |
| 1a. E-file rows added (filings not yet in processed data) | No Going Back PAC | 1,214 | $208,200,886 |
| 1a. E-file rows added (filings not yet in processed data) | WinSenate | 253 | $157,206,132 |
| 1a. E-file rows added (filings not yet in processed data) | CLF | 354 | $107,399,761 |
| 1a. E-file rows added (filings not yet in processed data) | SLF | 176 | $106,570,874 |
| 1a. E-file rows added (filings not yet in processed data) | HMP | 462 | $78,994,806 |
| 1a. E-file rows added (filings not yet in processed data) | MAGA Inc. | 73 | $33,755,863 |
| 1a. E-file rows added (filings not yet in processed data) | Texas PAC | 11 | $16,781,793 |
| 1a. E-file rows added (filings not yet in processed data) | Safety & Affordability PAC | 30 | $16,216,832 |
| 1a. E-file rows added (filings not yet in processed data) | Texas Forever | 8 | $10,742,129 |
| 1a. E-file rows added (filings not yet in processed data) | North Star | 20 | $4,733,245 |
| 1a. E-file rows added (filings not yet in processed data) | The Maine Standard | 12 | $4,459,990 |
| 1a. E-file rows added (filings not yet in processed data) | Cornhusker Majority | 10 | $2,333,681 |
| 1a. E-file rows added (filings not yet in processed data) | The Georgia Way | 2 | $1,021,945 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **12,432** | **$1,305,171,505** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | All other committees | 373 | $13,356,073 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **373** | **$13,356,073** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 213 | $5,150,132 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **213** | **$5,150,132** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 2,713 | $144,117,150 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 304 | $35,042,403 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **3,017** | **$179,159,552** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 3,014 | $8,049,071,454 |
| 3. Dropped: memo / memoed-subtotal rows | HMP | 278 | $7,711,075 |
| 3. Dropped: memo / memoed-subtotal rows | WinSenate | 1 | $50,000 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 4 | $39,110 |
| 3. Dropped: memo / memoed-subtotal rows | North Star | 1 | $2,520 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **3,298** | **$8,056,874,159** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 22,617 | $1,634,862,631 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 494 | $248,266,539 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | No Going Back PAC | 1,146 | $183,785,844 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Texas PAC | 46 | $148,311,446 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 180 | $104,644,851 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 291 | $67,478,606 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 429 | $46,771,985 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 108 | $36,291,873 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Safety & Affordability PAC | 26 | $12,555,808 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | North Star | 26 | $7,360,546 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Cornhusker Majority | 25 | $7,079,253 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | The Maine Standard | 15 | $6,796,637 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | The Georgia Way | 7 | $6,100,125 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Texas Forever | 2 | $2,113,210 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **25,412** | **$2,512,419,353** |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | HMP | 86 | $39,896,855 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | CLF | 152 | $18,583,322 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | WinSenate | 13 | $14,884,081 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | Texas Forever | 2 | $5,200,000 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | Safety & Affordability PAC | 4 | $3,661,025 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | North Star | 2 | $275,000 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | No Going Back PAC | 2 | $133,864 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | **All** | **261** | **$82,634,147** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 466 | $1,001,232,437 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **469** | **$1,001,263,343** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 298 | $3,183,242 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **298** | **$3,183,242** |
| 5. Dropped: not 2026 general (other) | All other committees | 19 | $1,000,970,122 |
| 5. Dropped: not 2026 general (other) | **All** | **19** | **$1,000,970,122** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,647 | $1,698,527,305 |
| 5. Dropped: not 2026 general (primary) | SLF | 76 | $5,269,976 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **12,744** | **$1,704,061,521** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 707 | $60,428,148 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **709** | **$61,255,859** |
| 5. Dropped: not 2026 general (special) | All other committees | 674 | $25,713,846 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **713** | **$28,352,984** |

Final cleaned general-election independent expenditure rows: **21,739**, $1,979,422,246.

Coordinated party expenditure rows added (Schedule F): **1,335**, $270,313,810.
- NRCC filing 2033415: 339 Schedule F rows read from the raw filing because the API had not loaded them
- NRCC filing 2039287: 213 Schedule F rows read from the raw filing because the API had not loaded them
- NRSC filing 2032982: 35 Schedule F rows read from the raw filing because the API had not loaded them
- NRSC filing 2038496: 11 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2033299: 139 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2038977: 111 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2033001: 164 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2038862: 61 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2028658: 27 Schedule F rows read from the raw filing because the API had not loaded them

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-09-30; SLF 2026-10-14; Texas PAC 2026-10-14; Cornhusker Majority 2026-10-14; The Maine Standard 2026-10-14; MAGA Inc. 2026-10-14; No Going Back PAC 2026-10-14; Safety & Affordability PAC 2026-10-14; HMP 2026-09-30; SMP 2026-09-30; WinSenate 2026-09-30; Texas Forever 2026-09-30; North Star 2026-09-30; The Georgia Way 2026-09-30. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

163 rows, $1,004,315,712. These are left out of the tables and charts.

| Race | Candidate | Party | Support/oppose | Rows | Amount |
|---|---|---|---|---|---|
| FL-SEN | BETTIS, SHAWN STEFAN | nan | S | 1 | $1,000,000,000 |
| OH-SEN | REDPATH, WILLIAM | LIB | S | 8 | $1,652,884 |
| OH-SEN | LEVY, GREGORY LEE | IND | S | 4 | $682,850 |
| CA-48 | WILPERT, MARNI VON | nan | S | 21 | $635,683 |
| OH-SEN | LEVY, GREGORY | IND | S | 3 | $578,418 |
| IA-SEN | LAEHN, THOMAS RAYMOND DR. | LIB | S | 3 | $161,653 |
| NH-SEN | LAPLANTE, EDMOND | RNC | S | 4 | $105,736 |
| NY-23 | LANGWORTHY, NICK | nan | S | 1 | $95,900 |
| KS-SEN | GRAHAM, DAVID C. | LIB | S | 2 | $79,077 |
| NE-06 | HARDING, BRINKER | nan | O | 17 | $40,637 |
| OH-13 | SKYES, EMILIA | nan | S | 2 | $35,029 |
| OH-13 | COLEMAN, CAREY | REP | nan | 1 | $34,924 |
| OH-10 | MCMASTERS, THOMAS | LIB | S | 3 | $23,746 |
| SC-01 | ANDREWS, ANNIE | nan | S | 6 | $22,168 |
| KY-06 | BOWMAN, JAY | nan | S | 2 | $21,040 |
| AZ-06 | JUAN, CISCOMANI | REP | nan | 1 | $20,000 |
| IA-02 | STEWART, RICK | nan | S | 2 | $19,716 |
| WI-03 | STEIL, BRYAN REP. | nan | S | 2 | $13,114 |
| TX-34 | ROYAL, CHRIS B. | LIB | S | 1 | $12,358 |
| NJ-07 | JR., THOMAS KEAN | nan | O | 1 | $10,000 |
| WI-03 | STEIL, BRYAN | nan | O | 1 | $9,000 |
| WI-03 | BERMAN, MITCHELL | nan | S | 1 | $9,000 |
| CO-08 | WOOD, DAVE | nan | S | 2 | $8,981 |
| NY-18 | RYAN, PATRICK | nan | S | 3 | $7,435 |
| NV-02 | CHAPMAN, LYNN | IAP | S | 2 | $6,140 |

Plus 32 smaller groups totalling $30,224.

91 rows ($7,397,216) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

## Reconciliation against FEC aggregates

The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour notices. The comparison below therefore uses the regular-report rows in this dataset, across all election types, for the named committees. Spending after the coverage end date, and spending by the other committees, has no FEC aggregate checked here.

| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |
|---|---|---|---|---|---|
| CLF | $70,416,487 | $264,240 | +99.6% **(over 2%)** | $67,898,719 (2026-09-30) | +3.6% **(over 2%)** |
| NRCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| SLF | $81,428,552 | $5,770,959 | +92.9% **(over 2%)** | $248,237,806 (2026-10-14) | -67.2% **(over 2%)** |
| Texas PAC | $16,781,793 | $0 | +100.0% **(over 2%)** | $148,311,446 (2026-10-14) | -88.7% **(over 2%)** |
| Cornhusker Majority | $2,333,681 | $0 | +100.0% **(over 2%)** | $7,079,253 (2026-10-14) | -67.0% **(over 2%)** |
| The Maine Standard | $3,048,046 | $0 | +100.0% **(over 2%)** | $6,796,637 (2026-10-14) | -55.2% **(over 2%)** |
| NRSC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| MAGA Inc. | $36,291,836 | $2,535,973 | +93.0% **(over 2%)** | $36,291,873 (2026-10-14) | -0.0% |
| No Going Back PAC | $187,807,190 | $0 | +100.0% **(over 2%)** | $187,807,636 (2026-10-14) | -0.0% |
| Safety & Affordability PAC | $16,216,832 | $0 | +100.0% **(over 2%)** | $16,216,833 (2026-10-14) | -0.0% |
| HMP | $118,107,458 | $44,661,964 | +62.2% **(over 2%)** | $45,720,411 (2026-09-30) | +61.3% **(over 2%)** |
| DCCC | $0 | $0 | n/a | $0 (2026-10-14) | n/a |
| SMP | $0 | $0 | n/a | $0 (2026-09-30) | n/a |
| WinSenate | $167,311,970 | $12,464,041 | +92.6% **(over 2%)** | $104,355,290 (2026-09-30) | +37.6% **(over 2%)** |
| Texas Forever | $8,738,910 | $0 | +100.0% **(over 2%)** | $2,113,210 (2026-09-30) | +75.8% **(over 2%)** |
| North Star | $4,622,883 | $0 | +100.0% **(over 2%)** | $7,310,546 (2026-09-30) | -36.8% **(over 2%)** |
| The Georgia Way | $1,021,945 | $0 | +100.0% **(over 2%)** | $6,058,657 (2026-09-30) | -83.1% **(over 2%)** |
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
| CLF | AK-AL | $453,000 | $0 |
| CLF | AZ-01 | $2,233,634 | $0 |
| CLF | AZ-06 | $1,199,272 | $0 |
| CLF | CA-13 | $2,111,416 | $44,696 |
| CLF | CA-22 | $2,954,988 | $219,544 |
| CLF | CO-08 | $2,244,774 | $0 |
| CLF | FL-14 | $2,861,949 | $0 |
| CLF | FL-22 | $792,378 | $0 |
| CLF | FL-25 | $6,129,428 | $0 |
| CLF | IA-01 | $824,401 | $0 |
| CLF | IA-02 | $1,010,170 | $0 |
| CLF | IA-03 | $1,442,416 | $0 |
| CLF | ME-02 | $1,801,384 | $0 |
| CLF | MI-04 | $825,135 | $0 |
| CLF | MI-07 | $4,447,218 | $0 |
| CLF | MI-08 | $356,977 | $0 |
| CLF | MI-10 | $3,785,297 | $0 |
| CLF | NC-01 | $4,226,187 | $0 |
| CLF | NE-02 | $10,000 | $0 |
| CLF | NJ-07 | $2,104,640 | $0 |
| CLF | NM-02 | $1,916,453 | $0 |
| CLF | NY-03 | $222,535 | $0 |
| CLF | NY-17 | $3,381,751 | $0 |
| CLF | OH-01 | $843,926 | $0 |
| CLF | OH-07 | $2,245,309 | $0 |
| CLF | OH-09 | $1,505,642 | $0 |
| CLF | PA-01 | $1,358,750 | $0 |
| CLF | PA-07 | $2,705,928 | $0 |
| CLF | PA-08 | $1,441,174 | $0 |
| CLF | PA-10 | $516,070 | $0 |
| CLF | SC-01 | $749,574 | $0 |
| CLF | TX-15 | $792,730 | $0 |
| CLF | TX-28 | $1,139,731 | $0 |
| CLF | TX-34 | $2,408,915 | $0 |
| CLF | VA-01 | $437,092 | $0 |
| CLF | VA-02 | $1,409,580 | $0 |
| CLF | WA-03 | $2,201,341 | $0 |
| CLF | WI-01 | $1,067,500 | $0 |
| CLF | WI-03 | $2,257,822 | $0 |
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
| WinSenate | AK-SEN | $3,682,091 | $0 |
| WinSenate | IA-SEN | $28,204,147 | $1,786,417 |
| WinSenate | KS-SEN | $3,345,621 | $0 |
| WinSenate | ME-SEN | $25,018,249 | $3,026 |
| WinSenate | MI-SEN | $28,971,021 | $1,892,820 |
| WinSenate | NC-SEN | $21,642,563 | $8,776,153 |
| WinSenate | NH-SEN | $14,347,362 | $0 |
| WinSenate | OH-SEN | $42,077,516 | $5,625 |
| WinSenate | TX-SEN | $23,400 | $0 |
| MAGA Inc. | AK-SEN | $28,767 | $0 |
| MAGA Inc. | AL-02 | $23,424 | $0 |
| MAGA Inc. | AZ-01 | $50,928 | $0 |
| MAGA Inc. | AZ-02 | $35,045 | $0 |
| MAGA Inc. | AZ-06 | $45,151 | $0 |
| MAGA Inc. | CA-13 | $15,896 | $0 |
| MAGA Inc. | CA-22 | $21,273 | $0 |
| MAGA Inc. | CA-48 | $67,133 | $0 |
| MAGA Inc. | CO-03 | $23,525 | $0 |
| MAGA Inc. | CO-05 | $63,212 | $0 |
| MAGA Inc. | CO-08 | $26,039 | $0 |
| MAGA Inc. | FL-07 | $73,376 | $0 |
| MAGA Inc. | FL-09 | $31,061 | $0 |
| MAGA Inc. | FL-14 | $48,560 | $0 |
| MAGA Inc. | FL-22 | $74,183 | $0 |
| MAGA Inc. | FL-25 | $36,305 | $0 |
| MAGA Inc. | IA-01 | $25,420 | $0 |
| MAGA Inc. | IA-02 | $28,630 | $0 |
| MAGA Inc. | IA-03 | $51,224 | $0 |
| MAGA Inc. | IA-SEN | $189,608 | $0 |
| MAGA Inc. | KY-06 | $59,223 | $0 |
| MAGA Inc. | ME-02 | $105,032 | $0 |
| MAGA Inc. | ME-SEN | $44,506 | $0 |
| MAGA Inc. | MI-04 | $78,550 | $0 |
| MAGA Inc. | MI-07 | $27,987 | $0 |
| MAGA Inc. | MI-08 | $19,772 | $0 |
| MAGA Inc. | MI-10 | $37,331 | $0 |
| MAGA Inc. | MI-SEN | $354,212 | $0 |
| MAGA Inc. | MN-01 | $20,405 | $0 |
| MAGA Inc. | MT-01 | $20,761 | $0 |
| MAGA Inc. | NC-11 | $83,610 | $0 |
| MAGA Inc. | NE-02 | $20,435 | $0 |
| MAGA Inc. | NH-01 | $30,416 | $0 |
| MAGA Inc. | NH-SEN | $37,477 | $0 |
| MAGA Inc. | NJ-07 | $38,976 | $0 |
| MAGA Inc. | NM-02 | $50,031 | $0 |
| MAGA Inc. | NV-02 | $31,688 | $0 |
| MAGA Inc. | NV-03 | $38,215 | $0 |
| MAGA Inc. | NY-03 | $26,833 | $0 |
| MAGA Inc. | NY-17 | $33,798 | $0 |
| MAGA Inc. | OH-01 | $17,751 | $0 |
| MAGA Inc. | OH-07 | $37,329 | $0 |
| MAGA Inc. | OH-09 | $39,887 | $0 |
| MAGA Inc. | OH-10 | $34,188 | $0 |
| MAGA Inc. | OH-15 | $34,557 | $0 |
| MAGA Inc. | OH-SEN | $230,269 | $0 |
| MAGA Inc. | PA-01 | $100,894 | $0 |
| MAGA Inc. | PA-07 | $49,322 | $0 |
| MAGA Inc. | PA-08 | $15,981 | $0 |
| MAGA Inc. | PA-10 | $36,623 | $0 |
| MAGA Inc. | SC-01 | $30,774 | $0 |
| MAGA Inc. | TN-05 | $75,093 | $0 |
| MAGA Inc. | TN-09 | $25,690 | $0 |
| MAGA Inc. | TX-15 | $11,997 | $0 |
| MAGA Inc. | TX-23 | $25,484 | $0 |
| MAGA Inc. | TX-28 | $3,046 | $0 |
| MAGA Inc. | TX-34 | $26,096 | $0 |
| MAGA Inc. | TX-35 | $15,120 | $0 |
| MAGA Inc. | TX-SEN | $30,415,490 | $0 |
| MAGA Inc. | VA-01 | $119,048 | $0 |
| MAGA Inc. | VA-02 | $32,566 | $0 |
| MAGA Inc. | VA-05 | $110,478 | $0 |
| MAGA Inc. | WA-03 | $28,429 | $0 |
| MAGA Inc. | WA-05 | $26,761 | $0 |
| MAGA Inc. | WI-01 | $61,633 | $0 |
| MAGA Inc. | WI-03 | $33,339 | $0 |
| The Georgia Way | GA-SEN | $1,021,945 | $0 |
| North Star | AK-SEN | $4,622,883 | $0 |
| Texas PAC | TX-SEN | $16,781,793 | $0 |
| No Going Back PAC | AK-AL | $283,104 | $0 |
| No Going Back PAC | AK-SEN | $9,018,287 | $0 |
| No Going Back PAC | AL-02 | $1,291,800 | $0 |
| No Going Back PAC | AZ-01 | $340,420 | $0 |
| No Going Back PAC | AZ-02 | $1,884,204 | $0 |
| No Going Back PAC | AZ-06 | $505,944 | $0 |
| No Going Back PAC | CA-13 | $127,509 | $0 |
| No Going Back PAC | CA-48 | $329,872 | $0 |
| No Going Back PAC | CO-03 | $629,854 | $0 |
| No Going Back PAC | CO-05 | $2,377,906 | $0 |
| No Going Back PAC | CO-08 | $1,406,067 | $0 |
| No Going Back PAC | FL-07 | $257,297 | $0 |
| No Going Back PAC | FL-09 | $326,196 | $0 |
| No Going Back PAC | FL-14 | $6,577,592 | $0 |
| No Going Back PAC | FL-22 | $4,098,992 | $0 |
| No Going Back PAC | FL-25 | $7,878,129 | $0 |
| No Going Back PAC | GA-SEN | $5,160,173 | $0 |
| No Going Back PAC | IA-01 | $377,316 | $0 |
| No Going Back PAC | IA-02 | $3,807,676 | $0 |
| No Going Back PAC | IA-03 | $1,299,786 | $0 |
| No Going Back PAC | IA-SEN | $823,202 | $0 |
| No Going Back PAC | KY-06 | $2,460,591 | $0 |
| No Going Back PAC | ME-02 | $159,305 | $0 |
| No Going Back PAC | MI-04 | $5,095,174 | $0 |
| No Going Back PAC | MI-07 | $229,357 | $0 |
| No Going Back PAC | MI-08 | $184,256 | $0 |
| No Going Back PAC | MI-10 | $206,002 | $0 |
| No Going Back PAC | MI-SEN | $29,786,045 | $0 |
| No Going Back PAC | MT-01 | $3,480,139 | $0 |
| No Going Back PAC | NC-01 | $505,622 | $0 |
| No Going Back PAC | NC-11 | $5,079,472 | $0 |
| No Going Back PAC | NC-SEN | $9,937,241 | $0 |
| No Going Back PAC | NE-02 | $161,317 | $0 |
| No Going Back PAC | NH-01 | $232,264 | $0 |
| No Going Back PAC | NH-SEN | $11,821,633 | $0 |
| No Going Back PAC | NJ-07 | $160,573 | $0 |
| No Going Back PAC | NJ-09 | $304,942 | $0 |
| No Going Back PAC | NM-02 | $1,358,300 | $0 |
| No Going Back PAC | NV-03 | $202,749 | $0 |
| No Going Back PAC | NY-03 | $6,622,795 | $0 |
| No Going Back PAC | NY-04 | $251,105 | $0 |
| No Going Back PAC | NY-17 | $274,056 | $0 |
| No Going Back PAC | OH-01 | $566,598 | $0 |
| No Going Back PAC | OH-09 | $453,465 | $0 |
| No Going Back PAC | OH-10 | $371,453 | $0 |
| No Going Back PAC | OH-15 | $505,621 | $0 |
| No Going Back PAC | OH-SEN | $27,770,035 | $0 |
| No Going Back PAC | PA-07 | $331,557 | $0 |
| No Going Back PAC | PA-08 | $249,726 | $0 |
| No Going Back PAC | PA-10 | $2,329,699 | $0 |
| No Going Back PAC | SC-01 | $690,791 | $0 |
| No Going Back PAC | TX-09 | $738,727 | $0 |
| No Going Back PAC | TX-15 | $4,469,464 | $0 |
| No Going Back PAC | TX-23 | $535,707 | $0 |
| No Going Back PAC | TX-28 | $206,117 | $0 |
| No Going Back PAC | TX-34 | $2,593,722 | $0 |
| No Going Back PAC | TX-35 | $4,917,329 | $0 |
| No Going Back PAC | TX-SEN | $5,615,928 | $0 |
| No Going Back PAC | VA-01 | $301,368 | $0 |
| No Going Back PAC | VA-02 | $2,161,206 | $0 |
| No Going Back PAC | VA-05 | $452,494 | $0 |
| No Going Back PAC | WA-03 | $4,447,605 | $0 |
| No Going Back PAC | WI-01 | $532,102 | $0 |
| No Going Back PAC | WI-03 | $252,212 | $0 |
| Safety & Affordability PAC | AZ-01 | $3,759,166 | $0 |
| Safety & Affordability PAC | AZ-06 | $416,666 | $0 |
| Safety & Affordability PAC | CO-03 | $868,050 | $0 |
| Safety & Affordability PAC | ME-02 | $1,840,008 | $0 |
| Safety & Affordability PAC | MI-07 | $1,086,269 | $0 |
| Safety & Affordability PAC | NC-01 | $1,478,467 | $0 |
| Safety & Affordability PAC | OH-09 | $1,175,000 | $0 |
| Safety & Affordability PAC | OH-10 | $1,400,000 | $0 |
| Safety & Affordability PAC | OH-15 | $625,000 | $0 |
| Safety & Affordability PAC | PA-07 | $750,000 | $0 |
| Safety & Affordability PAC | PA-08 | $1,216,666 | $0 |
| Safety & Affordability PAC | WI-03 | $1,601,540 | $0 |
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
| NATIONAL ASSOCIATION OF REALTORS POLITICAL ACTION COMMITTEE | KILEY, KEVIN | CA-03 | CA-06 | 3 | $68,057 |
| NATIONAL ASSOCIATION OF REALTORS POLITICAL ACTION COMMITTEE | MOSKOWITZ, JARED | FL-23 | FL-25 | 4 | $76,073 |
| NEBRASKA APPLESEED ACTION FUND | OSBORN, DAN | NB-SEN | NE-SEN | 2 | $31,680 |
| NEBRASKA APPLESEED ACTION FUND | POWELL, DENISE | NB-02 | NE-02 | 4 | $66,680 |
| PROGRESSIVE TURNOUT PROJECT | MOSKOWITZ, JARED | FL-23 | FL-25 | 5 | $342,382 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | ASKAR, CASEY | FL-19 | FL-22 | 1 | $11,705 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | BALDACCI, JOHN ELIAS | IA-03 | ME-02 | 1 | $249 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | EL-SAYED, ABDUL | MN-SEN | MI-SEN | 1 | $1 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | KIGGANS, JENNIFER | FL-22 | VA-02 | 1 | $14,000 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | MANZUR, KARISHMA | NC-SEN | NH-SEN | 2 | $166 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | OSBORN, DAN | NV-SEN | NE-SEN | 1 | $92 |
| THE CONSERVATIVE CAUCUS DBA AMERICANS FOR CONSTITUTIONAL LIBERTY | PAPPAS, CHRIS | NC-SEN | NH-SEN | 2 | $166 |
| TOGETHER FOR WORKING PEOPLE | BAUMGARTNER, MICHAEL JAMES | WA-03 | WA-05 | 1 | $47,081 |
| TOGETHER WE ELECT PAC | JACKSON, TROY DALE | MP-SEN | ME-SEN | 1 | $10 |
| WHEEL DOG PAC | HILL, BILL | AZ-AL | AK-AL | 1 | $417,562 |

## Expenditures not mapped to a race

8 general-election rows, $12,000,023,747, had no usable state or House district. Largest:

| Committee | Candidate | Office | State | District | Amount | Date | Filing |
|---|---|---|---|---|---|---|---|
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $9,000,000,000 | 2026-04-03 | 1957531 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $1,000,000,000 | 2026-05-15 | 1975315 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $1,000,000,000 | 2026-05-14 | 1975235 |
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $1,000,000,000 | 2026-04-22 | 1970917 |
| WOMEN SPEAK OUT PAC | JAMES, LINDSAY | H | IA | nan | $23,447 | 2026-10-01 | 2031580 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $100 | 2026-05-26 | 1979441 |
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $100 | 2026-07-06 | 1989236 |
| nan | BETTIS, SHAWN STEFAN | H | nan | nan | $100 | 2026-06-25 | 1986763 |

## Most recent transaction per spender

| Spender | Latest date in cleaned data | Latest filing received | Rows | Total |
|---|---|---|---|---|
| CLF | 2026-10-21 | 2026-10-22 | 465 | $159,684,492 |
| NRCC | 2026-10-14 | n/a | 619 | $84,028,433 |
| SLF | 2026-10-21 | 2026-10-22 | 268 | $120,268,533 |
| Texas PAC | 2026-10-21 | 2026-10-22 | 17 | $49,616,924 |
| Cornhusker Majority | 2026-10-09 | 2026-10-22 | 10 | $2,333,681 |
| The Maine Standard | 2026-10-21 | 2026-10-22 | 13 | $4,463,082 |
| NRSC | 2026-10-14 | n/a | 113 | $86,953,589 |
| MAGA Inc. | 2026-10-22 | 2026-10-22 | 75 | $41,155,863 |
| No Going Back PAC | 2026-10-21 | 2026-10-22 | 1,396 | $219,856,394 |
| Safety & Affordability PAC | 2026-10-21 | 2026-10-22 | 56 | $33,178,360 |
| Other R | 2026-10-24 | 2026-10-23 | 6,546 | $366,459,737 |
| HMP | 2026-10-21 | 2026-10-22 | 1,293 | $220,939,746 |
| DCCC | 2026-10-13 | n/a | 345 | $60,946,873 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-10-21 | 2026-10-22 | 429 | $264,871,692 |
| Texas Forever | 2026-10-21 | 2026-10-22 | 18 | $20,312,896 |
| North Star | 2026-10-21 | 2026-10-22 | 42 | $11,214,365 |
| The Georgia Way | 2026-10-06 | 2026-10-22 | 4 | $2,041,891 |
| DSCC | 2026-10-14 | n/a | 258 | $38,384,915 |
| Other D | 2026-10-24 | 2026-10-23 | 11,016 | $455,627,374 |
