"""Render output/ie_report.html (single self-contained file) from output/data.json."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "output", "data.json")))

HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>2026 House and Senate Outside Spending Tracker</title>
<style>
:root{color-scheme:light;--bg:#fcfcfb;--panel:#ffffff;--line:#e4e3df;--text:#0b0b0b;--text2:#52514e;--muted:#8a8985;
--r:#e34948;--d:#2a78d6;--zero:#f0efec;
--h1:#cde2fb;--h2:#9ec5f4;--h3:#6da7ec;--h4:#3987e5;--h5:#256abf;--h6:#184f95;--h7:#0d366b}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--bg:#1a1a19;--panel:#222221;--line:#3a3a37;--text:#ffffff;--text2:#c3c2b7;--muted:#8f8e86;
--r:#e66767;--d:#3987e5;--zero:#2a2a28;
--h1:#0d366b;--h2:#184f95;--h3:#256abf;--h4:#3987e5;--h5:#6da7ec;--h6:#9ec5f4;--h7:#cde2fb}}
:root[data-theme="dark"]{color-scheme:dark;--bg:#1a1a19;--panel:#222221;--line:#3a3a37;--text:#ffffff;--text2:#c3c2b7;--muted:#8f8e86;
--r:#e66767;--d:#3987e5;--zero:#2a2a28;
--h1:#0d366b;--h2:#184f95;--h3:#256abf;--h4:#3987e5;--h5:#6da7ec;--h6:#9ec5f4;--h7:#cde2fb}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:1180px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:24px;margin:0 0 4px}h2{font-size:18px;margin:40px 0 4px}h3{font-size:14px;margin:0 0 2px}
p{margin:4px 0 12px;color:var(--text2);max-width:80ch}
.sub{color:var(--text2);font-size:13px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:16px 0}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px}
.tile b{display:block;font-size:22px;font-variant-numeric:tabular-nums}.tiles.big{grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-bottom:0}.tiles.big .tile b{font-size:30px}.tiles.big .tile span{font-size:13px}.tile span{color:var(--text2);font-size:12px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px;margin:12px 0;overflow-x:auto}
.controls{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:8px 0}
button,select{font:inherit;color:var(--text);background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:5px 10px;cursor:pointer}
button[aria-pressed="true"]{background:var(--text);color:var(--bg);border-color:var(--text)}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}
th,td{padding:5px 8px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}
th{font-weight:600;color:var(--text2);font-size:12px}th:first-child,td:first-child,th.l,td.l{text-align:left}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;vertical-align:baseline}
.up::before{content:"▲ "}.down::before{content:"▼ "}
.legend{display:flex;gap:16px;align-items:center;color:var(--text2);font-size:12px;margin:6px 0;flex-wrap:wrap}
.swatch{display:inline-block;width:14px;height:10px;margin-right:1px;vertical-align:middle}
.key{display:inline-block;width:14px;height:3px;margin-right:5px;vertical-align:middle;border-radius:2px}
svg text{fill:var(--text2);font-size:11px}svg .lab{fill:var(--text);font-size:11px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.mini{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px}
.mini .who{color:var(--text2);font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#tip{position:fixed;pointer-events:none;background:var(--text);color:var(--bg);padding:6px 9px;border-radius:6px;font-size:12px;display:none;z-index:9;max-width:300px}
.note{font-size:12px;color:var(--text2)}
</style></head><body><main>
<h1>2026 House and Senate Outside Spending Tracker</h1>
<div class="sub" id="asof"></div>
<div class="tiles big" id="toptiles"></div>
<div class="tiles" id="tiles"></div>

<h2>Cumulative spending: most competitive House races</h2>
<p id="cooknote"></p>
<div class="legend"><span><i class="key" style="background:var(--r)"></i>Republican-side committees</span><span><i class="key" style="background:var(--d)"></i>Democratic-side committees</span><span>Each panel has its own vertical scale; the top gridline is labelled.</span></div>
<div class="grid" id="house"></div>
<h2>Cumulative spending: Senate races</h2>
<div class="legend"><span><i class="key" style="background:var(--r)"></i>Republican-side committees</span><span><i class="key" style="background:var(--d)"></i>Democratic-side committees</span><span>Each panel has its own vertical scale.</span></div>
<div class="grid" id="senate"></div>

<p class="note">General-election spending in House and Senate races. Named committees are shown individually; every other committee making general-election independent expenditures is grouped as "Other R" or "Other D" by which side each expenditure helps. NRCC, NRSC, DCCC and DSCC figures are coordinated party expenditures, which are reported only in monthly reports, so they run about a month or more behind the independent expenditure data. Weeks start Monday and use the dissemination date, falling back to the expenditure date. The current week is partial. Time charts begin with the week of <span id="cs"></span>, which contains September 1; totals count all general-election spending to date.</p>

<h2>Which races are being prioritized</h2>
<p>Races ranked by dollars from the tracked committees. Each race has one bar per party side. Switch the period to see where recent money is going, as opposed to the total to date.</p>
<div class="controls"><span class="sub">Office</span><span id="p-office"></span><span class="sub">Period</span><span id="p-period"></span></div>
<div class="legend"><span><i class="swatch" style="background:var(--r)"></i> Republican-side committees</span><span><i class="swatch" style="background:var(--d)"></i> Democratic-side committees</span><span id="p-note"></span></div>
<div class="card" id="p-chart"></div>

<h2>Each committee's priorities</h2>
<p>A committee's races ranked by share of its spending in the chosen period. The vertical tick marks the race's share in the preceding period of the same length, so a bar past its tick is a race moving up and a bar short of its tick is a race moving down.</p>
<div class="controls"><span class="sub">Spender</span><select id="c-sp"></select><span class="sub">Period</span><span id="c-period"></span></div>
<div class="legend"><span><i class="swatch" style="background:var(--muted)"></i> share this period</span><span><i style="display:inline-block;width:2px;height:12px;background:var(--text);vertical-align:middle;margin-right:5px"></i> share in the preceding period</span><span id="c-note"></span></div>
<div class="card" id="c-chart"></div>

<h2>Biggest recent movers</h2>
<p>Change in a race's share of the spender's total, comparing the most recent weeks with the same number of weeks before them. Shares are of that spender's general-election independent expenditures in each window.</p>
<div class="controls"><span class="sub">Window</span><span id="winbtn"></span><span class="sub">Spender</span><select id="spsel"></select><label class="sub"><input type="checkbox" id="thin" checked> Hide thin comparisons (spender's prior-window total under 10% of its recent total)</label></div>
<div class="card"><table id="movers"></table><div class="note" id="moversnote"></div></div>

<h2>Weekly spending by race</h2>
<p>One heatmap per spender, then each party side combined. Races are sorted by spend since the first week shown. Colour shows dollars in that week, scaled within each heatmap.</p>
<div id="heat"></div>


<h2>First entries</h2>
<p>The week each committee first spent in a race, most recent first.</p>
<div class="controls"><span class="sub">Spender</span><select id="ensel"></select></div>
<div class="card"><table id="entries"></table></div>

<h2>Races where spending stopped</h2>
<p>Races with earlier spending by a committee and none in the two most recent full weeks or the current partial week.</p>
<div class="card"><table id="stopped"></table></div>

<h2>Committees in "Other R" and "Other D"</h2>
<p>Every committee counted in the two "Other" groups, with its general-election independent expenditures to date. A committee is placed on a side one expenditure at a time, so a committee that helps both sides appears once under each. The committee name links to its FEC page.</p>
<div class="controls"><span class="sub">Side</span><span id="oc-side"></span><input id="oc-q" type="search" placeholder="Search committee or race" style="font:inherit;padding:5px 10px;border:1px solid var(--line);border-radius:6px;background:var(--panel);color:var(--text);min-width:220px"><span class="sub" id="oc-n"></span></div>
<div class="card" style="max-height:640px;overflow:auto"><table id="oc"></table></div>

<h2>How current each spender is</h2>
<div class="card"><table id="currency"></table></div>
<div id="tip"></div>
</main>
<script>
const DATA = __DATA__;
const $ = s => document.querySelector(s);
const fmt = v => v >= 1e6 ? '$' + (v/1e6).toFixed(v >= 1e7 ? 1 : 2) + 'M' : v >= 1e3 ? '$' + Math.round(v/1e3) + 'K' : '$' + Math.round(v);
const full = v => '$' + Math.round(v).toLocaleString('en-US');
const wk = s => { const d = new Date(s + 'T00:00:00'); return (d.getMonth()+1) + '/' + d.getDate(); };
const side = Object.assign({}, DATA.spender_side); side['All R committees'] = 'R'; side['All D committees'] = 'D';
const dot = sp => `<i class="dot" style="background:var(--${side[sp] === 'R' ? 'r' : 'd'})"></i>`;
const tip = $('#tip');
function showTip(e, html){ tip.innerHTML = html; tip.style.display = 'block';
  const x = Math.min(e.clientX + 14, innerWidth - tip.offsetWidth - 8), y = Math.min(e.clientY + 14, innerHeight - tip.offsetHeight - 8);
  tip.style.left = x + 'px'; tip.style.top = y + 'px'; }
function hideTip(){ tip.style.display = 'none'; }
const W = DATA.weeks, NW = W.length;
const CS = Math.max(0, W.findIndex(w => w >= DATA.chart_start));
document.querySelector('#cs').textContent = wk(W[CS]);
const spenders = Object.keys(DATA.heat);
const cmts = spenders.filter(s => !s.startsWith('All '));

// ---- header
$('#asof').textContent = `Independent expenditure data through ${DATA.last_date}. Pulled from the FEC ${DATA.generated} Eastern. Source: OpenFEC Schedule E (processed data plus the raw e-file feed) and Schedule F.`;
const tot = s => DATA.heat[s] ? Object.values(DATA.heat[s].values).reduce((a, v) => a + v.reduce((x, y) => x + y, 0), 0) : 0;
const totOff = (s, sen) => DATA.heat[s] ? Object.entries(DATA.heat[s].values).filter(([race]) => race.endsWith('-SEN') === sen).reduce((a, [, v]) => a + v.reduce((x, y) => x + y, 0), 0) : 0;
$('#toptiles').innerHTML = [['All R committees', false, 'House, Republican side'], ['All D committees', false, 'House, Democratic side'], ['All R committees', true, 'Senate, Republican side'], ['All D committees', true, 'Senate, Democratic side']]
  .map(([s, sen, l]) => `<div class="tile"><b>${fmt(totOff(s, sen))}</b><span>${dot(s)}${l}</span></div>`).join('');
$('#tiles').innerHTML = [['All R committees','Republican side, total'],['All D committees','Democratic side, total']]
  .map(([s,l]) => `<div class="tile"><b>${fmt(tot(s))}</b><span>${dot(s)}${l}</span></div>`).join('') +
  cmts.map(s => `<div class="tile"><b>${fmt(tot(s))}</b><span>${dot(s)}${s}</span></div>`).join('');

// ---- priorities
const PERIODS = [['all','All to date',NW],['4','Last 4 weeks',4],['2','Last 2 weeks',2]];
const sumW = (arr, from, to) => { let t = 0; for (let i = Math.max(0, from); i < Math.min(NW, to); i++) t += arr[i]; return t; };
const val = (sp, race, n, back) => { const v = DATA.heat[sp] && DATA.heat[sp].values[race]; return v ? sumW(v, NW - n*(back+1), NW - n*back) : 0; };
const btns = (id, opts, cur) => $(id).innerHTML = opts.map(([k, l]) => `<button data-k="${k}" aria-pressed="${k === cur}">${l}</button>`).join(' ');
let pOff = 'H', pPer = '4', cSp = 'All R committees', cPer = '4';
const allRaces = Object.keys(DATA.race_totals);
function prio(){
  btns('#p-office', [['H','House'],['S','Senate']], pOff); btns('#p-period', PERIODS, pPer);
  const n = PERIODS.find(p => p[0] === pPer)[2];
  let rows = allRaces.filter(r => r.endsWith('-SEN') === (pOff === 'S')).map(r => ({race: r, R: val('All R committees', r, n, 0), D: val('All D committees', r, n, 0)}))
    .filter(x => x.R + x.D > 0).sort((a, b) => (b.R + b.D) - (a.R + a.D));
  const total = rows.length; rows = rows.slice(0, 25);
  $('#p-note').textContent = pPer === 'all' ? `Top ${rows.length} of ${total} races, all general-election spending to date.` : `Top ${rows.length} of ${total} races, weeks of ${wk(W[NW - n])} to ${wk(W[NW-1])} (current week partial).`;
  const max = Math.max(...rows.flatMap(x => [x.R, x.D])), lx = 150, bw = 620, rh = 34, width = lx + bw + 90;
  let s = `<svg width="${width}" height="${rows.length * rh + 6}" role="img" aria-label="Races ranked by spending, by party side">`;
  rows.forEach((x, i) => {
    const y = i * rh + 4, who = (DATA.race_cands[x.race] || []).slice(0, 2).map(c => c.split(',')[0]).join(' / ');
    const detail = cmts.map(c => [c, val(c, x.race, n, 0)]).filter(e => e[1] > 0).sort((a, b) => b[1] - a[1]).map(e => `${e[0]}: <b>${full(e[1])}</b>`).join('<br>') +
      ['Other R', 'Other D'].map(o => { const t = ((DATA.other_top[o] || {})[x.race] || []).slice(0, 3).map(e => e[0]).join(', '); return t ? `<br><i>${o}, largest to date: ${t}</i>` : ''; }).join('');
    s += `<text class="lab" x="0" y="${y + 12}" style="font-weight:600">${i + 1}. ${x.race}</text><text x="0" y="${y + 25}">${who.slice(0, 24)}</text>`;
    [['R','--r'],['D','--d']].forEach(([k, c], j) => {
      const w = x[k] / max * bw, by = y + 2 + j * 13;
      if (x[k] > 0) s += `<path d="M${lx} ${by}h${Math.max(w - 3, 0)}a3 3 0 0 1 3 3v5a3 3 0 0 1 -3 3h-${Math.max(w - 3, 0)}z" fill="var(${c})"/>`;
      s += `<text x="${lx + w + 6}" y="${by + 10}">${x[k] > 0 ? fmt(x[k]) : (k + ' none')}</text>`;
    });
    s += `<rect x="0" y="${y}" width="${width}" height="${rh - 4}" fill="transparent" data-t="<b>${x.race}</b> · ${fmt(x.R + x.D)}<br>${detail}"></rect>`;
  });
  $('#p-chart').innerHTML = s + '</svg>';
}
function cprio(){
  btns('#c-period', PERIODS.slice(1), cPer);
  const n = +cPer, h = DATA.heat[cSp];
  const tr = h.races.reduce((a, r) => a + val(cSp, r, n, 0), 0), tp = h.races.reduce((a, r) => a + val(cSp, r, n, 1), 0);
  let rows = h.races.map(r => ({race: r, v: val(cSp, r, n, 0), p: val(cSp, r, n, 1)})).filter(x => x.v > 0 || x.p > 0)
    .map(x => Object.assign(x, {s: tr ? x.v / tr : 0, ps: tp ? x.p / tp : null})).sort((a, b) => b.s - a.s || b.p - a.p);
  const total = rows.length; rows = rows.slice(0, 30);
  const thin = tp < 0.10 * tr;
  $('#c-note').textContent = `${cSp}: ${fmt(tr)} in the weeks of ${wk(W[NW - n])} to ${wk(W[NW-1])}; ${fmt(tp)} in the preceding ${n} weeks.` + (thin ? ' The preceding period is under 10% of this one, so its shares rest on little money.' : '') + (total > 30 ? ` Top 30 of ${total} races.` : '');
  const max = Math.max(...rows.flatMap(x => [x.s, x.ps || 0])), lx = 70, bw = 600, rh = 22, width = lx + bw + 190, col = side[cSp] === 'R' ? '--r' : '--d';
  let s = `<svg width="${width}" height="${rows.length * rh + 6}" role="img" aria-label="${cSp} races by share of spending">`;
  rows.forEach((x, i) => {
    const y = i * rh + 4, w = x.s / max * bw, ch = x.ps === null ? null : (x.s - x.ps) * 100;
    s += `<text class="lab" x="${lx - 8}" y="${y + 12}" text-anchor="end">${x.race}</text>`;
    if (w > 0) s += `<path d="M${lx} ${y + 2}h${Math.max(w - 3, 0)}a3 3 0 0 1 3 3v6a3 3 0 0 1 -3 3h-${Math.max(w - 3, 0)}z" fill="var(${col})"/>`;
    if (x.ps !== null) s += `<rect x="${lx + x.ps / max * bw - 1}" y="${y - 1}" width="2" height="18" fill="var(--text)"/>`;
    s += `<text x="${lx + Math.max(w, (x.ps || 0) / max * bw) + 8}" y="${y + 13}">${(x.s * 100).toFixed(1)}% · ${fmt(x.v)}${ch === null ? '' : ' · ' + (ch >= 0 ? '▲ +' : '▼ ') + ch.toFixed(1) + ' pts'}${x.p === 0 && x.v > 0 ? ' · new' : ''}</text>`;
    s += `<rect x="0" y="${y}" width="${width}" height="${rh - 2}" fill="transparent" data-t="<b>${x.race}</b><br>This period: ${full(x.v)} (${(x.s * 100).toFixed(1)}%)<br>Preceding: ${full(x.p)}${x.ps === null ? '' : ' (' + (x.ps * 100).toFixed(1) + '%)'}"></rect>`;
  });
  $('#c-chart').innerHTML = s + '</svg>';
}
$('#c-sp').innerHTML = spenders.slice().sort((a, b) => b.startsWith('All ') - a.startsWith('All ')).map(s => `<option>${s}</option>`).join('');
$('#p-office').onclick = e => { if (e.target.dataset.k) { pOff = e.target.dataset.k; prio(); } };
$('#p-period').onclick = e => { if (e.target.dataset.k) { pPer = e.target.dataset.k; prio(); } };
$('#c-period').onclick = e => { if (e.target.dataset.k) { cPer = e.target.dataset.k; cprio(); } };
$('#c-sp').onchange = e => { cSp = e.target.value; cprio(); };
prio(); cprio();
['#p-chart', '#c-chart'].forEach(id => { $(id).addEventListener('mousemove', e => { const t = e.target.dataset && e.target.dataset.t; t ? showTip(e, t) : hideTip(); }); $(id).addEventListener('mouseleave', hideTip); });

// ---- movers
let win = 4, msp = 'All';
$('#winbtn').innerHTML = [2,4,8].map(n => `<button data-n="${n}" aria-pressed="${n===win}">${n} weeks</button>`).join(' ');
$('#spsel').innerHTML = ['All', ...spenders].map(s => `<option>${s}</option>`).join('');
function movers(){
  const rows = DATA.movers.filter(m => m.window === win && m.change_pp !== null && (msp === 'All' || m.spender === msp) && !(document.querySelector('#thin').checked && m.thin_base))
    .sort((a, b) => Math.abs(b.change_pp) - Math.abs(a.change_pp)).slice(0, 30);
  $('#movers').innerHTML = '<tr><th>Spender</th><th class="l">Race</th><th>Prior share</th><th>Recent share</th><th>Change (points)</th><th>Prior $</th><th>Recent $</th></tr>' +
    rows.map(m => `<tr><td>${dot(m.spender)}${m.spender}</td><td class="l">${m.race}</td><td>${(m.prior_share*100).toFixed(1)}%</td><td>${(m.recent_share*100).toFixed(1)}%</td>
      <td class="${m.change_pp >= 0 ? 'up' : 'down'}">${m.change_pp >= 0 ? '+' : ''}${m.change_pp.toFixed(1)}</td><td>${full(m.prior)}</td><td>${full(m.recent)}</td></tr>`).join('');
  const a = W[Math.max(0, NW - win)], b = W[Math.max(0, NW - 2*win)], c = W[Math.max(0, NW - win - 1)];
  $('#moversnote').textContent = `Recent window: weeks of ${wk(a)} to ${wk(W[NW-1])}. Prior window: weeks of ${wk(b)} to ${wk(c)}. Top 30 by size of change. A spender with no spending in the prior window has no change figure and is left out.`;
}
$('#winbtn').onclick = e => { if (e.target.dataset.n) { win = +e.target.dataset.n; document.querySelectorAll('#winbtn button').forEach(b => b.setAttribute('aria-pressed', +b.dataset.n === win)); movers(); } };
$('#spsel').onchange = e => { msp = e.target.value; movers(); };
$('#thin').onchange = movers;
movers();

// ---- heatmaps
const steps = ['--h1','--h2','--h3','--h4','--h5','--h6','--h7'];
function heat(sp){
  const h = DATA.heat[sp], first = CS, cols = W.slice(first);
  const since = r => h.values[r].slice(first).reduce((a, b) => a + b, 0);
  let races = h.races.filter(r => since(r) > 0).sort((a, b) => since(b) - since(a));
  const cur = DATA.currency.find(c => c.committee === sp), kind = cur && cur.kind !== 'independent expenditures' ? ' · ' + cur.kind : '';
  if (!races.length) return `<div class="card"><h3>${dot(sp)}${sp}</h3><div class="sub">${fmt(tot(sp))} total to date${kind}. No spending dated since the week of ${wk(W[CS])} in the data${cur && cur.latest ? '; latest transaction ' + cur.latest : ''}.</div></div>`;
  const nAll = races.length; races = races.slice(0, 40);
  const max = Math.max(...races.flatMap(r => h.values[r].slice(first)));
  const cw = Math.max(22, Math.min(64, Math.floor(820 / cols.length))), ch = 18, lx = 70, tx = 78;
  const width = lx + cols.length * cw + tx, height = 22 + races.length * ch + 4;
  let s = `<svg width="${width}" height="${height}" role="img" aria-label="${sp} weekly spending by race">`;
  cols.forEach((w, j) => { s += `<text x="${lx + j*cw + cw/2}" y="14" text-anchor="middle">${wk(w)}</text>`; });
  races.forEach((r, i) => {
    const y = 22 + i * ch, vals = h.values[r].slice(first);
    s += `<text class="lab" x="${lx - 8}" y="${y + 13}" text-anchor="end">${r}</text>`;
    vals.forEach((v, j) => {
      const k = v <= 0 ? null : steps[Math.min(6, Math.floor(Math.sqrt(v / max) * 7))];
      s += `<rect x="${lx + j*cw + 1}" y="${y + 1}" width="${cw - 2}" height="${ch - 2}" rx="2" fill="var(${k || '--zero'})" data-t="${r} · week of ${wk(cols[j])}<br><b>${full(v)}</b>"></rect>`;
    });
    s += `<text x="${lx + cols.length*cw + 8}" y="${y + 13}">${fmt(since(r))}</text>`;
  });
  s += '</svg>';
  const leg = `<div class="legend"><span>${steps.map(k => `<i class="swatch" style="background:var(${k})"></i>`).join('')} low to high (max ${fmt(max)} in a week)</span><span><i class="swatch" style="background:var(--zero)"></i> no spending</span><span>Right column: total since the week of ${wk(W[CS])}</span></div>`;
  return `<div class="card"><h3>${dot(sp)}${sp}</h3><div class="sub">${nAll > 40 ? 'Top 40 of ' + nAll : nAll} races since the week of ${wk(W[CS])}; ${fmt(tot(sp))} total to date${kind}</div>${leg}${s}</div>`;
}
$('#heat').innerHTML = spenders.map(heat).join('');
$('#heat').addEventListener('mousemove', e => { const t = e.target.dataset && e.target.dataset.t; t ? showTip(e, t) : hideTip(); });
$('#heat').addEventListener('mouseleave', hideTip);

// ---- cumulative small multiples
function sideSeries(race){
  const out = {};
  [['R','All R committees'],['D','All D committees']].forEach(([k, sp]) => {
    const v = (DATA.heat[sp] && DATA.heat[sp].values[race]) || W.map(() => 0); let c = 0; out[k] = v.map(x => c += x); });
  return out;
}
const START = Math.min(CS, NW - 2);
function mini(race){
  const s = sideSeries(race), w = 250, h = 130, l = 6, r = 66, t = 16, b = 20, n = NW - START;
  const max = Math.max(s.R[NW-1], s.D[NW-1], 1), x = i => l + (i - START) / (n - 1) * (w - l - r), y = v => t + (1 - v / max) * (h - t - b);
  const path = a => a.slice(START).map((v, i) => (i ? 'L' : 'M') + x(i + START).toFixed(1) + ' ' + y(v).toFixed(1)).join('');
  let ry = y(s.R[NW-1]) + 4, dy = y(s.D[NW-1]) + 4;
  if (Math.abs(ry - dy) < 12) { if (ry <= dy) { ry -= (12 - (dy - ry)) / 2; dy = ry + 12; } else { dy -= (12 - (ry - dy)) / 2; ry = dy + 12; } }
  const who = (DATA.race_cands[race] || []).slice(0, 3).join(', ');
  return `<div class="mini"><h3>${race} <span class="sub" style="font-weight:400">${fmt(DATA.race_totals[race] || 0)}${RATING[race] ? ' · ' + RATING[race] : ''}</span></h3><div class="who" title="${who}">${who}</div>
  <svg width="100%" viewBox="0 0 ${w} ${h}" data-race="${race}" role="img" aria-label="${race} cumulative spending by side">
  <line x1="${l}" x2="${w - r}" y1="${t}" y2="${t}" stroke="var(--line)"/><line x1="${l}" x2="${w - r}" y1="${h - b}" y2="${h - b}" stroke="var(--line)"/>
  <text x="${l}" y="${t - 4}">${fmt(max)}</text>
  <text x="${l}" y="${h - 6}">${wk(W[START])}</text><text x="${w - r}" y="${h - 6}" text-anchor="end">${wk(W[NW-1])}</text>
  <path d="${path(s.R)}" fill="none" stroke="var(--r)" stroke-width="2" stroke-linejoin="round"/>
  <path d="${path(s.D)}" fill="none" stroke="var(--d)" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="${x(NW-1)}" cy="${y(s.R[NW-1])}" r="3" fill="var(--r)"/><circle cx="${x(NW-1)}" cy="${y(s.D[NW-1])}" r="3" fill="var(--d)"/>
  <text class="lab" x="${w - r + 7}" y="${ry}">R ${fmt(s.R[NW-1])}</text><text class="lab" x="${w - r + 7}" y="${dy}">D ${fmt(s.D[NW-1])}</text>
  <line class="cross" y1="${t}" y2="${h - b}" stroke="var(--muted)" stroke-dasharray="2 2" visibility="hidden"/>
  <rect x="${l}" y="${t}" width="${w - l - r}" height="${h - t - b}" fill="transparent"/></svg></div>`;
}
const byTot = Object.entries(DATA.race_totals).sort((a, b) => b[1] - a[1]).map(e => e[0]);
const RATING = {}; Object.entries(DATA.cook.ratings).forEach(([k, v]) => v.forEach(x => RATING[x] = k));
const spendOrder = (a, b) => (DATA.race_totals[b] || 0) - (DATA.race_totals[a] || 0);
const tossups = DATA.cook.ratings['Toss Up'].slice().sort(spendOrder);
const leans = DATA.cook.ratings['Lean Democrat'].concat(DATA.cook.ratings['Lean Republican']).sort(spendOrder);
const FLOOR = 'VA-01';  // show every Lean race with at least as much spending as this one
const leanR = new Set(DATA.cook.ratings['Lean Republican']);
const house30 = tossups.concat(leans.filter(x => leanR.has(x) || (DATA.race_totals[x] || 0) >= (DATA.race_totals[FLOOR] || 0))).concat(Object.keys(DATA.cook.also_show || {}));
Object.entries(DATA.cook.also_show || {}).forEach(([k, v]) => RATING[k] = v);
$('#cooknote').innerHTML = `Races are chosen by <a href="${DATA.cook.url}" target="_blank" rel="noopener" style="color:inherit">${DATA.cook.source}</a> as of ${DATA.cook.as_of}: all ${tossups.length} Toss Up races, then every Lean Republican race (${leanR.size}) and the Lean Democrat races with at least as much spending as ${FLOOR} (${house30.filter(x => RATING[x] === 'Lean Democrat').length} of ${DATA.cook.ratings['Lean Democrat'].length}). Within each group, races are ordered by spending.${Object.keys(DATA.cook.also_show || {}).length ? ' Also shown by request: ' + Object.entries(DATA.cook.also_show).map(([k, v]) => k + ' (' + v + ')').join(', ') + '.' : ''} The ratings list is fixed in cook_ratings.json and does not update on its own.`;
$('#house').innerHTML = house30.map(mini).join('');
$('#senate').innerHTML = byTot.filter(r => r.endsWith('-SEN')).map(mini).join('');
document.querySelectorAll('.mini svg').forEach(svg => {
  const race = svg.dataset.race, s = sideSeries(race), cross = svg.querySelector('.cross'), n = NW - START;
  svg.addEventListener('mousemove', e => {
    const bb = svg.getBoundingClientRect(), px = (e.clientX - bb.left) / bb.width * 250;
    const i = Math.max(0, Math.min(n - 1, Math.round((px - 6) / (250 - 6 - 66) * (n - 1)))) + START;
    const cx = 6 + (i - START) / (n - 1) * (250 - 6 - 66);
    cross.setAttribute('x1', cx); cross.setAttribute('x2', cx); cross.setAttribute('visibility', 'visible');
    showTip(e, `${race} · through week of ${wk(W[i])}<br>R side: <b>${full(s.R[i])}</b><br>D side: <b>${full(s.D[i])}</b>`);
  });
  svg.addEventListener('mouseleave', () => { cross.setAttribute('visibility', 'hidden'); hideTip(); });
});

// ---- entries / stopped / currency
let ocSide = 'All';
function ocRender(){
  btns('#oc-side', [['All','All'],['Other R','Other R'],['Other D','Other D']], ocSide);
  const q = $('#oc-q').value.trim().toLowerCase();
  const rows = DATA.other_committees.filter(c => (ocSide === 'All' || c.spender === ocSide) &&
    (!q || c.name.toLowerCase().includes(q) || c.id.toLowerCase().includes(q) || c.top.some(t => t[0].toLowerCase().includes(q))));
  $('#oc-n').textContent = `${rows.length.toLocaleString('en-US')} committees, ${fmt(rows.reduce((a, c) => a + c.total, 0))}`;
  const esc = s => String(s).replace(/[&<>"]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch]));
  $('#oc').innerHTML = '<tr><th>Committee</th><th class="l">Group</th><th>Total</th><th>Races</th><th class="l">Largest races</th><th>Latest</th></tr>' +
    rows.map(c => `<tr><td style="white-space:normal;min-width:240px"><a href="https://www.fec.gov/data/committee/${c.id}/" target="_blank" rel="noopener" style="color:inherit">${esc(c.name)}</a></td><td class="l">${dot(c.spender)}${c.spender}</td><td>${full(c.total)}</td><td>${c.races}</td><td class="l">${c.top.map(t => t[0] + ' ' + fmt(t[1])).join(', ')}</td><td>${c.latest}</td></tr>`).join('');
}
$('#oc-side').onclick = e => { if (e.target.dataset.k) { ocSide = e.target.dataset.k; ocRender(); } };
$('#oc-q').oninput = ocRender;
ocRender();
$('#ensel').innerHTML = ['All committees', ...cmts].map(s => `<option>${s}</option>`).join('');
function entries(){
  const f = $('#ensel').value;
  const rows = DATA.entries.filter(e => !e.spender.startsWith('All ') && (f === 'All committees' || e.spender === f))
    .sort((a, b) => b.first_week.localeCompare(a.first_week) || b.total - a.total).slice(0, 60);
  $('#entries').innerHTML = '<tr><th>Committee</th><th class="l">Race</th><th>First week</th><th>Spend that week</th><th>Total to date</th></tr>' +
    rows.map(e => `<tr><td>${dot(e.spender)}${e.spender}</td><td class="l">${e.race}</td><td>${e.first_week}</td><td>${full(e.first_week_spend)}</td><td>${full(e.total)}</td></tr>`).join('');
}
$('#ensel').onchange = entries; entries();
const st = DATA.stopped.filter(e => !e.spender.startsWith('All ')).sort((a, b) => b.total - a.total);
$('#stopped').innerHTML = st.length ? '<tr><th>Committee</th><th class="l">Race</th><th>Last week with spending</th><th>Full weeks silent</th><th>Weeks active</th><th>Total to date</th></tr>' +
  st.map(e => `<tr><td>${dot(e.spender)}${e.spender}</td><td class="l">${e.race}</td><td>${e.last_week}</td><td>${e.weeks_silent}</td><td>${e.active_weeks}</td><td>${full(e.total)}</td></tr>`).join('')
  : '<tr><td>No race meets this test.</td></tr>';
$('#currency').innerHTML = '<tr><th>Spender</th><th class="l">Type</th><th>Latest transaction date</th><th>Latest filing received</th><th>Rows</th><th>General-election total</th></tr>' +
  DATA.currency.map(c => `<tr><td>${dot(c.committee)}${c.committee}${c.ncommittees > 1 ? ' (' + c.ncommittees + ' committees)' : ''}</td><td class="l">${c.kind}</td><td>${c.latest || 'none'}</td><td>${c.latest_filing || ''}</td><td>${c.rows.toLocaleString('en-US')}</td><td>${full(c.total)}</td></tr>`).join('');
</script></body></html>
"""

out = os.path.join(HERE, "output", "ie_report.html")
open(out, "w").write(HTML.replace("__DATA__", json.dumps(data, separators=(",", ":"))))
print("wrote", out, f"{os.path.getsize(out)/1024:.0f} KB")
