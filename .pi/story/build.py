#!/usr/bin/env python3
"""把故事内容重新拼进 ai.html 的导航与 D 对象，题库和交互逻辑原样保留。

用法：python3 .pi/story/build.py
只改 ai.html 里的两个块：侧栏导航、const D = {...}；其余字节不动。
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nav as NAVMOD, figs, review, acts_a, acts_b, acts_c, acts_d, acts_e

TARGET = os.path.normpath(os.path.join(HERE, '..', '..', 'ai.html'))
COLORS = ["c1", "c2", "c3", "c4", "c5", "c6"]


def build_nav():
    import re
    lines = ['  <aside class="side" id="side">']
    counter = [0]

    def item(sid, txt, cls="nav"):
        counter[0] += 1
        txt = re.sub(r"^\d+\.\s*", "", txt)
        return f'<button class="{cls}" data-id="{sid}">{counter[0]}. {txt}</button>'

    lines.append('    <div class="group c0"><div class="group-title">开篇</div>'
                 + item("intro", "任务简报：给一辆车装上会说话的地图", "nav on") + '</div>')
    for i, (label, short, _prefix, items) in enumerate(NAVMOD.ACTS[1:]):
        lines.append(f'    <div class="group {COLORS[i % 6]}"><div class="group-title">{label} · {short}</div>')
        for sid, txt in items:
            lines.append("      " + item(sid, txt))
        lines.append('    </div>')
    lines.append('    <div class="group c6"><div class="group-title">尾声</div>'
                 + item("final", "尾声：五个问题的答案") + '</div>')
    lines.append('    <div class="group c-exam"><div class="group-title">考试中心</div>'
                 '<button class="nav" data-id="exam">🎯 通关测验（1000 题库随机抽题）</button></div>')
    lines.append('  </aside>')
    return "\n".join(lines)


def build_d():
    sections = acts_a.S + acts_b.S + acts_c.S + acts_d.S + acts_e.S
    ids = [x[0] for x in sections]
    assert len(ids) == len(set(ids)), "duplicate section id"
    out = ['const D = {']
    for sid, tag, title, html in sections:
        fig = figs.F.get(sid, '')
        html = fig + html if fig else html
        if sid in review.R:
            label, question, lines = review.R[sid]
            html = html + (
                f'<div class="note check"><div class="note-t">📌 {label}复盘 · '
                f'回答的是「{question}」</div><ul>'
                f'<li><strong>一笔账：</strong>{lines[0]}</li>'
                f'<li><strong>三个坑：</strong>{lines[1]}</li>'
                f'<li><strong>带走一句：</strong>{lines[2]}</li></ul></div>'
            )
        assert '`' not in html and '${' not in html, f"backtick/'${{' in {sid}"
        out.append(f'{sid}:{{tag:{json.dumps(tag, ensure_ascii=False)},'
                   f'title:{json.dumps(title, ensure_ascii=False)},html:`{html}`}},')
    out.append('};')
    return "\n".join(out) + "\n\n"


def main():
    s = open(TARGET, encoding='utf-8').read()
    i = s.index('<aside class="side" id="side">')
    j = s.index('</aside>', i) + len('</aside>')
    k = s.index('const D = {')
    e = s.index('// ======= 题库')
    new = s[:i].rstrip(' ') + build_nav() + s[j:k] + build_d() + s[e:]
    open(TARGET, 'w', encoding='utf-8').write(new)
    print(f"rebuilt {TARGET}: {len(new)} bytes")


if __name__ == '__main__':
    main()
