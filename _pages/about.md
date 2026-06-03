---
permalink: /
title: "Zhenyang Li's Academic Homepage"
excerpt: "Ph.D. Student in Computer Vision and Graphics"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<div hidden data-page-title-en="Zhenyang Li's Academic Homepage" data-page-title-zh="李镇洋学术主页"></div>

<div class="lang-switcher" data-lang-switcher aria-label="Language switcher">
  <span class="lang-switcher__label">
    <span class="lang-en lang-inline">Language</span>
    <span class="lang-zh lang-inline">语言</span>
  </span>
  <div class="lang-switcher__buttons">
    <button class="lang-switcher__button is-active" type="button" data-set-lang="en" aria-pressed="true">EN</button>
    <button class="lang-switcher__button" type="button" data-set-lang="zh" aria-pressed="false">中文</button>
  </div>
</div>

<div class="lang-en lang-block" markdown="1">
I am currently a Ph.D. student (since Fall 2023) in the [Department of Electrical and Computer Engineering (ECE, formerly EEE)](https://ece.hku.hk/) at [The University of Hong Kong (HKU)](https://www.hku.hk/)<img src="images/hku-32x32.png" style="width: 1em;">.

Prior to joining HKU, I received my M.S. degree in Big Data Engineering from the Department of Automation and Shenzhen International Graduate School at [Tsinghua University (THU)](https://www.tsinghua.edu.cn/)<img src="images/tsinghua-32x32.png" style="width: 1em;">, and my B.S. degree in Electronic and Information Engineering from [Nanjing University of Science and Technology (NJUST)](https://eoe.njust.edu.cn/)<img src="images/njust-32x32.png" style="width: 1em;">.

I am fortunate to be under the guidance of [Dr. Yifan (Evan) Peng](https://www.eee.hku.hk/~evanpeng/#opennewwindow) from the WeLightLab@HKU in the ECE (formerly EEE) & CS department at HKU and advised by [Prof. Kai Zhang](https://www.sigs.tsinghua.edu.cn/zk_en/main.htm) from the Intelligent Transportation Joint Laboratory at Tsinghua University.

My research interests encompass Computer Vision (3D/4D), Computer Graphics (Rendering), VR/AR/MR, and Holographic Imaging/Display.

**📊 Research Impact:** <a href='https://scholar.google.com/citations?user=r9f4mLMAAAAJ' class="scholar-stat-badge" target="_blank" rel="noopener"><span class="scholar-stat-badge__segment scholar-stat-badge__segment--label"><i class="ai ai-google-scholar" aria-hidden="true"></i><span>Citations</span></span><span class="scholar-stat-badge__segment scholar-stat-badge__segment--value" data-total-cit>{{ site.data.scholar.citedby | default: "..." }}</span></a>

**📄 Curriculum Vitae:** <a href="/assets/pdf/Zhenyang_Li_CV_20260603_fast.pdf" target="_blank" rel="noopener">Open English PDF</a>  
The CV language follows the current homepage language.
</div>

<div class="lang-zh lang-block" markdown="1">
我目前是[香港大学（HKU）](https://www.hku.hk/)<img src="images/hku-32x32.png" style="width: 1em;">[电机与计算机工程系（ECE，原 EEE）](https://ece.hku.hk/)博士研究生，于 2023 年秋季入学。

在加入港大之前，我于[清华大学（THU）](https://www.tsinghua.edu.cn/)<img src="images/tsinghua-32x32.png" style="width: 1em;">自动化系与深圳国际研究生院获得大数据工程硕士学位，并于[南京理工大学（NJUST）](https://eoe.njust.edu.cn/)<img src="images/njust-32x32.png" style="width: 1em;">获得电子信息工程学士学位。

目前我在港大 ECE（原 EEE）与计算机科学相关团队的 WeLightLab@HKU，师从[Yifan（Evan）Peng 博士](https://www.eee.hku.hk/~evanpeng/#opennewwindow)，同时也接受清华大学智能交通联合实验室[Kai Zhang 教授](https://www.sigs.tsinghua.edu.cn/zk_en/main.htm)的指导。

我的研究兴趣包括计算机视觉（3D/4D）、计算机图形学（渲染）、VR/AR/MR，以及计算成像与全息显示。

**📊 学术影响力：** <a href='https://scholar.google.com/citations?user=r9f4mLMAAAAJ' class="scholar-stat-badge" target="_blank" rel="noopener"><span class="scholar-stat-badge__segment scholar-stat-badge__segment--label"><i class="ai ai-google-scholar" aria-hidden="true"></i><span>Citations</span></span><span class="scholar-stat-badge__segment scholar-stat-badge__segment--value" data-total-cit>{{ site.data.scholar.citedby | default: "..." }}</span></a>

**📄 个人简历：** <a href="/assets/pdf/Zhenyang_Li_CV_ZH_20260603_fast.pdf" target="_blank" rel="noopener">打开中文 PDF</a>  
简历语言与当前主页语言一致。
</div>

<!-- <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 25px; margin: 25px 0; color: white; box-shadow: 0 8px 16px rgba(102, 126, 234, 0.2);">
  <h3 style="color: white; margin-top: 0; text-align: center; font-size: 1.5em;">🎯 Research at a Glance</h3>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; text-align: center; margin-top: 20px;">
    <div>
      <div style="font-size: 2.5em; font-weight: bold; margin-bottom: 5px;">13+</div>
      <div style="opacity: 0.95; font-size: 1.1em;">Publications</div>
    </div>
    <div>
      <div style="font-size: 2.5em; font-weight: bold; margin-bottom: 5px;">89</div>
      <div style="opacity: 0.95; font-size: 1.1em;">Citations</div>
    </div>
    <div>
      <div style="font-size: 2.5em; font-weight: bold; margin-bottom: 5px;">5</div>
      <div style="opacity: 0.95; font-size: 1.1em;">H-index</div>
    </div>
    <div>
      <div style="font-size: 2.5em; font-weight: bold; margin-bottom: 5px;">12+</div>
      <div style="opacity: 0.95; font-size: 1.1em;">Conferences Reviewed</div>
    </div>
  </div>
</div> -->

## <span class="lang-en lang-inline">🔬 Research Focus</span><span class="lang-zh lang-inline">🔬 研究方向</span>

<div class="lang-en lang-block" markdown="1">
My research sits at the intersection of **Computer Vision**, **Computer Graphics**, and **Artificial Intelligence**. I focus on reconstructing, rendering, and reasoning about dynamic 3D/4D visual worlds, with an emphasis on physically grounded and multimodal systems.
</div>

<div class="lang-zh lang-block" markdown="1">
我的研究位于**计算机视觉**、**计算机图形学**与**人工智能**的交叉领域，关注动态 3D/4D 视觉世界的重建、渲染与理解，尤其强调物理一致性与多模态智能系统。
</div>

<div class="lang-en lang-block" style="margin: 25px 0;">
  <div style="border-left: 4px solid #667eea; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #f8f9ff, #ffffff);">
    <h3 style="margin-top: 0; color: #667eea;">🎨 3D/4D Scene Reconstruction & Rendering</h3>
    <ul style="margin-bottom: 0;">
      <li><strong>Neural scene representations:</strong> NeRF and 3D Gaussian Splatting for high-fidelity geometry, appearance, and view synthesis</li>
      <li><strong>Dynamic reconstruction:</strong> 4D scene modeling from videos and event streams, including fast motion and velocity-field estimation</li>
      <li><strong>Geometric perception:</strong> Multi-view stereo, depth estimation, visual odometry, and robust feature correspondence</li>
    </ul>
  </div>

  <div style="border-left: 4px solid #e91e63; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #fff5f8, #ffffff);">
    <h3 style="margin-top: 0; color: #e91e63;">🧩 Physics-aware & Generative Visual Modeling</h3>
    <ul style="margin-bottom: 0;">
      <li><strong>Physical reasoning:</strong> Inferring material and system properties from visual observations</li>
      <li><strong>Controllable generation:</strong> Producing physically plausible visual content for videos, garments, and simulated scenes</li>
      <li><strong>Rendering foundations:</strong> Path tracing, event-camera rendering, and realistic appearance modeling</li>
    </ul>
  </div>

  <div style="border-left: 4px solid #764ba2; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #fcf8ff, #ffffff);">
    <h3 style="margin-top: 0; color: #764ba2;">🤖 Multimodal & Embodied Visual Intelligence</h3>
    <ul style="margin-bottom: 0;">
      <li><strong>Vision-language-action models:</strong> Connecting visual perception with language, planning, and action</li>
      <li><strong>Embodied navigation:</strong> Zero-shot object navigation and semantic executive control for interactive agents</li>
      <li><strong>Computational imaging:</strong> Holographic display and camera-calibrated neural imaging systems</li>
    </ul>
  </div>
</div>

<div class="lang-zh lang-block" style="margin: 25px 0;">
  <div style="border-left: 4px solid #667eea; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #f8f9ff, #ffffff);">
    <h3 style="margin-top: 0; color: #667eea;">🎨 3D/4D 场景重建与渲染</h3>
    <ul style="margin-bottom: 0;">
      <li><strong>神经场景表示：</strong>研究 NeRF 与 3D Gaussian Splatting 等方法，用于高保真几何、外观与新视角合成</li>
      <li><strong>动态场景重建：</strong>从视频与事件流中重建 4D 场景，建模快速运动与速度场</li>
      <li><strong>几何感知：</strong>多视图立体、深度估计、视觉里程计与稳健图像对应</li>
    </ul>
  </div>

  <div style="border-left: 4px solid #e91e63; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #fff5f8, #ffffff);">
    <h3 style="margin-top: 0; color: #e91e63;">🧩 物理感知与生成式视觉建模</h3>
    <ul style="margin-bottom: 0;">
      <li><strong>物理推理：</strong>从视觉观测中推断材料属性与物理系统参数</li>
      <li><strong>可控生成：</strong>生成符合物理规律的视频、服装与仿真场景内容</li>
      <li><strong>真实感渲染：</strong>路径追踪、事件相机渲染与真实外观建模</li>
    </ul>
  </div>

  <div style="border-left: 4px solid #764ba2; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #fcf8ff, #ffffff);">
    <h3 style="margin-top: 0; color: #764ba2;">🤖 多模态与具身视觉智能</h3>
    <ul style="margin-bottom: 0;">
      <li><strong>视觉-语言-动作模型：</strong>连接视觉感知、语言理解、规划与动作执行</li>
      <li><strong>具身导航：</strong>面向交互式智能体的零样本目标导航与语义执行控制</li>
      <li><strong>计算成像：</strong>全息显示与基于相机标定的神经成像系统</li>
    </ul>
  </div>
</div>

---

<span class='anchor' id='-news'></span>

# <span class="lang-en lang-inline">🔥 News</span><span class="lang-zh lang-inline">🔥 新闻动态</span>

<div class="lang-en lang-block" markdown="1">
- *2026.06*: &nbsp;🏆 One paper on **Fast Motion Reconstruction** (**ERF-GS**) is accepted to <a href="https://cg.cs.tsinghua.edu.cn/cvmj/" target="_blank" rel="noopener"><strong>Computational Visual Media (CVMJ)</strong></a>!
- *2026.05*: &nbsp;🏆 One paper on **Event Camera Rendering** (**EventTracer**) is accepted to <a href="https://www.computer.org/csdl/journal/tg" target="_blank" rel="noopener"><strong>IEEE Transactions on Visualization and Computer Graphics (TVCG)</strong></a>!
- *2026.04*: &nbsp;🏆 One paper on **3D Garment Modeling** (<a href="https://lagrangeli.github.io/PatternGSL/" target="_blank" rel="noopener"><strong>PatternGSL</strong></a>) is accepted to **SIGGRAPH 2026**!
- *2026.05*: &nbsp;📄 One paper on **Zero-Shot Object Navigation** (**ConsistNav**) is released on **arXiv**! Closing the action consistency gap with semantic executive control.
- *2026.04*: &nbsp;📄 One paper on **AR-assisted dental implant surgery** is published in **Journal of the Society for Information Display (JSID) 2026**!
- *2026.03*: &nbsp;📄 One paper on **Panoramic Instance Segmentation** (SAP) is released on **arXiv**! Segment Any 4K Panorama for high-resolution 360° scenes.
- *2026.03*: &nbsp;🏆 One paper on **Stereo Matching Generalization** is accepted to **3DV 2026**! Structure-grounded training strategies for robust stereo matching.
- *2026.03*: &nbsp;🎓 Serving as **Program Committee Member** for **34th ACM Multimedia (ACMMM) 2026**!
- *2025.07*: &nbsp;🏆 One paper on **4D Gaussian Splatting** is accepted to **ISMAR 2025**! This work focuses on enhanced velocity field modeling for video reconstruction.
- *2025.07*: &nbsp;🏆 One paper on **Physically Correct Video Generation** is accepted to **ICCV 2025**! Material-agnostic system identification from videos.
</div>

<div class="lang-zh lang-block" markdown="1">
- *2026.06*: &nbsp;🏆 一篇关于**快速运动重建**的论文（**ERF-GS**）被 <a href="https://cg.cs.tsinghua.edu.cn/cvmj/" target="_blank" rel="noopener"><strong>Computational Visual Media (CVMJ)</strong></a> 接收！
- *2026.05*: &nbsp;🏆 一篇关于**事件相机渲染**的论文（**EventTracer**）被 <a href="https://www.computer.org/csdl/journal/tg" target="_blank" rel="noopener"><strong>IEEE Transactions on Visualization and Computer Graphics (TVCG)</strong></a> 接收！
- *2026.04*: &nbsp;🏆 一篇关于**三维服装建模**的论文（<a href="https://lagrangeli.github.io/PatternGSL/" target="_blank" rel="noopener"><strong>PatternGSL</strong></a>）被 **SIGGRAPH 2026** 接收！
- *2026.05*: &nbsp;📄 一篇关于**零样本目标导航**的论文（**ConsistNav**）已发布于 **arXiv**！聚焦通过语义执行控制弥合动作一致性鸿沟。
- *2026.04*: &nbsp;📄 一篇关于**增强现实辅助牙种植导航**的论文发表于 **Journal of the Society for Information Display (JSID) 2026**！
- *2026.03*: &nbsp;📄 **全景实例分割**论文 **SAP** 已发布于 **arXiv**！工作聚焦高分辨率 360° 场景的 `Segment Any 4K Panorama`。
- *2026.03*: &nbsp;🏆 一篇关于**立体匹配泛化**的论文被 **3DV 2026** 接收！提出面向稳健立体匹配的结构先验训练策略。
- *2026.03*: &nbsp;🎓 担任 **第 34 届 ACM Multimedia（ACMMM）2026** 程序委员会成员！
- *2025.07*: &nbsp;🏆 一篇关于 **4D Gaussian Splatting** 的论文被 **ISMAR 2025** 接收！该工作聚焦视频重建中的增强速度场建模。
- *2025.07*: &nbsp;🏆 一篇关于**物理正确视频生成**的论文被 **ICCV 2025** 接收！研究从视频中进行材料无关系统辨识。
</div>

<span class='anchor' id='-publications'></span>

# <span class="lang-en lang-inline">📝 Publications</span><span class="lang-zh lang-inline">📝 论文发表</span>

## <span class="lang-en lang-inline">🎯 Selected Publications (* indicates equal contribution)</span><span class="lang-zh lang-inline">🎯 代表性论文（* 表示共同一作）</span>

### 2026
- <img alt="arXiv" src="https://img.shields.io/badge/arXiv-2026-b31b1b"> [**ConsistNav: Closing the Action Consistency Gap in Zero-Shot Object Navigation with Semantic Executive Control**](https://arxiv.org/abs/2605.09869)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.ap-guangzhou.myqcloud.com/publications/consisnav.png" alt="ConsistNav teaser" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Haosen Wang\*, **Zhenyang Li\***, Yinqiang Zhang, Zongqi He, Lutao Jiang, Kai Li, Yizhou Zhao, Liaoyuan Fan, Wenjian Hou, Tingbang Liang, Yibin Wen, Defeng Gu.

- <img alt="JSID" src="https://img.shields.io/badge/JSID-2026-blue"> [**Augmented Reality Integration Improves Ergonomics in Dynamic Navigation for Dental Implant Surgery**](https://sid.onlinelibrary.wiley.com/doi/pdf/10.1002/jsid.70061)  
  Pui Hang Leung, Feng Wang, **Zhenyang Li**, Zongqi He, Yifan Peng, Wei-fa Yang.

- <img alt="SIGGRAPH" src="https://img.shields.io/badge/SIGGRAPH-2026-red"> <a href="https://lagrangeli.github.io/PatternGSL/" target="_blank" rel="noopener"><strong>PatternGSL: A Structured Specification Language for Template-Free and Simulation-Ready 3D Garments</strong></a>
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.ap-guangzhou.myqcloud.com/publications/garment_teaser.png" alt="PatternGSL teaser" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  **Zhenyang Li\***, Lutao Jiang*, Yizhou Zhao, Weikai Chen, Ying-Cong Chen, Xin Wang, Yifan Peng.

- <img alt="arXiv" src="https://img.shields.io/badge/arXiv-2026-b31b1b"> [**SAP: Segment Any 4K Panorama**](https://arxiv.org/abs/2603.12759)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.ap-guangzhou.myqcloud.com/publications/sap-teaser.jpg" alt="SAP teaser" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Lutao Jiang, Zidong Cao, Weikai Chen, Xu Zheng, Yuanhuiyi Lyu, **Zhenyang Li**, Zeyu Hu, Yingda Yin, Keyang Luo, Runze Zhang, Kai Yan, Shengju Qian, Haidi Fan, Yifan Peng, Xin Wang, Hui Xiong, Ying-Cong Chen.

- <img alt="3DV" src="https://img.shields.io/badge/3DV-2026-blue"> [**Structure-grounded Training Strategies Aid Generalization in Stereo Matching**](https://openreview.net/forum?id=rIeputhlON)  
  <div style="text-align: center; margin: 10px 0;">
    <div style="display: inline-flex; gap: 8px; width: 90%; max-width: 700px; align-items: center;">
      <div style="flex: 3; min-width: 0; display: flex; flex-direction: column; gap: 8px;">
        <img src="https://homepage-1301698759.cos.ap-guangzhou.myqcloud.com/publications/3dv-aux_task.png" alt="Auxiliary Task" style="width: 100%; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
        <img src="https://homepage-1301698759.cos.ap-guangzhou.myqcloud.com/publications/3dv-pipeline.png" alt="Pipeline" style="width: 100%; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
      </div>
      <div style="flex: 2; min-width: 0;">
        <img src="https://homepage-1301698759.cos.ap-guangzhou.myqcloud.com/publications/3dv-geom_aug_1.png" alt="Geometric Augmentation" style="width: 100%; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
      </div>
    </div>
  </div>
  Liangxun Ou, Yuhui Liu, **Zhenyang Li**, Xiaoyang Bai, Yifan Peng.

- <img alt="TVCG" src="https://img.shields.io/badge/TVCG-2026-blue"> [**EventTracer: Fast Path Tracing-based Event Stream Rendering**](https://arxiv.org/abs/2508.18071)<br>
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/eventtracer.jpg" alt="EventTracer" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  **Zhenyang Li\***, Xiaoyang Bai*, Jinfan Lu, Pengfei Shen, Yifan Peng.<br>
  Accepted to <a href="https://www.computer.org/csdl/journal/tg" target="_blank" rel="noopener"><strong>IEEE Transactions on Visualization and Computer Graphics (TVCG)</strong></a>.

- <img alt="CVMJ" src="https://img.shields.io/badge/CVMJ-2026-blue"> **ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints**<br>
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/event-rgb-gaussians.jpg" alt="ERF-GS" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Xiaoyang Bai*, **Zhenyang Li\***, Weiwei Xu, Edmund Y. Lam, Yifan Peng.<br>
  Accepted to <a href="https://cg.cs.tsinghua.edu.cn/cvmj/" target="_blank" rel="noopener"><strong>Computational Visual Media (CVMJ)</strong></a>.

### 2025
- <img alt="ICCV" src="https://img.shields.io/badge/ICCV-2025-blue"> [**Toward Material-Agnostic System Identification from Videos**](https://arxiv.org/pdf/2508.01112?)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/material-agnostic.jpg" alt="Material-Agnostic System Identification" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Yizhou Zhao, Haoyu Chen, Chunjiang Liu, **Zhenyang Li**, Charles Herrmann, Junhwa Hur, Yinxiao Li, Ming-Hsuan Yang, Bhiksha Raj, Min Xu.

- <img alt="ISMAR" src="https://img.shields.io/badge/ISMAR-2025-orange"> [**Enhanced Velocity Field Modeling for Gaussian Video Reconstruction**](https://arxiv.org/abs/2507.23704)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/velocity-field-4dgs.jpg" alt="Enhanced Velocity Field Modeling" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  **Zhenyang Li\***, Xiaoyang Bai*, Tongchen Zhang, Pengfei Shen, Weiwei Xu, Yifan Peng.

- <img alt="Under Review" src="https://img.shields.io/badge/Status-Under_Review-yellow"> **ORBIT: Overlapping Region-Based Image Feature Matching Technique** *(Preprint Coming Soon)*  
  <!-- <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/orbit.png" alt="ORBIT Feature Matching" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div> -->
  Qi Luo*, **Zhenyang Li\***, Linsong Xue, Haojie Wu, Yifan Peng, Kai Zhang.



### 2024
- <img alt="Optics Letters" src="https://img.shields.io/badge/Optics_Letters-2024-green"> [**3D-HoloNet: Fast, unfiltered, 3D hologram generation with camera-calibrated network learning**](https://opg.optica.org/ol/abstract.cfm?uri=ol-50-4-1188)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/3d-holonet.png" alt="3D-HoloNet" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Wenbin Zhou, Feifan Qu, Xiangyu Meng, **Zhenyang Li**, Yifan Peng

- <img alt="MICCAI" src="https://img.shields.io/badge/MICCAI-2024-red"> [**CryoSAM: Training-free CryoET Tomogram Segmentation with Foundation Models**](https://www.arxiv.org/abs/2407.06833)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/cryosam.png" alt="CryoSAM" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Yizhou Zhao, Hengwei Bian, Michael Mu, Mostofa R. Uddin, **Zhenyang Li**, Xiang Li, Tianyang Wang, Min Xu.

- <img alt="arXiv" src="https://img.shields.io/badge/arXiv-2024-b31b1b"> [**Point Resampling and Ray Transformation Aid to Editable NeRF Models**](https://arxiv.org/abs/2405.07306)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/editable-nerf.jpg" 
    alt="Editable NeRF Models" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  **Zhenyang Li\***, Zilong Chen*, Feifan Qu, Mingqing Wang, Yizhou Zhao, Kai Zhang, Yifan Peng.

### 2023
- <img alt="WWW" src="https://img.shields.io/badge/WWW-2023-purple"> [**Breaking Filter Bubble: A Reinforcement Learning Framework of Controllable Recommender System**](https://dl.acm.org/doi/pdf/10.1145/3543507.3583856)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/filter-bubble.jpg" alt="Breaking Filter Bubble" style="width: 60%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  **Zhenyang Li\***, Yancheng Dong*, Chen Gao, Yizhou Zhao, Dong Li, Jianye Hao, Kai Zhang, Yong Li, Zhi Wang.

- <img alt="ICIP" src="https://img.shields.io/badge/ICIP-2023-lightblue"> [**Unsupervised Anomaly Detection with Local-Sensitive VQVAE and Global-Sensitive Transformers**](https://arxiv.org/pdf/2303.17505)  
  <!-- <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/anomaly-detection.png" alt="Anomaly Detection" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div> -->
  Mingqing Wang, Jiawei Li, **Zhenyang Li**, Chengxiao Luo, Bin Chen, Shu-Tao Xia, Zhi Wang.

### 2022
- <img alt="NeurIPS" src="https://img.shields.io/badge/NeurIPS-2022-blue"> [**Alignment-guided Temporal Attention for Video Action Recognition**](https://proceedings.neurips.cc/paper_files/paper/2022/file/5820ad65b1c27411417ae8b59433e580-Paper-Conference.pdf)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/temporal-attention.png" alt="Alignment-guided Temporal Attention" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Yizhou Zhao*, **Zhenyang Li\***, Xun Guo, Yan Lu.

- <img alt="ACCV" src="https://img.shields.io/badge/ACCV-2022-orange"> [**Adaptive Range guided Multi-view Depth Estimation with Normal Ranking Loss**](https://openaccess.thecvf.com/content/ACCV2022/papers/Ding_Adaptive_Range_guided_Multi-view_Depth_Estimation_with_Normal_Ranking_Loss_ACCV_2022_paper.pdf)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/depth-estimation.png" alt="Multi-view Depth Estimation" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Yikang Ding*, **Zhenyang Li\***, Dihe Huang, Kai Zhang, Zhiheng Li, Wensen Feng.

- <img alt="ICIP" src="https://img.shields.io/badge/ICIP-2022-lightblue"> [**Enhancing multi-view stereo with contrastive matching and weighted focal loss**](https://arxiv.org/pdf/2206.10360)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/mvs-contrastive.jpg" alt="Multi-view Stereo" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Yikang Ding*, **Zhenyang Li\***, Dihe Huang, Zhiheng Li, Kai Zhang.

<span class='anchor' id='-honors-and-awards'></span>

# <span class="lang-en lang-inline">🎖 Honors and Awards</span><span class="lang-zh lang-inline">🎖 荣誉与奖励</span>

<div class="lang-en lang-block" markdown="1">
### 🏆 Competitions
- *2023.12* **Champion** 🥇, Guangdong-Hong Kong-Macao Greater Bay Area (Huangpu) International Algorithm Case Competition  
  *Topic: Three-dimensional reconstruction of objects using neural implicit representation*
  
- *2020.04* **Top 7/256** 🥈, High-energy particle collision classification challenge, Beindata

- *2019.05* **Second Prize** 🥉, American College Student Mathematical Modeling Contest (MCM)

### 💰 Scholarships & Academic Honors
- *2017* **TE Connectivity Scholarship** (Top 1/600), **Beijing SMC Education Foundation Outstanding Scholarship Special Award** (Top 1/600), **Second Prize** in National Mathematics Competition for College Students
</div>

<div class="lang-zh lang-block" markdown="1">
### 🏆 竞赛获奖
- *2023.12* **冠军** 🥇，粤港澳大湾区（黄埔）国际算法算例大赛  
  *赛题：基于神经隐式表示的物体三维重建*
  
- *2020.04* **前 7 / 256** 🥈，高能粒子碰撞分类挑战赛，Beindata

- *2019.05* **二等奖** 🥉，美国大学生数学建模竞赛（MCM）

### 💰 奖学金与学术荣誉
- *2017* **TE Connectivity Scholarship**（Top 1/600）、**北京晟铭创科教育基金会优秀学生奖学金特等奖**（Top 1/600）、**全国大学生数学竞赛二等奖**
</div>

<span class='anchor' id='-educations'></span>

# <span class="lang-en lang-inline">📖 Educations</span><span class="lang-zh lang-inline">📖 教育经历</span>

<div class="lang-en lang-block" markdown="1">
- 🎓 **Ph.D. in Electrical and Computer Engineering (formerly EEE)** | *2023.09 - Present*  
  [The University of Hong Kong (HKU)](https://www.hku.hk/) <img src="images/hku-32x32.png" style="width: 1em;">  
  *Advisor: Dr. Yifan (Evan) Peng*
  
- 🎓 **M.S. in Big Data Engineering** | *2020.09 - 2023.07*  
  [Tsinghua University (THU)](https://www.tsinghua.edu.cn/) <img src="images/tsinghua-32x32.png" style="width: 1em;">  
  *Department of Automation & Shenzhen International Graduate School*  
  *Advisor: Prof. Kai Zhang*
  
- 🎓 **B.S. in Electronic and Information Engineering** | *2016.09 - 2020.07*  
  [Nanjing University of Science and Technology (NJUST)](https://eoe.njust.edu.cn/) <img src="images/njust-32x32.png" style="width: 1em;">  
  *School of Electronic and Optical Engineering*
</div>

<div class="lang-zh lang-block" markdown="1">
- 🎓 **电机与电子工程博士（原 EEE）** | *2023.09 - 至今*  
  [香港大学（HKU）](https://www.hku.hk/) <img src="images/hku-32x32.png" style="width: 1em;">  
  *导师：Yifan（Evan）Peng 博士*
  
- 🎓 **大数据工程硕士** | *2020.09 - 2023.07*  
  [清华大学（THU）](https://www.tsinghua.edu.cn/) <img src="images/tsinghua-32x32.png" style="width: 1em;">  
  *自动化系、深圳国际研究生院*  
  *导师：Kai Zhang 教授*
  
- 🎓 **电子信息工程学士** | *2016.09 - 2020.07*  
  [南京理工大学（NJUST）](https://eoe.njust.edu.cn/) <img src="images/njust-32x32.png" style="width: 1em;">  
  *电子与光学工程学院*
</div>

<span class='anchor' id='-internships'></span>

# <span class="lang-en lang-inline">💻 Internships</span><span class="lang-zh lang-inline">💻 实习经历</span>

<div class="lang-en lang-block" markdown="1">
- 🏢 **Research Intern** | *Oct. 2025 - Present*  
  [**Tencent LIGHTSPEED STUDIOS**](https://www.lightspeed-studios.com/), Shenzhen, Guangdong, China  
  *Research Focus: Multimodal & 3D Content Generation and Simulation*

- 🏢 **Research Intern** | *Jul. 2022 - Nov. 2022*  
  [**Megvii Technology Limited (Face++)**](https://www.megvii.com/), Beijing, China  
  *Research Focus: Visual Odometry, NeRF, Multi-View Stereo (MVS), Feature Matching*
  
- 🏢 **Research Intern** | *Nov. 2021 - May. 2022*  
  [**Microsoft Research Asia (MSRA)**](https://www.microsoft.com/en-us/research/lab/microsoft-research-asia/), Beijing, China  
  *Research Focus: Video Understanding, Learning-based Computer Vision*
  
- 🏢 **Artificial Intelligence Researcher** | *Mar. 2021 - Sep. 2021*  
  [**Huawei Technologies Co., Ltd.**](https://www.huawei.com/), Shenzhen, Guangdong, China  
  *Research Focus: 3D Reconstruction, Visual Localization*
</div>

<div class="lang-zh lang-block" markdown="1">
- 🏢 **研究实习生** | *2025.10 - 至今*  
  [**Tencent LIGHTSPEED STUDIOS**](https://www.lightspeed-studios.com/)，中国广东深圳  
  *研究方向：多模态与 3D 内容生成及仿真*

- 🏢 **研究实习生** | *2022.07 - 2022.11*  
  [**Megvii Technology Limited (Face++)**](https://www.megvii.com/)，中国北京  
  *研究方向：视觉里程计、NeRF、多视图立体（MVS）、特征匹配*
  
- 🏢 **研究实习生** | *2021.11 - 2022.05*  
  [**Microsoft Research Asia (MSRA)**](https://www.microsoft.com/en-us/research/lab/microsoft-research-asia/)，中国北京  
  *研究方向：视频理解、学习式计算机视觉*
  
- 🏢 **人工智能研究员** | *2021.03 - 2021.09*  
  [**Huawei Technologies Co., Ltd.**](https://www.huawei.com/)，中国广东深圳  
  *研究方向：三维重建、视觉定位*
</div>

<span class='anchor' id='-academic-services'></span>

# <span class="lang-en lang-inline">🧑‍⚖️ Academic Services</span><span class="lang-zh lang-inline">🧑‍⚖️ 学术服务</span>

<div class="lang-en lang-block" markdown="1">
## Program Committee Member

- 34th ACM Multimedia (ACMMM) 2026

## Conference Reviewer

### 2026
- CVPR 2026, ECCV 2026, NeurIPS 2026, BMVC 2026, 3DV 2026, ISMAR 2026

### 2025
- SIGGRAPH Asia 2025 (XR Track), ICCV 2025, ISMAR 2025
- NeurIPS 2025 (Main + Datasets and Benchmarks), ICML 2025, ICLR 2025
- ACM MM 2025, AISTATS 2025, ACML 2025, 3DV 2025

### 2024
- NeurIPS 2024

## Journal Reviewer

- IEEE Journal of Selected Topics in Signal Processing (J-STSP)
</div>

<div class="lang-zh lang-block" markdown="1">
## 程序委员会成员

- 第 34 届 ACM Multimedia（ACMMM）2026

## 会议审稿

### 2026
- CVPR 2026、ECCV 2026、NeurIPS 2026、BMVC 2026、3DV 2026、ISMAR 2026

### 2025
- SIGGRAPH Asia 2025（XR Track）、ICCV 2025、ISMAR 2025
- NeurIPS 2025（Main + Datasets and Benchmarks）、ICML 2025、ICLR 2025
- ACM MM 2025、AISTATS 2025、ACML 2025、3DV 2025

### 2024
- NeurIPS 2024

## 期刊审稿

- IEEE Journal of Selected Topics in Signal Processing（J-STSP）
</div>

<span class='anchor' id='-invited-talks'></span>

# <span class="lang-en lang-inline">💬 Invited Talks & Teaching</span><span class="lang-zh lang-inline">💬 报告与教学</span>

<div class="lang-en lang-block" markdown="1">
- 🎤 **Workshop Organizer & Speaker** | *Dec. 2025*  
  [**WeLight Workshop**](https://hku.welight.fun/events/workshop_25Dec/), The University of Hong Kong  
  *Organized by WeLightLab@HKU*

- 🎤 **Guest Lecturer** | *May 2023*  
  **ELEC4544: AI and Deep Learning**, The University of Hong Kong  
  *Invited by Dr. Yifan (Evan) Peng*
</div>

<div class="lang-zh lang-block" markdown="1">
- 🎤 **Workshop 组织者与报告人** | *2025.12*  
  [**WeLight Workshop**](https://hku.welight.fun/events/workshop_25Dec/)，香港大学  
  *由 WeLightLab@HKU 组织*

- 🎤 **特邀讲师** | *2023.05*  
  **ELEC4544: AI and Deep Learning**，香港大学  
  *由 Yifan（Evan）Peng 博士邀请*
</div>
