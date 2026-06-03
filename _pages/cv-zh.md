---
permalink: /cv-zh/
title: "李镇洋 - 个人简历"
author_profile: false
---

<style>
  .cv-viewer__bar {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem 1rem;
    justify-content: space-between;
    margin: 0 0 1rem;
  }

  .cv-viewer__title {
    font-size: 1.35rem;
    font-weight: 700;
    margin: 0;
  }

  .cv-viewer__actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .cv-viewer__actions a {
    font-size: 0.95rem;
  }

  .cv-viewer__pages {
    background: #f3f5f8;
    border: 1px solid #d8dee8;
    border-radius: 4px;
    padding: 1rem;
  }

  .cv-viewer__page {
    background: #fff;
    box-shadow: 0 2px 10px rgba(30, 41, 59, 0.16);
    display: block;
    height: auto;
    margin: 0 auto 1rem;
    max-width: 100%;
  }

  .cv-viewer__status {
    color: #526173;
    font-size: 0.95rem;
    margin: 1rem 0;
  }
</style>

<div class="cv-viewer__bar">
  <h1 class="cv-viewer__title">李镇洋 - 个人简历</h1>
  <div class="cv-viewer__actions">
    <a href="/Zhenyang%20LI%20-%20CV%20-%20phd%20-%20zh.pdf?v={{ site.time | date: '%Y%m%d%H%M' }}" target="_blank" rel="noopener">打开 PDF</a>
  </div>
</div>

<div id="cv-status" class="cv-viewer__status">正在加载简历...</div>
<div id="cv-pages" class="cv-viewer__pages" aria-label="Rendered CV pages"></div>

<script type="module">
  import * as pdfjsLib from "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.10.38/build/pdf.min.mjs";

  pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.10.38/build/pdf.worker.min.mjs";

  const pdfUrl = "/Zhenyang%20LI%20-%20CV%20-%20phd%20-%20zh.pdf?v={{ site.time | date: '%Y%m%d%H%M' }}";
  const pagesEl = document.getElementById("cv-pages");
  const statusEl = document.getElementById("cv-status");

  function pageScale(viewport) {
    const containerWidth = Math.max(320, pagesEl.clientWidth - 32);
    return Math.min(1.65, containerWidth / viewport.width);
  }

  async function renderPdf() {
    const pdf = await pdfjsLib.getDocument(pdfUrl).promise;
    statusEl.textContent = `正在渲染 ${pdf.numPages} 页...`;

    for (let pageNumber = 1; pageNumber <= pdf.numPages; pageNumber += 1) {
      const page = await pdf.getPage(pageNumber);
      const baseViewport = page.getViewport({ scale: 1 });
      const viewport = page.getViewport({ scale: pageScale(baseViewport) });
      const canvas = document.createElement("canvas");
      const context = canvas.getContext("2d");

      canvas.className = "cv-viewer__page";
      canvas.width = Math.floor(viewport.width);
      canvas.height = Math.floor(viewport.height);
      canvas.setAttribute("aria-label", `CV page ${pageNumber}`);
      pagesEl.appendChild(canvas);

      await page.render({ canvasContext: context, viewport }).promise;
    }

    statusEl.textContent = "";
  }

  renderPdf().catch((error) => {
    statusEl.innerHTML = `简历预览加载失败。<a href="${pdfUrl}" target="_blank" rel="noopener">直接打开 PDF</a>。`;
    console.error(error);
  });
</script>
