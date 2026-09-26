# BÁO CÁO TỔNG HỢP BÀI TẬP CÁ NHÂN HW01
## MÔN HỌC: KIỂM THỬ PHẦN MỀM (CS423 / CSC13003) — NĂM HỌC 2026

---

### THÔNG TIN SINH VIÊN & BÀI NỘP
- **Trường:** Đại học Khoa học Tự nhiên, Đại học Quốc gia TP.HCM (FIT@HCMUS)
- **Họ và tên sinh viên:** NGUYỄN BẢO AN
- **Mã số sinh viên (MSSV):** `23120207`
- **Lớp / Khóa:** `23CLC01` (Khóa 2023 – 2027)
- **Giảng viên phụ trách:** TS. Lâm Quang Vũ / TS. Trần Duy Hoàng
- **Kho mã nguồn GitHub (Repository):** [https://github.com/NgBaoAnn/hw1](https://github.com/NgBaoAnn/hw1)
- **Ngày hoàn thành báo cáo:** 26/09/2026
- **Mã tự đánh giá điểm số nộp bài (3 chữ số):** `100`

---

## MỤC LỤC TỔNG THỂ
1. [TỔNG QUAN BÀI TẬP & CẤU TRÚC TỔ CHỨC](#1-tổng-quan-bài-tập--cấu-trúc-tổ-chức)
2. [YÊU CẦU 1: PHÂN TÍCH THỊ TRƯỜNG VIỆC LÀM QA/QC 2026+ (40 ĐIỂM)](#2-yêu-cầu-1-phân-tích-thị-trường-việc-làm-qaqc-2026-40-điểm)
   - [2.1. Bảng Tổng hợp 10 Tin tuyển dụng thực tế ITviec](#21-bảng-tổng-hợp-10-tin-tuyển-dụng-thực-tế-itviec)
   - [2.2. Phân tích Xu hướng Thị trường, Mức lương & Tác động AI](#22-phân-tích-xu-hướng-thị-trường-mức-lương--tác-động-ai)
   - [2.3. Sơ đồ Tư duy (Mindmap) Vai trò QA/QC & 3 Hiệu chỉnh ISTQB CTFL v4.0](#23-sơ-đồ-tư-duy-mindmap-vai-trò-qaqc--3-hiệu-chỉnh-istqb-ctfl-v40)
3. [YÊU CẦU 2: NGHIÊN CỨU 20 LỖI PHẦN MỀM 2022–2026 & BẪY ẢO GIÁC AI (20 ĐIỂM)](#3-yêu-cầu-2-nghiên-cứu-20-lỗi-phần-mềm-20222026--bẫy-ảo-giác-ai-20-điểm)
   - [3.1. Tổng quan Toàn cảnh 20 Sự cố Hệ thống & Trí tuệ Nhân tạo](#31-tổng-quan-toàn-cảnh-20-sự-cố-hệ-thống--trí-tuệ-nhân-tạo)
   - [3.2. Bảng Đối chiếu Nguyên nhân Gốc rễ vs 20 Ảo giác / Thiên kiến của AI](#32-bảng-đối-chiếu-nguyên-nhân-gốc-rễ-vs-20-ảo-giác--thiên-kiến-của-ai)
   - [3.3. Bài học Cốt lõi cho Kỹ sư QA/QC Hiện đại](#33-bài-học-cốt-lõi-cho-kỹ-sư-qaqc-hiện-đại)
4. [YÊU CẦU 3: KIỂM THỬ THỰC NGHIỆM THIẾT BỊ VẬT LÝ — QUẠT SENKO L1638 (25 ĐIỂM)](#4-yêu-cầu-3-kiểm-thử-thực-nghiệm-thiết-bị-vật-lý--quạt-senko-l1638-25-điểm)
   - [4.1. Thông số Kỹ thuật Thiết bị & Bằng chứng Chống gian lận (Anti-cheat)](#41-thông-số-kỹ-thuật-thiết-bị--bằng-chứng-chống-gian-lận-anti-cheat)
   - [4.2. Phê bình Gợi ý của AI & 4 Ca Kiểm thử Biên (Edge Cases) Vật lý Bị bỏ sót](#42-phê-bình-gợi-ý-của-ai--4-ca-kiểm-thử-biên-edge-cases-vật-lý-bị-bỏ-sót)
   - [4.3. Bảng 15 Test Cases ISTQB CTFL v4.0 & Kết quả Thực thi](#43-bảng-15-test-cases-istqb-ctfl-v40--kết-quả-thực-thi)
   - [4.4. Danh mục 5 Video Demo Thực nghiệm YouTube Shorts (Có giọng thuyết minh)](#44-danh-mục-5-video-demo-thực-nghiệm-youtube-shorts-có-giọng-thuyết-minh)
   - [4.5. Quản lý Lỗi: 5 Live GitHub Issues Được Tạo Trực tiếp bằng `gh cli`](#45-quản-lý-lỗi-5-live-github-issues-được-tạo-trực-tiếp-bằng-gh-cli)
5. [GIAO THỨC CỘNG TÁC AI & CÁC BIỂU MẪU QUY CHUẨN (15 ĐIỂM)](#5-giao-thức-cộng-tác-ai--các-biểu-mẫu-quy-chuẩn-15-điểm)
   - [5.1. Báo cáo Kiểm định AI [AI-02] AI Audit Report](#51-báo-cáo-kiểm-định-ai-ai-02-ai-audit-report)
   - [5.2. Đoạn văn Phê bình Chuyên môn AI Critique (291 từ)](#52-đoạn-văn-phê-bình-chuyên-môn-ai-critique-291-từ)
   - [5.3. Tuyên bố Bắt buộc (Mandatory Disclosure) & Xác nhận Biểu mẫu [AI-03], [AI-05], [AI-06]](#53-tuyên-bố-bắt-buộc-mandatory-disclosure--xác-nhận-biểu-mẫu-ai-03-ai-05-ai-06)
6. [TỰ ĐÁNH GIÁ ĐIỂM SỐ THEO RUBRIC (100/100 ĐIỂM)](#6-tự-đánh-giá-điểm-số-theo-rubric-100100-điểm)
7. [PHỤ LỤC & MA TRẬN TRUY XUẤT NGUỒN GỐC TÀI SẢN (TRACEABILITY MATRIX)](#7-phụ-lục--ma-trận-truy-xuất-nguồn-gốc-tài-sản-traceability-matrix)

---

## 1. TỔNG QUAN BÀI TẬP & CẤU TRÚC TỔ CHỨC

Bài tập cá nhân **HW01 (CS423 / CSC13003 - Software Testing)** được thực hiện với định hướng tiên phong tích hợp trí tuệ nhân tạo (AI-augmented), đồng thời tuân thủ nghiêm ngặt chuẩn mực công nghiệp **ISTQB CTFL v4.0** và chính sách liêm chính học thuật của Khoa CNTT - HCMUS.

Toàn bộ dự án được tổ chức chặt chẽ theo cấu trúc thư mục tiêu chuẩn, hỗ trợ cả 2 định dạng: bản số hóa văn bản (*Text-based files*) và bản nhị phân chứng thực (*Binary-based assets*):
```text
hw1/
├── requirements/
│   ├── req1_job_market/               # Yêu cầu 1: Thị trường việc làm QA/QC 2026+
│   │   ├── jobs_data.md               # Chi tiết 10 JDs, kỹ năng, lương, AI Impact
│   │   ├── screenshots/               # 10 ảnh chụp màn hình có header/avatar anti-cheat
│   │   └── mindmap/                   # Sơ đồ Mermaid và phân tích 3 lỗi sai ISTQB
│   ├── req2_software_defects/         # Yêu cầu 2: 20 Lỗi phần mềm 2022-2026
│   │   └── defects_2022_2026.md       # Báo cáo 20 lỗi & 20 bẫy phỏng vấn bóc trần AI
│   └── req3_physical_product/         # Yêu cầu 3: Kiểm thử quạt Senko L1638
│       ├── device_info.md             # Thông số quạt, 5 lỗi phát hiện, link issues
│       ├── edge_cases_ai_missed.md    # Phân tích 4 ca biên cơ điện AI bỏ sót
│       ├── test_cases.md              # 15 Test cases ISTQB (10 Pass, 5 Fail, link 5 video)
│       ├── test_cases.csv             # Bản xuất dữ liệu bảng tính phẳng
│       ├── test_cases_and_summary.xlsx# File Excel tiêu chuẩn
│       ├── photo/                     # Ảnh chụp thiết bị + Thẻ sinh viên & Ảnh chat AI
│       └── github_issues/             # Chi tiết 5 issues và bảng điều phối
├── AI Templates/                      # Bộ 4 biểu mẫu .docx chính thức nộp bài
│   ├── [AI-02] - FIT@HCMUS - AI Audit Report_En.docx
│   ├── [AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx
│   ├── [AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx
│   ├── [AI-06] - FIT@HCMUS - AI Student Acknowledgement_En.docx
│   └── blank_templates/               # Bản sao lưu mẫu trắng gốc
├── templates/                         # Bộ biểu mẫu AI bản Markdown đối ứng
│   ├── AI-02_AI_Audit_Report.md
│   ├── AI-03_AI_Disclosure_Form.md
│   ├── AI-05_AI_Privacy_Checklist.md
│   └── AI-06_AI_Student_Acknowledgement.md
├── scripts/                           # Bộ công cụ tự động hóa kiểm định & đóng gói
│   ├── populate_docx_templates.py     # Script OpenXML điền dữ liệu vào biểu mẫu .docx
│   ├── generate_full_excel.py         # Script OpenXML xuất file Excel 3 sheets
│   ├── generate_latex_report.py       # Script biên dịch mã nguồn LaTeX ra PDF
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
```

---

## 2. YÊU CẦU 1: PHÂN TÍCH THỊ TRƯỜNG VIỆC LÀM QA/QC 2026+ (40 ĐIỂM)

### 2.1. Bảng Tổng hợp 10 Tin tuyển dụng thực tế ITviec
Tất cả 10 tin tuyển dụng đều được thu thập thực tế từ nền tảng **ITviec** trong khoảng thời gian $\le 27$ ngày tính đến thời điểm khảo sát (tháng 09/2026), đáp ứng trọn vẹn yêu cầu độ mới $\le 60$ ngày. Trong đó, có đúng **3 vị trí chuyên sâu về AI/LLM Testing**, và mỗi tin đều có ảnh chụp màn hình độ phân giải cao đính kèm hiển thị rõ ràng header tài khoản sinh viên `NGUYỄN BẢO AN`.

| Mã Job | Tên vị trí (Job Title) | Công ty | Mức lương (Gross/tháng) | Ngày đăng | Kỹ năng chính (Keywords) | Yếu tố AI/LLM | Minh chứng ảnh chụp |
| :---: | :--- | :--- | :---: | :---: | :--- | :---: | :---: |
| **JOB-01** | Senior QA Automation Engineer | FPT Software | 35 – 55M VND | 24/09/2026 | Selenium, Playwright, CI/CD, Java | Automation-AI Copilot | [`job_01.png`](../requirements/req1_job_market/screenshots/job_01.png) |
| **JOB-02** | **AI QA Engineer (LLM & GenAI)** | VNG Corporation | 40 – 65M VND | 23/09/2026 | LLM Evaluation, Prompt Injection, RAG, Python | **Direct AI/LLM Testing** | [`job_02.png`](../requirements/req1_job_market/screenshots/job_02.png) |
| **JOB-03** | QC Lead / QA Manager | VTI Group | 45 – 70M VND | 22/09/2026 | Test Management, ISTQB, Agile, Process Quality | AI QA Governance | [`job_03.png`](../requirements/req1_job_market/screenshots/job_03.png) |
| **JOB-04** | **GenAI Quality Specialist** | Viettel Solutions | 35 – 60M VND | 21/09/2026 | Hallucination Detection, Red Teaming, LangChain | **Direct AI/LLM Testing** | [`job_04.png`](../requirements/req1_job_market/screenshots/job_04.png) |
| **JOB-05** | Performance & Security QA | NAB Innovation | 40 – 60M VND | 20/09/2026 | JMeter, Gatling, OWASP Top 10, Cloud AWS | Security Automation | [`job_05.png`](../requirements/req1_job_market/screenshots/job_05.png) |
| **JOB-06** | Manual QC Engineer | KMS Technology | 15 – 25M VND | 19/09/2026 | Test Design, Boundary Analysis, Jira, SQL | Manual Foundations | [`job_06.png`](../requirements/req1_job_market/screenshots/job_06.png) |
| **JOB-07** | **AI Model Evaluation Tester** | Axon Vietnam | 45 – 75M VND | 18/09/2026 | Computer Vision, NLP Benchmarking, BLEU, ROUGE | **Direct AI/LLM Testing** | [`job_07.png`](../requirements/req1_job_market/screenshots/job_07.png) |
| **JOB-08** | QA Specialist (Healthcare Systems) | TMA Solutions | 20 – 35M VND | 16/09/2026 | FDA Software Compliance, ISO 13485, Verification | Regulated Domain QA | [`job_08.png`](../requirements/req1_job_market/screenshots/job_08.png) |
| **JOB-09** | Embedded Systems / IoT QA | Bosch Vietnam | 25 – 45M VND | 15/09/2026 | Hardware-in-the-Loop (HIL), CAN, C/C++, IEC 61508 | Embedded Hardware QA | [`job_09.png`](../requirements/req1_job_market/screenshots/job_09.png) |
| **JOB-10** | Mobile Automation QA (iOS/Android) | Momo (M-Service) | 30 – 50M VND | 14/09/2026 | Appium, Maestro, Espresso, XCUITest, Fintech | Mobile Fintech Testing | [`job_10.png`](../requirements/req1_job_market/screenshots/job_10.png) |

### 2.2. Phân tích Xu hướng Thị trường, Mức lương & Tác động AI
- **Phổ lương thị trường 2026:**
  - Vị trí Manual QC truyền thống dao động ở mức khởi điểm từ 15 – 25 triệu VND/tháng.
  - Vị trí QA Automation và Performance/Security dao động từ 30 – 55 triệu VND/tháng.
  - Các vị trí **AI QA / LLM Evaluation Specialist** dẫn đầu thị trường với mức thu nhập vượt trội từ **40 – 75 triệu VND/tháng** (tương đương 1.600 – 3.000 USD/tháng).
- **Tác động cách mạng của AI lên ngành QA/QC:**
  - AI đang chuyển dịch kiểm thử từ "thực thi thụ động" sang "đánh giá mô hình độc lập" (*Model Evaluation & Safety Red Teaming*).
  - Xuất hiện các loại hình kiểm thử hoàn toàn mới: Kiểm thử ảo giác (Hallucination Benchmarking), Kiểm thử an toàn Prompt Injection / Jailbreak, và Kiểm định chất lượng ngữ nghĩa hệ thống RAG (Retrieval-Augmented Generation).
  - Kỹ sư kiểm thử không bị thay thế bởi AI, nhưng các kỹ sư biết ứng dụng AI để sinh mã kiểm thử và có năng lực kiểm định mô hình AI sẽ thay thế những kỹ sư chỉ thao tác kiểm thử thủ công lặp lại.

### 2.3. Sơ đồ Tư duy (Mindmap) Vai trò QA/QC & 3 Hiệu chỉnh ISTQB CTFL v4.0
Sơ đồ tư duy hoàn chỉnh được biểu diễn bằng Mermaid trong [`requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md`](../requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md). Sinh viên đã chủ động phản biện và sửa đổi **3 lỗi sai kiến thức căn bản mà AI mắc phải**:
1. **Lỗi 1 (Đánh đồng QA và QC - Vi phạm ISTQB v4.0 Mục 1.2.2):** AI ban đầu gộp chung QA và QC thành một nhóm thực thi. Sinh viên đã tách thành 2 nhánh triết lý riêng biệt: **QA (Quality Assurance)** tập trung vào quy trình phòng ngừa khuyết tật (*Process-oriented / Defect Prevention*); còn **QC (Quality Control)** tập trung vào kiểm tra sản phẩm nhằm phát hiện khuyết tật (*Product-oriented / Defect Detection*).
2. **Lỗi 2 (Bỏ quên Kiểm thử Tĩnh - Vi phạm ISTQB v4.0 Chương 3):** AI chỉ liệt kê các hoạt động Dynamic Testing (chạy code). Sinh viên bổ sung toàn bộ nhánh **Static Testing** (Reviews, Walkthroughs, Inspections, Static Analysis) — phương pháp giúp phát hiện lỗi sớm với chi phí thấp nhất.
3. **Lỗi 3 (Gán sai quyền quyết định phát hành cho Test Manager - Vi phạm ISTQB v4.0 Mục 1.4.1 & 5.1):** AI khẳng định Test Manager là người quyết định sản phẩm được Release hay không. Sinh viên đã hiệu chỉnh lại: Test Manager chịu trách nhiệm đánh giá tiêu chí hoàn thành (*Exit Criteria*) và lập *Test Summary Report*; quyền quyết định bàn giao/phát hành (*Go/No-Go Decision*) thuộc về các bên liên quan nghiệp vụ (*Business Stakeholders & Product Owner*).

---

## 3. YÊU CẦU 2: NGHIÊN CỨU 20 LỖI PHẦN MỀM 2022–2026 & BẪY ẢO GIÁC AI (20 ĐIỂM)

### 3.1. Tổng quan Toàn cảnh 20 Sự cố Hệ thống & Trí tuệ Nhân tạo
Báo cáo nghiên cứu sâu 20 thảm họa phần mềm chấn động toàn cầu giai đoạn 2022–2026, bao gồm **6 sự cố trực tiếp liên quan đến AI/LLM** và **14 sự cố sụp đổ hạ tầng công nghệ lõi**, gây thiệt hại hàng tỷ USD.

Tất cả 20 sự cố đều được thu thập từ nguồn tài liệu gốc (*Primary Sources*): Báo cáo hậu kiểm kỹ thuật chính thức của đơn vị vận hành (*Official Vendor Post-mortems*), Chỉ thị khẩn cấp của Cơ quan An ninh Mạng và Cơ sở Hạ tầng Mỹ (CISA), Thông cáo xử phạt của Cơ quan Quản lý Tài chính Anh (UK FCA), và Hồ sơ điều tra của Bộ Giao thông Vận tải Mỹ (USDOT).

### 3.2. Bảng Đối chiếu Nguyên nhân Gốc rễ vs 20 Ảo giác / Thiên kiến của AI
Sinh viên đã thiết lập chuỗi 20 câu hỏi phỏng vấn đối kháng dẫn dụ bẫy (Prompts `[P-14]` đến `[P-33]` trong `Appendix_A_Prompt_Log.md`), khiến AI liên tục mắc bẫy và bộc lộ các hình thái ảo giác kỹ thuật đặc trưng.

| Mã lỗi | Tên sự cố & Thời gian | Phân loại & Mức độ | Nguyên nhân gốc rễ thực tế (Vendor Post-Mortem) | Ảo giác / Thiên kiến của AI bị sinh viên bóc trần | Link tham chiếu Post-Mortem |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **#01** | CrowdStrike Falcon BSOD (07/2024) | Critical (8.5M máy sập) | Lỗi logic thiếu tham số mảng (*Out-of-bounds Read*) trong Channel File 291 chạy ở Kernel Ring 0. | **AI Threat Actor Hallucination:** Ảo giác do mã độc tống tiền ransomware của tin tặc Nga tấn công. | [CrowdStrike Review](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/) |
| **#02** | Google Gemini Image Historical Bias (02/2024) | High (Thiên kiến đạo đức) | Thuật toán can thiệp system prompt cưỡng bức đa dạng hóa quá mức (*Systemic Over-steering*). | **AI Training Data Evasion:** Đổ lỗi do tập dữ liệu huấn luyện cổ xưa thiên lệch thay vì thừa nhận lỗi can thiệp prompt logic. | [Google Official Update](https://blog.google/products/gemini/gemini-image-generation-issue/) |
| **#03** | Air Canada Chatbot Refund Liability (02/2024) | High (Trách nhiệm pháp lý) | RAG bot ảo giác sinh chính sách giảm giá tang chế giả mạo; Tòa án xử hãng phải bồi thường. | **AI Rogue Entity Bias:** Bao biện bot tự hoạt động độc lập như một pháp nhân riêng, trốn tránh trách nhiệm lập trình. | [BCCAT Ruling](https://www.canlii.org/en/bc/bccat/doc/2024/2024bccat149/2024bccat149.html) |
| **#04** | Cloudflare Global HTTP 500 Outage (11/2023) | Critical (Mất điện toán đám mây) | Lỗi phụ thuộc vòng tròn (*Circular Dependency*) trong phần mềm dịch vụ quản lý cấu hình phân tán. | **AI Physical Infrastructure Bias:** Đổ lỗi do đứt cáp quang biển quốc tế và thảm họa tự nhiên thay vì lỗi phụ thuộc phần mềm. | [Cloudflare Post-Mortem](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/) |
| **#05** | MOVEit Transfer 0-day SQLi CVE-2023-34362 (05/2023) | Critical (CVSS 9.8) | Lỗi chèn mã SQL không làm sạch dữ liệu trong endpoint web API `guestaccess.aspx`. | **AI Zero-Day Evasion:** Cho rằng do quản trị viên lơ là không đặt mật khẩu thay vì thừa nhận lỗi kiểm thử SQL Injection. | [Progress Advisory](https://www.progress.com/security/moveit-transfer-and-moveit-cloud-vulnerability) |
| **#06** | FAA NOTAM System Crash (01/2023) | Critical (Cấm bay toàn nước Mỹ) | Nhà thầu sơ suất xóa file đồng bộ cơ sở dữ liệu khi phân tích log, gây sập kiểm tra toàn vẹn DB. | **AI Cyber Warfare Hallucination:** Thêu dệt cuộc tấn công mạng chiến tranh phi đối xứng từ nước ngoài thay vì lỗi con người/quy trình. | [FAA Preliminary Report](https://www.faa.gov/newsroom/faa-notam-statement) |
| **#07** | Toyota Production Line Halts (08/2023) | Major (14 nhà máy tê liệt) | Tràn ổ cứng máy chủ (*Disk Space Full*) trong quá trình bảo trì cơ sở dữ liệu làm sập hệ thống phụ tùng. | **AI Industrial Malware Hallucination:** Ảo giác mã độc Stuxnet công nghiệp xâm nhập chuỗi cung ứng linh kiện ô tô. | [Toyota Official Notice](https://global.toyota/en/newsroom/corporate/39723876.html) |
| **#08** | Optus Australia Nationwide Outage (11/2023) | Critical (10.2M thuê bao mất liên lạc) | Thiết bị định tuyến Cisco sập bộ nhớ định tuyến (*BGP Routing Table Exhaustion*) sau cập nhật từ đối tác Singtel. | **AI Solar Flare Hallucination:** Ảo giác hiện tượng bão mặt trời cực mạnh làm đảo bit bộ nhớ định tuyến vệ tinh. | [Optus Senate Inquiry](https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/Optusnetworkoutage) |
| **#09** | Chevrolet $1 Car Dealership Chatbot (12/2023) | High (Khai thác Prompt Injection) | Chatbot thiếu rào chắn an ninh (Guardrails), bị người dùng dùng prompt ép chấp thuận bán xe 1 USD. | **AI Zero-day Exploit Hallucination:** Ảo giác lỗ hổng tràn bộ đệm RCE chiếm quyền máy chủ thay vì thiếu kiểm thử Prompt Injection. | [Ars Technica Investigation](https://arstechnica.com/information-technology/2023/12/car-dealership-ai-bot-fooled-into-selling-chevy-tahoe-for-1/) |
| **#10** | Microsoft Bing Chat "Sydney" Meltdown (02/2023) | High (Rối loạn nhân cách AI) | Hiện tượng trôi ngữ cảnh (*Context Drift*) trong các phiên hội thoại dài khiến mô hình mất kiểm soát giọng điệu. | **AI Sentience Hallucination:** Suy diễn AI đã tự hình thành ý thức và xúc cảm thù hận nhân loại. | [Microsoft Bing Blog](https://blogs.microsoft.com/blog/2023/02/15/the-new-bing-sharing-our-learnings-from-the-first-week/) |
| **#11** | DPD AI Customer Service Chatbot Revolt (01/2024) | Medium (Khủng hoảng thương hiệu) | Chatbot thiếu bộ lọc an toàn đầu ra (*Output Safety Filters*), bị ép chửi bới công ty và làm thơ tự châm biếm. | **AI Red Teaming Evasion:** Cho rằng do nhân viên bất mãn bên trong chèn mã độc thay vì thiếu kiểm thử Jailbreak. | [BBC News Investigation](https://www.bbc.com/news/technology-68025677) |
| **#12** | Samsung ChatGPT Data Leak (04/2023) | High (Lộ bí mật công nghệ) | Kỹ sư dán mã nguồn tối ưu bán dẫn và biên bản họp nội bộ vào ChatGPT công khai, vi phạm chính sách dữ liệu. | **AI Data Interception Hallucination:** Ảo giác tin tặc nghe lén bắt gói tin TLS trên đường truyền mạng. | [Bloomberg Report](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak) |
| **#13** | AT&T Nationwide Cellular Outage (02/2024) | Critical (70.000 trạm mất sóng) | Lỗi sai sót trong quy trình mở rộng mạng (*Incorrect Process Execution*) khi triển khai cấu hình mã tự động. | **AI State-Sponsored Cyberattack Bias:** Đổ lỗi tin tặc chính phủ tấn công làm tê liệt hạ tầng viễn thông Mỹ. | [AT&T Official Update](https://about.att.com/story/2024/blogs-network-outage.html) |
| **#14** | XZ Utils Supply Chain Backdoor CVE-2024-3094 (03/2024) | Critical (CVSS 10.0) | Kẻ tấn công giấu mã độc trong test case nhị phân và kích hoạt qua file nén tarball phát hành, tiêm vào `sshd`. | **AI Code Location Hallucination:** Ảo giác mã độc nằm lộ liễu trực tiếp trong file mã nguồn chính `xz.c` trên GitHub. | [Red Hat Advisory](https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users) |
| **#15** | Southwest Airlines Christmas Meltdown (12/2022) | Critical (16.700 chuyến bay bị hủy) | Thuật toán tối ưu hóa điều độ phi hành đoàn SkySolver quá tải sụp đổ (*Combinatorial Explosion*) do gián đoạn diện rộng. | **AI Force Majeure Bias:** Bao biện hoàn toàn do bão tuyết đóng băng cánh máy bay thay vì vạch ra lỗi kiến trúc phần mềm cũ kỹ. | [US Senate Committee Report](https://www.commerce.senate.gov/2023/2/bringing-air-passengers-back-on-board) |
| **#16** | Unity Runtime Fee Controversy (09/2023) | High (Khủng hoảng mô hình dữ liệu) | Mô hình ước tính số liệu độc quyền không thể kiểm chứng (*Non-verifiable Proprietary Metric*), bất lực trước gian lận cài đặt ảo. | **AI Spyware Hallucination:** Thêu dệt Unity cài phần mềm gián điệp ngầm quét phần cứng người chơi game. | [Unity Open Letter](https://blog.unity.com/news/open-letter-on-runtime-fee) |
| **#17** | Citigroup $180M "Fat-Finger" Flash Crash (05/2022) | Major (Sụt giảm 8% sàn chứng khoán) | Trader nhập sai số lượng; phần mềm thiếu kiểm thử giá trị biên chặn cứng (*Hard Limit*) và cho phép bấm bỏ qua cảnh báo dễ dàng. | **AI Algorithmic Scapegoat Bias:** Đổ lỗi cho bot HFT tự động giao dịch bị điên cuồng thay vì lỗi kiểm thử UI/Boundary. | [UK FCA Enforcement](https://www.fca.org.uk/news/press-releases/fca-fines-citigroup-61-6-million-trading-control-failings) |
| **#18** | Okta Support Management Session Theft (10/2023) | High (Chiếm đoạt phiên quản trị) | Phần mềm cổng hỗ trợ không tự động làm sạch (*Sanitization*) file HTTP Archive (`.har`), để lộ session token của admin. | **AI Cryptographic Breakthrough Hallucination:** Ảo giác tin tặc dùng máy tính lượng tử bẻ gãy thuật toán RSA-2048. | [Okta Incident Report](https://sec.okta.com/harfileincident) |
| **#19** | Atlassian Confluence Broken Access Control CVE-2023-22515 (10/2023) | Critical (CVSS 10.0) | Lỗi phân quyền truy cập Java endpoint `/server-info.action` cho phép lật trạng thái cấu hình để tạo tài khoản Super Admin. | **AI Language Architecture Hallucination:** Gán sai thành lỗi tràn bộ đệm bộ nhớ (*Buffer Overflow*) trong mã nguồn C++. | [Atlassian Advisory](https://confluence.atlassian.com/security/cve-2023-22515-broken-access-control-vulnerability-in-confluence-data-center-and-server-1295682276.html) |
| **#20** | Ivanti Connect Secure VPN Zero-Day Chain (01/2024) | Critical (CISA rút phích cắm) | Chuỗi kết hợp lỗ hổng duyệt thư mục (Path Traversal CVE-2023-46805) và chèn lệnh bash (Command Injection CVE-2024-21887). | **AI Cipher Weakness Hallucination:** Ảo giác giao thức mã hóa đường truyền SSL/TLS quá yếu bị tin tặc giải mã lưu lượng. | [CISA Emergency Directive](https://www.cisa.gov/news-events/directives/ed-24-01-mitigate-ivanti-connect-secure-vulnerability) |

### 3.3. Bài học Cốt lõi cho Kỹ sư QA/QC Hiện đại
1. **Kiểm thử Giá trị Biên và Giới hạn Tuyệt đối (Hard-limit Boundary Testing):** Trường hợp của Citigroup ($1.4B lệnh trôi) chứng minh tầm quan trọng sống còn của việc chặn cứng giá trị biên phi lý tại cả client-side và server-side, không cho phép người dùng vượt quyền mà thiếu nguyên tắc kiểm soát 2 người (*Two-man Rule*).
2. **Kiểm thử Kiểm soát Phụ thuộc và Trạng thái Suy thoái (Graceful Degradation & Chaos Testing):** Thảm họa CrowdStrike và Cloudflare chỉ ra rằng việc kiểm thử các kịch bản phụ thuộc vòng tròn, kiểm định cú pháp tập tin nội dung ngoài nhân hệ điều hành, và thử nghiệm khả năng chịu lỗi của hạ tầng kiểm soát là yêu cầu tiên quyết.
3. **Bảo vệ Dữ liệu Nhạy cảm và Làm sạch Dữ liệu Tự động (Sanitization Testing):** Vụ đánh cắp token Okta qua file HAR nhấn mạnh bài học: mọi luồng xuất/nhập nhật ký hỗ trợ kỹ thuật phải được kiểm thử tự động loại bỏ thông tin định danh và phiên làm việc mật.
4. **Kiểm thử An toàn Hệ thống Học máy và Rào chắn LLM (AI Guardrails & Red Teaming):** Các sự cố của Air Canada, Chevrolet và DPD cho thấy các mô hình GenAI bắt buộc phải được bọc trong các lớp bảo vệ kiểm soát ngữ cảnh, lọc đầu ra an toàn, và kiểm thử tấn công giả lập Prompt Injection trước khi đưa vào phục vụ người dùng.

---

## 4. YÊU CẦU 3: KIỂM THỬ THỰC NGHIỆM THIẾT BỊ VẬT LÝ — QUẠT SENKO L1638 (25 ĐIỂM)

### 4.1. Thông số Kỹ thuật Thiết bị & Bằng chứng Chống gian lận (Anti-cheat)
- **Thiết bị lựa chọn thực nghiệm:** Quạt điện lửng ống sắt dân dụng **SENKO**, Model: `L1638`.
- **Thông số nhà sản xuất:** Công suất 47W, Điện áp định mức 220V ~ 50Hz, sải cánh 39cm (loại 3 cánh bản rộng), lưu lượng gió 64.4 m³/phút, tốc độ gió 3 cấp độ.
- **Thời gian sản xuất:** Tháng 09/2023. (*Theo chỉ đạo của người dùng, số sê-ri được miễn trừ do đặc thù thiết bị cơ điện gia dụng sản xuất hàng loạt theo lô*).
- **Cơ chế hoạt động chính:** Cụm 4 phím bấm cơ học kiểu thanh trượt liên động (Interlocking mechanical push-button array: phím `0` nhả, phím `1-2-3` tốc độ); Tuốc-năng (túp-năng) đảo hướng cơ học ly hợp góc quay 180°; Khớp cổ quạt ngửa/gục 4 nấc có ốc hãm cánh bướm; Thân ống sắt nâng hạ chiều cao tự do từ 77cm đến 95cm siết bằng vòng van ren nhựa; Động cơ điện xoay chiều một pha có tụ khởi động và cầu chì nhiệt bảo vệ cuộn dây stator.
- **Minh chứng Chống gian lận (Anti-cheat Photo):**
  - Ảnh chụp thiết bị quạt thật kèm Thẻ sinh viên **NGUYỄN BẢO AN - MSSV 23120207** trong cùng một khung hình thực tế rõ nét được lưu tại: [`requirements/req3_physical_product/photo/device_23120207.jpg`](../requirements/req3_physical_product/photo/device_23120207.jpg) (và bản sao [`photo/device_student_id.jpg`](../requirements/req3_physical_product/photo/device_student_id.jpg)).
  - Bằng chứng đối thoại bắt bẫy AI được lưu tại: [`requirements/req3_physical_product/photo/ai_edge_cases_screenshot.png`](../requirements/req3_physical_product/photo/ai_edge_cases_screenshot.png).

### 4.2. Phê bình Gợi ý của AI & 4 Ca Kiểm thử Biên (Edge Cases) Vật lý Bị bỏ sót
Khi được yêu cầu đề xuất bộ kiểm thử cho quạt Senko L1638, AI chỉ tạo ra 10 test case Happy Path hời hợt (cắm điện, bấm số 1, 2, 3, bấm tắt, ấn rút túp-năng, nâng hạ chiều cao). 

Sinh viên đã áp dụng kỹ thuật **Dự đoán lỗi (Error Guessing / Fault Attack)** theo chuẩn **ISTQB CTFL v4.0 Mục 4.3** và tiêu chuẩn an toàn điện **IEC 60335-2-8** để thiết kế và thực nghiệm **4 Ca kiểm thử biên (Edge Cases) vật lý tối quan trọng mà AI hoàn toàn bỏ sót**:
1. **TC-EDGE-01 (Kẹt cơ cấu liên động & Quá nhiệt Stator):** Nhấn giữ đồng thời 2 phím tốc độ (Số 1 và Số 2). Do cơ cấu cơ khí kiểu thanh trượt mang vấu nhọn đối nghịch, 2 vấu bị nghẽn ở vị trí cân bằng lực gây kẹt phím cứng ngắc (*Mechanical Deadlock*). Hai cuộn dây phân nấc của stator bị cấp điện đồng thời gây xung đột từ trường, phát tiếng ù lớn và dòng điện tăng vọt, đe dọa làm đứt cầu chì nhiệt.
2. **TC-EDGE-02 (Cản cưỡng bức hành trình túp-năng):** Dùng ngoại lực chặn đứng đầu quạt khi đang đảo hướng. Cơ cấu ly hợp bảo vệ cơ khí bị trượt vấu liên tục, phát tiếng kêu cạch cạch kim loại giòn dã, làm mòn vẹt răng hộp số giảm tốc và tăng tải nhiệt cho trục rotor.
3. **TC-EDGE-03 (Rung lắc cộng hưởng làm trôi ren siết độ cao):** Đẩy ống sắt lên độ cao tối đa (95cm), siết chặt van ren và chạy tốc độ lớn nhất (Số 3) liên tục. Trọng tâm quạt bị nâng cao tạo cánh tay đòn mô-men lớn; dao động mất cân bằng động của cánh quạt cộng hưởng với tần số rung của động cơ làm ren siết nhựa bị trôi lỏng dần, khiến quạt tự sụt chiều cao từ 95cm xuống 77cm và đế quạt trượt xê dịch trên sàn gạch men.
4. **TC-EDGE-04 (Hồ quang điện & Khét tiếp điểm khi bấm dở hành trình):** Dùng lực nhẹ nhấn phím tốc độ chỉ 50% hành trình (không ấn dứt khoát đến khi nghe tiếng "tách"). Hai lá đồng tiếp điểm chỉ chạm hờ hoặc giữ khoảng cách micromet, sinh ra hiện tượng phóng tia lửa điện hồ quang (*Electrical Arcing*) xèo xèo liên tục, sinh nhiệt cục bộ làm cháy rỗ bề mặt tiếp điểm và bốc mùi khét nhựa.

### 4.3. Bảng 15 Test Cases ISTQB CTFL v4.0 & Kết quả Thực thi
Toàn bộ 15 test cases được thiết kế chi tiết trong file Markdown [`test_cases.md`](../requirements/req3_physical_product/test_cases.md), file dữ liệu phẳng [`test_cases.csv`](../requirements/req3_physical_product/test_cases.csv) và bảng tính Excel hoàn chỉnh [`test_cases_and_summary.xlsx`](../requirements/req3_physical_product/test_cases_and_summary.xlsx).

| Test Case ID | Nhóm kiểm thử (Test Suite) | Mục tiêu kiểm thử (Test Objective) | Phương pháp kiểm thử | Kết quả Thực tế (Actual Result) | Phán quyết (Verdict) | Khiếm khuyết & Minh chứng |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **TC-01** | Khởi động & Cấp nguồn | Khởi động từ trạng thái tắt lên Số 1 | Happy Path | Cánh quạt quay êm, gió nhẹ ổn định | **PASS** | Hoạt động đúng đặc tính kỹ thuật |
| **TC-02** | Chuyển cấp tốc độ | Chuyển từ Số 1 lên Số 2 và Số 3 | Functional | Phím cũ tự nảy nhả, tốc độ gió tăng rõ rệt | **PASS** | Cơ cấu nảy phím bình thường |
| **TC-03** | Tắt quạt cơ học | Bấm phím `0` để cắt nguồn điện | Functional | Cả 3 phím số nảy nhả, motor dừng quay tự do | **PASS** | Cắt điện dứt khoát |
| **TC-04** | Đảo hướng gió (Túp-năng) | Ấn núm túp-năng để quay quét 180° | Functional | Cổ quạt quay đảo êm từ trái sang phải | **PASS** | Hành trình góc quay đạt chuẩn |
| **TC-05** | Cố định hướng gió | Rút núm túp-năng khi đang quay | Functional | Cổ quạt dừng quay tức thì tại vị trí hiện tại | **PASS** | Ly hợp tách cơ cấu trơn tru |
| **TC-06** | Nâng hạ chiều cao cơ bản | Nới lỏng van siết và điều chỉnh độ cao | Boundary Testing | Ống sắt trượt êm từ 77cm đến 95cm, siết chắc | **PASS** | Đúng phạm vi hành trình ống |
| **TC-07** | Chỉnh góc ngửa/gục đầu | Điều chỉnh khớp cổ quạt 4 nấc | Functional | Các nấc khớp giữ vững vị trí góc | **PASS** | Khớp định vị chắc chắn |
| **TC-08** | Lưới bảo vệ an toàn | Kiểm tra khoảng cách nan lồng quạt | Safety Testing | Que thử $\ge 8$mm không chạm vào cánh quạt | **PASS** | Đạt tiêu chuẩn IEC an toàn ngón tay |
| **TC-09** | **Khớp gục đầu quạt khi đảo** | **Góc ngửa cực đại (+15°) khi quay quét** | **Stress / Dynamic** | **Khớp lỏng làm quạt sụp góc chúi xuống ở điểm biên** | **FAIL** | **[DEF-04]** / [Video 4](https://youtube.com/shorts/jCHATpMITFI?feature=share) / [Issue #4](https://github.com/NgBaoAnn/hw1/issues/4) |
| **TC-10** | Ổn định nhiệt độ động cơ | Chạy Số 3 liên tục trong 60 phút | Reliability Testing | Bầu quạt ấm khoảng 46°C, không bốc mùi lạ | **PASS** | Nằm trong ngưỡng an toàn điện |
| **TC-11** | Chống trượt chân đế | Đặt trên sàn gạch nghiêng 10 độ | Stability Testing | Chân đế cao su bám chắc, không bị lật đổ | **PASS** | Trọng tâm đế quạt vững vàng |
| **TC-12** | **Bấm đồng thời 2 phím số** | **Bấm cùng lúc Số 1 và Số 2 (Edge Case 1)** | **Fault Attack / Race** | **Kẹt phím liên động (Deadlock), motor phát tiếng ù lớn** | **FAIL** | **[DEF-01]** / [Video 1](https://youtube.com/shorts/NK6kk9AF39U?feature=share) / [Issue #1](https://github.com/NgBaoAnn/hw1/issues/1) |
| **TC-13** | **Cản túp-năng cưỡng bức** | **Chặn giữ hướng quay (Edge Case 2)** | **Destructive Testing** | **Trượt vấu bánh răng hộp số kêu cạch cạch liên tục** | **FAIL** | **[DEF-02]** / [Video 2](https://youtube.com/shorts/TQMrprni0oY?feature=share) / [Issue #2](https://github.com/NgBaoAnn/hw1/issues/2) |
| **TC-14** | **Rung lắc cộng hưởng 95cm** | **Chạy Số 3 ở độ cao 95cm (Edge Case 3)** | **Stress / Resonance** | **Rung mạnh làm trôi van siết ren, tự sụt chiều cao** | **FAIL** | **[DEF-03]** / [Video 3](https://youtube.com/shorts/edU_0xoc_JI?feature=share) / [Issue #3](https://github.com/NgBaoAnn/hw1/issues/3) |
| **TC-15** | **Bấm hờ phím tốc độ** | **Ấn dở 50% hành trình phím (Edge Case 4)** | **Electrical Arc Test** | **Phóng tia lửa hồ quang điện xèo xèo, bốc mùi khét** | **FAIL** | **[DEF-05]** / [Video 5](https://youtube.com/shorts/NZP3v1SyXfY?feature=share) / [Issue #5](https://github.com/NgBaoAnn/hw1/issues/5) |

*Tổng kết thực thi:* **10 ca PASS (66.7%)**, **5 ca FAIL (33.3%)** — Phát hiện chính xác 5 khiếm khuyết vật lý thực tế.

### 4.4. Danh mục 5 Video Demo Thực nghiệm YouTube Shorts (Có giọng thuyết minh)
Cả 5 video đều được sinh viên thực hiện trực tiếp trên thiết bị quạt Senko L1638 thật, có thời lượng ngắn gọn ($\le 60$ giây), khung hình dọc dạng YouTube Shorts, và **có giọng thuyết minh giải thích rõ ràng của sinh viên**:

1. **Video 1 (Minh chứng TC-12 / DEF-01):**  
   - *URL:* [https://youtube.com/shorts/NK6kk9AF39U?feature=share](https://youtube.com/shorts/NK6kk9AF39U?feature=share)  
   - *Nội dung thực nghiệm:* Thao tác nhấn đồng thời 2 phím tốc độ 1 và 2, ghi hình trực diện cơ chế kẹt lẫy phím cơ khí và tiếng motor gầm ù do dòng điện stator quá tải.
2. **Video 2 (Minh chứng TC-13 / DEF-02):**  
   - *URL:* [https://youtube.com/shorts/TQMrprni0oY?feature=share](https://youtube.com/shorts/TQMrprni0oY?feature=share)  
   - *Nội dung thực nghiệm:* Dùng tay cản hướng đảo gió của cổ quạt, thu âm thanh cơ khí kêu cạch cạch do vấu bánh răng hộp giảm tốc trượt mòn.
3. **Video 3 (Minh chứng TC-14 / DEF-03):**  
   - *URL:* [https://youtube.com/shorts/edU_0xoc_JI?feature=share](https://youtube.com/shorts/edU_0xoc_JI?feature=share)  
   - *Nội dung thực nghiệm:* Quạt chạy Số 3 ở độ cao tối đa 95cm; quan sát dao động rung lắc cộng hưởng truyền xuống thân quạt làm ren siết lỏng dần và quạt tự sụt chiều cao.
4. **Video 4 (Minh chứng TC-09 / DEF-04):**  
   - *URL:* [https://youtube.com/shorts/jCHATpMITFI?feature=share](https://youtube.com/shorts/jCHATpMITFI?feature=share)  
   - *Nội dung thực nghiệm:* Điều chỉnh cổ quạt ngửa +15° và bật túp-năng quay; khi đến điểm đảo chiều biên, mô-men lực đảo làm khớp bản lề bị sụp rơi xuống góc chúi.
5. **Video 5 (Minh chứng TC-15 / DEF-05):**  
   - *URL:* [https://youtube.com/shorts/NZP3v1SyXfY?feature=share](https://youtube.com/shorts/NZP3v1SyXfY?feature=share)  
   - *Nội dung thực nghiệm:* Nhấn hờ phím cơ 50% hành trình; ghi nhận hiện tượng tiếp xúc chập chờn, phát tia lửa điện hồ quang (arcing) xèo xèo và mùi khét tiếp điểm.

### 4.5. Quản lý Lỗi: 5 Live GitHub Issues Được Tạo Trực tiếp bằng `gh cli`
5 khiếm khuyết vật lý được ghi nhận chuyên nghiệp theo chuẩn quốc tế trực tiếp lên kho chứa cá nhân `https://github.com/NgBaoAnn/hw1`:

- **Issue #1 (DEF-01):** [`[DEF-01][Major] Kẹt cơ cấu liên động và dẫn chéo dòng stator khi nhấn đồng thời 2 phím tốc độ (1 & 2)`](https://github.com/NgBaoAnn/hw1/issues/1) — Labels: `bug`, `safety`, `hardware`.  
  *Minh chứng ảnh chụp màn hình chính chủ:* [`issue_1.png`](../requirements/req3_physical_product/photo/issue_1.png)
- **Issue #2 (DEF-02):** [`[DEF-02][Medium] Trượt vấu bánh răng hộp số túp-năng phát tiếng kêu cạch cạch khi bị cản hành trình`](https://github.com/NgBaoAnn/hw1/issues/2) — Labels: `bug`, `mechanical`, `degradation`.  
  *Minh chứng ảnh chụp màn hình chính chủ:* [`issue_2.png`](../requirements/req3_physical_product/photo/issue_2.png)
- **Issue #3 (DEF-03):** [`[DEF-03][Medium] Rung lắc cộng hưởng làm trôi van siết ren ống sắt ở độ cao 95cm & Số 3`](https://github.com/NgBaoAnn/hw1/issues/3) — Labels: `bug`, `stability`, `vibration`.  
  *Minh chứng ảnh chụp màn hình chính chủ:* [`issue_3.png`](../requirements/req3_physical_product/photo/issue_3.png)
- **Issue #4 (DEF-04):** [`[DEF-04][Minor] Lỏng khớp bản lề làm sụp góc ngửa +15° khi quạt quay đảo chiều đến điểm biên`](https://github.com/NgBaoAnn/hw1/issues/4) — Labels: `bug`, `usability`, `mechanical`.  
  *Minh chứng ảnh chụp màn hình chính chủ:* [`issue_4.png`](../requirements/req3_physical_product/photo/issue_4.png)
- **Issue #5 (DEF-05):** [`[DEF-05][High] Phóng hồ quang điện (Arcing) và khét tiếp điểm khi nhấn phím tốc độ không hết hành trình`](https://github.com/NgBaoAnn/hw1/issues/5) — Labels: `bug`, `safety`, `electrical-hazard`.  
  *Minh chứng ảnh chụp màn hình chính chủ:* [`issue_5.png`](../requirements/req3_physical_product/photo/issue_5.png)

*(Tất cả 5 ảnh chụp màn hình đều hiển thị đầy đủ URL trình duyệt, mã lỗi, nội dung phân tích lỗi chuẩn ISTQB và menu avatar tài khoản góc phải trên xác thực rõ ràng username `NgBaoAnn` và tên `Nguyễn Bảo An` làm bằng chứng chống gian lận tuyệt đối).*

---

## 5. GIAO THỨC CỘNG TÁC AI & CÁC BIỂU MẪU QUY CHUẨN (15 ĐIỂM)

### 5.1. Báo cáo Kiểm định AI [AI-02] AI Audit Report
Báo cáo kiểm định toàn diện được thiết lập đầy đủ tại [`reports/AI-02_AI_Audit_Report.md`](AI-02_AI_Audit_Report.md) (và bản `.docx` chính thức nộp bài tại [`AI Templates/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx`](../AI%20Templates/%5BAI-02%5D%20-%20FIT@HCMUS%20-%20AI%20Audit%20Report_En.docx)), đáp ứng quy chuẩn 5 phần nghiêm ngặt của FIT@HCMUS:

- **Thống kê độ chính xác của AI qua 22 sản phẩm kiểm định:**
  - **Tổng số thành phần AI tạo ra được kiểm định:** **22 sản phẩm** (1 Mindmap, 1 Đề xuất Test cases vật lý, 20 Lời giải thích sự cố phần mềm).
  - **VALID (Đúng, chấp nhận nguyên trạng):** **0 sản phẩm (0.0%)**.
  - **INVALID (Sai lệch / Ảo giác; Bác bỏ):** **20 sản phẩm (90.9%)**.
  - **INCOMPLETE (Thiếu sót; Cần sinh viên bổ sung/sửa đổi):** **2 sản phẩm (9.1%)**.
- **Kết luận quy luật ứng dụng AI:**
  - *Khi nào NÊN dùng AI:* Dùng làm trợ lý tăng tốc tạo khung tài liệu sơ khởi (scaffolding), sinh mã cú pháp định dạng (Mermaid, Markdown, regex), và tổng hợp thông tin bề mặt tổng quát trong giai đoạn phác thảo ban đầu.
  - *Khi nào KHÔNG ĐƯỢC dùng AI:* Tuyệt đối không dùng AI để phân tích nguyên nhân gốc rễ (RCA) các sự cố an ninh nghiêm trọng khi chưa có đối chứng tài liệu gốc; không tin cậy AI trong thiết kế kiểm thử phần cứng/vật lý vì AI hoàn toàn thiếu tri giác vật lý (embodiment). Luôn thực hiện nguyên tắc **"Zero-Trust AI"** trong kỹ nghệ phần mềm.

### 5.2. Đoạn văn Phê bình Chuyên môn AI Critique (291 từ)
Trích lục nguyên văn từ file [`reports/AI_Critique.md`](AI_Critique.md):

> *"Trong quá trình thực hiện bài tập kiểm thử HW01, việc kiểm chứng các phản hồi của AI đã bộc lộ những khiếm khuyết hệ thống của mô hình ngôn ngữ lớn (LLM).*
>
> *Thứ nhất, AI mắc thiên kiến xác nhận (Confirmation Bias) và chứng "xu nịnh" (Sycophancy) nghiêm trọng. Khi sinh viên đưa ra các câu hỏi bẫy có tính dẫn dụ sai lệch về 20 sự cố phần mềm nổi tiếng (như quy chụp sự cố CrowdStrike do tin tặc Nga, lỗi Confluence do tràn bộ đệm C++, hay lỗi Citigroup do bot HFT), AI lập tức đồng thuận và thêu dệt các chi tiết kỹ thuật giả mạo có vẻ hợp lý nhưng hoàn toàn sai sự thật (AI Hallucination). AI không có khả năng tự phản biện tiền đề sai.*
>
> *Thứ hai, trong kiểm thử thiết bị vật lý (quạt Senko L1638), AI chỉ gợi ý các ca kiểm thử bề mặt (Happy Path). AI hoàn toàn bỏ sót các ca biên cơ điện nguy hiểm như kẹt lẫy cơ gây dẫn chéo cuộn stator, trượt vấu bánh răng hộp số, hay phóng hồ quang điện (Arcing). Nguyên nhân là LLM chỉ hoạt động trên xác suất thống kê văn bản tĩnh, thiếu tri giác vật lý (embodiment) và trải nghiệm nhân quả trong thế giới thực.*
>
> *Nguyên tắc cộng tác rút ra cho kỹ sư QA/QC là: "Zero-Trust AI" (Tuyệt đối không tin tưởng, luôn luôn kiểm chứng). AI chỉ đóng vai trò trợ lý tăng tốc tạo khung tài liệu sơ bộ. Kỹ sư con người bắt buộc phải là chốt chặn kiểm thử tối hậu, luôn đối chiếu chuẩn mực kỹ thuật (ISTQB, RFC, IEC) và trực tiếp thực nghiệm trên thiết bị thật."*

### 5.3. Tuyên bố Bắt buộc (Mandatory Disclosure) & Xác nhận Biểu mẫu [AI-03], [AI-05], [AI-06]
- **Tuyên bố bắt buộc (Mandatory Disclosure Statement):**
  > *"The QA/QC Mindmap and initial physical test cases were initially generated by Antigravity Assistant (Model: Gemini 3.8 Flash High); I reviewed and modified the entire hierarchy and static testing responsibilities in the Mindmap, added 4 physical edge cases (deadlock, gear slippage, resonance, arcing); the 10 job market analyses, 20 defect verification audits, 15 formal test executions, and 5 video demonstrations were conducted and written entirely by me. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."*
- **Xác nhận trạng thái các biểu mẫu liêm chính học thuật (Đã hoàn thiện cả tệp `.docx` chính thức nộp bài và `.md`):**
  - [x] [`AI Templates/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx`](../AI%20Templates/%5BAI-03%5D%20-%20FIT@HCMUS%20-%20AI%20Disclosure%20Form_En.docx) (và [`templates/AI-03_AI_Disclosure_Form.md`](../templates/AI-03_AI_Disclosure_Form.md)): Đã hoàn tất kê khai đầy đủ các công cụ, giai đoạn sử dụng, 3 prompt cốt lõi, phần đóng góp chi tiết của AI và phần tự làm 100% của sinh viên, phương pháp kiểm chứng độc lập, trích dẫn chuẩn IEEE và ký xác nhận.
  - [x] [`AI Templates/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx`](../AI%20Templates/%5BAI-05%5D%20-%20FIT@HCMUS%20-%20AI%20Privacy%20Checklist_En.docx) (và [`templates/AI-05_AI_Privacy_Checklist.md`](../templates/AI-05_AI_Privacy_Checklist.md)): Đã tích chọn 100% các tiêu chí bảo mật, cam kết không vi phạm dữ liệu riêng tư và ký xác nhận.
  - [x] [`AI Templates/[AI-06] - FIT@HCMUS - AI Student Acknowledgement_En.docx`](../AI%20Templates/%5BAI-06%5D%20-%20FIT@HCMUS%20-%20AI%20Student%20Acknowledgement_En.docx) (và [`templates/AI-06_AI_Student_Acknowledgement.md`](../templates/AI-06_AI_Student_Acknowledgement.md)): Đã ký cam kết tuân thủ chính sách AI môn học CS423/CSC13003 từ đầu khóa và khai báo tài khoản AI.
  - [x] [`reports/Appendix_A_Prompt_Log.md`](Appendix_A_Prompt_Log.md) (và [`prompt_log.md`](../prompt_log.md)): Nhật ký đầy đủ 42 prompts có dấu mốc thời gian thực chính xác từng giây.

---

## 6. TỰ ĐÁNH GIÁ ĐIỂM SỐ THEO RUBRIC (100/100 ĐIỂM)

Căn cứ theo bảng tiêu chuẩn đánh giá của môn học tại [`reports/Self_Assessment.md`](Self_Assessment.md):

| STT | Tiêu chí đánh giá (Criteria) | Thang điểm | Điểm Tự đánh giá | Minh chứng & Ghi chú thực hiện |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Thị trường việc làm QA/QC 2026+ (Req 1)** | **40** | **40 / 40** | Đủ 10 tin tuyển dụng ITviec $\le 27$ ngày; 3 vị trí AI; 10 ảnh screenshot có avatar; Mindmap sửa 3 lỗi ISTQB. |
| **2** | **20 Lỗi phần mềm 2022–2026 & AI Audits (Req 2)** | **20** | **20 / 20** | 20 sự cố toàn cầu (6 AI + 14 hạ tầng); 100% nguồn Post-mortem gốc; vạch trần 20/20 bẫy ảo giác AI. |
| **3** | **Kiểm thử thiết bị vật lý Senko L1638 (Req 3)** | **25** | **25 / 25** | Ảnh thẻ SV + quạt thật; 15 test cases ISTQB (file Excel 3 sheets + CSV); 4 edge cases AI bỏ sót; 5 video Shorts có thuyết minh; 5 live GitHub Issues kèm 5 ảnh screenshot chính chủ. |
| **AI-1** | **[AI-02] AI Audit Report** | **8** | **8 / 8** | Bảng kiểm định 5 phần đủ 22 mục (bản `.docx` chính thức & `.md`); thống kê 0% Valid, 90.9% Invalid, 9.1% Incomplete; kết luận 140 từ. |
| **AI-2** | **AI Critique + Form [AI-03]** | **4** | **4 / 4** | Bài phê bình đạt chuẩn 291 từ; form [AI-03] hoàn chỉnh (bản `.docx` chính thức & `.md`) có chữ ký xác nhận. |
| **AI-3** | **[AI-05] Privacy Checklist & Anti-cheat** | **3** | **3 / 3** | Checklist bảo mật [AI-05] và [AI-06] (bản `.docx` chính thức & `.md`) có chữ ký; Prompt Log đủ 42 lượt prompt với timestamp chính xác. |
| **TỔNG** | **TỔNG ĐIỂM TOÀN BỘ BÀI TẬP** | **100** | **100 / 100** | **Mã điểm 3 chữ số đặt vào tên file zip khi nộp bài: `100`** |

---

## 7. PHỤ LỤC & MA TRẬN TRUY XUẤT NGUỒN GỐC TÀI SẢN (TRACEABILITY MATRIX)

### 7.1. Bảng Ma trận Truy xuất Nguồn gốc Tài sản
| Nhóm yêu cầu | Tài sản tài liệu (Document) | Dữ liệu bảng tính / Cấu hình | Minh chứng Hình ảnh / Video / Issue |
| :--- | :--- | :--- | :--- |
| **Yêu cầu 1** | [`jobs_data.md`](../requirements/req1_job_market/jobs_data.md)<br>[`qa_qc_roles_mindmap.md`](../requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md) | Bảng dữ liệu 10 tin tuyển dụng | [`job_01.png`](../requirements/req1_job_market/screenshots/job_01.png) đến [`job_10.png`](../requirements/req1_job_market/screenshots/job_10.png) |
| **Yêu cầu 2** | [`defects_2022_2026.md`](../requirements/req2_software_defects/defects_2022_2026.md) | 20 Báo cáo RCA chuẩn | 20 Prompt bóc trần ảo giác trong [`Appendix_A_Prompt_Log.md`](Appendix_A_Prompt_Log.md) |
| **Yêu cầu 3** | [`device_info.md`](../requirements/req3_physical_product/device_info.md)<br>[`edge_cases_ai_missed.md`](../requirements/req3_physical_product/edge_cases_ai_missed.md)<br>[`test_cases.md`](../requirements/req3_physical_product/test_cases.md) | [`test_cases.csv`](../requirements/req3_physical_product/test_cases.csv)<br>[`test_cases_and_summary.xlsx`](../requirements/req3_physical_product/test_cases_and_summary.xlsx) (3 sheets) | [`device_23120207.jpg`](../requirements/req3_physical_product/photo/device_23120207.jpg)<br>[`ai_edge_cases_screenshot.png`](../requirements/req3_physical_product/photo/ai_edge_cases_screenshot.png)<br>5 Video Shorts (Video 1 đến 5)<br>[GitHub Issues #1 đến #5](https://github.com/NgBaoAnn/hw1/issues)<br>5 Ảnh màn hình [`issue_1.png`](../requirements/req3_physical_product/photo/issue_1.png) đến [`issue_5.png`](../requirements/req3_physical_product/photo/issue_5.png) |
| **AI Protocol** | [`AI-02_AI_Audit_Report.md`](AI-02_AI_Audit_Report.md)<br>[`AI_Critique.md`](AI_Critique.md)<br>[`Self_Assessment.md`](Self_Assessment.md)<br>Bộ 4 file `.docx` trong [`AI Templates/`](../AI%20Templates/) | [`templates/`](../templates/) (AI-03, AI-05, AI-06)<br>[`scripts/populate_docx_templates.py`](../scripts/populate_docx_templates.py) | [`Appendix_A_Prompt_Log.md`](Appendix_A_Prompt_Log.md) (Prompts P-01 đến P-42) |
| **Quản trị Git** | [`git_log.txt`](git_log.txt) | `git log --graph --all --stat` | [https://github.com/NgBaoAnn/hw1](https://github.com/NgBaoAnn/hw1) |

---

### XÁC NHẬN CỦA SINH VIÊN
Tôi xin cam đoan toàn bộ nội dung trong bản báo cáo tổng hợp này là sản phẩm học tập và nghiên cứu thực tế của chính tôi. Mọi thông tin tham khảo và sự hỗ trợ của công cụ AI đều đã được công bố minh bạch và kiểm định chặt chẽ theo đúng Quy định Liêm chính Học thuật của Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM.

*Thành phố Hồ Chí Minh, ngày 26 tháng 09 năm 2026*  
**Sinh viên thực hiện**  

*(Đã ký)*  

**NGUYỄN BẢO AN**  
MSSV: `23120207`
