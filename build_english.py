"""Generate the English page from the existing Chinese page and translations."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'timeline.fragment.html').read_text()
translations = json.loads((ROOT / 'translations.en.json').read_text())
ids = re.findall(r"\{id:'([^']+)'", source)
assert len(ids) == len(set(ids)) == 28
assert set(ids) == set(translations), 'Translate every entry before building'

def translate_record(match):
    line = match.group(0)
    paper_id = re.search(r"id:'([^']+)'", line).group(1)
    return re.sub(
        r"(short|venue|method|relation):'[^']*'",
        lambda field: field[1] + ':' + json.dumps(translations[paper_id][field[1]], ensure_ascii=False),
        line,
    )

english = re.sub(r"^ \{id:.*$", translate_record, source, flags=re.M)
english = re.sub(r'^const labels=.*$', 'const labels={};', english, flags=re.M)
ui = {
    '通向 WSP 的研究时间线': 'Research leading to WSP',
    '1992—2026 · 28 项代表工作 · 5 条研究路线': '1992–2026 · 28 representative works · 5 research routes',
    '按年份与研究方向排列的论文': 'Works arranged by year and research route',
    '◆ 后续补充 12 项　● 初版 16 项 · 点击名称查看方法与原文': '◆ 12 later additions · ● 16 initial entries · Select a work for details and its source',
    '按所列工作的首次公开年份分组；年份间距不代表时长。分类表示概念关联，不表示直接继承或概念首创。': 'Grouped by first public year; spacing is not proportional to elapsed time. Routes indicate conceptual relationships, not direct influence or priority claims.',
    '年份': 'Year',
    '读取机制': 'Mechanisms',
    '编辑行为': 'Behavior editing',
    '生成权重': 'Weight generation',
    '构造网络': 'Network construction',
    '研究与优化': 'Research & optimization',
    'WSP 研究对象': 'WSP itself',
    '补充条目': 'Later addition',
    '方法：': 'Method: ',
    '与 WSP 的关系：': 'Relation to WSP: ',
    '11 月 2 日 · 通用 LLM 读取、修复与构造权重': 'November 2 · A general-purpose LLM reads, repairs, and constructs weights',
    '，': ', ',
}
for original, replacement in ui.items():
    english = english.replace(original, replacement)
assert not re.search(r'[\u3400-\u9fff]', english), 'Untranslated Chinese text remains'
(ROOT / 'timeline.en.fragment.html').write_text(english)

# Keep the Chinese diagram and all its existing paper data byte-for-byte intact.
page = (ROOT / 'index.html').read_text()
frame_match = re.search(r'data-srcdoc="(.*?)"', page, re.S)
original_frame = frame_match[1]
frame = html.unescape(original_frame)
d3_tag = '<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>'
prefix, suffix = source.split(d3_tag)
bundle = re.search(re.escape(prefix) + r'<script>(.*?)</script>' + re.escape(suffix), frame, re.S)
assert bundle, 'Chinese export must match its editable source'
english_frame = frame.replace(bundle[0], english.replace(d3_tag, '<script>' + bundle[1] + '</script>'))
english_frame = english_frame.replace('lang="zh-CN"', 'lang="en"')

def add_switch(document, language):
    document = re.sub(r'<a data-language-switch=.*?</a>', '', document)
    if language == 'zh-CN':
        switch = '<a data-language-switch="en" href="en.html" lang="en" hreflang="en" aria-label="Switch to English">English</a>'
    else:
        switch = '<a data-language-switch="zh-CN" href="index.html" lang="zh-CN" hreflang="zh-CN" aria-label="切换到中文版">中文</a>'
    document = document.replace('</nav></header>', switch + '</nav></header>', 1)
    document = document.replace('header nav{display:flex;gap:18px;font-size:14px}', 'header nav{display:flex;flex-wrap:wrap;align-items:center;gap:18px;font-size:14px}')
    if 'header [data-language-switch]' not in document:
        document = document.replace('header strong{', 'header [data-language-switch]{border:1px solid currentColor;border-radius:6px;padding:5px 10px}header strong{', 1)
    return document

english_page = page[:frame_match.start(1)] + html.escape(english_frame, quote=True) + page[frame_match.end(1):]
english_page = english_page.replace('<html lang="zh-CN"', '<html lang="en"', 1)
english_page = english_page.replace('<title>Awesome WSP · Research Timeline</title>', '<title>Awesome WSP · Research Timeline (English)</title>', 1)
english_page = english_page.replace('资源清单 ↗', 'Resources ↗', 1)
(ROOT / 'en.html').write_text(add_switch(english_page, 'en'))
chinese_page = add_switch(page, 'zh-CN')
assert re.search(r'data-srcdoc="(.*?)"', chinese_page, re.S)[1] == original_frame
(ROOT / 'index.html').write_text(chinese_page)
print('Built English version: 28 translated entries; Chinese diagram unchanged.')
