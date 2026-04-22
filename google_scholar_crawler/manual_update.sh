#!/bin/bash
# 手动更新 Google Scholar 引用数
# 使用方法: ./manual_update.sh 111 6 3
# 参数: citations h-index i10-index

CITATIONS=${1:-89}
HINDEX=${2:-5}
I10INDEX=${3:-2}

echo "📊 更新 Google Scholar 统计数据..."
echo "Citations: $CITATIONS"
echo "H-index: $HINDEX"
echo "i10-index: $I10INDEX"

cd "$(dirname "$0")/.."
# 更新 JSON 文件和手动 floor
python3 << EOF
import json
from pathlib import Path

root = Path(".")
result_paths = [
    root / "google_scholar_crawler" / "results" / "gs_data.json",
    root / "results" / "gs_data.json",
    root / "_data" / "scholar.json",
]

for path in result_paths:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data['citedby'] = $CITATIONS
    data['citedby5y'] = max(data.get('citedby5y', 0), $CITATIONS)
    data['hindex'] = $HINDEX
    data['i10index'] = $I10INDEX

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": "$CITATIONS"
}

for path in [
    root / "google_scholar_crawler" / "results" / "gs_data_shieldsio.json",
    root / "results" / "gs_data_shieldsio.json",
]:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(shieldio_data, f, ensure_ascii=False)

manual_floor = {
    "citedby": $CITATIONS,
    "citedby5y": $CITATIONS
}

with open(root / "google_scholar_crawler" / "manual_citation_floor.json", 'w', encoding='utf-8') as f:
    json.dump(manual_floor, f, ensure_ascii=False)

print("✅ 已更新 JSON 数据文件")
EOF

echo ""
echo "🎉 更新完成！"
echo "运行 ./run_server.sh 查看效果"
