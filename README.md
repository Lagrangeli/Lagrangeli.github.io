# 🎓 Zhenyang Li's Academic Homepage

[![Website](https://img.shields.io/website?url=https%3A%2F%2Flagrangeli.github.io)](https://lagrangeli.github.io)
[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-89%20citations-4285F4?logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user=r9f4mLMAAAAJ)
[![GitHub stars](https://img.shields.io/github/stars/Lagrangeli/Lagrangeli.github.io)](https://github.com/Lagrangeli/Lagrangeli.github.io)
[![License](https://img.shields.io/github/license/Lagrangeli/Lagrangeli.github.io)](./LICENSE)

> **Live Website:** [https://lagrangeli.github.io/](https://lagrangeli.github.io/)

A modern, responsive academic personal homepage showcasing my research in Computer Vision, Computer Graphics, and AI.

<div align="center">
  <img src="docs/screenshot.png" width="90%" alt="Homepage Preview"/>
</div>

---

## 👤 About Me

I'm a Ph.D. student at **The University of Hong Kong (HKU)** 🇭🇰, working on:
- 🎨 3D/4D Scene Reconstruction & Generation
- 🖼️ Computational Imaging & Holography
- 🤖 Vision-Language & Multimodal AI

**Research Impact:**
- 📚 **13+ Publications** at top-tier conferences (ICCV, NeurIPS, ISMAR, etc.)
- 📊 **89 Citations** on Google Scholar
- 🏆 **H-index: 5** | **i10-index: 2**

---

## ✨ Key Features

### 🤖 **Automated Google Scholar Updates**
- Daily automatic crawling of citation statistics
- Auto-update of homepage badges
- Powered by GitHub Actions

### 📱 **Responsive Design**
- Mobile-friendly layout
- Smooth scroll navigation
- Fast loading with CDN acceleration

### 🎨 **Modern UI/UX**
- Research statistics visualization
- Publication preview images
- Color-coded research areas
- Clean and professional design

### 🚀 **Performance Optimized**
- Tencent Cloud COS global CDN for images
- Optimized image formats (JPEG for large files)
- Lazy loading and caching

### 📊 **Rich Content**
- Interactive research focus cards
- Publication images with links
- Google Scholar integration
- Detailed CV sections

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Static Site Generator** | Jekyll 4.x |
| **Frontend** | HTML5, CSS3 (SCSS), JavaScript |
| **Styling** | Custom SCSS + Minimal Mistakes Theme |
| **Automation** | GitHub Actions + Python |
| **CDN** | Tencent Cloud COS (Global Accelerate) |
| **Analytics** | Google Analytics (optional) |
| **Citation Crawler** | scholarly Python library |

---

## 📂 Project Structure

```
Lagrangeli.github.io/
├── _config.yml                 # Jekyll configuration
├── _pages/
│   └── about.md               # Main homepage content
├── _includes/                 # HTML partials
├── _layouts/                  # Page layouts
├── _sass/                     # Stylesheets
├── images/
│   ├── publications/          # Publication preview images
│   └── *.png                  # Favicon and icons
├── google_scholar_crawler/    # Auto-update scripts
│   ├── main.py               # Scholar data crawler
│   ├── update_badge.py       # Badge updater
│   └── results/              # Citation data
├── .github/workflows/
│   └── update-google-scholar.yml  # Auto-update workflow
└── assets/                    # CSS, JS, fonts
```

---

## 🚀 Quick Start

### For Visitors

Just visit **[https://lagrangeli.github.io/](https://lagrangeli.github.io/)** 🌐

### For Local Development

```bash
# Clone the repository
git clone https://github.com/Lagrangeli/Lagrangeli.github.io.git
cd Lagrangeli.github.io

# Install dependencies (requires Ruby)
bundle install

# Run local server with live reload
./run_server.sh
# or
bundle exec jekyll serve --livereload

# Open http://localhost:4000 in your browser
```

---

## 🔄 Automatic Updates

### Google Scholar Citations

The homepage automatically updates citation counts daily at **00:00 UTC** (08:00 Beijing Time).

**Manual Update:**
```bash
./update_citations.sh
```

**How it works:**
1. GitHub Actions triggers daily
2. Python crawler fetches latest data from Google Scholar
3. Updates JSON files and badges
4. Commits changes automatically
5. GitHub Pages redeploys

**Configuration:**
- Set `GOOGLE_SCHOLAR_ID` in GitHub Secrets
- See [QUICK_START.md](./QUICK_START.md) for details

---

## 📝 Content Management

### Update Publications

1. Add publication details in `_pages/about.md`
2. Add preview image to `images/publications/`
3. Supported formats: PNG, JPG (optimized for web)

**Image Requirements:**
- **Size:** 1200px width recommended
- **Format:** PNG or JPEG
- **Aspect Ratio:** 2:1 or similar
- **Location:** `images/publications/paper-name.jpg`

### Update News

Edit the `# 🔥 News` section in `_pages/about.md`:

```markdown
- *2025.XX*: 🎉 Your news item here!
```

### Update Research Areas

Modify the `## 🔬 Research Focus` section in `_pages/about.md`.

---

## 🖼️ CDN Configuration

Publication images are hosted on **Tencent Cloud COS** with global acceleration:

```
https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/
```

**Benefits:**
- ⚡ 7x faster loading speed
- 🌍 Global CDN acceleration
- 💾 Reduced GitHub Pages bandwidth

**Note:** Images in `images/publications/` are synced to COS manually.

---

## 🎨 Customization

### Update Personal Info

Edit `_config.yml`:

```yaml
title: "Your Name's Homepage"
author:
  name: "Your Name"
  bio: "Your Title/Position"
  location: "Your City, Country"
  employer: "Your Institution"
  email: "your.email@example.com"
```

### Modify Theme Colors

Edit `_sass/_variables.scss` to change colors, fonts, and spacing.

### Add New Sections

Add anchor tags and update `_data/navigation.yml`:

```yaml
- title: "New Section"
  url: "/#-new-section"
```

Then add the section in `_pages/about.md`:

```markdown
<span class='anchor' id='-new-section'></span>

# 🎯 New Section
Content here...
```

---

## 📊 Analytics & SEO

### Google Analytics (Optional)

1. Get your GA tracking ID
2. Set `google_analytics_id` in `_config.yml`
3. Rebuild and deploy

### SEO Optimization

- ✅ Semantic HTML structure
- ✅ Meta descriptions
- ✅ Open Graph tags
- ✅ Sitemap.xml auto-generated
- ✅ robots.txt configured

---

## 🛡️ Maintenance

### Update Dependencies

```bash
# Update Ruby gems
bundle update

# Commit lockfile
git add Gemfile.lock
git commit -m "Update dependencies"
git push
```

### Monitor GitHub Actions

Check workflow status: **Actions** tab → **Update Google Scholar Stats**

### Troubleshooting

See detailed guides:
- [SETUP_AUTO_UPDATE.md](./SETUP_AUTO_UPDATE.md) - Auto-update configuration
- [UPDATE_CITATIONS.md](./UPDATE_CITATIONS.md) - Citation update guide
- [QUICK_START.md](./QUICK_START.md) - Quick setup instructions

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

This homepage is built upon:
- [**Minimal Mistakes**](https://github.com/mmistakes/minimal-mistakes) - Jekyll theme
- [**Academic Pages**](https://github.com/academicpages/academicpages.github.io) - Academic template inspiration
- [**AcadHomepage**](https://github.com/RayeRen/acad-homepage.github.io) - Original template
- [**scholarly**](https://github.com/scholarly-python-package/scholarly) - Google Scholar crawler
- [**Font Awesome**](https://fontawesome.com/) - Icon library
- **Tencent Cloud COS** - CDN service

Special thanks to all open-source contributors! 🌟

---

## 📧 Contact

- **Email:** lagrangelzy@gmail.com
- **Google Scholar:** [r9f4mLMAAAAJ](https://scholar.google.com/citations?user=r9f4mLMAAAAJ)
- **GitHub:** [@Lagrangeli](https://github.com/Lagrangeli)
- **Homepage:** [https://lagrangeli.github.io/](https://lagrangeli.github.io/)

---

## 📈 Stats

![GitHub last commit](https://img.shields.io/github/last-commit/Lagrangeli/Lagrangeli.github.io)
![GitHub repo size](https://img.shields.io/github/repo-size/Lagrangeli/Lagrangeli.github.io)
![GitHub language count](https://img.shields.io/github/languages/count/Lagrangeli/Lagrangeli.github.io)

---

<div align="center">

**⭐ If you find this homepage template useful, please consider giving it a star!**

Made with ❤️ by Zhenyang Li

</div>
