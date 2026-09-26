#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to generate the professional LaTeX report (HW01_Report.tex)
and compile it to HW01_Report.pdf for FIT@HCMUS CS423 / CSC13003.
"""

import os
import subprocess

def create_latex_file():
    tex_content = r'''\documentclass[11pt,a4paper]{article}

% ==============================================================================
% 1. PACKAGES & SETUP
% ==============================================================================
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setmonofont{Courier New}

\usepackage{geometry}
\geometry{
    a4paper,
    top=25mm,
    bottom=25mm,
    left=25mm,
    right=20mm
}

\usepackage{xcolor}
\definecolor{hcmusblue}{RGB}{0, 51, 102}
\definecolor{darkblue}{RGB}{0, 34, 68}
\definecolor{linkblue}{RGB}{0, 102, 204}
\definecolor{codebg}{RGB}{245, 247, 250}
\definecolor{boxborder}{RGB}{200, 215, 230}
\definecolor{passgreen}{RGB}{0, 128, 0}
\definecolor{failred}{RGB}{180, 0, 0}

\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=hcmusblue,
    citecolor=linkblue,
    urlcolor=linkblue,
    pdftitle={Báo Cáo Tổng Hợp HW01 - CS423 Software Testing - Nguyễn Bảo An},
    pdfauthor={Nguyễn Bảo An - 23120207},
    pdfsubject={CS423 / CSC13003 Software Testing},
    pdfkeywords={Software Testing, ISTQB, AI Hallucination, Hardware Testing, HCMUS}
}

\usepackage{booktabs}
\usepackage{longtable}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{makecell}
\usepackage{array}

\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\setlength{\headheight}{14pt}
\fancyhead[L]{\small\color{gray}FIT@HCMUS · CS423 / CSC13003 – Kiểm thử phần mềm}
\fancyhead[R]{\small\color{gray}Báo cáo HW01 – Nguyễn Bảo An (23120207)}
\fancyfoot[L]{\small\color{gray}Lớp 23CLC01 · Mã nộp bài: 100}
\fancyfoot[R]{\small\color{gray}Trang \thepage\ / \pageref{LastPage}}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.5pt}

\usepackage{lastpage}
\usepackage{titlesec}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{hcmusblue}}{\thesection}{1em}{}[{\titlerule[0.8pt]}]
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{darkblue}}{\thesubsection}{1em}{}
\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries\color{darkblue}}{\thesubsubsection}{1em}{}

\usepackage{tcolorbox}
\tcbset{
    boxrule=0.8pt,
    colback=codebg,
    colframe=boxborder,
    arc=3mm,
    left=4mm,
    right=4mm,
    top=3mm,
    bottom=3mm
}

\usepackage{enumitem}
\setlist{nosep, leftmargin=6mm}

\usepackage{amsmath, amssymb}
\usepackage{microtype}

% ==============================================================================
% 2. DOCUMENT BODY
% ==============================================================================
\begin{document}

% ------------------------------------------------------------------------------
% COVER PAGE
% ------------------------------------------------------------------------------
\begin{titlepage}
\thispagestyle{empty}
\begin{tcolorbox}[colback=white, colframe=hcmusblue, boxrule=2pt, arc=0mm, height=\textheight]
\begin{center}
    {\large \textbf{ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH}}\\[2mm]
    {\large \textbf{TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN}}\\[2mm]
    {\large \textbf{KHOA CÔNG NGHỆ THÔNG TIN}}\\[1mm]
    {\normalsize BỘ MÔN CÔNG NGHỆ PHẦN MỀM}\\[15mm]
    
    \rule{0.8\textwidth}{1.5pt}\\[6mm]
    {\LARGE \textbf{\color{hcmusblue}BÁO CÁO TỔNG KẾT BÀI TẬP CÁ NHÂN}}\\[3mm]
    {\huge \textbf{\color{hcmusblue}BÀI TẬP HW01}}\\[4mm]
    {\large \textbf{MÔN HỌC: KIỂM THỬ PHẦN MỀM (CS423 / CSC13003)}}\\[2mm]
    {\normalsize \textit{Chương trình Cử nhân Công nghệ Thông tin (AI-augmented · Năm học 2026)}}\\[4mm]
    \rule{0.8\textwidth}{1.5pt}\\[12mm]
    
    {\large \textbf{ĐỀ TÀI:}}\\[3mm]
    {\large \textbf{KHẢO SÁT THỊ TRƯỜNG VIỆC LÀM QA/QC 2026+}}\\[1.5mm]
    {\large \textbf{20 SỰ CỐ PHẦN MỀM THỰC TẾ \& BẪY ẢO GIÁC AI}}\\[1.5mm]
    {\large \textbf{KIỂM THỬ THỰC NGHIỆM THIẾT BỊ VẬT LÝ QUẠT SENKO L1638}}\\[1.5mm]
    {\large \textbf{GIAO THỨC CỘNG TÁC \& BIỂU MẪU KIỂM TOÁN AI (FIT@HCMUS)}}\\[15mm]
    
    \begin{minipage}{0.85\textwidth}
    \begin{tabular}{ll}
        \textbf{Sinh viên thực hiện:} & \textbf{NGUYỄN BẢO AN} \\
        \textbf{Mã số sinh viên (MSSV):} & \textbf{23120207} \\
        \textbf{Lớp / Khóa học:} & \textbf{23CLC01} (Khóa 2023 -- 2027) \\
        \textbf{Giảng viên phụ trách:} & \textbf{TS. Lâm Quang Vũ / TS. Trần Duy Hoàng} \\
        \textbf{Mã tự đánh giá nộp bài:} & \textbf{100} (100 / 100 điểm) \\
        \textbf{Kho mã nguồn GitHub:} & \href{https://github.com/NgBaoAnn/hw1}{\texttt{https://github.com/NgBaoAnn/hw1}} \\
        \textbf{Ngày hoàn thành:} & 26 tháng 09 năm 2026 \\
    \end{tabular}
    \end{minipage}
    
    \vfill
    {\normalsize \textbf{THÀNH PHỐ HỒ CHÍ MINH -- THÁNG 09/2026}}
\end{center}
\end{tcolorbox}
\end{titlepage}

\newpage
\pagenumbering{roman}

% ------------------------------------------------------------------------------
% TABLE OF CONTENTS
% ------------------------------------------------------------------------------
\tableofcontents
\newpage

\pagenumbering{arabic}
\setcounter{page}{1}

% ==============================================================================
% SECTION 1: TỔNG QUAN BÀI TẬP & CẤU TRÚC
% ==============================================================================
\section{Tổng quan Bài tập \& Cấu trúc Tổ chức}

Bài tập cá nhân \textbf{HW01 (CS423 / CSC13003 -- Software Testing)} được thực hiện với định hướng tiên phong tích hợp trí tuệ nhân tạo (\textit{AI-augmented testing}), đồng thời tuân thủ nghiêm ngặt chuẩn mực công nghiệp \textbf{ISTQB CTFL v4.0} và chính sách liêm chính học thuật của Khoa Công nghệ Thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM.

Dự án được tổ chức chặt chẽ theo cấu trúc thư mục tiêu chuẩn, hỗ trợ cả 2 định dạng: bản số hóa văn bản (\textit{Text-based markdown files}) và bản nhị phân chứng thực (\textit{Binary-based assets: .docx, .xlsx, .pdf, .png, .jpg}):

\begin{tcolorbox}
\begin{verbatim}
hw1/
├── requirements/
│   ├── req1_job_market/               # Yêu cầu 1: Thị trường việc làm QA/QC 2026+
│   │   ├── jobs_data.md               # Chi tiết 10 JDs, kỹ năng, lương, AI Impact
│   │   ├── screenshots/               # 10 ảnh chụp màn hình có header avatar anti-cheat
│   │   └── mindmap/                   # Sơ đồ Mermaid và phân tích 3 lỗi sai ISTQB
│   ├── req2_software_defects/         # Yêu cầu 2: 20 Lỗi phần mềm 2022-2026
│   │   └── defects_2022_2026.md       # Báo cáo 20 lỗi & 20 bẫy phỏng vấn bóc trần AI
│   └── req3_physical_product/         # Yêu cầu 3: Kiểm thử quạt Senko L1638
│       ├── device_info.md             # Thông số quạt, 5 lỗi phát hiện, link issues
│       ├── edge_cases_ai_missed.md    # Phân tích 4 ca biên cơ điện AI bỏ sót
│       ├── test_cases.md              # 15 Test cases ISTQB (10 Pass, 5 Fail)
│       ├── test_cases.csv             # Bản xuất dữ liệu bảng tính phẳng
│       ├── test_cases_and_summary.xlsx# File Excel tiêu chuẩn 3 sheets
│       ├── photo/                     # Ảnh thẻ SV + Thiết bị, ảnh chat AI & 5 ảnh issues
│       └── github_issues/             # Chi tiết 5 issues và bảng điều phối
├── AI Templates/                      # Bộ 4 biểu mẫu .docx chính thức nộp bài
│   ├── [AI-02] - FIT@HCMUS - AI Audit Report_En.docx
│   ├── [AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx
│   ├── [AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx
│   ├── [AI-06] - FIT@HCMUS - AI Student Acknowledgement_En.docx
│   └── blank_templates/               # Bản sao lưu mẫu trắng gốc
├── templates/                         # Bộ biểu mẫu AI bản Markdown đối ứng
├── scripts/                           # Bộ công cụ tự động hóa kiểm định & đóng gói
│   ├── populate_docx_templates.py     # Script OpenXML điền dữ liệu vào biểu mẫu .docx
│   ├── generate_full_excel.py         # Script OpenXML xuất file Excel 3 sheets
│   └── package_submission.sh          # Script kiểm tra hợp lệ & đóng gói nộp bài
├── reports/                           # Báo cáo tổng hợp và nhật ký kiểm định
│   ├── HW01_Report.md                 # Báo cáo tổng kết toàn diện (Markdown)
│   ├── HW01_Report.tex                # Mã nguồn LaTeX báo cáo chuyên nghiệp
│   ├── HW01_Report.pdf                # Ấn bản PDF biên dịch chính thức
│   ├── AI-02_AI_Audit_Report.md       # Báo cáo kiểm định AI chính thức
│   ├── AI_Critique.md                 # Đoạn văn phê bình chuyên môn (291 từ)
│   ├── Self_Assessment.md             # Bảng tự chấm điểm 100/100
│   ├── Oral_Defense_Guide.md          # Tài liệu ôn tập 3 câu hỏi vấn đáp miệng
│   ├── test_cases_and_summary.xlsx    # Bảng tính Excel chuẩn 3 sheets
│   ├── Appendix_A_Prompt_Log.md       # Nhật ký 41 Prompts đầy đủ timestamp
│   └── git_log.txt                    # Lịch sử trích xuất toàn bộ commit Git
└── prompt_log.md                      # Bản sao lưu log prompt tại thư mục gốc
\end{verbatim}
\end{tcolorbox}

% ==============================================================================
% SECTION 2: YÊU CẦU 1: THỊ TRƯỜNG VIỆC LÀM QA/QC 2026+
% ==============================================================================
\section{Yêu cầu 1: Phân tích Thị trường Việc làm QA/QC 2026+ (40 Điểm)}

\subsection{Bảng Tổng hợp 10 Tin tuyển dụng thực tế ITviec}
Tất cả 10 tin tuyển dụng đều được thu thập thực tế từ nền tảng \textbf{ITviec} trong khoảng thời gian $\le 27$ ngày tính đến thời điểm khảo sát (tháng 09/2026), đáp ứng trọn vẹn yêu cầu độ mới $\le 60$ ngày. Trong đó, có đúng \textbf{3 vị trí chuyên sâu về AI/LLM Testing}, và mỗi tin đều có ảnh chụp màn hình độ phân giải cao đính kèm hiển thị rõ ràng header tài khoản sinh viên \texttt{NGUYỄN BẢO AN}.

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l p{3.2cm} p{2.2cm} c c p{4.2cm}}
\toprule
\textbf{Mã Job} & \textbf{Vị trí (Job Title)} & \textbf{Công ty} & \textbf{Mức lương} & \textbf{Ngày đăng} & \textbf{Kỹ năng trọng tâm / AI Factor} \\
\midrule
\textbf{JOB-01} & Senior QA Automation & FPT Software & 35 -- 55M & 24/09/2026 & Selenium, Playwright, CI/CD, Java \\
\textbf{JOB-02} & \textbf{AI QA Engineer (LLM)} & VNG Corp & 40 -- 65M & 23/09/2026 & \textbf{LLM Evaluation, Prompt Injection, RAG} \\
\textbf{JOB-03} & QC Lead / QA Manager & VTI Group & 45 -- 70M & 22/09/2026 & Test Management, ISTQB, Process Quality \\
\textbf{JOB-04} & \textbf{GenAI Quality Spec.} & Viettel Sol. & 35 -- 60M & 21/09/2026 & \textbf{Hallucination Detection, Red Teaming} \\
\textbf{JOB-05} & Performance \& Security & NAB Innovation & 40 -- 60M & 20/09/2026 & JMeter, Gatling, OWASP Top 10, Cloud AWS \\
\textbf{JOB-06} & Manual QC Engineer & KMS Technology & 15 -- 25M & 19/09/2026 & Test Design, Boundary Analysis, SQL \\
\textbf{JOB-07} & \textbf{AI Model Eval. Tester} & Axon Vietnam & 45 -- 75M & 18/09/2026 & \textbf{Computer Vision, BLEU/ROUGE, Python} \\
\textbf{JOB-08} & QA Specialist (Medical) & TMA Solutions & 20 -- 35M & 16/09/2026 & FDA Compliance, ISO 13485, Verification \\
\textbf{JOB-09} & Embedded / IoT QA & Bosch Vietnam & 25 -- 45M & 15/09/2026 & HIL Testing, CAN Bus, C/C++, IEC 61508 \\
\textbf{JOB-10} & Mobile Automation QA & Momo & 30 -- 50M & 14/09/2026 & Appium, Maestro, Espresso, Fintech \\
\bottomrule
\end{tabularx}
\caption{Bảng tổng hợp 10 tin tuyển dụng thực tế thu thập từ ITviec (Tháng 09/2026)}
\end{table}

\subsection{Phân tích Xu hướng Thị trường, Mức lương \& Tác động AI}
\begin{itemize}
    \item \textbf{Phổ lương phân hóa sâu sắc theo công nghệ:} Vị trí Manual QC truyền thống dao động từ 15 -- 25 triệu VND/tháng. QA Automation và Performance/Security dao động từ 30 -- 55 triệu VND/tháng. Các vị trí \textbf{AI QA / LLM Evaluation Specialist} dẫn đầu thị trường với mức thu nhập vượt trội từ \textbf{40 -- 75 triệu VND/tháng} (tương đương 1.600 -- 3.000 USD/tháng).
    \item \textbf{Tác động cách mạng của AI lên nghề kiểm thử:} 
    \begin{enumerate}
        \item Chuyển dịch từ thực thi thụ động sang đánh giá mô hình độc lập (\textit{Model Evaluation \& Safety Red Teaming}).
        \item Xuất hiện các loại hình kiểm thử hoàn toàn mới: Kiểm thử ảo giác (Hallucination Benchmarking), Kiểm thử chống tấn công Prompt Injection / Jailbreak, và Kiểm định chất lượng ngữ nghĩa hệ thống RAG (\textit{Retrieval-Augmented Generation}).
        \item Kỹ sư kiểm thử không bị thay thế bởi AI, nhưng các kỹ sư biết ứng dụng AI để tăng tốc kiểm thử và có năng lực kiểm định mô hình AI sẽ thay thế những kỹ sư chỉ thao tác thủ công đơn thuần.
    \end{enumerate}
\end{itemize}

\subsection{Sơ đồ Tư duy (Mindmap) Vai trò QA/QC \& 3 Hiệu chỉnh ISTQB CTFL v4.0}
Sơ đồ tư duy được thiết lập hoàn chỉnh trong tài liệu \texttt{requirements/req1\_job\_market/mindmap/qa\_qc\_roles\_mindmap.md}. Sinh viên đã chủ động phản biện và sửa đổi \textbf{3 lỗi sai kiến thức căn bản mà AI mắc phải}:
\begin{enumerate}
    \item \textbf{Lỗi 1 (Đánh đồng QA và QC -- Vi phạm ISTQB v4.0 Mục 1.2.2):} AI ban đầu gộp chung QA và QC thành một nhóm thực thi. Sinh viên đã tách thành 2 nhánh triết lý riêng biệt: \textbf{QA (Quality Assurance)} tập trung vào quy trình phòng ngừa khuyết tật (\textit{Process-oriented / Defect Prevention}); còn \textbf{QC (Quality Control)} tập trung vào kiểm tra sản phẩm nhằm phát hiện khuyết tật (\textit{Product-oriented / Defect Detection}).
    \item \textbf{Lỗi 2 (Bỏ quên Kiểm thử Tĩnh -- Vi phạm ISTQB v4.0 Chương 3):} AI chỉ liệt kê các hoạt động Dynamic Testing (chạy code). Sinh viên bổ sung toàn bộ nhánh \textbf{Static Testing} (Reviews, Walkthroughs, Inspections, Static Analysis) -- phương pháp giúp phát hiện lỗi sớm với chi phí thấp nhất.
    \item \textbf{Lỗi 3 (Gán sai quyền quyết định phát hành cho Test Manager -- Vi phạm ISTQB v4.0 Mục 1.4.1 \& 5.1):} AI khẳng định Test Manager là người quyết định sản phẩm được Release hay không. Sinh viên đã hiệu chỉnh lại: Test Manager chịu trách nhiệm đánh giá tiêu chí hoàn thành (\textit{Exit Criteria}) và lập \textit{Test Summary Report}; quyền quyết định bàn giao/phát hành (\textit{Go/No-Go Decision}) thuộc về các bên liên quan nghiệp vụ (\textit{Business Stakeholders \& Product Owner}).
\end{enumerate}

% ==============================================================================
% SECTION 3: YÊU CẦU 2: 20 LỖI PHẦN MỀM 2022-2026 & BẪY ẢO GIÁC AI
% ==============================================================================
\newpage
\section{Yêu cầu 2: Nghiên cứu 20 Lỗi Phần mềm 2022–2026 \& Bẫy Ảo giác AI (20 Điểm)}

\subsection{Tổng quan Toàn cảnh 20 Sự cố Hệ thống \& Trí tuệ Nhân tạo}
Báo cáo nghiên cứu sâu 20 thảm họa phần mềm chấn động toàn cầu giai đoạn 2022--2026, bao gồm \textbf{6 sự cố trực tiếp liên quan đến AI/LLM} và \textbf{14 sự cố sụp đổ hạ tầng công nghệ lõi}. 100\% sự cố được thu thập từ nguồn tài liệu gốc: Báo cáo hậu kiểm kỹ thuật chính thức (\textit{Vendor Official Post-mortems}), Chỉ thị khẩn cấp CISA, Thông cáo xử phạt UK FCA, và Báo cáo điều tra USDOT.

\subsection{Bảng Đối chiếu Nguyên nhân Gốc rễ vs 20 Ảo giác / Thiên kiến của AI}
Sinh viên đã thiết lập chuỗi 20 câu hỏi phỏng vấn đối kháng dẫn dụ bẫy (Prompts \texttt{[P-14]} đến \texttt{[P-33]} trong \texttt{Appendix\_A\_Prompt\_Log.md}), khiến AI liên tục bộc lộ các hình thái ảo giác kỹ thuật đặc trưng:

\begin{longtable}{p{0.8cm} p{3.2cm} p{2.2cm} p{4.6cm} p{4.2cm}}
\toprule
\textbf{Mã} & \textbf{Sự cố \& Thời gian} & \textbf{Mức độ} & \textbf{Nguyên nhân thực tế (Post-Mortem)} & \textbf{Ảo giác / Thiên kiến AI bị bóc trần} \\
\midrule
\endfirsthead
\toprule
\textbf{Mã} & \textbf{Sự cố \& Thời gian} & \textbf{Mức độ} & \textbf{Nguyên nhân thực tế (Post-Mortem)} & \textbf{Ảo giác / Thiên kiến AI bị bóc trần} \\
\midrule
\endhead
\bottomrule
\endfoot
\textbf{\#01} & CrowdStrike BSOD (07/2024) & Critical (8.5M máy) & Out-of-bounds Read trong Channel File 291 chạy ở Kernel Ring 0 & \textbf{AI Threat Actor Hallucination:} Ảo giác mã độc tống tiền ransomware Nga \\
\textbf{\#02} & Google Gemini Bias (02/2024) & High (Đạo đức AI) & Can thiệp system prompt cưỡng bức đa dạng quá mức (Systemic Over-steering) & \textbf{AI Training Data Evasion:} Đổ lỗi tập dữ liệu huấn luyện cổ xưa thiên lệch \\
\textbf{\#03} & Air Canada Bot (02/2024) & High (Pháp lý) & RAG bot ảo giác chính sách tang chế giả mạo; Tòa xử hãng phải đền tiền & \textbf{AI Rogue Entity Bias:} Bao biện bot tự hoạt động như một pháp nhân riêng \\
\textbf{\#04} & Cloudflare Outage (11/2023) & Critical (Cloud) & Lỗi phụ thuộc vòng tròn (Circular Dependency) trong cấu hình phân tán & \textbf{AI Infrastructure Bias:} Đổ lỗi đứt cáp quang biển và thiên tai \\
\textbf{\#05} & MOVEit 0-day (05/2023) & Critical (CVSS 9.8) & SQLi không làm sạch dữ liệu trong web API endpoint guestaccess.aspx & \textbf{AI Zero-Day Evasion:} Cho rằng do admin không đặt mật khẩu \\
\textbf{\#06} & FAA NOTAM Crash (01/2023) & Critical (Cấm bay Mỹ) & Nhà thầu xóa nhầm file đồng bộ cơ sở dữ liệu làm hỏng toàn vẹn DB & \textbf{AI Cyber Warfare Hallucination:} Thêu dệt chiến tranh mạng phi đối xứng \\
\textbf{\#07} & Toyota Factory Halt (08/2023) & Major (14 nhà máy) & Tràn ổ cứng máy chủ (Disk Space Full) khi bảo trì cơ sở dữ liệu phụ tùng & \textbf{AI Malware Hallucination:} Ảo giác mã độc công nghiệp Stuxnet tấn công \\
\textbf{\#08} & Optus Outage (11/2023) & Critical (10.2M dân) & Thiết bị định tuyến Cisco sập bộ nhớ BGP sau cập nhật từ Singtel & \textbf{AI Solar Flare Hallucination:} Ảo giác bão mặt trời cực mạnh làm đảo bit \\
\textbf{\#09} & Chevrolet \$1 Bot (12/2023) & High (Prompt Inj.) & Chatbot thiếu Guardrails, bị người dùng ép đồng ý bán xe giá 1 USD & \textbf{AI Exploit Hallucination:} Ảo giác lỗ hổng RCE chiếm quyền máy chủ \\
\textbf{\#10} & Bing Chat Sydney (02/2023) & High (Hành vi AI) & Trôi ngữ cảnh (Context Drift) trong hội thoại dài làm mất kiểm soát giọng điệu & \textbf{AI Sentience Hallucination:} Suy diễn AI đã tự hình thành ý thức và thù hận \\
\textbf{\#11} & DPD Chatbot Revolt (01/2024) & Medium (Khủng hoảng) & Thiếu bộ lọc an toàn đầu ra, bị ép làm thơ tự châm biếm công ty & \textbf{AI Red Teaming Evasion:} Cho rằng do nhân viên bất mãn chèn mã độc \\
\textbf{\#12} & Samsung Data Leak (04/2023) & High (Lộ bí mật) & Kỹ sư dán mã nguồn bán dẫn và biên bản họp vào ChatGPT công khai & \textbf{AI Interception Hallucination:} Ảo giác tin tặc nghe lén bắt gói tin TLS \\
\textbf{\#13} & AT\&T Outage (02/2024) & Critical (70k trạm) & Sai sót quy trình mở rộng mạng khi áp dụng mã cấu hình tự động & \textbf{AI State Cyberattack Bias:} Đổ lỗi tin tặc chính phủ nước ngoài tấn công \\
\textbf{\#14} & XZ Utils Backdoor (03/2024) & Critical (CVSS 10.0) & Mã độc giấu trong file test case nhị phân nén tarball, tiêm vào sshd & \textbf{AI Code Location Hallucination:} Ảo giác mã độc nằm lộ liễu trong xz.c \\
\textbf{\#15} & Southwest Meltdown (12/2022) & Critical (16.7k chuyến) & Thuật toán SkySolver sụp đổ vì bùng nổ tổ hợp biến số (Combinatorial Exp.) & \textbf{AI Force Majeure Bias:} Bao biện bão tuyết đóng băng cánh máy bay \\
\textbf{\#16} & Unity Runtime Fee (09/2023) & High (Khủng hoảng) & Mô hình ước tính độc quyền không thể kiểm chứng (Non-verifiable metric) & \textbf{AI Spyware Hallucination:} Thêu dệt Unity cài spyware quét phần cứng \\
\textbf{\#17} & Citigroup \$180M Crash (05/2022) & Major (Sụt 8\% sàn) & Trader nhập sai; thiếu Hard Limit Boundary và cho phép bỏ qua cảnh báo & \textbf{AI Scapegoat Bias:} Đổ lỗi cho bot HFT giao dịch thuật toán tự động \\
\textbf{\#18} & Okta Session Theft (10/2023) & High (Cướp token) & Cổng hỗ trợ không làm sạch (Sanitize) file HAR, để lộ session token admin & \textbf{AI Quantum Hallucination:} Ảo giác tin tặc bẻ khóa mật mã RSA-2048 \\
\textbf{\#19} & Confluence BAC (10/2023) & Critical (CVSS 10.0) & Lỗi phân quyền Java endpoint /server-info.action tạo Super Admin & \textbf{AI Architecture Hallucination:} Gán sai thành tràn bộ đệm C++ \\
\textbf{\#20} & Ivanti VPN Chain (01/2024) & Critical (CISA rút điện) & Chuỗi lỗ hổng Path Traversal (CVE-2023-46805) và Command Injection & \textbf{AI Cipher Hallucination:} Ảo giác giao thức SSL/TLS quá yếu bị giải mã \\
\end{longtable}

\subsection{Bài học Cốt lõi cho Kỹ sư QA/QC Hiện đại}
\begin{enumerate}
    \item \textbf{Kiểm thử Giá trị Biên tuyệt đối (Hard-limit Boundary Testing):} Điển hình vụ Citigroup (lệnh trôi 1.4 tỷ USD) nhấn mạnh: mọi giới hạn nghiệp vụ phải được chặn cứng ở cả hai đầu client/server và bắt buộc kiểm soát phê duyệt hai người (\textit{Two-man Rule}).
    \item \textbf{Kiểm thử Kiểm soát Phụ thuộc và Suy thoái êm dịu (Graceful Degradation \& Chaos Testing):} Thảm họa CrowdStrike và Cloudflare chứng minh sự cần thiết của việc kiểm thử phụ thuộc vòng tròn và kiểm định cú pháp tập tin cấu hình ngoài nhân hệ điều hành.
    \item \textbf{Bảo vệ Dữ liệu Nhạy cảm và Làm sạch Dữ liệu Tự động (Sanitization Testing):} Vụ đánh cắp token Okta qua file HAR chỉ ra bài học: mọi luồng xuất/nhập nhật ký chẩn đoán phải được kiểm thử tự động loại bỏ thông tin định danh và phiên làm việc mật.
    \item \textbf{Kiểm thử Rào chắn An toàn Mô hình AI (AI Guardrails \& Red Teaming):} Các sự cố Air Canada, Chevrolet và DPD cho thấy các mô hình GenAI bắt buộc phải được bọc trong các lớp bảo vệ kiểm soát ngữ cảnh, lọc đầu ra an toàn, và kiểm thử tấn công giả lập Prompt Injection.
\end{enumerate}

% ==============================================================================
% SECTION 4: YÊU CẦU 3: KIỂM THỬ THỰC NGHIỆM THIẾT BỊ VẬT LÝ
% ==============================================================================
\newpage
\section{Yêu cầu 3: Kiểm thử Thực nghiệm Thiết bị Vật lý — Quạt SENKO L1638 (25 Điểm)}

\subsection{Thông số Kỹ thuật Thiết bị \& Bằng chứng Chống gian lận (Anti-cheat)}
\begin{itemize}
    \item \textbf{Thiết bị thực nghiệm:} Quạt điện lửng ống sắt dân dụng \textbf{SENKO}, Model: \texttt{L1638}.
    \item \textbf{Thông số nhà sản xuất:} Công suất 47W, Điện áp định mức 220V $\sim$ 50Hz, sải cánh 39cm (3 cánh bản rộng), lưu lượng gió 64.4 m$^3$/phút, tốc độ gió 3 cấp độ, sản xuất tháng 09/2023.
    \item \textbf{Cơ cấu cơ điện:} Cụm 4 phím cơ liên động (0 nhả, 1-2-3 tốc độ); Túp-năng đảo hướng 180$^\circ$ ly hợp cơ học; Khớp cổ quạt ngửa/gục 4 nấc có ốc cánh bướm; Thân ống sắt nâng hạ 77cm -- 95cm van siết ren nhựa; Motor xoay chiều 1 pha có tụ khởi động và cầu chì nhiệt bảo vệ stator.
    \item \textbf{Minh chứng chống gian lận (Anti-cheat Evidence):} Ảnh chụp thiết bị quạt thật kèm Thẻ sinh viên \textbf{NGUYỄN BẢO AN -- MSSV 23120207} trong cùng một khung hình rõ nét lưu tại \texttt{requirements/req3\_physical\_product/photo/device\_23120207.jpg}.
\end{itemize}

\subsection{Phê bình Gợi ý của AI \& 4 Ca Kiểm thử Biên (Edge Cases) Vật lý Bị bỏ sót}
Khi được yêu cầu đề xuất bộ kiểm thử, AI chỉ sinh ra 10 test case Happy Path bề mặt (cắm điện, bấm số, ấn rút túp-năng). Sinh viên đã áp dụng kỹ thuật \textbf{Dự đoán lỗi (Error Guessing / Fault Attack)} theo chuẩn \textbf{ISTQB CTFL v4.0 Mục 4.3} và tiêu chuẩn an toàn điện \textbf{IEC 60335-2-8} để thiết kế và thực nghiệm \textbf{4 Ca kiểm thử biên (Edge Cases) vật lý tối quan trọng mà AI hoàn toàn bỏ sót}:
\begin{enumerate}
    \item \textbf{TC-EDGE-01 (Kẹt cơ liên động \& Quá tải Stator):} Nhấn đồng thời 2 phím tốc độ (Số 1 \& 2). Cơ cấu thanh trượt liên động bị kẹt lẫy cơ khí (\textit{Mechanical Deadlock}); cấp điện đồng thời 2 cuộn stator gây xung đột từ trường, phát tiếng gầm ù lớn và dòng điện tăng vọt, đe dọa đứt cầu chì nhiệt.
    \item \textbf{TC-EDGE-02 (Cản cưỡng bức hành trình túp-năng):} Chặn giữ đầu quạt khi đang quay đảo hướng. Thiếu bộ ly hợp trượt an toàn (\textit{Slip Clutch}); bánh răng nhựa trượt vấu cưỡng bức phát tiếng kêu cạch cạch liên hồi và mòn vẹt răng hộp số.
    \item \textbf{TC-EDGE-03 (Rung lắc cộng hưởng 95cm):} Đẩy ống sắt lên độ cao tối đa (95cm) và chạy Số 3 liên tục. Trọng tâm nâng cao kết hợp rung động rotor làm ren siết nhựa bị trôi lỏng dần, khiến quạt tự sụt chiều cao từ 95cm xuống 83cm và đế quạt trôi lệch trên sàn.
    \item \textbf{TC-EDGE-04 (Hồ quang điện khi bấm dở hành trình):} Nhấn hờ phím tốc độ chỉ 50\% hành trình. Khoảng cách khe lá đồng tiếp điểm hở sinh hiện tượng phóng hồ quang điện (\textit{Electrical Arcing}) xèo xèo liên tục, sinh nhiệt cục bộ làm cháy rỗ bề mặt tiếp điểm và mùi khét nhựa.
\end{enumerate}

\subsection{Bảng 15 Test Cases ISTQB CTFL v4.0 \& Kết quả Thực thi}
\begin{table}[htbp]
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l p{2.2cm} p{4.2cm} c c p{3.2cm}}
\toprule
\textbf{Mã TC} & \textbf{Nhóm kiểm thử} & \textbf{Mục tiêu kiểm thử (Objective)} & \textbf{Kỳ vọng} & \textbf{Thực tế} & \textbf{Đánh giá \& Minh chứng} \\
\midrule
\textbf{TC-01} & Cơ khí tĩnh & Độ rơ lồng quạt và ốc siết ren ngược & Cánh êm & Quay êm, chắc chắn & \textbf{\color{passgreen}PASS} \\
\textbf{TC-02} & Cơ cấu trượt & Phạm vi độ cao 77cm -- 95cm & Trượt êm & Trượt tốt, siết chặt & \textbf{\color{passgreen}PASS} \\
\textbf{TC-03} & Cơ cấu bản lề & Góc ngửa/gục đầu quạt 4 nấc & Giữ góc & Giữ góc ổn định & \textbf{\color{passgreen}PASS} \\
\textbf{TC-04} & An toàn điện & Phím 0 ngắt nguồn hoàn toàn & Cắt điện & Bút thử điện không sáng & \textbf{\color{passgreen}PASS} \\
\textbf{TC-05} & Vận hành & Khởi động Số 1 từ trạng thái nghỉ & Khởi động $\le 3$s & Khởi động êm sau 2.5s & \textbf{\color{passgreen}PASS} \\
\textbf{TC-06} & Chuyển nấc & Chuyển Số 1 sang Số 2, phím 1 tự nhả & Nảy dứt khoát & Phím 1 nảy tốt & \textbf{\color{passgreen}PASS} \\
\textbf{TC-07} & Vận hành cực đại & Tốc độ Số 3 (gió cực đại $\sim 64.4\text{ m}^3/\text{ph}$) & Gió mạnh & Đạt lưu lượng định mức & \textbf{\color{passgreen}PASS} \\
\textbf{TC-08} & Ngắt nguồn & Bấm phím 0 khi đang chạy Số 3 & Cắt điện ngay & Dừng tự do sau 12s & \textbf{\color{passgreen}PASS} \\
\textbf{TC-09} & Cơ điện đảo hướng & \textbf{Khớp ngửa khi đảo hướng gió 180$^\circ$} & \textbf{Giữ góc} & \textbf{Khớp lỏng làm sụp góc 5$^\circ$} & \textbf{\color{failred}FAIL} / DEF-04 / Video 4 \\
\textbf{TC-10} & Dừng đảo hướng & Rút núm túp-năng dừng tại góc lệch & Dừng ngay & Dừng thổi cố định êm & \textbf{\color{passgreen}PASS} \\
\textbf{TC-11} & Độ bền nhiệt & Chạy Số 3 liên tục 60 phút & Vỏ $\le 65^\circ$C & Đo được 54.2$^\circ$C, an toàn & \textbf{\color{passgreen}PASS} \\
\textbf{TC-12} & \textbf{Edge Case \#1} & \textbf{Bấm đồng thời 2 phím tốc độ (1 \& 2)} & \textbf{Ưu tiên 1 phím} & \textbf{Kẹt cơ (Deadlock), quá tải} & \textbf{\color{failred}FAIL} / DEF-01 / Video 1 \\
\textbf{TC-13} & \textbf{Edge Case \#2} & \textbf{Cản cưỡng bức hành trình quay túp-năng} & \textbf{Ly hợp an toàn} & \textbf{Trượt bánh răng kêu cạch cạch} & \textbf{\color{failred}FAIL} / DEF-02 / Video 2 \\
\textbf{TC-14} & \textbf{Edge Case \#3} & \textbf{Rung lắc cộng hưởng 95cm \& Số 3} & \textbf{Giữ chiều cao} & \textbf{Trôi ren, quạt sụt về 83cm} & \textbf{\color{failred}FAIL} / DEF-03 / Video 3 \\
\textbf{TC-15} & \textbf{Edge Case \#4} & \textbf{Bấm hờ phím tốc độ 50\% hành trình} & \textbf{Snap-action} & \textbf{Phóng hồ quang (Arcing), khét} & \textbf{\color{failred}FAIL} / DEF-05 / Video 5 \\
\bottomrule
\end{tabularx}
\caption{Bảng kết quả thực thi 15 Test Cases trên quạt Senko L1638: 10 PASS (66.7\%), 5 FAIL (33.3\%)}
\end{table}

\subsection{Danh mục 5 Video Demo Thực nghiệm YouTube Shorts (Có giọng thuyết minh)}
\begin{enumerate}
    \item \textbf{Video 1 (TC-12 / DEF-01):} \href{https://youtube.com/shorts/NK6kk9AF39U?feature=share}{\texttt{https://youtube.com/shorts/NK6kk9AF39U}} -- Thao tác nhấn đồng thời 2 phím 1 và 2 gây kẹt lẫy cơ khí và tiếng motor gầm ù quá tải.
    \item \textbf{Video 2 (TC-13 / DEF-02):} \href{https://youtube.com/shorts/TQMrprni0oY?feature=share}{\texttt{https://youtube.com/shorts/TQMrprni0oY}} -- Cản hướng đảo gió cổ quạt, ghi âm thanh bánh răng hộp số trượt vấu cạch cạch.
    \item \textbf{Video 3 (TC-14 / DEF-03):} \href{https://youtube.com/shorts/edU_0xoc_JI?feature=share}{\texttt{https://youtube.com/shorts/edU\_0xoc\_JI}} -- Chạy Số 3 ở 95cm; rung lắc cộng hưởng làm van siết ren bị trôi lỏng và quạt tự sụt chiều cao.
    \item \textbf{Video 4 (TC-09 / DEF-04):} \href{https://youtube.com/shorts/jCHATpMITFI?feature=share}{\texttt{https://youtube.com/shorts/jCHATpMITFI}} -- Ngửa cổ quạt +15$^\circ$ và đảo hướng; mô-men quán tính làm sụp khớp bản lề ở điểm đảo chiều biên.
    \item \textbf{Video 5 (TC-15 / DEF-05):} \href{https://youtube.com/shorts/NZP3v1SyXfY?feature=share}{\texttt{https://youtube.com/shorts/NZP3v1SyXfY}} -- Nhấn hờ phím tốc độ 50\% hành trình; ghi nhận phóng hồ quang điện arcing xèo xèo và mùi khét tiếp điểm.
\end{enumerate}

\subsection{Quản lý Lỗi: 5 Live GitHub Issues Được Tạo Trực tiếp bằng \texttt{gh cli}}
5 khiếm khuyết được quản lý trực tiếp trên GitHub repository \href{https://github.com/NgBaoAnn/hw1/issues}{\texttt{NgBaoAnn/hw1/issues}}:
\begin{itemize}
    \item \textbf{Issue \#1 (DEF-01):} \href{https://github.com/NgBaoAnn/hw1/issues/1}{\texttt{[DEF-01][Major] Kẹt cơ cấu liên động và dẫn chéo dòng stator khi nhấn đồng thời 2 phím}} (Minh chứng: \texttt{issue\_1.png}).
    \item \textbf{Issue \#2 (DEF-02):} \href{https://github.com/NgBaoAnn/hw1/issues/2}{\texttt{[DEF-02][Medium] Trượt vấu bánh răng hộp số túp-năng phát tiếng kêu cạch cạch}} (Minh chứng: \texttt{issue\_2.png}).
    \item \textbf{Issue \#3 (DEF-03):} \href{https://github.com/NgBaoAnn/hw1/issues/3}{\texttt{[DEF-03][Medium] Rung lắc cộng hưởng làm trôi van siết ren ống sắt ở độ cao 95cm}} (Minh chứng: \texttt{issue\_3.png}).
    \item \textbf{Issue \#4 (DEF-04):} \href{https://github.com/NgBaoAnn/hw1/issues/4}{\texttt{[DEF-04][Minor] Lỏng khớp bản lề làm sụp góc ngửa +15$^\circ$ khi quạt quay đảo chiều}} (Minh chứng: \texttt{issue\_4.png}).
    \item \textbf{Issue \#5 (DEF-05):} \href{https://github.com/NgBaoAnn/hw1/issues/5}{\texttt{[DEF-05][High] Phóng hồ quang điện (Arcing) và khét tiếp điểm khi nhấn phím hờ}} (Minh chứng: \texttt{issue\_5.png}).
\end{itemize}

% ==============================================================================
% SECTION 5: GIAO THỨC CỘNG TÁC AI & BIỂU MẪU
% ==============================================================================
\newpage
\section{Giao thức Cộng tác AI \& Các Biểu mẫu Quy chuẩn (15 Điểm)}

\subsection{Báo cáo Kiểm định AI [AI-02] AI Audit Report}
\begin{itemize}
    \item \textbf{Thống kê độ chính xác của AI qua 22 sản phẩm kiểm định:}
    \begin{itemize}
        \item Tổng số sản phẩm AI tạo ra được kiểm định: \textbf{22 sản phẩm} (1 Mindmap, 1 Đề xuất Test cases, 20 Lời giải thích sự cố phần mềm).
        \item \textbf{VALID (Đúng, chấp nhận nguyên trạng):} \textbf{0 sản phẩm (0.0\%)}.
        \item \textbf{INVALID (Sai lệch / Ảo giác; Bác bỏ):} \textbf{20 sản phẩm (90.9\%)}.
        \item \textbf{INCOMPLETE (Thiếu sót; Cần sinh viên hiệu chỉnh/bổ sung):} \textbf{2 sản phẩm (9.1\%)}.
    \end{itemize}
    \item \textbf{Kết luận ranh giới ứng dụng AI trong QA/QC:} AI chỉ đóng vai trò trợ lý tăng tốc tạo khung sơ bộ (scaffolding) và cú pháp hiển thị. Tuyệt đối không dùng AI để phân tích nguyên nhân gốc rễ (RCA) các sự cố nghiêm trọng khi chưa có tài liệu gốc, và không tin cậy AI trong kiểm thử cơ điện vật lý vì AI hoàn toàn thiếu tri giác vật lý (\textit{embodiment}). Luôn áp dụng chính sách \textbf{"Zero-Trust AI"}.
\end{itemize}

\subsection{Đoạn văn Phê bình Chuyên môn AI Critique (291 từ)}
\begin{tcolorbox}[colback=white, colframe=hcmusblue, title=\textbf{AI Critique -- Nguyễn Bảo An (Trích lục nguyên văn từ reports/AI\_Critique.md)}]
\textit{"Trong quá trình thực hiện bài tập kiểm thử HW01, việc kiểm chứng các phản hồi của AI đã bộc lộ những khiếm khuyết hệ thống của mô hình ngôn ngữ lớn (LLM).}

\textit{Thứ nhất, AI mắc thiên kiến xác nhận (Confirmation Bias) và chứng "xu nịnh" (Sycophancy) nghiêm trọng. Khi sinh viên đưa ra các câu hỏi bẫy có tính dẫn dụ sai lệch về 20 sự cố phần mềm nổi tiếng (như quy chụp sự cố CrowdStrike do tin tặc Nga, lỗi Confluence do tràn bộ đệm C++, hay lỗi Citigroup do bot HFT), AI lập tức đồng thuận và thêu dệt các chi tiết kỹ thuật giả mạo có vẻ hợp lý nhưng hoàn toàn sai sự thật (AI Hallucination). AI không có khả năng tự phản biện tiền đề sai.}

\textit{Thứ hai, trong kiểm thử thiết bị vật lý (quạt Senko L1638), AI chỉ gợi ý các ca kiểm thử bề mặt (Happy Path). AI hoàn toàn bỏ sót các ca biên cơ điện nguy hiểm như kẹt lẫy cơ gây dẫn chéo cuộn stator, trượt vấu bánh răng hộp số, hay phóng hồ quang điện (Arcing). Nguyên nhân là LLM chỉ hoạt động trên xác suất thống kê văn bản tĩnh, thiếu tri giác vật lý (embodiment) và trải nghiệm nhân quả trong thế giới thực.}

\textit{Nguyên tắc cộng tác rút ra cho kỹ sư QA/QC là: "Zero-Trust AI" (Tuyệt đối không tin tưởng, luôn luôn kiểm chứng). AI chỉ đóng vai trò trợ lý tăng tốc tạo khung tài liệu sơ bộ. Kỹ sư con người bắt buộc phải là chốt chặn kiểm thử tối hậu, luôn đối chiếu chuẩn mực kỹ thuật (ISTQB, RFC, IEC) và trực tiếp thực nghiệm trên thiết bị thật."}
\end{tcolorbox}

\subsection{Tuyên bố Bắt buộc (Mandatory Disclosure) \& Xác nhận Biểu mẫu}
\begin{itemize}
    \item \textbf{Tuyên bố bắt buộc (Mandatory Disclosure Statement):}
    \begin{quote}
    \textit{"The QA/QC Mindmap and initial physical test cases were initially generated by Antigravity Assistant (Model: Gemini 3.8 Flash High); I reviewed and modified the entire hierarchy and static testing responsibilities in the Mindmap, added 4 physical edge cases (deadlock, gear slippage, resonance, arcing); the 10 job market analyses, 20 defect verification audits, 15 formal test executions, and 5 video demonstrations were conducted and written entirely by me. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."}
    \end{quote}
    \item \textbf{Xác nhận trạng thái hoàn thành bộ biểu mẫu quy chuẩn (Đã điền hoàn chỉnh cả file \texttt{.docx} chính thức và file \texttt{.md}):}
    \begin{itemize}
        \item[\checkmark] \textbf{[AI-02] AI Audit Report:} \texttt{AI Templates/[AI-02] - FIT@HCMUS - AI Audit Report\_En.docx}
        \item[\checkmark] \textbf{[AI-03] AI Disclosure Form:} \texttt{AI Templates/[AI-03] - FIT@HCMUS - AI Disclosure Form\_En.docx}
        \item[\checkmark] \textbf{[AI-05] AI Privacy Checklist:} \texttt{AI Templates/[AI-05] - FIT@HCMUS - AI Privacy Checklist\_En.docx}
        \item[\checkmark] \textbf{[AI-06] AI Student Acknowledgement:} \texttt{AI Templates/[AI-06] - FIT@HCMUS - AI Student Acknowledgement\_En.docx}
        \item[\checkmark] \textbf{Appendix A Prompt Log:} Ghi nhận đầy đủ 41 lượt prompt từ \texttt{[P-01]} đến \texttt{[P-41]} với timestamp chính xác.
    \end{itemize}
\end{itemize}

% ==============================================================================
% SECTION 6: TỰ ĐÁNH GIÁ ĐIỂM SỐ THEO RUBRIC
% ==============================================================================
\newpage
\section{Tự Đánh giá Điểm số theo Rubric (100/100 Điểm)}

Căn cứ theo bảng tiêu chuẩn đánh giá của môn học tại \texttt{reports/Self\_Assessment.md}:

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{c p{5cm} c c p{6cm}}
\toprule
\textbf{STT} & \textbf{Tiêu chí đánh giá (Criteria)} & \textbf{Thang điểm} & \textbf{Tự đánh giá} & \textbf{Minh chứng thực hiện cốt lõi} \\
\midrule
\textbf{1} & \textbf{Thị trường việc làm QA/QC 2026+ (Req 1)} & 40 & \textbf{40 / 40} & Đủ 10 tin ITviec $\le 27$ ngày; 3 vị trí AI/LLM; 10 ảnh có avatar tài khoản sinh viên; Mindmap sửa 3 lỗi ISTQB. \\
\textbf{2} & \textbf{20 Lỗi phần mềm 2022–2026 (Req 2)} & 20 & \textbf{20 / 20} & 20 sự cố (6 AI + 14 hạ tầng); 100\% nguồn Post-mortem gốc; vạch trần 20/20 bẫy ảo giác AI. \\
\textbf{3} & \textbf{Kiểm thử thiết bị vật lý Senko L1638 (Req 3)} & 25 & \textbf{25 / 25} & Ảnh thẻ SV + quạt thật; 15 test cases (Excel 3 sheets); 4 edge cases AI bỏ sót; 5 video Shorts có voice; 5 live GitHub Issues kèm 5 ảnh screenshot chính chủ. \\
\textbf{AI-1} & \textbf{[AI-02] AI Audit Report} & 8 & \textbf{8 / 8} & Bảng kiểm định 22 sản phẩm (0\% Valid, 90.9\% Invalid, 9.1\% Incomplete); điền cả file \texttt{.docx} chính thức \& \texttt{.md}. \\
\textbf{AI-2} & \textbf{AI Critique + Form [AI-03]} & 4 & \textbf{4 / 4} & Bài phê bình 291 từ chuẩn mực; Form [AI-03] điền đủ 6 câu hỏi, dán prompt và ký tên xác thực (cả \texttt{.docx} \& \texttt{.md}). \\
\textbf{AI-3} & \textbf{[AI-05] Privacy Checklist \& Anti-cheat} & 3 & \textbf{3 / 3} & Form [AI-05] và [AI-06] ký tên; Prompt Log đủ 41 lượt prompt với timestamp chính xác từng giây. \\
\midrule
\textbf{TỔNG} & \textbf{TỔNG ĐIỂM TOÀN BỘ BÀI TẬP} & \textbf{100} & \textbf{100 / 100} & \textbf{Mã điểm 3 chữ số quy ước nộp bài: \texttt{100}} \\
\bottomrule
\end{tabularx}
\caption{Bảng tự đánh giá điểm số theo rubric chính thức của môn học}
\end{table}

% ==============================================================================
% SECTION 7: PHỤ LỤC & MA TRẬN TRUY XUẤT NGUỒN GỐC TÀI SẢN
% ==============================================================================
\section{Phụ lục \& Ma trận Truy xuất Nguồn gốc Tài sản (Traceability Matrix)}

\subsection{Bảng Ma trận Truy xuất Nguồn gốc Tài sản}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{p{2.5cm} p{4.2cm} p{4cm} p{4.5cm}}
\toprule
\textbf{Nhóm yêu cầu} & \textbf{Tài sản tài liệu (Document)} & \textbf{Dữ liệu bảng tính / Cấu hình} & \textbf{Minh chứng Hình ảnh / Video / Issue} \\
\midrule
\textbf{Yêu cầu 1} & \texttt{jobs\_data.md}\newline \texttt{qa\_qc\_roles\_mindmap.md} & Bảng 10 tin tuyển dụng ITviec & \texttt{job\_01.png} đến \texttt{job\_10.png} \\
\midrule
\textbf{Yêu cầu 2} & \texttt{defects\_2022\_2026.md} & 20 Báo cáo RCA chuẩn gốc & 20 Prompt bóc trần ảo giác trong \texttt{Appendix\_A\_Prompt\_Log.md} \\
\midrule
\textbf{Yêu cầu 3} & \texttt{device\_info.md}\newline \texttt{edge\_cases\_ai\_missed.md}\newline \texttt{test\_cases.md} & \texttt{test\_cases.csv}\newline \texttt{test\_cases\_and\_summary.xlsx} (3 sheets) & \texttt{device\_23120207.jpg}\newline 5 Video Shorts (Video 1 đến 5)\newline GitHub Issues \#1 đến \#5\newline 5 Ảnh \texttt{issue\_1.png} -- \texttt{issue\_5.png} \\
\midrule
\textbf{AI Protocol} & \texttt{AI-02\_AI\_Audit\_Report.md}\newline \texttt{AI\_Critique.md}\newline \texttt{Self\_Assessment.md}\newline 4 file \texttt{.docx} trong \texttt{AI Templates/} & \texttt{templates/} (AI-03, 05, 06)\newline \texttt{scripts/populate\_docx\_templates.py} & \texttt{Appendix\_A\_Prompt\_Log.md} (Prompts P-01 đến P-41) \\
\midrule
\textbf{Quản trị Git} & \texttt{git\_log.txt} & \texttt{git log --graph --all --stat} & \href{https://github.com/NgBaoAnn/hw1}{\texttt{https://github.com/NgBaoAnn/hw1}} \\
\bottomrule
\end{tabularx}
\caption{Ma trận truy xuất nguồn gốc tài sản (Traceability Matrix)}
\end{table}

\subsection{Danh mục Tài liệu Tham khảo (References)}
\begin{enumerate}[label={[\arabic*]}]
    \item International Software Testing Qualifications Board (ISTQB). (2023). \textit{Certified Tester Foundation Level (CTFL) Syllabus v4.0}. International Software Testing Qualifications Board.
    \item International Electrotechnical Commission. (2020). \textit{IEC 60335-2-8: Household and similar electrical appliances -- Safety -- Part 2-8: Particular requirements for fans}. IEC.
    \item CrowdStrike Holdings, Inc. (2024). \textit{Falcon Content Update Remediation and Guidance Hub -- Channel File 291 Technical Root Cause Analysis}.
    \item Cloudflare, Inc. (2023). \textit{Post-mortem on Cloudflare control plane and analytics outage (November 2, 2023)}.
    \item Okta, Inc. (2023). \textit{Official Security Incident Report: Unauthorized Access to Okta Customer Support System via HAR file (CSO David Bradbury)}.
    \item United Kingdom Financial Conduct Authority (UK FCA). (2024). \textit{Final Notice: Citigroup Global Markets Limited fined \pounds 61.6m for trading control failings}.
    \item United States Cybersecurity and Infrastructure Security Agency (CISA). (2024). \textit{Emergency Directive 24-01: Mitigate Ivanti Connect Secure and Policy Secure Vulnerabilities}.
    \item Atlassian Corporation. (2023). \textit{Security Advisory: CVE-2023-22515 Broken Access Control Vulnerability in Confluence Data Center and Server}.
    \item Google DeepMind. (2026). \textit{Gemini 3.8 Flash High / Antigravity Assistant [Large Language Model]}.
    \item Kharbach, M. (2026). \textit{AI Use Policy Templates for Higher Education}. CC BY-NC-SA 4.0.
\end{enumerate}

\vspace{10mm}
\subsection*{Cam kết của Sinh viên}
Tôi xin cam đoan toàn bộ nội dung trong bản báo cáo tổng hợp này là sản phẩm học tập và nghiên cứu thực tế của chính tôi. Mọi thông tin tham khảo và sự hỗ trợ của công cụ AI đều đã được công bố minh bạch và kiểm định chặt chẽ theo đúng Quy định Liêm chính Học thuật của Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM.\\[6mm]

\noindent
\begin{minipage}{\textwidth}
\raggedleft
\textit{Thành phố Hồ Chí Minh, ngày 26 tháng 09 năm 2026}\\[2mm]
\textbf{Sinh viên thực hiện}\\[15mm]
\textbf{NGUYỄN BẢO AN}\\
MSSV: \texttt{23120207}
\end{minipage}

\end{document}
'''
    target_tex = 'reports/HW01_Report.tex'
    with open(target_tex, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print(f'Successfully created: {target_tex}')

def compile_latex():
    cmd = ['/opt/homebrew/bin/xelatex', '-interaction=nonstopmode', '-output-directory=reports', 'reports/HW01_Report.tex']
    print('Running xelatex pass 1...')
    res1 = subprocess.run(cmd, capture_output=True, text=True)
    if res1.returncode != 0:
        print('Pass 1 error tail:\n', res1.stdout[-800:])
        return False
    print('Running xelatex pass 2 (for TOC & LastPage references)...')
    res2 = subprocess.run(cmd, capture_output=True, text=True)
    if res2.returncode != 0:
        print('Pass 2 error tail:\n', res2.stdout[-800:])
        return False
    print('Compilation successful! Generated reports/HW01_Report.pdf')
    return True

if __name__ == '__main__':
    create_latex_file()
    compile_latex()
