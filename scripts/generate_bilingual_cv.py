import json
from pathlib import Path
import shutil
from datetime import datetime

from reportlab.lib import colors, fonts
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
PHOTO = ROOT / "assets" / "images" / "cv-profile.jpg"
SCHOLAR_DATA = ROOT / "_data" / "scholar.json"
ZH_FONT = Path("/usr/local/texlive/2026/texmf-dist/fonts/truetype/public/lxgw-fonts/LXGWNeoZhiSongScreen.ttf")
SERIF_DIR = Path("/System/Library/Fonts/Supplemental")
SERIF_FONTS = {
    "CVSerif": SERIF_DIR / "Times New Roman.ttf",
    "CVSerif-Bold": SERIF_DIR / "Times New Roman Bold.ttf",
    "CVSerif-Italic": SERIF_DIR / "Times New Roman Italic.ttf",
    "CVSerif-BoldItalic": SERIF_DIR / "Times New Roman Bold Italic.ttf",
}
BLUE = colors.HexColor("#527DB8")
LIGHT_BLUE = colors.HexColor("#DDE7F4")
TEXT = colors.HexColor("#161616")


def scholar_summary():
    data = json.loads(SCHOLAR_DATA.read_text(encoding="utf-8"))
    updated = datetime.fromisoformat(data["updated"]).strftime("%b. %Y")
    return (
        f'{data["citedby"]} citations, h-index {data["hindex"]}, '
        f'i10-index {data["i10index"]} ({updated})'
    )


PUBLICATIONS = [
    {
        "title": "Scenix: Sparse-View 3D Scene Reconstruction via Executable Scene Programs",
        "venue": "arXiv preprint, 2026",
        "authors": "Kai Li, Lutao Jiang, Zhenyang Li, Jiayu Dong, Jierui Zhang, Yingda Yin, Runze Zhang, Kai Yan, Xiaoyang Huang, Keyang Luo, Xin Wang, Xiangyu Zhao, and Weikai Chen.",
        "url": "https://arxiv.org/abs/2608.07012",
    },
    {
        "title": "E2Pano: Learning Event-to-Panorama Image Reconstruction",
        "venue": "arXiv preprint, 2026",
        "authors": "Zhenyang Li, Zongqi He, Jia Pan, Shijie Lin, and Yifan Peng.",
        "url": "https://arxiv.org/abs/2608.00694",
    },
    {
        "title": "O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking and Reasoning",
        "venue": "European Conference on Computer Vision (ECCV), 2026",
        "authors": "Mei Yuan, Qi Long, Qifeng Wu, Zhenyang Li, Yizhou Zhao, Lei Wang, Yang Liu, and Min Xu.",
        "url": "https://arxiv.org/abs/2607.18142",
    },
    {
        "title": "ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints",
        "venue": "Computational Visual Media (CVMJ), 2026",
        "authors": "Xiaoyang Bai*, Zhenyang Li*, Weiwei Xu, Edmund Y. Lam, and Yifan Peng.",
        "url": "https://arxiv.org/abs/2608.08531",
    },
    {
        "title": "PatternGSL: A Structured Specification Language for Template-Free and Simulation-Ready 3D Garments",
        "venue": "ACM SIGGRAPH, 2026",
        "authors": "Zhenyang Li*, Lutao Jiang*, Yizhou Zhao, Ying-Cong Chen, Xin Wang, Weikai Chen, and Yifan Peng.",
        "url": "https://dl.acm.org/doi/10.1145/3799902.3811044",
    },
    {
        "title": "EventTracer: Fast Path Tracing-based Event Stream Rendering",
        "venue": "IEEE Transactions on Visualization and Computer Graphics (TVCG), 2026",
        "authors": "Zhenyang Li*, Xiaoyang Bai*, Jinfan Lu, Pengfei Shen, Edmund Y. Lam, and Yifan Peng.",
        "url": "https://doi.org/10.1109/TVCG.2026.3701141",
    },
    {
        "title": "SAP: Segment Any 4K Panorama",
        "venue": "arXiv preprint, 2026",
        "authors": "Lutao Jiang, Zidong Cao, Weikai Chen, Xu Zheng, Yuanhuiyi Lyu, Zhenyang Li, Zeyu Hu, Yingda Yin, Keyang Luo, Runze Zhang, Kai Yan, Shengju Qian, Haidi Fan, Yifan Peng, Xin Wang, Hui Xiong, and Ying-Cong Chen.",
        "url": "https://arxiv.org/abs/2603.12759",
    },
    {
        "title": "Augmented Reality Integration Improves Ergonomics in Dynamic Navigation for Dental Implant Surgery",
        "venue": "Journal of the Society for Information Display, 2026",
        "authors": "Pui Hang Leung, Feng Wang, Zhenyang Li, Zongqi He, Yifan Peng, and Wei-fa Yang.",
        "url": "https://doi.org/10.1002/jsid.70061",
    },
    {
        "title": "Structure-grounded Training Strategies Aid Generalization in Stereo Matching",
        "venue": "International Conference on 3D Vision (3DV), 2026",
        "authors": "Liangxun Ou, Yuhui Liu, Zhenyang Li, Xiaoyang Bai, and Yifan Peng.",
        "url": "https://openreview.net/forum?id=rIeputhlON",
    },
    {
        "title": "ConsistNav: Closing the Action Consistency Gap in Zero-Shot Object Navigation with Semantic Executive Control",
        "venue": "arXiv preprint, 2026",
        "authors": "Haosen Wang*, Zhenyang Li*, Yinqiang Zhang, Zongqi He, Lutao Jiang, Kai Li, Yizhou Zhao, Liaoyuan Fan, Wenjian Hou, Tingbang Liang, Yibin Wen, and Defeng Gu.",
        "url": "https://arxiv.org/abs/2605.09869",
    },
    {
        "title": "Enhanced Velocity Field Modeling for Gaussian Video Reconstruction",
        "venue": "IEEE International Symposium on Mixed and Augmented Reality (ISMAR), 2025",
        "authors": "Zhenyang Li*, Xiaoyang Bai*, Tongchen Zhang, Pengfei Shen, Weiwei Xu, and Yifan Peng.",
    },
    {
        "title": "Toward Material-Agnostic System Identification from Videos",
        "venue": "IEEE/CVF International Conference on Computer Vision (ICCV), 2025",
        "authors": "Yizhou Zhao, Haoyu Chen, Chunjiang Liu, Zhenyang Li, Charles Herrmann, Junhwa Hur, Yinxiao Li, Ming-Hsuan Yang, Bhiksha Raj, and Min Xu.",
    },
    {
        "title": "ORBIT: Overlapping Region-Based Image Feature Matching Technique",
        "venue": "Under review, 2025",
        "authors": "Qi Luo*, Zhenyang Li*, Linsong Xue, Haojie Wu, Yifan Peng, and Kai Zhang.",
    },
    {
        "title": "3D-HoloNet: Fast, unfiltered, 3D hologram generation with camera-calibrated network learning",
        "venue": "Optics Letters, 2025",
        "authors": "Wenbin Zhou, Feifan Qu, Xiangyu Meng, Zhenyang Li, and Yifan Peng.",
        "url": "https://doi.org/10.1364/OL.544816",
    },
    {
        "title": "Point Resampling and Ray Transformation Aid to Editable NeRF Models",
        "venue": "arXiv preprint, 2024",
        "authors": "Zhenyang Li*, Zilong Chen*, Feifan Qu, Mingqing Wang, Yizhou Zhao, Kai Zhang, and Yifan Peng.",
        "url": "https://arxiv.org/abs/2405.07306",
    },
    {
        "title": "CryoSAM: Training-free CryoET Tomogram Segmentation with Foundation Models",
        "venue": "Medical Image Computing and Computer Assisted Intervention (MICCAI), 2024",
        "authors": "Yizhou Zhao, Hengwei Bian, Michael Mu, Mostofa R. Uddin, Zhenyang Li, Xiang Li, Tianyang Wang, and Min Xu.",
    },
    {
        "title": "Breaking Filter Bubble: A Reinforcement Learning Framework of Controllable Recommender System",
        "venue": "The ACM Web Conference (WWW), 2023",
        "authors": "Zhenyang Li*, Yancheng Dong*, Chen Gao, Yizhou Zhao, Dong Li, Jianye Hao, Kai Zhang, Yong Li, and Zhi Wang.",
    },
    {
        "title": "Unsupervised Anomaly Detection with Local-Sensitive VQVAE and Global-Sensitive Transformers",
        "venue": "IEEE International Conference on Image Processing (ICIP), 2023",
        "authors": "Mingqing Wang, Jiawei Li, Zhenyang Li, Chengxiao Luo, Bin Chen, Shu-Tao Xia, and Zhi Wang.",
    },
    {
        "title": "Enhancing multi-view stereo with contrastive matching and weighted focal loss",
        "venue": "IEEE International Conference on Image Processing (ICIP), 2022",
        "authors": "Yikang Ding*, Zhenyang Li*, Dihe Huang, Zhiheng Li, and Kai Zhang.",
    },
    {
        "title": "Adaptive Range guided Multi-view Depth Estimation with Normal Ranking Loss",
        "venue": "Asian Conference on Computer Vision (ACCV), 2022",
        "authors": "Yikang Ding*, Zhenyang Li*, Dihe Huang, Kai Zhang, Zhiheng Li, and Wensen Feng.",
    },
    {
        "title": "Alignment-guided Temporal Attention for Video Action Recognition",
        "venue": "Advances in Neural Information Processing Systems (NeurIPS), 2022",
        "authors": "Yizhou Zhao*, Zhenyang Li*, Xun Guo, and Yan Lu.",
    },
]


EN = {
    "lang": "en",
    "name": "Zhenyang Li",
    "location": "Shenzhen / Hong Kong",
    "sections": {
        "education": "Education",
        "experience": "Research / Industry Experience",
        "publications": "Selected Publications & Patent",
        "skills": "Research Focus & Technical Skills",
        "service": "Academic Service, Talks & Honors",
    },
    "equal": "* indicates equal contribution.",
    "continued": "Selected Publications & Patent (continued)",
    "education": [
        ("2023.09 - Present", "<b>The University of Hong Kong (HKU)</b>, Ph.D. in Electrical and Computer Engineering (formerly EEE).<br/>Advisors: Dr. Yifan (Evan) Peng and Prof. Jia Pan. Research areas: computer vision, computer graphics, VR/AR/MR, and computational imaging."),
        ("2020.09 - 2023.07", "<b>Tsinghua University (THU)</b>, M.S. in Big Data Engineering.<br/>Department of Automation and Shenzhen International Graduate School. Advisor: Prof. Kai Zhang."),
        ("2016.09 - 2020.07", "<b>Nanjing University of Science and Technology (NJUST)</b>, B.S. in Electronic and Information Engineering.<br/>School of Electronic and Optical Engineering."),
    ],
    "experience": [
        ("2025.10 - Present", "<b>Research Intern, Tencent LIGHTSPEED STUDIOS</b>, Shenzhen, China.<br/>Research focus: multimodal and 3D content generation and simulation."),
        ("2022.07 - 2022.11", "<b>Research Intern, Megvii Technology Limited (Face++)</b>, Beijing, China.<br/>Research focus: visual odometry, NeRF, multi-view stereo, and feature matching."),
        ("2021.11 - 2022.05", "<b>Research Intern, Microsoft Research Asia (MSRA)</b>, Beijing, China.<br/>Research focus: video understanding and learning-based computer vision."),
        ("2021.03 - 2021.09", "<b>Artificial Intelligence Researcher, Huawei Technologies Co., Ltd.</b>, Shenzhen, China.<br/>Research focus: 3D reconstruction and visual localization."),
    ],
    "skills": [
        ("Research Areas", "World models; 3D/4D scene reconstruction and generation; 3D Gaussian Splatting; neural rendering; event-based vision."),
        ("Core Methods", "NeRF/3DGS; video and 3D generation; path tracing; multi-view geometry; stereo/depth estimation; vision-language-action models."),
        ("Applications", "Dynamic visual world modeling; fast motion reconstruction; simulation-ready garments; AR/MR navigation; holographic imaging and display."),
    ],
    "service": [
        ("PC Member", "<b>AAAI 2027; 34th ACM Multimedia (ACMMM) 2026.</b>"),
        ("Reviewer", "CVPR 2026, ECCV 2026, NeurIPS 2026, BMVC 2026, 3DV 2026, ISMAR 2026, ACML 2026; SIGGRAPH Asia 2025 (XR Track), ICCV 2025, ISMAR 2025, NeurIPS 2025, ICML 2025, ICLR 2025, ACM MM 2025, AISTATS 2025, ACML 2025, 3DV 2025, NeurIPS 2024."),
        ("Journal", "IEEE Journal of Selected Topics in Signal Processing (J-STSP)."),
        ("Talks", "<b>2025.12 WeLight Workshop</b>, Organizer and Speaker, The University of Hong Kong; <b>2023.05 ELEC4544: AI and Deep Learning</b>, Guest Lecturer, The University of Hong Kong."),
        ("Honors", "<b>2023.12 Champion</b>, Guangdong-Hong Kong-Macao Greater Bay Area International Algorithm Case Competition; <b>2020.04 Top 7/256</b>, High-energy particle collision classification challenge; <b>2019.05 Second Prize</b>, Mathematical Contest in Modeling; <b>2017 TE Connectivity Scholarship</b> (Top 1/600), Beijing SMC Education Foundation Outstanding Scholarship Special Award (Top 1/600), and Second Prize in National Mathematics Competition for College Students."),
    ],
}


ZH = {
    "lang": "zh",
    "name": "李镇洋",
    "location": "深圳 / 香港",
    "sections": {
        "education": "教育背景",
        "experience": "科研与产业经历",
        "publications": "代表性论文与专利",
        "skills": "研究方向与技术能力",
        "service": "学术服务、报告与荣誉",
    },
    "equal": "* 表示共同一作。",
    "continued": "代表性论文与专利（续）",
    "education": [
        ("2023.09 - 至今", "<b>香港大学（HKU）</b>，电机与计算机工程博士研究生（原电子电气工程）。<br/>导师：Yifan (Evan) Peng 博士与 Jia Pan 教授。研究方向：计算机视觉、计算机图形学、VR/AR/MR、计算成像。"),
        ("2020.09 - 2023.07", "<b>清华大学（THU）</b>，大数据工程硕士。<br/>自动化系与深圳国际研究生院。导师：Kai Zhang 教授。"),
        ("2016.09 - 2020.07", "<b>南京理工大学（NJUST）</b>，电子信息工程学士。<br/>电子工程与光电技术学院。"),
    ],
    "experience": [
        ("2025.10 - 至今", "<b>腾讯光子工作室群，研究实习生</b>，深圳，中国。<br/>研究方向：多模态与三维内容生成及仿真。"),
        ("2022.07 - 2022.11", "<b>旷视科技（Face++），研究实习生</b>，北京，中国。<br/>研究方向：视觉里程计、NeRF、多视图立体与特征匹配。"),
        ("2021.11 - 2022.05", "<b>微软亚洲研究院（MSRA），研究实习生</b>，北京，中国。<br/>研究方向：视频理解与学习式计算机视觉。"),
        ("2021.03 - 2021.09", "<b>华为技术有限公司，人工智能研究员</b>，深圳，中国。<br/>研究方向：三维重建与视觉定位。"),
    ],
    "skills": [
        ("研究方向", "世界模型；3D/4D 场景重建与生成；3D Gaussian Splatting；神经渲染；事件视觉。"),
        ("核心方法", "NeRF/3DGS；视频与三维生成；路径追踪；多视图几何；立体/深度估计；视觉-语言-动作模型。"),
        ("应用场景", "动态视觉世界建模；快速运动重建；仿真就绪三维服装；AR/MR 导航；全息成像与显示。"),
    ],
    "service": [
        ("程序委员", "<b>AAAI 2027；第 34 届 ACM Multimedia（ACMMM）2026。</b>"),
        ("审稿人", "CVPR 2026、ECCV 2026、NeurIPS 2026、BMVC 2026、3DV 2026、ISMAR 2026、ACML 2026；SIGGRAPH Asia 2025（XR Track）、ICCV 2025、ISMAR 2025、NeurIPS 2025、ICML 2025、ICLR 2025、ACM MM 2025、AISTATS 2025、ACML 2025、3DV 2025、NeurIPS 2024。"),
        ("期刊审稿", "IEEE Journal of Selected Topics in Signal Processing（J-STSP）。"),
        ("报告与教学", "<b>2025.12 WeLight Workshop</b>，组织者与报告人，香港大学；<b>2023.05 ELEC4544: AI and Deep Learning</b>，客座讲师，香港大学。"),
        ("荣誉奖励", "<b>2023.12 冠军</b>，粤港澳大湾区国际算法算例大赛；<b>2020.04 第 7 名 / 256</b>，高能粒子碰撞分类挑战赛；<b>2019.05 二等奖</b>，美国大学生数学建模竞赛；<b>2017 TE Connectivity 奖学金</b>（前 1/600）、北京 SMC 教育基金会优秀奖学金特别奖（前 1/600）及全国大学生数学竞赛二等奖。"),
    ],
}


class SectionHeader(Flowable):
    def __init__(self, text, font_name):
        super().__init__()
        self.text = text
        self.font_name = font_name
        self.height = 18

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return avail_width, self.height

    def draw(self):
        canvas = self.canv
        canvas.setStrokeColor(LIGHT_BLUE)
        canvas.setLineWidth(0.7)
        canvas.line(0, 1.8, self.width, 1.8)
        label_width = max(83, pdfmetrics.stringWidth(self.text, self.font_name, 11) + 18)
        canvas.setFillColor(BLUE)
        canvas.rect(0, 1.8, label_width, 16, stroke=0, fill=1)
        path = canvas.beginPath()
        path.moveTo(label_width, 1.8)
        path.lineTo(label_width + 13, 1.8)
        path.lineTo(label_width + 7, 17.8)
        path.lineTo(label_width, 17.8)
        path.close()
        canvas.setFillColor(LIGHT_BLUE)
        canvas.drawPath(path, stroke=0, fill=1)
        canvas.setFillColor(colors.white)
        canvas.setFont(self.font_name, 11)
        canvas.drawString(8, 5.2, self.text)


def emphasize_name(authors):
    return authors.replace("Zhenyang Li", "<u>Zhenyang Li</u>")


def make_styles(lang):
    if lang == "zh":
        base_font = "LXGW"
        bold_font = "LXGW"
        body_size = 8.45
    else:
        base_font = "Times-Roman"
        bold_font = "Times-Bold"
        body_size = 8.3

    return {
        "name": ParagraphStyle("name", fontName=bold_font, fontSize=18, leading=20, textColor=TEXT, spaceAfter=4),
        "contact": ParagraphStyle("contact", fontName=base_font, fontSize=7.6, leading=10.4, textColor=colors.HexColor("#253A59")),
        "body": ParagraphStyle("body", fontName=base_font, fontSize=body_size, leading=10.2, textColor=TEXT),
        "date": ParagraphStyle("date", fontName=base_font, fontSize=7.8, leading=10.2, textColor=TEXT),
        "pub_title": ParagraphStyle(
            "pub_title",
            fontName="CVSerif",
            fontSize=8.55,
            leading=10.45,
            textColor=TEXT,
            spaceAfter=0.8,
        ),
        "pub_authors": ParagraphStyle(
            "pub_authors",
            fontName="CVSerif",
            fontSize=8.15,
            leading=9.95,
            textColor=TEXT,
            spaceAfter=3.2,
        ),
        "note": ParagraphStyle("note", fontName=base_font, fontSize=7.2, leading=8.5, textColor=colors.HexColor("#333333"), spaceAfter=3),
        "label": ParagraphStyle("label", fontName=base_font, fontSize=8.0, leading=10, textColor=TEXT, alignment=TA_LEFT),
    }


def dated_rows(rows, styles):
    story = []
    for date, body in rows:
        table = Table(
            [[Paragraph(date, styles["date"]), Paragraph(body, styles["body"])]],
            colWidths=[35 * mm, 1],
            hAlign="LEFT",
        )
        table._argW[1] = 159 * mm - table._argW[0]
        table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (0, -1), 5),
                    ("RIGHTPADDING", (1, 0), (1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )
        story.append(table)
    return story


def publication_flowables(styles, publications):
    items = []
    for publication in publications:
        title = publication["title"]
        if publication.get("url"):
            title = f'<font name="CVSerif-Bold"><link href="{publication["url"]}" color="#111111">{title}</link></font>'
        else:
            title = f'<font name="CVSerif-Bold">{title}</font>'
        title_line = f'{title}, <font name="CVSerif-Italic">{publication["venue"]}</font>.'
        authors = emphasize_name(publication["authors"])
        items.append(
            KeepTogether(
                [
                    Paragraph(title_line, styles["pub_title"]),
                    Paragraph(authors, styles["pub_authors"]),
                ]
            )
        )
    return items


def draw_page(canvas, doc):
    canvas.saveState()
    if doc.page == 1 and PHOTO.exists():
        canvas.drawImage(
            str(PHOTO),
            A4[0] - 38 * mm,
            A4[1] - 37 * mm,
            width=25 * mm,
            height=24 * mm,
            preserveAspectRatio=True,
            anchor="c",
            mask="auto",
        )
    canvas.restoreState()


def build_pdf(content, output_path):
    styles = make_styles(content["lang"])
    section_font = "LXGW" if content["lang"] == "zh" else "Times-Bold"
    doc = BaseDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=13 * mm,
        rightMargin=13 * mm,
        topMargin=12 * mm,
        bottomMargin=10 * mm,
        title=f"{content['name']} - Curriculum Vitae",
        author=content["name"],
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id="cv", frames=[frame], onPage=draw_page))

    contact = (
        f'<link href="mailto:lizy23@connect.hku.hk">lizy23@connect.hku.hk</link>  |  '
        f'<link href="mailto:lagrangelzy@gmail.com">lagrangelzy@gmail.com</link>  |  {content["location"]}<br/>'
        '<link href="https://lagrangeli.github.io/">lagrangeli.github.io</link>  |  '
        '<link href="https://github.com/Lagrangeli">github.com/Lagrangeli</link><br/>'
        '<link href="https://scholar.google.com/citations?user=r9f4mLMAAAAJ">Google Scholar</link>  |  '
        '<link href="https://linkedin.com/in/zhenyang-li-875a69181">LinkedIn</link>  |  '
        f'{scholar_summary()}'
    )
    story = [
        Paragraph(content["name"], styles["name"]),
        Paragraph(contact, styles["contact"]),
        Spacer(1, 8),
        SectionHeader(content["sections"]["education"], section_font),
        Spacer(1, 5),
        *dated_rows(content["education"], styles),
        Spacer(1, 4),
        SectionHeader(content["sections"]["experience"], section_font),
        Spacer(1, 5),
        *dated_rows(content["experience"], styles),
        Spacer(1, 4),
        SectionHeader(content["sections"]["publications"], section_font),
        Spacer(1, 4),
        Paragraph(content["equal"], styles["note"]),
        *publication_flowables(styles, PUBLICATIONS),
        KeepTogether(
            [
                Paragraph(
                    '<font name="CVSerif-Bold">Wireless network maximum safety rate power distribution method based on direction modulation</font>, '
                    '<font name="CVSerif-Italic">Authorized invention patent CN110635832A, 2019</font>.',
                    styles["pub_title"],
                ),
                Paragraph(
                    '<u>Zhenyang Li</u>, Yumeng Zhang, Jiayu Li, Feng Shu, Haochen Li, Tianyun Wang, Yu Wang, Yuefeng Huang, Linqing Gui, and Yuwen Qian.',
                    styles["pub_authors"],
                ),
            ]
        ),
        Spacer(1, 5),
        SectionHeader(content["sections"]["skills"], section_font),
        Spacer(1, 5),
        *dated_rows(content["skills"], styles),
        Spacer(1, 4),
        SectionHeader(content["sections"]["service"], section_font),
        Spacer(1, 5),
        *dated_rows(content["service"], styles),
    ]
    doc.build(story)


def main():
    if not ZH_FONT.exists():
        raise FileNotFoundError(f"Chinese CV font not found: {ZH_FONT}")
    missing_serif = [str(path) for path in SERIF_FONTS.values() if not path.exists()]
    if missing_serif:
        raise FileNotFoundError(f"CV serif fonts not found: {', '.join(missing_serif)}")
    pdfmetrics.registerFont(TTFont("LXGW", str(ZH_FONT)))
    for name, path in SERIF_FONTS.items():
        pdfmetrics.registerFont(TTFont(name, str(path)))
    fonts.addMapping("CVSerif", 0, 0, "CVSerif")
    fonts.addMapping("CVSerif", 1, 0, "CVSerif-Bold")
    fonts.addMapping("CVSerif", 0, 1, "CVSerif-Italic")
    fonts.addMapping("CVSerif", 1, 1, "CVSerif-BoldItalic")
    for bold in (0, 1):
        for italic in (0, 1):
            fonts.addMapping("LXGW", bold, italic, "LXGW")

    en_pdf = ROOT / "Zhenyang LI - CV - phd.pdf"
    zh_pdf = ROOT / "Zhenyang LI - CV - phd - zh.pdf"
    build_pdf(EN, en_pdf)
    build_pdf(ZH, zh_pdf)

    aliases = {
        en_pdf: [ROOT / "cv-en.pdf", ROOT / "assets/pdf/Zhenyang_Li_CV_202608.pdf"],
        zh_pdf: [ROOT / "cv-zh.pdf", ROOT / "assets/pdf/Zhenyang_Li_CV_ZH_202608.pdf"],
    }
    for source, targets in aliases.items():
        for target in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    print(f"Generated {en_pdf}")
    print(f"Generated {zh_pdf}")


if __name__ == "__main__":
    main()
