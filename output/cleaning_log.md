# Cleaning log

Data pulled 2026-10-21T13:09:00.

## Rows pulled

- Processed Schedule E rows, House and Senate candidates, 2026 cycle: 53,107 from 916 committees
- Raw e-file feed rows from filings received in the last 7 days: 21,389 distinct transactions (42,777 rows returned across overlapping pages)

## Rows added and dropped at each step

Independent expenditures only. "All other committees" is every committee not named in committees.json.

| Step | Committee | Rows | Amount |
|---|---|---|---|
| 1a. E-file rows added (filings not yet in processed data) | All other committees | 12,309 | $478,153,333 |
| 1a. E-file rows added (filings not yet in processed data) | No Going Back PAC | 1,187 | $188,600,213 |
| 1a. E-file rows added (filings not yet in processed data) | SLF | 268 | $166,809,145 |
| 1a. E-file rows added (filings not yet in processed data) | Texas PAC | 35 | $131,529,643 |
| 1a. E-file rows added (filings not yet in processed data) | WinSenate | 152 | $91,967,518 |
| 1a. E-file rows added (filings not yet in processed data) | CLF | 271 | $67,634,432 |
| 1a. E-file rows added (filings not yet in processed data) | HMP | 443 | $46,782,860 |
| 1a. E-file rows added (filings not yet in processed data) | MAGA Inc. | 73 | $33,755,863 |
| 1a. E-file rows added (filings not yet in processed data) | Safety & Affordability PAC | 30 | $16,216,832 |
| 1a. E-file rows added (filings not yet in processed data) | North Star | 27 | $7,361,038 |
| 1a. E-file rows added (filings not yet in processed data) | The Georgia Way | 7 | $6,058,653 |
| 1a. E-file rows added (filings not yet in processed data) | Cornhusker Majority | 15 | $4,745,563 |
| 1a. E-file rows added (filings not yet in processed data) | The Maine Standard | 5 | $3,748,584 |
| 1a. E-file rows added (filings not yet in processed data) | Texas Forever | 2 | $2,113,210 |
| 1a. E-file rows added (filings not yet in processed data) | **All** | **14,824** | **$1,245,476,887** |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | All other committees | 279 | $6,049,767 |
| 1b. E-file-only rows ignored (filing already superseded by an amendment) | **All** | **279** | **$6,049,767** |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | All other committees | 367 | $7,485,642 |
| 1c. Processed rows dropped (filing amended by a newer e-file-only filing) | **All** | **367** | **$7,485,642** |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | All other committees | 2,664 | $139,237,786 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | HMP | 304 | $35,042,403 |
| 2. Dropped: superseded amendment (not the most recent version of the filing) | **All** | **2,968** | **$174,280,189** |
| 3. Dropped: memo / memoed-subtotal rows | All other committees | 2,899 | $8,030,467,118 |
| 3. Dropped: memo / memoed-subtotal rows | HMP | 18 | $1,103,311 |
| 3. Dropped: memo / memoed-subtotal rows | North Star | 1 | $50,000 |
| 3. Dropped: memo / memoed-subtotal rows | WinSenate | 1 | $50,000 |
| 3. Dropped: memo / memoed-subtotal rows | SLF | 2 | $2,060 |
| 3. Dropped: memo / memoed-subtotal rows | **All** | **2,921** | **$8,031,672,489** |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | All other committees | 20,533 | $1,315,699,266 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | SLF | 356 | $173,251,256 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Texas PAC | 34 | $130,816,730 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | CLF | 291 | $67,478,606 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | WinSenate | 34 | $12,470,398 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | North Star | 26 | $7,360,546 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | The Georgia Way | 7 | $6,100,125 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Cornhusker Majority | 15 | $4,745,568 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | The Maine Standard | 5 | $3,748,587 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | MAGA Inc. | 35 | $2,535,973 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | Texas Forever | 2 | $2,113,210 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | HMP | 6 | $930,876 |
| 4a. Dropped: 24/48-hour notice dated within a period covered by a regular report | **All** | **21,344** | **$1,727,251,141** |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | No Going Back PAC | 279 | $109,661,407 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | MAGA Inc. | 7 | $30,000,000 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | Safety & Affordability PAC | 28 | $15,800,166 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | WinSenate | 18 | $10,485,357 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | HMP | 56 | $7,256,800 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | CLF | 2 | $410,035 |
| 4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates) | **All** | **390** | **$173,613,765** |
| 5. Dropped: not 2026 general (convention) | All other committees | 8 | $1,227 |
| 5. Dropped: not 2026 general (convention) | **All** | **8** | **$1,227** |
| 5. Dropped: not 2026 general (general in another year) | All other committees | 466 | $1,001,232,436 |
| 5. Dropped: not 2026 general (general in another year) | HMP | 3 | $30,906 |
| 5. Dropped: not 2026 general (general in another year) | **All** | **469** | **$1,001,263,343** |
| 5. Dropped: not 2026 general (no or other code) | All other committees | 1,795 | $32,643,251 |
| 5. Dropped: not 2026 general (no or other code) | **All** | **1,795** | **$32,643,251** |
| 5. Dropped: not 2026 general (other) | All other committees | 1 | $1,000,000,000 |
| 5. Dropped: not 2026 general (other) | No Going Back PAC | 2 | $5,151,145 |
| 5. Dropped: not 2026 general (other) | MAGA Inc. | 1 | $230,270 |
| 5. Dropped: not 2026 general (other) | **All** | **4** | **$1,005,381,415** |
| 5. Dropped: not 2026 general (primary) | All other committees | 12,355 | $1,678,633,352 |
| 5. Dropped: not 2026 general (primary) | SLF | 76 | $5,269,976 |
| 5. Dropped: not 2026 general (primary) | WinSenate | 4 | $912,670 |
| 5. Dropped: not 2026 general (primary) | CLF | 21 | $264,240 |
| 5. Dropped: not 2026 general (primary) | **All** | **12,456** | **$1,685,080,238** |
| 5. Dropped: not 2026 general (runoff) | All other committees | 638 | $56,574,371 |
| 5. Dropped: not 2026 general (runoff) | MAGA Inc. | 2 | $827,711 |
| 5. Dropped: not 2026 general (runoff) | **All** | **640** | **$57,402,082** |
| 5. Dropped: not 2026 general (special) | All other committees | 658 | $24,857,829 |
| 5. Dropped: not 2026 general (special) | MAGA Inc. | 33 | $1,708,262 |
| 5. Dropped: not 2026 general (special) | HMP | 6 | $930,876 |
| 5. Dropped: not 2026 general (special) | **All** | **697** | **$27,496,967** |

Final cleaned general-election independent expenditure rows: **23,758**, $2,217,988,301.

Coordinated party expenditure rows added (Schedule F): **940**, $192,355,727.
- NRCC filing 2033415: 339 Schedule F rows read from the raw filing because the API had not loaded them
- NRSC filing 2032982: 35 Schedule F rows read from the raw filing because the API had not loaded them
- DCCC filing 2033299: 139 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2033001: 164 Schedule F rows read from the raw filing because the API had not loaded them
- DSCC filing 2028658: 27 Schedule F rows read from the raw filing because the API had not loaded them

Notice cut-off for the named committees (latest regular-report coverage end date): CLF 2026-09-30; SLF 2026-09-30; Texas PAC 2026-09-30; Cornhusker Majority 2026-09-30; The Maine Standard 2026-09-30; MAGA Inc. 2026-08-31; No Going Back PAC none filed; Safety & Affordability PAC none filed; HMP 2026-08-31; SMP 2026-09-30; WinSenate 2026-08-31; Texas Forever 2026-09-30; North Star 2026-09-30; The Georgia Way 2026-09-30. For all other committees the cut-off is the latest date among that committee's regular-report rows.

## Expenditures by other committees that could not be assigned to a party side

105 rows, $1,003,290,897. These are left out of the tables and charts.

| Race | Candidate | Party | Support/oppose | Rows | Amount |
|---|---|---|---|---|---|
| FL-SEN | BETTIS, SHAWN STEFAN | nan | S | 1 | $1,000,000,000 |
| OH-SEN | LEVY, GREGORY LEE | IND | S | 6 | $1,170,580 |
| OH-SEN | REDPATH, WILLIAM | LIB | S | 4 | $819,014 |
| CA-48 | WILPERT, MARNI VON | nan | S | 21 | $746,721 |
| IA-01 | BRIDGFORD, MICHAEL | IND | S | 6 | $158,561 |
| NY-23 | LANGWORTHY, NICK | nan | S | 1 | $95,900 |
| WI-01 | COOKE, REBECCA | nan | S | 1 | $70,000 |
| NE-06 | HARDING, BRINKER | nan | O | 17 | $40,637 |
| NM-03 | VASQUEZ, GABE REP. | nan | S | 4 | $38,216 |
| OH-13 | SKYES, EMILIA | nan | S | 2 | $35,095 |
| OH-13 | COLEMAN, CAREY | REP | nan | 1 | $34,924 |
| AZ-06 | JUAN, CISCOMANI | REP | nan | 1 | $20,000 |
| WI-03 | STEIL, BRYAN REP. | nan | S | 2 | $13,114 |
| NJ-07 | JR., THOMAS KEAN | nan | O | 1 | $10,000 |
| WI-03 | BERMAN, MITCHELL | nan | S | 1 | $9,000 |
| WI-03 | STEIL, BRYAN | nan | O | 1 | $9,000 |
| NY-18 | RYAN, PATRICK | nan | S | 3 | $7,435 |
| NM-02 | VAZQUEZ, GABRIEL | nan | S | 5 | $4,825 |
| NH-SEN | LAPLANTE, EDMOND | RNC | S | 1 | $2,198 |
| SC-SEN | NORMAN, RALPH | nan | nan | 1 | $1,000 |
| WI-04 | BURKS, ARTHUR | nan | S | 5 | $856 |
| WA-08 | SCHRIER, KIM | nan | S | 1 | $537 |
| WA-04 | DURESKY, JOHN | nan | S | 1 | $480 |
| WA-01 | DELBENE, SUZAN | nan | S | 1 | $424 |
| WA-02 | LARSEN, RICK | nan | S | 1 | $424 |

Plus 9 smaller groups totalling $1,958.

61 rows ($3,800,283) are dated after the current week; they are in the transaction file but not the weekly tables or charts.

## Reconciliation against FEC aggregates

The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour notices. The comparison below therefore uses the regular-report rows in this dataset, across all election types, for the named committees. Spending after the coverage end date, and spending by the other committees, has no FEC aggregate checked here.

| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |
|---|---|---|---|---|---|
| CLF | $67,898,672 | $264,240 | +99.6% **(over 2%)** | $67,898,719 (2026-09-30) | -0.0% |
| NRCC | $0 | $0 | n/a | $0 (2026-09-30) | n/a |
| SLF | $173,259,505 | $5,770,959 | +96.7% **(over 2%)** | $173,259,573 (2026-09-30) | -0.0% |
| Texas PAC | $131,529,643 | $0 | +100.0% **(over 2%)** | $131,529,652 (2026-09-30) | -0.0% |
| Cornhusker Majority | $4,745,563 | $0 | +100.0% **(over 2%)** | $4,745,568 (2026-09-30) | -0.0% |
| The Maine Standard | $3,748,584 | $0 | +100.0% **(over 2%)** | $3,748,587 (2026-09-30) | -0.0% |
| NRSC | $0 | $0 | n/a | $0 (2026-09-30) | n/a |
| MAGA Inc. | $36,291,836 | $2,535,973 | +93.0% **(over 2%)** | $2,535,973 (2026-08-31) | +93.0% **(over 2%)** |
| No Going Back PAC | $187,807,190 | $0 | +100.0% **(over 2%)** | $0 (n/a) | +100.0% **(over 2%)** |
| Safety & Affordability PAC | $16,216,832 | $0 | +100.0% **(over 2%)** | $0 (n/a) | +100.0% **(over 2%)** |
| HMP | $45,720,328 | $961,782 | +97.9% **(over 2%)** | $961,782 (2026-08-31) | +97.9% **(over 2%)** |
| DCCC | $0 | $0 | n/a | $0 (2026-09-30) | n/a |
| SMP | $0 | $0 | n/a | $0 (2026-09-30) | n/a |
| WinSenate | $104,355,259 | $12,464,041 | +88.1% **(over 2%)** | $12,464,041 (2026-08-31) | +88.1% **(over 2%)** |
| Texas Forever | $2,113,210 | $0 | +100.0% **(over 2%)** | $2,113,210 (2026-09-30) | +0.0% |
| North Star | $7,310,538 | $0 | +100.0% **(over 2%)** | $7,310,546 (2026-09-30) | -0.0% |
| The Georgia Way | $6,058,653 | $0 | +100.0% **(over 2%)** | $6,058,657 (2026-09-30) | -0.0% |
| DSCC | $0 | $0 | n/a | $0 (2026-09-30) | n/a |

### Coordinated party expenditures

| Committee | Schedule F rows here (House and Senate) | FEC committee-total coordinated expenditures (through) | Gap |
|---|---|---|---|
| NRCC | $55,180,719 | $55,180,733 (2026-09-30) | -0.0% |
| NRSC | $82,111,428 | $82,111,442 (2026-09-30) | -0.0% |
| DCCC | $32,821,410 | $32,821,424 (2026-09-30) | -0.0% |
| DSCC | $22,242,170 | $22,242,172 (2026-09-30) | -0.0% |

### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)

| Committee | Race | Regular-report rows here | FEC by_candidate |
|---|---|---|---|
| HMP | AK-AL | $607,153 | $0 |
| HMP | AZ-01 | $794,162 | $0 |
| HMP | AZ-06 | $1,974,603 | $4,250 |
| HMP | CA-22 | $2,456,774 | $0 |
| HMP | CA-48 | $2,735,998 | $0 |
| HMP | CO-05 | $232,472 | $0 |
| HMP | CO-08 | $2,276,244 | $0 |
| HMP | FL-13 | $133,831 | $0 |
| HMP | FL-14 | $608,160 | $0 |
| HMP | FL-22 | $54,930 | $0 |
| HMP | FL-25 | $879,053 | $0 |
| HMP | IA-01 | $96,654 | $0 |
| HMP | IA-02 | $1,471,744 | $0 |
| HMP | IA-03 | $753,921 | $0 |
| HMP | ME-02 | $2,114,988 | $0 |
| HMP | MI-04 | $1,764,057 | $0 |
| HMP | MI-07 | $2,186,927 | $0 |
| HMP | MI-10 | $350,774 | $0 |
| HMP | NC-01 | $2,862,862 | $0 |
| HMP | NC-11 | $1,399,254 | $0 |
| HMP | NE-02 | $1,367,375 | $0 |
| HMP | NJ-07 | $1,058,446 | $0 |
| HMP | NM-02 | $204,000 | $0 |
| HMP | NY-17 | $473,780 | $0 |
| HMP | OH-09 | $1,916,555 | $0 |
| HMP | OH-15 | $173,468 | $0 |
| HMP | PA-01 | $422,447 | $0 |
| HMP | PA-07 | $586,537 | $0 |
| HMP | PA-08 | $1,231,374 | $0 |
| HMP | PA-10 | $765,552 | $0 |
| HMP | TX-15 | $1,860,296 | $0 |
| HMP | TX-28 | $645,469 | $0 |
| HMP | TX-34 | $2,892,882 | $0 |
| HMP | TX-35 | $39,392 | $0 |
| HMP | VA-01 | $1,743,330 | $0 |
| HMP | VA-02 | $1,307,846 | $0 |
| HMP | WA-03 | $472,335 | $0 |
| HMP | WI-03 | $1,847,151 | $0 |
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
| WinSenate | AK-SEN | $2,534,961 | $0 |
| WinSenate | IA-SEN | $13,280,100 | $1,786,417 |
| WinSenate | ME-SEN | $14,983,716 | $3,026 |
| WinSenate | MI-SEN | $15,894,894 | $1,892,820 |
| WinSenate | NC-SEN | $21,635,313 | $8,776,153 |
| WinSenate | NH-SEN | $9,290,524 | $0 |
| WinSenate | OH-SEN | $26,723,251 | $5,625 |
| WinSenate | TX-SEN | $12,500 | $0 |
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
| The Georgia Way | GA-SEN | $6,058,653 | $0 |
| North Star | AK-SEN | $7,310,538 | $0 |
| Texas PAC | TX-SEN | $131,529,643 | $0 |
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
| BUILDING A STRONG AMERICA | ECHOLS, MICHAEL CHARLES | LA-06 | LA-05 | 1 | $85,000 |
| CLUB FOR GROWTH PAC | MIGUEZ, BLAKE | LA-05 | LA-06 | 2 | $4,017 |
| DCCC | MOSKOWITZ, JARED | FL-23 | FL-25 | 4 | $2,008,778 |
| FREEDOM CAUCUS FUND | BOEBERT, LAUREN | CO-03 | CO-04 | 10 | $364,236 |
| FREEDOM CAUCUS FUND | LAUBACHER, EILEEN | CO-03 | CO-04 | 1 | $79,027 |
| GROWING ECONOMIC OPPORTUNITIES | BENNETT, REBECCA | NE-07 | NJ-07 | 1 | $100 |
| INDIGO PAC | GRAY, ADAM | OH-09 | CA-13 | 1 | $95 |
| JOBS & PROSPERITY PAC | POINDEXTER, BRIAN | OH-AL | OH-07 | 1 | $25,000 |
| LATINOS FOR CONSERVATIVE VALUES | CAMMACK, KAT | FL-13 | FL-03 | 2 | $30,870 |
| LATINOS FOR CONSERVATIVE VALUES | PAULINA LUNA, ANNA | FL-03 | FL-13 | 1 | $3,000 |
| LGBTQ CONNECTION PAC | HARDING, BRINKER | NE-06 | NE-02 | 20 | $16,120 |
| NATIONAL ASSOCIATION OF REALTORS POLITICAL ACTION COMMITTEE | KILEY, KEVIN | CA-03 | CA-06 | 3 | $68,057 |
| NEBRASKA APPLESEED ACTION FUND | OSBORN, DAN | NB-SEN | NE-SEN | 2 | $31,680 |
| NEBRASKA APPLESEED ACTION FUND | POWELL, DENISE | NB-02 | NE-02 | 4 | $66,680 |
| PROGRESSIVE TURNOUT PROJECT | MOSKOWITZ, JARED | FL-23 | FL-25 | 5 | $342,382 |
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

9 general-election rows, $12,000,025,641, had no usable state or House district. Largest:

| Committee | Candidate | Office | State | District | Amount | Date | Filing |
|---|---|---|---|---|---|---|---|
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $9,000,000,000 | 2026-04-03 | 1957531 |
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $1,000,000,000 | 2026-04-22 | 1970917 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $1,000,000,000 | 2026-05-14 | 1975235 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $1,000,000,000 | 2026-05-15 | 1975315 |
| WOMEN SPEAK OUT PAC | JAMES, LINDSAY | H | IA | nan | $23,447 | 2026-10-01 | 2031580 |
| CAROLINA FEDERATION | COOPER, ROY | S | nan | nan | $1,894 | 2026-10-21 | 2033989 |
| nan | BETTIS, SHAWN STEFAN | H | FL | nan | $100 | 2026-07-06 | 1989236 |
| nan | BETTIS, SHAWN STEFAN | H | nan | nan | $100 | 2026-06-25 | 1986763 |
| nan | BETTIS, SHAWN STEFAN | H | CA | nan | $100 | 2026-05-26 | 1979441 |

## Most recent transaction per spender

| Spender | Latest date in cleaned data | Latest filing received | Rows | Total |
|---|---|---|---|---|
| CLF | 2026-10-18 | 2026-10-19 | 529 | $138,046,450 |
| NRCC | 2026-09-30 | n/a | 406 | $55,180,719 |
| SLF | 2026-10-19 | 2026-10-20 | 486 | $248,353,803 |
| Texas PAC | 2026-10-17 | 2026-10-17 | 50 | $149,287,719 |
| Cornhusker Majority | 2026-10-09 | 2026-10-15 | 25 | $7,079,247 |
| The Maine Standard | 2026-10-17 | 2026-10-18 | 16 | $6,799,727 |
| NRSC | 2026-09-25 | n/a | 102 | $82,111,428 |
| MAGA Inc. | 2026-10-12 | 2026-10-20 | 138 | $37,281,493 |
| No Going Back PAC | 2026-10-19 | 2026-10-20 | 2,151 | $265,485,914 |
| Safety & Affordability PAC | 2026-10-15 | 2026-10-20 | 32 | $16,633,499 |
| Other R | 2026-10-23 | 2026-10-21 | 6,901 | $434,311,982 |
| HMP | 2026-10-19 | 2026-10-20 | 1,305 | $165,085,238 |
| DCCC | 2026-09-29 | n/a | 235 | $32,821,410 |
| SMP | no general-election spending | n/a | 0 | $0 |
| WinSenate | 2026-10-19 | 2026-10-20 | 440 | $251,221,189 |
| Texas Forever | 2026-10-18 | 2026-10-19 | 11 | $10,880,777 |
| North Star | 2026-10-19 | 2026-10-20 | 48 | $12,356,535 |
| The Georgia Way | 2026-10-06 | 2026-10-15 | 9 | $7,078,599 |
| DSCC | 2026-09-30 | n/a | 197 | $22,242,170 |
| Other D | 2026-10-24 | 2026-10-21 | 11,556 | $464,285,846 |
