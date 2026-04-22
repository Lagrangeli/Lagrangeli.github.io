#!/bin/bash
# 一键更新 Google Scholar 引用数据
# 用法: ./update_citations.sh

set -e

echo "🚀 正在从 Google Scholar 获取最新引用数据..."
echo ""

cd google_scholar_crawler

# 激活虚拟环境（如果存在）
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "⚠️  虚拟环境不存在，正在创建..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -q -r requirements.txt
    echo "✅ 虚拟环境创建完成"
    echo ""
fi

# 运行爬虫
echo "📊 正在爬取 Google Scholar 数据..."
GOOGLE_SCHOLAR_ID=r9f4mLMAAAAJ python3 main.py > /dev/null 2>&1

# 读取最新数据
CITATIONS=$(python3 -c "import json; data = json.load(open('results/gs_data.json')); print(data.get('citedby', 0))")
HINDEX=$(python3 -c "import json; data = json.load(open('results/gs_data.json')); print(data.get('hindex', 0))")
I10INDEX=$(python3 -c "import json; data = json.load(open('results/gs_data.json')); print(data.get('i10index', 0))")

echo "✅ 成功获取数据："
echo "   📚 Citations: $CITATIONS"
echo "   🏆 H-index: $HINDEX"
echo "   ⭐ i10-index: $I10INDEX"
echo ""

cd ..
echo ""
echo "🎉 更新完成！"
echo "💡 运行 ./run_server.sh 查看效果"
echo ""
