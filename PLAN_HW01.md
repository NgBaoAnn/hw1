# Kế hoạch Thực hiện Bài tập HW01: QA/QC Jobs · 20 Defects · Test a Physical Product

> **Phương thức thực hiện:** Tuân thủ chuẩn mực quy trình phần mềm và chính sách AI minh bạch (AI Collaboration Protocol). Kế hoạch chia thành các tác vụ độc lập, có thể nghiệm thu từng phần (bite-sized tasks).

**Mục tiêu:** Hoàn thành xuất sắc 100% các tiêu chí của bài tập cá nhân HW01 (đạt điểm tối đa $\ge 9.5/10$ hoặc $10/10$), tuân thủ nghiêm ngặt các quy định về liêm chính học thuật, bằng chứng chống gian lận AI (Anti-cheat) và chuẩn bị sẵn sàng cho phần vấn đáp miệng (Oral Defense).

**Tài liệu tham chiếu:**
- Đề bài: `2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf`
- Hướng dẫn chung của giảng viên: `note.txt`
- Giáo trình ISTQB Foundation Level Syllabus (CTFL v4.0).

---

## 1. Các Ràng buộc Bắt buộc Toàn cục (Global Constraints)

1. **Anti-AI-Cheat (Quy định đỏ - Vi phạm = 0 điểm & kỷ luật):**
   - Ảnh chụp thiết bị vật lý **bắt buộc** phải chụp chung với **Thẻ sinh viên thật** trong cùng 1 khung hình.
   - Video demo thực thi kiểm thử ($\ge 5$ video $\le 60$s) **bắt buộc** có **giọng nói thuyết minh chính chủ của sinh viên**.
   - Toàn bộ 10 ảnh chụp màn hình tin tuyển dụng **bắt buộc** hiển thị **tên tài khoản đăng nhập** ở góc màn hình.
   - File nhật ký `Appendix_A_Prompt_Log.md` ghi nhận 100% các prompt kèm **mốc thời gian (timestamp)** thực tế.
2. **Quy tắc GitHub & Mantis:**
   - Hệ thống Mantis **không dùng** cho HW01. Toàn bộ lỗi tìm thấy trên thiết bị thật phải được tạo thành **GitHub Issues** trên repo cá nhân và chụp ảnh màn hình có thấy username GitHub.
   - Khởi tạo Git repo và commit thường xuyên theo chuẩn Conventional Commits. Cuối bài xuất `git log --graph --all --stat` theo đúng dặn dò trong `note.txt`.
3. **Quy định 2 phiên bản (2 versions):**
   - Phải cung cấp đầy đủ cả bản text-based (`.md`, `.txt`, `.csv`) và bản binary-based (`.pdf`, `.xlsx`, `.png`, `.jpg`).
4. **Cấu trúc đặt tên file nộp:**
   - Định dạng nộp: `StudentID_HW01_AI_<grade>.zip` (ví dụ: `21127000_HW01_AI_095.zip`).

---

## 2. Cấu trúc Thư mục Dự án Đề xuất

```text
hw1/
├── 2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf
├── note.txt
├── PLAN_HW01.md                           <-- Bản kế hoạch lưu trong workspace
├── requirements/
│   ├── req1_job_market/
│   │   ├── jobs_data.md                   <-- 10 tin tuyển dụng + JD + AI Impact Analysis
│   │   ├── screenshots/                   <-- 10 ảnh chụp màn hình (hiển thị account name)
│   │   └── mindmap/                       <-- Mindmap ISTQB role (PNG / Markdown) + 3 lỗi AI
│   ├── req2_software_defects/
│   │   └── defects_2022_2026.md           <-- 20 lỗi (≥ 5 AI/LLM) + 20 trường hợp AI hallucination/bias
│   └── req3_physical_product/
│       ├── device_info.md                 <-- Brand, Model, Year, Masked Serial, Specs
│       ├── test_cases.md                  <-- 15 Test cases chi tiết (Objective, Input, Steps, Expected, Actual, Verdict)
│       ├── edge_cases_ai_missed.md        <-- ≥ 3 edge cases AI bỏ sót + ảnh chat + phân tích lý do
│       ├── photo/                         <-- Ảnh chụp thiết bị + Thẻ sinh viên chung khung hình
│       ├── videos/                        <-- Link YouTube Unlisted (kèm transcript/voiceover)
│       └── github_issues/                 <-- Ảnh chụp Issues trên GitHub repo
├── reports/
│   ├── HW01_Report.md                     <-- Báo cáo chính (Markdown format)
│   ├── HW01_Report.pdf                    <-- Báo cáo chính xuất PDF
│   ├── test_cases_and_summary.xlsx        <-- File Excel (Test Cases / Checklist / Test Summary Report)
│   ├── Appendix_A_Prompt_Log.md           <-- Toàn bộ Prompt Log có timestamp
│   ├── AI_Critique.md                     <-- Đoạn văn phản biện AI 200–300 từ
│   └── Self_Assessment.md                 <-- Bảng rubric tự chấm 100đ
├── templates/
│   ├── AI-02_AI_Audit_Report.md           <-- 5 mục theo chuẩn cho từng artifact
│   ├── AI-03_AI_Disclosure_Form.md        <-- Form công bố (ký tên)
│   └── AI-05_AI_Privacy_Checklist.md      <-- Checklist quyền riêng tư (ký tên)
└── scripts/
    └── package_submission.sh              <-- Script kiểm tra tính đầy đủ và đóng gói .zip
```

---

## 3. Kế hoạch Triển khai Chi tiết Từng Task

### Task 0: Thiết lập Workspace & Khởi tạo Git Repo
- [x] **Bước 0.1:** Khởi tạo Git repository trong workspace (`git init`).
- [x] **Bước 0.2:** Tạo cấu trúc thư mục như thiết kế ở trên.
- [x] **Bước 0.3:** Tạo file `.gitignore` phù hợp (bỏ qua file tạm OS, build caches, nhưng giữ các artifact báo cáo).
- [x] **Bước 0.4:** Commit khởi tạo đầu tiên (`chore: initialize project structure and workspace`).

---

### Task 1: Thu thập & Phân tích 10 Tin tuyển dụng QA/QC 2026+ (Yêu cầu 1 - 40 điểm)
- [x] **Bước 1.1: Tìm kiếm 10 tin tuyển dụng:**
  - Nền tảng: ITviec.
  - Điều kiện: Đăng trong vòng 60 ngày gần nhất (thực tế toàn bộ <= 27 ngày, 100% hợp lệ).
  - Phân loại: Có 3 vị trí đòi hỏi kỹ năng AI/LLM (Saritasa #02, Golden Gate #04, TrustedAI #06).
- [x] **Bước 1.2: Chụp ảnh màn hình bằng chứng (Anti-cheat):**
  - Đảm bảo góc màn hình có tài khoản đăng nhập `NgBaoAnn` / Avatar.
  - Lưu ảnh vào `requirements/req1_job_market/screenshots/job_01.png` đến `job_10.png`.
- [x] **Bước 1.3: Trích xuất thông tin & Soạn thảo nội dung:**
  - Đã tạo `requirements/req1_job_market/jobs_data.md`.
  - Với mỗi tin: Link, Vị trí & Công ty, Ngày đăng, Mức lương, Tóm tắt JD, Kỹ năng yêu cầu, và **1–2 câu Phân tích tác động của AI (AI Impact Analysis)** cho đủ 10/10 tin.
- [x] **Bước 1.4: Tạo Mindmap quy trình/vai trò QA/QC (CLO G9.1):**
  - Soạn prompt yêu cầu AI vẽ Mindmap về các vai trò QA/QC theo chuẩn ISTQB.
  - Ghi nhận lại phản hồi của AI.
  - Phân tích và chỉ ra **3 lỗi sai / điểm thiếu sót** trong mindmap của AI theo ISTQB CTFL v4.0.
  - Vẽ lại mindmap chuẩn bằng Mermaid lưu vào `requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md`.
  - Cập nhật mục này vào `templates/AI-02_AI_Audit_Report.md`.
- [x] **Bước 1.5: Commit kết quả Task 1** vào Git.

---

### Task 2: Nghiên cứu 20 Lỗi phần mềm 2022–2026 & Bẫy Ảo giác AI (Yêu cầu 2 - 20 điểm)
- [x] **Bước 2.1: Thu thập danh sách 20 sự cố/lỗi phần mềm nổi tiếng (2022–2026):**
  - Đảm bảo $\ge 5$ sự cố trực tiếp liên quan đến AI/LLM: Đã chọn 6 lỗi AI (Gemini Image Bias, Air Canada Chatbot, Chevrolet $1 Car, Bing Sydney, DPD Delivery Bot, Samsung Semiconductor ChatGPT leak).
  - 14 sự cố hệ thống toàn cầu khác (CrowdStrike BSOD, Cloudflare BGP, MOVEit SQLi, FAA NOTAM, Toyota Disk Full, Optus Outage, AT&T Outage, XZ Utils Backdoor, Southwest Airlines Meltdown, Unity Runtime Fee, Citigroup Flash Crash, Okta HAR Session Theft, Atlassian Confluence, Ivanti VPN).
  - Đã hoàn tất bảng tổng hợp và chi tiết 20 lỗi tại `requirements/req2_software_defects/defects_2022_2026.md`.
- [x] **Bước 2.2: Phỏng vấn AI về từng lỗi để tìm AI Bias / Hallucination (Yêu cầu MỚI):**
  - Với **từng lỗi trong cả 20 lỗi**, đã gửi prompt chất vấn dẫn dụ bẫy AI (`[P-14]` đến `[P-33]`).
  - Đã so sánh đối chiếu với báo cáo gốc (Post-mortem) của đơn vị bị sự cố.
  - Bắt lỗi AI: Đã vạch trần chính xác 20/20 điểm AI đưa ra thông tin thiên vị (bias), suy diễn sai, hoặc ảo giác (hallucination).
- [x] **Bước 2.3: Tổng hợp báo cáo 20 lỗi:**
  - Hoàn thiện file `requirements/req2_software_defects/defects_2022_2026.md` với đầy đủ cấu trúc 7 phần:
    1. Tên lỗi & Thời gian & Đơn vị.
    2. Link nguồn dẫn chứng chính thức (Official Vendor Post-mortems, CISA, USDOT, UK FCA, v.v.).
    3. Phân loại & Mức độ nghiêm trọng (Severity).
    4. Mô tả nguyên nhân kỹ thuật (RCA).
    5. Hậu quả thực tế (Consequences).
    6. Giải pháp khắc phục (Solution & Lessons Learned).
    7. **Phỏng vấn AI & Vạch lỗi Bias / Hallucination** (kèm câu hỏi, phản hồi AI, phán quyết INVALID, và đối chiếu kỹ thuật chi tiết).
- [x] **Bước 2.4: Cập nhật Audit Report và Commit:**
  - Ghi nhận đầy đủ 20 prompt và kết quả vào `reports/Appendix_A_Prompt_Log.md`, đồng bộ `prompt_log.md` và cập nhật Artifact #3 vào `templates/AI-02_AI_Audit_Report.md`.
  - Đã commit toàn bộ kết quả Task 2 vào Git theo từng sự cố và tổng thể.

---

### Task 3: Thiết kế Kiểm thử & Quay video Thực nghiệm Thiết bị Vật lý (Yêu cầu 3 - 40 điểm)
- [x] **Bước 3.1: Lựa chọn thiết bị gia dụng:**
  - Đã chọn: Quạt điện lửng dân dụng SENKO, Model L1638, sản xuất tháng 09/2023.
  - Thu thập đầy đủ thông số kỹ thuật (47W, 220V/50Hz, sải cánh 39cm, 4 phím cơ liên động 0-1-2-3, túp-năng 180°, ống rút 77cm-95cm, cầu chì nhiệt stator) và lưu tại `requirements/req3_physical_product/device_info.md`.
- [x] **Bước 3.2: Chụp ảnh bằng chứng chống gian lận (Anti-cheat photo):**
  - Đã chụp ảnh Quạt Senko L1638 cùng Thẻ sinh viên (NGUYỄN BẢO AN - MSSV 23120207) trong cùng 1 khung hình rõ nét, hợp lệ 100%.
  - Lưu vào `requirements/req3_physical_product/photo/device_23120207.jpg` và `photo/device_student_id.jpg`.
- [x] **Bước 3.3: Dùng AI gợi ý ban đầu & Bắt lỗi Edge Cases (CLO G9.3):**
  - Đã gửi prompt yêu cầu AI đề xuất test cases cho quạt Senko L1638.
  - Phê bình phản hồi hời hợt của AI (chỉ sinh 10 test case Happy Path bề mặt).
  - Vạch trần **4 Edge Cases vật lý / cơ điện trọng yếu mà AI bỏ sót**:
    1. Nhấn đồng thời 2 phím tốc độ (kẹt lẫy cơ & đoản mạch chéo cuộn dây).
    2. Cản cưỡng bức hành trình túp-năng (trượt mòn vấu bánh răng hộp số).
    3. Rung lắc cộng hưởng khi chạy Số 3 ở độ cao 95cm (trôi ren siết ống sắt làm quạt tự sụt chiều cao).
    4. Nhấn hờ phím tốc độ (phóng hồ quang điện arcing nguy cơ chập cháy).
  - Hoàn thiện tài liệu `requirements/req3_physical_product/edge_cases_ai_missed.md` và cập nhật Artifact #2 trong `templates/AI-02_AI_Audit_Report.md`.
- [x] **Bước 3.4: Xây dựng bộ 15 Test Cases hoàn chỉnh:**
  - Soạn thảo bảng 15 test cases chuẩn theo ISTQB CTFL v4.0 vào `requirements/req3_physical_product/test_cases.md` gồm đầy đủ các cột: ID | Nhóm | Objective | Input | Steps | Expected | Actual | Verdict | Khiếm khuyết & Video Demo.
  - Lồng ghép 4 Edge Cases (`TC-12`, `TC-13`, `TC-14`, `TC-15`) phát hiện 5 lỗi vật lý thực tế (`DEF-01` đến `DEF-05`).
  - Xuất bảng tính `test_cases.csv` và sinh file Excel chuẩn `requirements/req3_physical_product/test_cases_and_summary.xlsx`.
- [x] **Bước 3.5: Thực nghiệm trên thiết bị & Quay $\ge 5$ video demo (Thời lượng $\le 60$s):**
  - Đã thực hiện trên thiết bị quạt Senko L1638 thật và quay 5 video demo có giọng thuyết minh của sinh viên.
  - Tải lên YouTube (Unlisted) thành công và tích hợp vào `requirements/req3_physical_product/test_cases.md` cùng các GitHub Issues:
    1. Video 1 (TC-12 / DEF-01): https://youtube.com/shorts/NK6kk9AF39U?feature=share
    2. Video 2 (TC-13 / DEF-02): https://youtube.com/shorts/TQMrprni0oY?feature=share
    3. Video 3 (TC-14 / DEF-03): https://youtube.com/shorts/edU_0xoc_JI?feature=share
    4. Video 4 (TC-09 / DEF-04): https://youtube.com/shorts/jCHATpMITFI?feature=share
    5. Video 5 (TC-15 / DEF-05): https://youtube.com/shorts/NZP3v1SyXfY?feature=share
- [ ] **Bước 3.6: Ghi nhận lỗi lên GitHub Issues (Thay thế Mantis):**
  - Ghi nhận các khiếm khuyết/bất cập phát hiện được trong quá trình test thành các Issue trên GitHub repository cá nhân.
  - Chụp ảnh màn hình trang Issues có hiển thị rõ GitHub Username của sinh viên.
- [ ] **Bước 3.7: Commit kết quả Task 3** vào Git.

---

### Task 4: Hoàn thiện AI Collaboration Protocol & Các Biểu mẫu Bắt buộc
- [ ] **Bước 4.1: Xây dựng `[AI-02] AI Audit Report`:**
  - Tổng hợp các đợt prompt cho từng sản phẩm theo đúng mẫu 5 phần:
    `(1) Prompt + tool + timestamp -> (2) Full AI output -> (3) Verdict -> (4) Reasoning (ISTQB) -> (5) Student fix`.
  - Thống kê tỷ lệ chính xác của AI (% VALID, % INVALID, % INCOMPLETE).
  - Viết kết luận: Khi nào nên dùng và khi nào không nên dùng AI trong quy trình kiểm thử phần mềm/phần cứng.
- [ ] **Bước 4.2: Viết đoạn phê bình `AI Critique` (200–300 từ):**
  - Phân tích sâu về thiên vị (bias), ảo giác (hallucination) và hạn chế ngữ cảnh thực tế của AI.
  - Rút ra nguyên tắc cộng tác hiệu quả giữa kỹ sư QA và AI.
- [ ] **Bước 4.3: Điền và Ký các Biểu mẫu:**
  - Hoàn thiện `[AI-03] AI Disclosure Form` (ký tên).
  - Hoàn thiện `[AI-05] AI Privacy & Responsible Use Checklist` (ký tên).
  - Dán đoạn mẫu `Mandatory Disclosure` vào cuối báo cáo trước phần phụ lục.
- [ ] **Bước 4.4: Chuẩn bị `Appendix A: Full Prompt Log`:**
  - Trích xuất toàn bộ lịch sử trao đổi với AI từ đầu bài tập, đánh dấu thời gian cụ thể `HH:MM dd/mm/yyyy`.
- [ ] **Bước 4.5: Commit kết quả Task 4** vào Git.

---

### Task 5: Tổng hợp Báo cáo Chính (PDF + Text), File Excel & Tự chấm điểm
- [ ] **Bước 5.1: Hoàn thiện File Excel tổng thể:**
  - Tạo `reports/test_cases_and_summary.xlsx` gồm các sheet:
    - Sheet 1: 15 Test Cases chi tiết.
    - Sheet 2: Danh sách khiếm khuyết (Defects Checklist / GitHub Issues mapping).
    - Sheet 3: Báo cáo tóm tắt kiểm thử (Test Summary Report).
- [ ] **Bước 5.2: Soạn thảo Báo cáo tổng thể `HW01_Report.md`:**
  - Kết nối toàn bộ kết quả từ Task 1, 2, 3, 4 vào một tài liệu hoàn chỉnh, trình bày thẩm mỹ, mục lục rõ ràng.
  - Bổ sung bảng tự chấm điểm (Self-Assessment Rubric) đủ 100 điểm.
- [ ] **Bước 5.3: Xuất bản PDF `HW01_Report.pdf`:**
  - Đảm bảo giữ nguyên cả bản text (`.md`) và bản binary (`.pdf`) theo đúng lưu ý của giảng viên.
- [ ] **Bước 5.4: Chuẩn bị Kịch bản Vấn đáp miệng (Oral Defense Preparation):**
  - Soạn sẵn tài liệu ôn tập 3 câu hỏi vấn đáp:
    1. Hướng dẫn chạy nhanh kịch bản test trên máy.
    2. Giải thích cơ sở kỹ thuật chọn Input X thay vì Input Y (Boundary Value Analysis / Equivalence Partitioning theo ISTQB).
    3. Trình bày chi tiết 1 lỗi tiêu biểu mà AI mắc phải và cách mình đã hiệu chỉnh.

---

### Task 6: Kiểm tra Tính Hợp lệ (Verification) & Đóng gói Nộp bài
- [ ] **Bước 6.1: Viết script kiểm tra & đóng gói `scripts/package_submission.sh`:**
  - Kiểm tra sự tồn tại của toàn bộ các file bắt buộc:
    - Ảnh thẻ SV + Thiết bị
    - $\ge 5$ link YouTube
    - 10 ảnh screenshot việc làm có account name
    - File Excel test cases
    - GitHub issues screenshot
    - Prompt log `.md` có timestamp
    - Các form AI-02, AI-03, AI-05
    - Báo cáo chính PDF + MD
- [ ] **Bước 6.2: Trích xuất Git commit log:**
  - Chạy lệnh theo yêu cầu của thầy: `git log --graph --all --stat > reports/git_log.txt`.
- [ ] **Bước 6.3: Nén file nộp bài:**
  - Đóng gói file `StudentID_HW01_AI_<grade>.zip`.
  - Kiểm tra mở thử file zip xem các đường dẫn có bị lỗi font hoặc hỏng liên kết hay không.

---

## 4. Kế hoạch Nghiệm thu & Kiểm tra Chéo (Verification Plan)

| Tiêu chí | Cách thức kiểm tra | Kết quả mong đợi |
| :--- | :--- | :--- |
| **Yêu cầu 1 (40đ)** | Kiểm tra đủ 10 tin $\le 60$ ngày; $\ge 3$ tin AI; 10 ảnh có account name; Mindmap có 3 lỗi AI. | Đầy đủ dữ liệu, ảnh không che mất tên tài khoản, phân tích AI Impact sắc sảo. |
| **Yêu cầu 2 (20đ)** | Đủ 20 lỗi (2022–2026), $\ge 5$ lỗi AI; 20 trường hợp phát hiện AI hallucination/bias. | Có link dẫn chứng, phân tích bẫy ảo giác của AI có cơ sở kỹ thuật thuyết phục. |
| **Yêu cầu 3 (40đ)** | Ảnh thiết bị + Thẻ SV; 15 test cases (gồm $\ge 3$ edge case AI bỏ sót); $\ge 5$ video demo YouTube có voice; Issues trên GitHub. | Video chạy tốt, có giọng nói chính chủ, test case chuẩn định dạng ISTQB. |
| **Tuân thủ AI (15-20đ)** | Đối chiếu form AI-02, AI-03, AI-05, đoạn Critique 200-300 từ, Prompt log đầy đủ timestamp. | Khớp 100% với rubric kiểm định AI, không thiếu bất kỳ mục nào. |
| **Đóng gói** | Chạy script `package_submission.sh` và giải nén thử nghiệm file `.zip`. | File zip đúng định dạng tên, giải nén không lỗi, đầy đủ cả text và binary. |
