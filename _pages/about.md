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

I am currently a Ph.D. student (since Fall 2023) in the Department of Electrical and Electronic Engineering at [The University of Hong Kong (HKU)](https://www.hku.hk/)<img src="images/hku-32x32.png" style="width: 1em;">. 

Prior to joining HKU, I received my M.S. degree in Big Data Engineering from the Department of Automation and Shenzhen International Graduate School at [Tsinghua University (THU)](https://www.tsinghua.edu.cn/)<img src="images/tsinghua-32x32.png" style="width: 1em;">, and my B.S. degree in Electronic and Information Engineering from [Nanjing University of Science and Technology (NJUST)](https://eoe.njust.edu.cn/)<img src="images/njust-32x32.png" style="width: 1em;">.

I am fortunate to be under the guidance of [Dr. Yifan (Evan) Peng](https://www.eee.hku.hk/~evanpeng/#opennewwindow) from the WeLightLab@HKU in the EEE&CS department at HKU and advised by [Prof. Kai Zhang](https://www.sigs.tsinghua.edu.cn/zk_en/main.htm) from the Intelligent Transportation Joint Laboratory at Tsinghua University.

My research interests encompass Computer Vision (3D/4D), Computer Graphics (Rendering), VR/AR/MR, and Holographic Imaging/Display.

**📊 Research Impact:** <a href='https://scholar.google.com/citations?user=r9f4mLMAAAAJ'><img src="https://img.shields.io/badge/Google%20Scholar-90%20citations-4285F4?logo=googlescholar&logoColor=white&style=flat"></a>

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

## 🔬 Research Focus

My research interests lie at the intersection of **Computer Vision**, **Computer Graphics**, and **Artificial Intelligence**. I focus on enabling machines to perceive, understand, and generate photorealistic 3D/4D visual content. Specifically, my work concentrates on the following areas:

<div style="margin: 25px 0;">

<div style="border-left: 4px solid #667eea; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #f8f9ff, #ffffff);">
  <h3 style="margin-top: 0; color: #667eea;">🎨 3D/4D Reconstruction & Generation</h3>
  <ul style="margin-bottom: 0;">
    <li><strong>Neural Representations:</strong> Neural Radiance Fields (NeRF) and 3D Gaussian Splatting for high-fidelity scene modeling</li>
    <li><strong>Dynamic Scenes:</strong> 4D reconstruction with enhanced velocity field modeling for video sequences</li>
    <li><strong>Physics-based Generation:</strong> Material-agnostic system identification and physically correct video synthesis</li>
    <li><strong>Event-based Vision:</strong> Event camera rendering and dynamic scene reconstruction using event streams</li>
  </ul>
</div>

<div style="border-left: 4px solid #e91e63; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #fff5f8, #ffffff);">
  <h3 style="margin-top: 0; color: #e91e63;">🤖 Vision-Language & Multimodal AI</h3>
  <ul style="margin-bottom: 0;">
    <li><strong>Visual-Language-Action Models:</strong> Embodied AI for robotics and interactive systems</li>
    <li><strong>Video Understanding:</strong> Temporal modeling and action recognition in dynamic scenes</li>
    <li><strong>Cross-modal Learning:</strong> Bridging vision, language, and action spaces</li>
  </ul>
</div>

<div style="border-left: 4px solid #764ba2; padding: 15px 20px; margin: 15px 0; background: linear-gradient(to right, #fcf8ff, #ffffff);">
  <h3 style="margin-top: 0; color: #764ba2;">🖼️ Computational Imaging & Holography</h3>
  <ul style="margin-bottom: 0;">
    <li><strong>Holographic Display:</strong> Computer-generated holography with camera-calibrated neural networks</li>
    <li><strong>3D Imaging:</strong> Multi-view stereo, depth estimation, and 3D scene understanding</li>
    <li><strong>Feature Matching:</strong> Overlapping region-based techniques for robust image correspondence</li>
  </ul>
</div>

</div>

---

<span class='anchor' id='-news'></span>

# 🔥 News
- *2025.08*: &nbsp;📄 One paper on **Event Camera Rendering** (EventTracer) is released on arXiv, exploring path tracing-based event stream rendering!
- *2025.07*: &nbsp;🏆 One paper on **4D Gaussian Splatting** is accepted to **ISMAR 2025**! This work focuses on enhanced velocity field modeling for video reconstruction.
- *2025.07*: &nbsp;🏆 One paper on **Physically Correct Video Generation** is accepted to **ICCV 2025**! Material-agnostic system identification from videos.

<span class='anchor' id='-publications'></span>

# 📝 Publications

## 🎯 Selected Publications (* indicates equal contribution)

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

- <img alt="Under Review" src="https://img.shields.io/badge/Status-Under_Review-yellow"> [**EventTracer: Fast Path Tracing-based Event Stream Rendering**](https://arxiv.org/abs/2508.18071)  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/eventtracer.jpg" alt="EventTracer" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  **Zhenyang Li\***, Xiaoyang Bai*, Jinfan Lu, Pengfei Shen, Yifan Peng.

- <img alt="Under Review" src="https://img.shields.io/badge/Status-Under_Review-yellow"> **Learning Fast Real-world Dynamics with Event-RGB Fused Gaussians** *(Preprint Coming Soon)*  
  <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/event-rgb-gaussians.jpg" alt="Event-RGB Fused Gaussians" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div>
  Xiaoyang Bai*, **Zhenyang Li\***, Weiwei Xu, Edmund Y. Lam, Yifan Peng.

- <img alt="Under Review" src="https://img.shields.io/badge/Status-Under_Review-yellow"> **ORBIT: Overlapping Region-Based Image Feature Matching Technique** *(Preprint Coming Soon)*  
  <!-- <div style="text-align: center; margin: 10px 0;">
    <img src="https://homepage-1301698759.cos.accelerate.myqcloud.com/publications/orbit.png" alt="ORBIT Feature Matching" style="width: 90%; max-width: 700px; border-radius: 4px; box-shadow: 0 3px 8px rgba(0,0,0,0.12);">
  </div> -->
  Qi Luo*, **Zhenyang Li\***, Linsong Xue, Haojie Wu, Yifan Peng, Kai Zhang.



### 2024
- <img alt="Optics Letters" src="https://img.shields.io/badge/Optics_Letters-2024-green"> [**3D-HoloNet: Fast, unfiltered, 3D hologram generation with camera-calibrated network learning**](https://opg-optica-org.eproxy.lib.hku.hk/ol/viewmedia.cfm?uri=ol-50-4-1188&html=true)  
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

# 🎖 Honors and Awards

### 🏆 Competitions
- *2023.12* **Champion** 🥇, Guangdong-Hong Kong-Macao Greater Bay Area (Huangpu) International Algorithm Case Competition  
  *Topic: Three-dimensional reconstruction of objects using neural implicit representation*
  
- *2020.04* **Top 7/256** 🥈, High-energy particle collision classification challenge, Beindata

- *2019.05* **Second Prize** 🥉, American College Student Mathematical Modeling Contest (MCM)

### 💰 Scholarships & Academic Honors
- *2017* **TE Connectivity Scholarship** (Top 1/600), **Beijing SMC Education Foundation Outstanding Scholarship Special Award** (Top 1/600), **Second Prize** in National Mathematics Competition for College Students

<span class='anchor' id='-educations'></span>

# 📖 Educations

- 🎓 **Ph.D. in Electrical and Electronic Engineering** | *2023.09 - Present*  
  [The University of Hong Kong (HKU)](https://www.hku.hk/) <img src="images/hku-32x32.png" style="width: 1em;">  
  *Advisor: Dr. Yifan (Evan) Peng*
  
- 🎓 **M.S. in Big Data Engineering** | *2020.09 - 2023.07*  
  [Tsinghua University (THU)](https://www.tsinghua.edu.cn/) <img src="images/tsinghua-32x32.png" style="width: 1em;">  
  *Department of Automation & Shenzhen International Graduate School*  
  *Advisor: Prof. Kai Zhang*
  
- 🎓 **B.S. in Electronic and Information Engineering** | *2016.09 - 2020.07*  
  [Nanjing University of Science and Technology (NJUST)](https://eoe.njust.edu.cn/) <img src="images/njust-32x32.png" style="width: 1em;">  
  *School of Electronic and Optical Engineering*

<span class='anchor' id='-internships'></span>

# 💻 Internships

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

<span class='anchor' id='-academic-services'></span>

# 🧑‍⚖️ Academic Services

## Conference Reviewer

### 2026
- CVPR 2026, 3DV 2026

### 2025
- SIGGRAPH Asia 2025 (XR Track), ICCV 2025, ISMAR 2025
- NeurIPS 2025 (Main + Datasets and Benchmarks), ICML 2025, ICLR 2025
- ACM MM 2025, AISTATS 2025, ACML 2025, 3DV 2025

### 2024
- NeurIPS 2024

<span class='anchor' id='-invited-talks'></span>

# 💬 Invited Talks & Teaching

- 🎤 **Workshop Organizer & Speaker** | *Dec. 2025*  
  [**WeLight Workshop**](https://hku.welight.fun/events/workshop_25Dec/), The University of Hong Kong  
  *Organized by WeLightLab@HKU*

- 🎤 **Guest Lecturer** | *May 2023*  
  **ELEC4544: AI and Deep Learning**, The University of Hong Kong  
  *Invited by Dr. Yifan (Evan) Peng*
