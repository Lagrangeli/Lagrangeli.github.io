#!/usr/bin/env python3
"""
自动更新 about.md 中的 Google Scholar 引用数
"""
import json
import re
import os

# 读取 Google Scholar 数据
with open('results/gs_data.json', 'r') as f:
    data = json.load(f)
    citations = data.get('citedby', 0)

print(f"Current citations: {citations}")

# 读取 about.md
about_path = '../_pages/about.md'
with open(about_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 更新徽章 URL 中的引用数
# 匹配模式：Google%20Scholar-数字%20citations
pattern = r'(Google%20Scholar-)\d+(%20citations)'
replacement = f'\\g<1>{citations}\\g<2>'
new_content = re.sub(pattern, replacement, content)

# 写回文件
if new_content != content:
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Updated badge to {citations} citations")
else:
    print("ℹ️  No changes needed")

