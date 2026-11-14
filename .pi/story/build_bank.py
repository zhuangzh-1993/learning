#!/usr/bin/env python3
"""把 bank.json 拼回 ai.html 的 QUIZ_BANK 数组。

题库的每一题：
  q 题干 / o 选项 / a 应选项下标 / e 整题解析 / t 幕号 / n 逐项解释（字母 -> 理由）
用法：python3 .pi/story/build_bank.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.normpath(os.path.join(HERE, '..', '..', 'ai.html'))
DATA = os.path.join(HERE, 'bank.json')
EXAM_COUNT = 30


def emit(it):
    parts = [
        'q: ' + json.dumps(it['q'], ensure_ascii=False),
        'o: ' + json.dumps(it['o'], ensure_ascii=False),
        'a: ' + json.dumps(it['a']),
        'e: ' + json.dumps(it['e'], ensure_ascii=False),
        't: %d' % it['t'],
    ]
    if it.get('n'):
        parts.append('n: ' + json.dumps(it['n'], ensure_ascii=False))
    return '  { ' + ', '.join(parts) + ' }'


def main():
    bank = json.load(open(DATA, encoding='utf-8'))
    s = open(TARGET, encoding='utf-8').read()
    i = s.index('const QUIZ_BANK = [')
    j = s.index('function pickExamQuestions()')
    head = (f'const QUIZ_BANK = [\n' + ',\n'.join(emit(it) for it in bank) + '\n];\n\n'
            f'const EXAM_COUNT = {EXAM_COUNT}; // 每次从整库随机抽 {EXAM_COUNT} 题\n'
            f'let EXAM_QS = null; // 首次进入考试页时抽取\n\n')
    open(TARGET, 'w', encoding='utf-8').write(s[:i] + head + s[j:])
    tot = sum(len(it['o']) for it in bank)
    got = sum(len(it.get('n', {})) for it in bank)
    print(f'{len(bank)} 题，逐项解释 {got}/{tot} ({got/tot:.0%})')


if __name__ == '__main__':
    main()
