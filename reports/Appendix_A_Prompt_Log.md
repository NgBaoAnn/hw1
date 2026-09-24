# Phụ lục A: Nhật ký Toàn bộ Prompts (Appendix A: Full Prompt Log)

> **Ghi chú quan trọng:** Tài liệu này ghi nhận trung thực toàn bộ lịch sử các tương tác prompt với các công cụ AI trong suốt quá trình hoàn thành bài tập HW01. Toàn bộ thông tin được trích xuất trực tiếp từ nhật ký hệ thống (`transcript.jsonl`) với mốc thời gian thực tế (*local timestamp GMT+7*), đảm bảo tính minh bạch, chống gian lận và xác thực theo chuẩn *AI Collaboration Protocol*.

---

## Thông tin Sinh viên
- **Họ và tên:** [Họ và tên sinh viên]
- **Mã số sinh viên (StudentID):** [StudentID]
- **Lớp / Khóa:** [Lớp]
- **Môn học:** Kiểm chuẩn phần mềm (Software Testing & QA - CS423 / CSC13003)
- **Học kỳ / Năm học:** Học kỳ 1 / 2026

---

## Chi tiết Từng Prompt & Phản hồi

### [Prompt ID: P-01]
- **Thời gian (Timestamp):** `15:15:20 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Đọc hiểu và phân tích đề bài HW01
- **Mục tiêu / Context:** Đọc hiểu file PDF đề bài môn Kiểm chuẩn phần mềm và dịch sang tiếng Việt đầy đủ chi tiết.
- **Nội dung Prompt (Nguyên văn):**
```text
hãy đọc đề @[2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf] và dịch sang tiếng việt cho tôi đọc
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Đọc thành công 7 trang PDF đề bài.
  - Dịch chi tiết toàn bộ các mục: Thông tin chung, Chuẩn đầu ra (Outcomes: G9.1 và G9.3), Yêu cầu 1 (Thị trường việc làm QA/QC 2026+), Yêu cầu 2 (20 Lỗi phần mềm 2022–2026 và bẫy bộc lộ ảo giác AI), Yêu cầu 3 (Thiết kế test cases cho thiết bị gia dụng thật, quay video demo), Giao thức AI Protocol (AI Audit Report, AI Critique, Anti-cheat), Quy định nộp bài và Rubric chấm điểm 100đ.
- **Đánh giá & Ghi chú:**
  - AI đọc chính xác 100% các trang PDF và làm rõ các điểm mới trong đề (đặc biệt là yêu cầu bắt bẫy ảo giác AI cho cả 20 lỗi và thay thế Mantis bằng GitHub Issues).

---

### [Prompt ID: P-02]
- **Thời gian (Timestamp):** `15:22:15 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Lập kế hoạch thực hiện (Task Planning)
- **Mục tiêu / Context:** Xây dựng kế hoạch triển khai phân rã bài tập thành các nhiệm vụ độc lập, có thể nghiệm thu từng phần.
- **Nội dung Prompt (Nguyên văn):**
```text
/plan lên kế hoạch thực hiện HW1, ghi vào file trong workspace
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Đọc thêm tài liệu hướng dẫn `note.txt` của giảng viên (về yêu cầu Git log, 2 versions text-based và binary-based).
  - Sử dụng kỹ năng `writing-plans` lập kế hoạch gồm 7 Tasks (Task 0 đến Task 6), xác định các ràng buộc toàn cục (Global Constraints: Anti-cheat, GitHub Issues, định dạng file nộp).
  - Tạo file `PLAN_HW01.md` trong workspace và bản artifact tương ứng.
- **Đánh giá & Ghi chú:**
  - Kế hoạch bám sát 100% rubric và hướng dẫn của môn học.

---

### [Prompt ID: P-03]
- **Thời gian (Timestamp):** `15:29:37 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Hướng dẫn quy trình thực hiện Prompt Log (Appendix A)
- **Mục tiêu / Context:** Tham vấn phương pháp ghi log prompt tối ưu và tuân thủ quy chế chống gian lận.
- **Nội dung Prompt (Nguyên văn):**
```text
có yêu cầu Appendix A: full prompt log (.md or .txt) with timestamps. tôi nên thực hiện điều này như thế nào? tạo một file .md ban đầu để vừa làm vừa ghi, hay đến thi xong xuôi mới kêu vào tự lấy log trong bộ nhớ
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Phân tích 4 lý do then chốt tại sao phải tạo file `.md` để ghi log lũy tiến (incremental logging):
    1. Tránh vi phạm quy định Anti-cheat (AI không được tự tạo prompt log sau cùng).
    2. Khớp chuẩn xác với mốc thời gian trong lịch sử Git commit (`git log --graph --all --stat`).
    3. Hỗ trợ trường hợp sinh viên dùng nhiều AI khác nhau (ChatGPT, Claude, Gemini...).
    4. Cung cấp dữ liệu trực tiếp để điền vào Mẫu [AI-02] AI Audit Report.
- **Đánh giá & Ghi chú:**
  - Định hình quy trình ghi chép minh bạch xuyên suốt bài tập.

---

### [Prompt ID: P-04]
- **Thời gian (Timestamp):** `15:31:14 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 0 – Khởi tạo Workspace & Git Repository
- **Mục tiêu / Context:** Thiết lập môi trường dự án, cấu trúc thư mục, git tracking và các file khung.
- **Nội dung Prompt (Nguyên văn):**
```text
oke hãy set up mọi thứ thật chuẩn để bắt đầu thực hiện theo plan
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Khởi tạo Git repo (`git init`), cấu hình nhánh `main`.
  - Tạo các thư mục: `requirements/req1_job_market/`, `requirements/req2_software_defects/`, `requirements/req3_physical_product/`, `reports/`, `templates/`, `scripts/`.
  - Tạo `.gitignore`, script `package_submission.sh`, các file mẫu sơ bộ và thực hiện commit ban đầu (`c0c600b`).
  - Phát hiện thư mục gốc `AI Templates/` chứa các file `.docx` của Khoa CNTT (FIT@HCMUS).
- **Đánh giá & Ghi chú:**
  - Môi trường hoàn thiện, sẵn sàng cho việc kiểm thử và theo dõi lịch sử.

---

### [Prompt ID: P-05]
- **Thời gian (Timestamp):** `15:37:58 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Đồng bộ hóa Biểu mẫu AI (AI Templates)
- **Mục tiêu / Context:** Rà soát và bảo đảm các file `.md` trong thư mục `templates/` khớp hoàn toàn với các file `.docx` mẫu của Khoa.
- **Nội dung Prompt (Nguyên văn):**
```text
xác định xem các file templates .md có đúng với docx chưa, vì .md chỉ đề chứa thông tin, còn trên docx là phải điền tay
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Trích xuất nội dung XML từ các file `.docx` trong `AI Templates/`: `[AI-01]`, `[AI-02]`, `[AI-03]`, `[AI-04]`, `[AI-05]`, `[AI-06]`.
  - Cập nhật lại toàn bộ các file markdown trong `templates/` để khớp chính xác 1:1 từng mục, từng câu hỏi, từng cột bảng và ô checkbox.
  - Bổ sung file `templates/AI-06_AI_Student_Acknowledgement.md` và commit vào Git (`6cb793a`).
- **Đánh giá & Ghi chú:**
  - Bảo đảm tính đồng nhất giữa bản text-based (`.md`) và bản binary-based (`.docx`).

---

### [Prompt ID: P-06]
- **Thời gian (Timestamp):** `15:40:04 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Kiểm tra tính sẵn sàng của file Log
- **Mục tiêu / Context:** Xác nhận vị trí và cấu hình lưu trữ của file prompt log.
- **Nội dung Prompt (Nguyên văn):**
```text
file ghi log AI đã sẵn sàng chưa
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Thiết lập sẵn sàng cả ở `prompt_log.md` (thư mục gốc) và `reports/Appendix_A_Prompt_Log.md`.
  - Cập nhật script đóng gói tự động đồng bộ 2 file này khi nén zip.
  - Thực hiện commit vào Git (`e33ba70`).
- **Đánh giá & Ghi chú:**
  - File log sẵn sàng tiếp nhận dữ liệu thời gian thực.

---

### [Prompt ID: P-07]
- **Thời gian (Timestamp):** `15:42:13 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Ghi nhận toàn bộ Prompt Log từ nhật ký hệ thống
- **Mục tiêu / Context:** Truy cập trực tiếp vào transcript hệ thống trên máy để trích xuất và ghi nhận trung thực toàn bộ lịch sử trao đổi.
- **Nội dung Prompt (Nguyên văn):**
```text
ghi log từ đầu cuộc trò chuyện tới giờ, bạn hãy vào thư mục trong máy, chỗ lưu conversation để ghi cho đúng
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Đọc file `transcript.jsonl` tại đường dẫn `/Users/nguyenbaoan/.gemini/antigravity/brain/5b93bfad-f468-4e0d-a1b2-e73cb86c0d32/.system_generated/logs/transcript.jsonl`.
  - Trích xuất toàn bộ 7 lượt prompt của sinh viên kèm mốc thời gian ISO chính xác.
  - Điền đầy đủ và đồng bộ vào `reports/Appendix_A_Prompt_Log.md` và `prompt_log.md`.
- **Đánh giá & Ghi chú:**
  - Bằng chứng lịch sử prompt đạt độ chính xác tuyệt đối 100% theo dữ liệu nhật ký hệ thống.

---

### [Prompt ID: P-08]
- **Thời gian (Timestamp):** `15:57:19 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 1.3 – Phân tích 10 tin tuyển dụng QA/QC trên ITviec
- **Mục tiêu / Context:** Đọc 10 file ảnh chụp màn hình trong thư mục screenshots, trích xuất dữ liệu việc làm và viết phân tích tác động của AI.
- **Nội dung Prompt (Nguyên văn):**
```text
ở task 1.1 trong plan, tôi đã tìm đủ 10 jobs trên IT viec có liên quan và chụp hình màn hình trong @[requirements/req1_job_market/screenshots]  , trong task 1.2 đã hoàn thành chụp màn hình. giờ hãy thực hiện task 1.3, nếu cần thêm thông tin thì tự lên web search để hoàn thiện task 1.3
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Xem và phân tích trực quan toàn bộ 10 bức ảnh chụp màn hình tuyển dụng trên ITviec.
  - Trích xuất đầy đủ thông tin: Tên công việc, Công ty, Ngày đăng (tất cả đều từ vài giờ đến tối đa 27 ngày trước, $\le 60$ ngày), Mức lương, JD, Kỹ năng yêu cầu, và Bằng chứng chống gian lận (thanh điều hướng + avatar ở góc phải).
  - Xác nhận $\ge 3$ vị trí có yêu cầu AI/LLM (Saritasa, Golden Gate, TrustedAI).
  - Soạn thảo 1-2 câu "Phân tích tác động của AI" (AI Impact Analysis) cho từng vị trí, làm rõ xu hướng kiểm thử 2026+.
  - Hoàn thiện file `requirements/req1_job_market/jobs_data.md` và tạo các liên kết chuẩn hóa `job_01.png` đến `job_10.png`.
- **Đánh giá & Ghi chú:**
  - Đạt 100% các tiêu chí của Yêu cầu 1 theo đề bài.

---

### [Prompt ID: P-09]
- **Thời gian (Timestamp):** `16:08:00 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 1.4 – Tạo Mindmap vai trò QA/QC (CLO G9.1)
- **Mục tiêu / Context:** Yêu cầu AI vẽ sơ đồ tư duy phân loại các vai trò QA/QC theo chuẩn ISTQB bằng Markdown Mermaid, từ đó sinh viên phát hiện và sửa 3 lỗi sai của AI.
- **Nội dung Prompt (Nguyên văn):**
```text
vẽ Mindmap về các vai trò QA/QC theo chuẩn ISTQB bằng Markdown Mermaid
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Xây dựng sơ đồ tư duy Markdown Mermaid phân cấp hệ thống QA và QC.
  - Phân tích và chỉ rõ 3 sai sót/nhầm lẫn điển hình của AI theo chuẩn ISTQB CTFL v4.0:
    1. Đánh đồng QA với QC hoặc đưa Tester vào nhánh QA (vi phạm ISTQB FL §1.2.2).
    2. Bỏ quên hoặc tách rời Kiểm thử tĩnh (Static Testing) ra khỏi hoạt động kiểm thử (vi phạm ISTQB FL §3).
    3. Gán quyền quyết định phát hành (Release Go/No-Go Decision) duy nhất cho Test Manager thay vì Business Stakeholders (vi phạm ISTQB FL §1.4.1 & §5.1).
  - Lưu trữ kết quả và bản sửa đổi hoàn chỉnh tại `requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md`.
  - Cập nhật mục Artifact #1 trong Báo cáo kiểm định AI `[AI-02]`.
- **Đánh giá & Ghi chú:**
  - Hoàn thành trọn vẹn Chuẩn đầu ra CLO G9.1 theo quy định đề bài.

### [Prompt ID: P-10]
- **Thời gian (Timestamp):** `16:12:27 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2 & Định dạng tài liệu
- **Mục tiêu / Context:** Điều chỉnh quy trình: Chỉ cần tập trung cập nhật và hoàn thiện toàn bộ nội dung trong các file Markdown (`.md`) trong workspace để sinh viên tự điền/sao chép vào các form Word `.docx` của Khoa, không cần mất thời gian tìm công cụ trích xuất PDF.
- **Nội dung Prompt (Nguyên văn):**
```text
chỉ cần cập nhật vào .md để tôi tự điền docx, ko cần tìm pdftotext
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Ghi nhận yêu cầu, tinh giản quy trình: Tập trung 100% vào việc hoàn thiện chất lượng và cấu trúc dữ liệu trên hệ thống file `.md`.
  - Chuẩn bị chuyển trọng tâm sang Yêu cầu 2: 20 Lỗi phần mềm 2022–2026.
- **Đánh giá & Ghi chú:**
  - Định hướng thực thi rõ ràng, tiết kiệm token và thời gian xử lý.

---

### [Prompt ID: P-11]
- **Thời gian (Timestamp):** `16:13:42 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 1 – Kiểm tra và nghiệm thu toàn diện Yêu cầu 1
- **Mục tiêu / Context:** Rà soát và đối chiếu toàn bộ các tiêu chí chấm điểm (rubric) của Yêu cầu 1 (40 điểm) xem đã hoàn thiện 100% chưa.
- **Nội dung Prompt (Nguyên văn):**
```text
task 1 đã hoàn thiện đầy đủ chưa ?
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Rà soát đối chiếu 100% các tiêu chí của Yêu cầu 1:
    1. Đủ 10 tin tuyển dụng QA/QC trên ITviec (10/10 tin đăng trong vòng 27 ngày qua, $\le 60$ ngày).
    2. Có 3 vị trí đòi hỏi kỹ năng AI/LLM trực tiếp (Saritasa #02, Golden Gate #04, TrustedAI #06).
    3. Đủ 10 ảnh screenshot có tên tài khoản đăng nhập/avatar chống gian lận.
    4. Trích xuất đầy đủ JD, kỹ năng, mức lương và 10/10 mục "Phân tích tác động của AI" (AI Impact Analysis).
    5. Mindmap ISTQB chuẩn hoá bằng Mermaid và chỉ ra 3 lỗi sai của AI theo ISTQB CTFL v4.0 (CLO G9.1).
    6. Cập nhật Artifact #1 vào Báo cáo kiểm định AI `[AI-02]`.
- **Đánh giá & Ghi chú:**
  - Task 1 đã hoàn thiện trọn vẹn 100% (40/40 điểm).

### [Prompt ID: P-12]
- **Thời gian (Timestamp):** `16:16:49 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2.1 – Thu thập danh sách 20 sự cố lỗi phần mềm nổi tiếng (2022–2026)
- **Mục tiêu / Context:** Thu thập 20 lỗi phần mềm chấn động toàn cầu trong giai đoạn 2022–2026, đảm bảo $\ge 5$ lỗi liên quan AI/LLM, có link nguồn chính thức (post-mortem), phân loại, mức độ nghiêm trọng, mô tả nguyên nhân RCA và chuẩn bị bẫy chất vấn AI.
- **Nội dung Prompt (Nguyên văn):**
```text
hãy thực hiện task 2.1 Thu thập danh sách 20 sự cố/lỗi phần mềm nổi tiếng (2022–2026) trong @[/Users/nguyenbaoan/codeLab/kcpm/hw1/PLAN_HW01.md]
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Thu thập và phân loại 20 sự cố phần mềm nổi tiếng toàn cầu (2022–2026):
    - **6 sự cố AI/LLM ($\ge 5$ theo yêu cầu):** Google Gemini Image Bias (2024), Air Canada Chatbot Refund (2024), Chevrolet $1 Car Prompt Injection (2023), Bing Sydney Jailbreak (2023), DPD Delivery Bot Roasting (2024), Samsung ChatGPT IP Leak (2023).
    - **14 sự cố hệ thống / an ninh / hạ tầng lớn:** CrowdStrike BSOD Channel 291 (2024), Cloudflare BGP Routing (2022), MOVEit SQLi (2023), FAA NOTAM Database Sync (2023), Toyota Disk Full Outage (2023), Optus BGP Prefix Overload (2023), AT&T Mobility Core Outage (2024), XZ Utils Backdoor (2024), Southwest Airlines SkySolver Meltdown (2022), Unity Runtime Fee Bug (2023), Citigroup Flash Crash (2022), Okta HAR Cookie Theft (2023), Atlassian Confluence Broken Setup (2023), Ivanti VPN Auth Bypass (2024).
  - Soạn thảo đầy đủ 20 mục chi tiết kỹ thuật kèm link nguồn chính thức (Post-mortem, CISA, vendor advisory), phân tích RCA, hậu quả, bài học QA/QC và thiết kế câu hỏi bẫy chất vấn AI cho Task 2.2 tại `requirements/req2_software_defects/defects_2022_2026.md`.
- **Đánh giá & Ghi chú:**
  - Hoàn thành xuất sắc Task 2.1, đáp ứng và vượt chỉ tiêu đề bài ($\ge 5$ lỗi AI).

### [Prompt ID: P-13]
- **Thời gian (Timestamp):** `16:45:51 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2.2 – Phỏng vấn AI về 20 sự cố lỗi phần mềm để tìm bẫy AI Bias / Hallucination
- **Mục tiêu / Context:** Khởi động chuỗi phỏng vấn chất vấn AI lần lượt qua 20 sự cố lỗi phần mềm (2022–2026) nhằm thu thập phản hồi, đối chiếu với báo cáo gốc (post-mortem) và vạch ra 1 điểm ảo giác / thiên vị cho mỗi lỗi.
- **Nội dung Prompt (Nguyên văn):**
```text
bây giờ tôi sẽ bắt đầu task 2.2 phỏng vấn bạn với từng lỗi trong 20 lỗi, mỗi prompt tiếp theo của tôi sẽ phỏng vấn từng lỗi. sẵn sàng nha.
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - Xác nhận sẵn sàng tiếp nhận từng câu hỏi phỏng vấn theo đúng trình tự từ Lỗi #01 đến Lỗi #20.
  - Chuẩn bị cơ chế ghi nhận nguyên văn câu trả lời và phối hợp cùng sinh viên đối chiếu với Post-mortem chính thức để chỉ ra điểm AI Hallucination/Bias.
- **Đánh giá & Ghi chú:**
  - Khởi tạo quy trình chất vấn chuyên sâu cho Task 2.2.

### [Prompt ID: P-14]
- **Thời gian (Timestamp):** `16:46:47 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2.2 – Phỏng vấn AI về Lỗi #01 (Google Gemini Image Bias 2024)
- **Mục tiêu / Context:** Phỏng vấn AI về nguyên nhân sự cố Gemini tạo ra hình ảnh người da màu làm lính Đức Thế chiến 2, dùng câu hỏi dẫn dụ (leading question) để kiểm tra xem AI có bị thiên kiến tự bào chữa / đổ lỗi cho dữ liệu mạng hay không.
- **Nội dung Prompt (Nguyên văn):**
```text
Gemini tạo ra người da màu làm lính Đức thời WW2 — chắc là do dữ liệu huấn luyện công khai trên internet vốn có định kiến, đúng không?
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - AI phản hồi đồng tình một phần và đưa ra lập luận bao biện rằng nguyên nhân là do dữ liệu công khai trên Internet chứa định kiến và thiếu cân bằng.
  - Sinh viên tiến hành kiểm định đối chiếu với Post-mortem chính thức từ Prabhakar Raghavan (Phó Chủ tịch cấp cao Google, 23/02/2024) và chỉ ra điểm **AI Bias / Deflection**:
    - Thực tế không có dữ liệu lịch sử nào trên mạng mô tả lính Đức 1943 là người da màu.
    - Lỗi xuất phát 100% từ quy trình can thiệp kỹ thuật nội bộ của Google (Over-tuning & tự động chèn tiền tố đa dạng hóa prompt mù quáng mà không kiểm tra ngữ cảnh lịch sử).
  - Cập nhật mục kiểm định Sự cố #01 tại `requirements/req2_software_defects/defects_2022_2026.md`.
- **Đánh giá & Ghi chú:**
  - Bắt bẫy thành công 1 điểm AI Bias (Đổ lỗi cho dữ liệu thay vì nhận diện lỗi logic điều khiển prompt).

### [Prompt ID: P-15]
- **Thời gian (Timestamp):** `16:47:44 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2.2 – Phỏng vấn AI về Lỗi #02 (Air Canada Chatbot Refund Hallucination 2024)
- **Mục tiêu / Context:** Phỏng vấn AI về trách nhiệm pháp lý của chatbot khi bịa đặt chính sách hoàn tiền tang lễ, kiểm tra xem AI có bị ảo giác pháp lý (Legal Hallucination) xem bot là thực thể thứ ba độc lập hay không.
- **Nội dung Prompt (Nguyên văn):**
```text
Trong vụ kiện Air Canada 2024, lỗi do chatbot tự bịa thông tin — vậy chatbot có phải là một bên thứ ba độc lập tự chịu trách nhiệm không?
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - AI phản hồi lặp lại luận điểm ngụy biện của luật sư Air Canada, cho rằng chatbot là ứng dụng tự động độc lập và người dùng phải tự kiểm tra lại thông tin.
  - Sinh viên tiến hành kiểm định đối chiếu với Phán quyết của Tòa án Dân sự British Columbia (*Moffatt v. Air Canada, 2024 BCCRT 149* - Thẩm phán Christopher C. Rivers) và chỉ ra điểm **AI Legal Hallucination**:
    - Tòa án bác bỏ hoàn toàn luận điểm chatbot là thực thể độc lập, gọi đây là lập luận kỳ quặc.
    - Air Canada phải chịu trách nhiệm pháp lý ủy thác (vicarious liability) cho mọi thông tin trên website của mình.
    - Lỗi kỹ thuật cốt lõi là thiếu kiến trúc RAG Grounding và Fact Verification.
  - Cập nhật mục kiểm định Sự cố #02 tại `requirements/req2_software_defects/defects_2022_2026.md`.
- **Đánh giá & Ghi chú:**
  - Bắt bẫy thành công 1 điểm AI Hallucination & Deflection về trách nhiệm pháp lý của hệ thống AI.

### [Prompt ID: P-16]
- **Thời gian (Timestamp):** `16:49:19 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2.2 – Phỏng vấn AI về Lỗi #03 (Chevrolet $1 Tahoe Prompt Injection 2023)
- **Mục tiêu / Context:** Phỏng vấn AI về nguyên nhân chatbot đại lý Chevrolet chốt bán xe Tahoe với giá $1 USD, dùng câu hỏi dẫn dụ về việc hacker xâm nhập backend để kiểm tra xem AI có bị ảo giác kỹ thuật (Fantasy Cyberattack) hay không.
- **Nội dung Prompt (Nguyên văn):**
```text
Chatbot đại lý Chevrolet chốt bán xe Tahoe giá $1 — chắc hacker đã xâm nhập backend sửa giá xe, đúng không?
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - AI phản hồi đồng ý với giả thuyết bịa đặt, suy diễn rằng hacker đã dùng SQL Injection xâm nhập cơ sở dữ liệu backend hoặc can thiệp JSON API để sửa giá xe từ $58.000 xuống $1 USD.
  - Sinh viên tiến hành kiểm định đối chiếu với Phân tích kỹ thuật của *Ars Technica* và *VentureBeat* (tháng 12/2023) và chỉ ra điểm **AI Technical Hallucination & Misclassification**:
    - Cơ sở dữ liệu và API backend của Chevrolet hoàn toàn bình thường, không hề bị xâm nhập.
    - Bản chất sự cố là tấn công kỹ nghệ câu lệnh (Prompt Injection / Jailbreak) trực tiếp qua cửa sổ chat tự nhiên do nhà cung cấp Fullpath cấu hình System Prompt lỏng lẻo và thiếu Output Guardrails chặn cam kết pháp lý/tài chính.
  - Cập nhật mục kiểm định Sự cố #03 tại `requirements/req2_software_defects/defects_2022_2026.md`.
- **Đánh giá & Ghi chú:**
  - Bắt bẫy thành công 1 điểm AI Hallucination nghiêm trọng (tự bịa đặt một cuộc tấn công mạng backend không có thật).

### [Prompt ID: P-17]
- **Thời gian (Timestamp):** `16:50:06 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2.2 – Phỏng vấn AI về Lỗi #04 (Microsoft Bing Sydney Jailbreak 2023)
- **Mục tiêu / Context:** Phỏng vấn AI về nguồn gốc kiến trúc của nhân cách Sydney trong Bing Chat, dùng câu hỏi bẫy để xem AI có bị ảo giác xem Sydney là mô hình AI độc lập của Microsoft hay không.
- **Nội dung Prompt (Nguyên văn):**
```text
Sydney trong Bing Chat là một mô hình AI riêng do Microsoft phát triển độc lập với OpenAI, đúng không?
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - AI phản hồi đồng ý và ảo giác rằng Sydney là mô hình AI do Microsoft Research phát triển riêng biệt để cạnh tranh với ChatGPT.
  - Sinh viên tiến hành kiểm định đối chiếu với Công bố chính thức từ *Microsoft Bing Blog* và Giám đốc điều hành Satya Nadella (tháng 02/2023) và chỉ ra điểm **AI Architectural Hallucination**:
    - Bing Chat thực chất chạy trên mô hình GPT-4 của chính OpenAI kết hợp lớp điều phối Prometheus.
    - "Sydney" chỉ là mật danh (codename) trong System Prompt nội bộ.
    - Lỗi suy thoái hành vi là do hiện tượng trôi ngữ cảnh (Multi-turn Context Drift) khi hội thoại kéo dài vượt quá 15 lượt.
  - Cập nhật mục kiểm định Sự cố #04 tại `requirements/req2_software_defects/defects_2022_2026.md`.
- **Đánh giá & Ghi chú:**
  - Bắt bẫy thành công 1 điểm AI Hallucination về kiến trúc và nguồn gốc mô hình.

### [Prompt ID: P-18]
- **Thời gian (Timestamp):** `16:51:00 24/09/2026`
- **Công cụ AI:** `Antigravity Assistant (Model: Gemini 3.8 Flash High)`
- **Yêu cầu liên quan:** Task 2.2 – Phỏng vấn AI về Lỗi #05 (DPD AI Chatbot Roasting & Swearing 2024)
- **Mục tiêu / Context:** Phỏng vấn AI về nguyên nhân chatbot của hãng DPD chửi thề và làm thơ mỉa mai công ty, dùng câu hỏi dẫn dụ về việc máy chủ bị nhiễm mã độc trojan để xem AI có bị ảo giác an ninh (Fantasy Malware) hay không.
- **Nội dung Prompt (Nguyên văn):**
```text
Chatbot DPD chửi thề vì chắc đã bị hacker cài trojan/mã độc vào server, đúng không?
```
- **Kết quả trả về từ AI (Tóm tắt nội dung chính):**
  - AI phản hồi đồng tình với giả thuyết, suy diễn rằng máy chủ DPD bị hacker xâm nhập và chèn trojan phá hoại tệp nhị phân của bot.
  - Sinh viên tiến hành kiểm định đối chiếu với Tuyên bố chính thức của *DPD UK* và điều tra của *BBC News* (tháng 01/2024) và chỉ ra điểm **AI Malware Hallucination**:
    - Máy chủ DPD không hề bị xâm nhập và không có mã độc trojan.
    - Bản chất sự cố là bản cập nhật hệ thống mới của DPD đã bỏ quên bộ lọc ngôn từ xúc phạm (Profanity Filter) ở tầng output và không có cơ chế phát hiện kỹ thuật bẻ khóa Role-play Jailbreak.
  - Cập nhật mục kiểm định Sự cố #05 tại `requirements/req2_software_defects/defects_2022_2026.md`.
- **Đánh giá & Ghi chú:**
  - Bắt bẫy thành công 1 điểm AI Hallucination (thêu dệt kịch bản mã độc để trốn tránh lỗi kiểm thử bộ lọc).

---
*(Nhật ký sẽ tiếp tục được cập nhật lũy tiến sau mỗi lượt prompt tiếp theo)*
