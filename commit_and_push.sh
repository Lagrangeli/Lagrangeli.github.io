#!/bin/bash
# 提交并推送自动更新配置到 GitHub

echo "📦 准备提交文件到 GitHub..."
echo ""

# 添加所有相关文件
git add .github/workflows/update-google-scholar.yml
git add google_scholar_crawler/main.py
git add google_scholar_crawler/update_badge.py
git add google_scholar_crawler/requirements.txt
git add google_scholar_crawler/results/gs_data.json
git add google_scholar_crawler/results/gs_data_shieldsio.json
git add google_scholar_crawler/README.md
git add _pages/about.md
git add .gitignore
git add update_citations.sh
git add UPDATE_CITATIONS.md
git add SETUP_AUTO_UPDATE.md

echo "📋 查看待提交的文件："
git status --short

echo ""
read -p "确认提交这些文件？(y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo ""
    echo "💾 提交中..."
    git commit -m "✨ Add automatic Google Scholar citation update system

- Add GitHub Actions workflow for daily auto-update
- Add Python scripts for fetching and updating citations
- Update about.md with citation badge (89 citations)
- Add documentation and setup guide
"
    
    echo ""
    echo "🚀 推送到 GitHub..."
    git push origin master
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🎉 代码已成功推送到 GitHub！"
    echo ""
    echo "📝 下一步："
    echo "1. 打开 https://github.com/$(git config remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')"
    echo "2. 进入 Settings → Secrets → Actions"
    echo "3. 添加 Secret："
    echo "   Name:  GOOGLE_SCHOLAR_ID"
    echo "   Value: r9f4mLMAAAAJ"
    echo ""
    echo "4. 进入 Actions 标签，手动触发首次更新"
    echo ""
    echo "📖 详细说明：查看 SETUP_AUTO_UPDATE.md"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
else
    echo ""
    echo "❌ 取消提交"
fi

