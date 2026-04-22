from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, HRFlowable


OUTPUT_PATH = "Zhenyang LI - CV - phd - zh.pdf"


CONTACT_LINE = (
    "电话：13910711766　　邮箱：lizy23@connect.hku.hk　　城市：深圳 / 香港　　"
    "微信：lagrangeli　　主页：https://lagrangeli.github.io/　　LinkedIn：linkedin.com/in/zhenyang-li-875a69181"
)

RESEARCH_INTERESTS = (
    "研究方向：3D/4D 场景与物体重建 / 生成，VR/AR/MR，事件视觉，计算成像与全息显示。"
)

EDUCATION = [
    "香港大学，电机与计算机工程（ECE）博士研究生，AI 与 VR/AR/MR 方向，2023.09 - 2027.08",
    "清华大学，大数据工程硕士（计算机视觉方向），GPA 3.79/4.0，排名 6/44，2020.09 - 2023.06",
    "南京理工大学，电子信息工程（通信工程）学士，GPA 3.66/4.0，2016.09 - 2020.06",
]

PUBLICATIONS = [
    "PatternGSL: A Structured Specification Language for Template-Free and Simulation-Ready 3D Garments. SIGGRAPH 2026. 2025.10 - 2026.01. Zhenyang Li*, Lutao Jiang*, Yizhou Zhao, Weikai Chen, Ying-Cong Chen, Xin Wang, Yifan Peng.",
    "E2Pano: Learning Event-to-Panorama Image Reconstruction. 在审. 2025.08 - 2025.11. Zhenyang Li*, Zongqi He*, Xiaoyang Bai, Shijie Lin, Yifan Peng.",
    "Structure-grounded Training Strategies Aid Generalization in Stereo Matching. 3DV 2026. 2025.04 - 2026.08. Liangxun Ou, Yuhui Liu, Zhenyang Li, Xiaoyang Bai, Yifan Peng.",
    "EventTracer: Fast Path Tracing-based Event Stream Rendering. TVCG. 2025.03 - 2025.05. Zhenyang Li*, Xiaoyang Bai*, Jinfan Lu, Pengfei Shen, Yifan Peng.",
    "ORBIT: Overlapping Region-Based Image Feature Matching Technique. 在审. 2025.04. Qi Luo*, Zhenyang Li*, Linsong Xue, Haojie Wu, Yifan Peng, Kai Zhang.",
    "Toward Material-Agnostic System Identification from Videos. ICCV 2025. 2025.03. Yizhou Zhao, Haoyu Chen, Chunjiang Liu, Zhenyang Li, Charles Herrmann, Junhwa Hur, Yinxiao Li, Ming-Hsuan Yang, Bhiksha Raj, Min Xu.",
    "Enhanced Velocity Field Modeling for Gaussian Video Reconstruction. ISMAR 2025. 2025.02. Zhenyang Li*, Xiaoyang Bai*, Tongchen Zhang, Weiwei Xu, Yifan Peng.",
    "Learning Fast Real-world Dynamics with Event-RGB Fused Gaussians. CVMJ. 2025.02. Xiaoyang Bai*, Zhenyang Li*, Weiwei Xu, Edmund Y. Lam, Yifan Peng.",
    "3D-HoloNet: Fast, unfiltered, 3D hologram generation with camera-calibrated network learning. Optics Letters. 2024.12. Wenbin Zhou, Feifan Qu, Xiangyu Meng, Zhenyang Li, Yifan Peng.",
    "CryoSAM: Training-free CryoET Tomogram Segmentation with Foundation Models. MICCAI 2024. 2024.03. Yizhou Zhao, Hengwei Bian, Michael Mu, Mostofa R. Uddin, Zhenyang Li, Xiang Li, Tianyang Wang, Min Xu.",
    "Point Resampling and Ray Transformation Aid to Editable NeRF Models. arXiv. 2023.08 - 2023.11. Zhenyang Li*, Zilong Chen*, Feifan Qu, Mingqing Wang, Yizhou Zhao, Kai Zhang, Yifan Peng.",
    "Alignment-guided Temporal Attention for Video Action Recognition. NeurIPS 2022. 2022.05. Yizhou Zhao*, Zhenyang Li*, Xun Guo, Yan Lu.",
    "Breaking Filter Bubble: A Reinforcement Learning Framework of Controllable Recommender System. WWW 2023. 2022.08 - 2022.10. Zhenyang Li*, Yancheng Dong*, Chen Gao, Yizhou Zhao, Dong Li, Jianye Hao, Kai Zhang, Yong Li, Zhi Wang.",
    "Adaptive Range guided Multi-view Depth Estimation with Normal Ranking Loss. ACCV 2022. 2022.02. Yikang Ding*, Zhenyang Li*, Dihe Huang, Zhiheng Li, Kai Zhang, Wensen Feng.",
    "Enhancing Multi-view Stereo with Contrastive Matching and Weighted Focal Loss. ICIP 2022. 2022.06. Yikang Ding*, Zhenyang Li*, Dihe Huang*, Zhiheng Li, Kai Zhang.",
    "Unsupervised Anomaly Detection with Aggregated VQVAE. ICIP 2023. 2022.06. Mingqing Wang, Jiawei Li, Zhenyang Li, Chengxiao Luo, Bin Chen, Shu-Tao Xia, Zhi Wang.",
]

PATENTS = [
    "A method of maximizing safe rate power allocation for wireless networks based on direction modulation. 授权发明专利 CN110635832A. 2019.04. Zhenyang Li, Yumeng Zhang, Jiayu Li, Feng Shu, Haochen Li, Tianyun Wang, Yu Wang, Yuefeng Huang, Linqing Gui, Yuwen Qian.",
]

EXPERIENCE = [
    "Tencent LIGHTSPEED，研究实习生，2025.10 - 至今",
    "旷视研究院（Megvii Research），研究实习生，2022.06 - 2023.03",
    "微软亚洲研究院（Microsoft Research Asia, MC Group），研究实习生，2021.11 - 2022.05",
    "华为 CMTI，研究实习生，2021.03 - 2021.08",
]

HONORS = [
    "2023 粤港澳大湾区（黄埔）国际算法算例大赛 Neural Implicit Representation 赛道冠军，2023.12",
    "Beindata 高能粒子碰撞分类挑战赛，第 7 / 256 名，2020.04",
    "美国大学生数学建模竞赛 H 奖，二等奖，2019.03",
    "TE Connectivity Scholarship（1/600），2017.12",
    "北京晟铭创科教育基金会优秀学生奖学金特等奖（1/600），2017.11",
    "全国大学生数学竞赛二等奖，2017.11",
]


def add_section(story, title, items, body_style, bullet_prefix="•"):
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(title, styles["section"]))
    story.append(Spacer(1, 1.5 * mm))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#d8e2f3")))
    story.append(Spacer(1, 2.5 * mm))
    for item in items:
        story.append(Paragraph(f"{bullet_prefix} {item}", body_style))
        story.append(Spacer(1, 1.5 * mm))


pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="title_zh",
        fontName="STSong-Light",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#183153"),
        spaceAfter=4 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="subtitle_zh",
        fontName="STSong-Light",
        fontSize=10.5,
        leading=15,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#4b5d79"),
    )
)
styles.add(
    ParagraphStyle(
        name="section",
        fontName="STSong-Light",
        fontSize=12.5,
        leading=16,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#0f4c9a"),
        spaceAfter=1 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="body_zh",
        fontName="STSong-Light",
        fontSize=9.6,
        leading=14.2,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#23364d"),
    )
)

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    leftMargin=16 * mm,
    rightMargin=16 * mm,
    topMargin=14 * mm,
    bottomMargin=12 * mm,
)

story = [
    Paragraph("李镇洋", styles["title_zh"]),
    Paragraph(CONTACT_LINE, styles["subtitle_zh"]),
    Spacer(1, 2 * mm),
    Paragraph(RESEARCH_INTERESTS, styles["subtitle_zh"]),
]

add_section(story, "教育背景", EDUCATION, styles["body_zh"])
add_section(story, "论文发表", PUBLICATIONS, styles["body_zh"])
add_section(story, "专利", PATENTS, styles["body_zh"])
add_section(story, "科研 / 工作经历", EXPERIENCE, styles["body_zh"])
add_section(story, "荣誉奖励", HONORS, styles["body_zh"])

doc.build(story)
print(f"Generated {OUTPUT_PATH}")
