#!/bin/bash
# 手动更新 Google Scholar 引用数
# 使用方法: ./manual_update.sh 89 5 2
# 参数: citations h-index i10-index

CITATIONS=${1:-89}
HINDEX=${2:-5}
I10INDEX=${3:-2}

echo "📊 更新 Google Scholar 统计数据..."
echo "Citations: $CITATIONS"
echo "H-index: $HINDEX"
echo "i10-index: $I10INDEX"

# 更新 about.md 中的徽章
cd "$(dirname "$0")/.."
sed -i.bak "s/Google%20Scholar-[0-9]*%20citations/Google%20Scholar-${CITATIONS}%20citations/g" _pages/about.md
echo "✅ 已更新 _pages/about.md"

# 更新 JSON 文件
cd google_scholar_crawler/results
python3 << EOF
import json

# 更新 gs_data.json
with open('gs_data.json', 'r') as f:
    data = json.load(f)

data['citedby'] = $CITATIONS
data['hindex'] = $HINDEX
data['i10index'] = $I10INDEX

with open('gs_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 更新 gs_data_shieldsio.json
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": "$CITATIONS"
}

with open('gs_data_shieldsio.json', 'w') as f:
    json.dump(shieldio_data, f, ensure_ascii=False)

print("✅ 已更新 JSON 数据文件")
EOF

echo ""
echo "🎉 更新完成！"
echo "运行 ./run_server.sh 查看效果"

