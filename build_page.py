"""Builds index.html for GitHub Pages: shell_head.html (tokens, d3, dash stand-in) + page.html
(the dashboard page as stored in the claude.ai artifact) + footer. Run after changing either file."""
import pathlib
here = pathlib.Path(__file__).parent
head = (here / 'shell_head.html').read_text(encoding='utf-8')
page = (here / 'page.html').read_text(encoding='utf-8').replace('<meta name="dash-one-writer">\n', '')
snap = ('<p class="lx-note" style="margin-top: var(--cds-gap-sm)">Снимок данных: '
        '<b data-draw="kpi" data-source="manifest" data-field="generated_at" data-row="0" data-fmt="date">—</b>. '
        'Обновляется скриптом dashboard_snapshot.py --push.</p>\n  </header>')
assert page.count('</header>') == 1
page = page.replace('</header>', snap, 1)
foot = ('<p class="lx-foot">Данные: GitHub API (публичные ишью, PR и комментарии itaskaev2 в '
        '<a href="https://github.com/valentderah/totk-pc-recomp">valentderah/totk-pc-recomp</a>) и локальные логи Claude Code. '
        'Цена по API — оценка по принятым тарифам, фактически оплачена только подписка. '
        'Исходники страницы: <a href="https://github.com/itaskaev2/totk-recomp-stats">itaskaev2/totk-recomp-stats</a>.</p>\n')
(here / 'index.html').write_text(head + page + foot + '</div>\n</body>\n</html>\n', encoding='utf-8')
print('index.html written')
