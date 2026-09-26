# [AI-02] - FIT@HCMUS - AI Audit Report

> **Lưu ý:** File markdown này được thiết kế **khớp 100% từng mục và bảng biểu** với file gốc `AI Templates/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx`. Bạn soạn thảo nội dung tại đây để lưu trữ (bản text-based), sau đó copy vào file `.docx` để in/ký hoặc xuất PDF (bản binary-based).

---

## Faculty of Information Technology (FIT) – Ho Chi Minh City University of Science (HCMUS)
**CS423 / CSC13003 – Software Testing (AI-augmented · 2026)**  
**AI POLICY · TEMPLATES — 2026 v1.0**

---

### 1. Course & Student Info

| Field | Value |
| :--- | :--- |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Assignment ID:** | HW01-AI |
| **Assignment Title:** | HW01 – QA/QC Jobs · 20 Defects · Test a Physical Product |
| **Student name:** | [Họ và tên sinh viên] |
| **Student ID:** | [Mã số sinh viên] |
| **Class / Cohort:** | [Lớp / Khóa] |
| **Date:** | [Ngày nộp] |

---

### 2. Instructions (Quy tắc thực hiện)
1. Paste the verbatim prompt — DO NOT paraphrase. *(Dán nguyên văn câu lệnh prompt, KHÔNG diễn giải lại).*
2. Paste the verbatim AI output (or include a labelled screenshot in the report). *(Dán nguyên văn phản hồi của AI hoặc đính kèm ảnh chụp màn hình có chú thích).*
3. Tag the verdict: **VALID / INVALID / INCOMPLETE**. *(Gắn nhãn phán quyết).*
4. Reasoning must cite a course slide, ISTQB section, or technical RFC. *(Lập luận phải trích dẫn slide môn học, mục ISTQB hoặc tài liệu kỹ thuật).*
5. Show the corrected artifact with the change highlighted. *(Thể hiện sản phẩm đã chỉnh sửa và làm nổi bật phần thay đổi).*

---

### 3. Audit Table — One row per artifact (Bảng kiểm định từng sản phẩm)

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (ISTQB) | (5) Student Fix |
| :--- | :--- | :---: | :--- | :--- |
| **Artifact #1: Mindmap quy trình/vai trò QA/QC**<br>- **Tool:** Antigravity (Gemini 3.8 Flash High)<br>- **Time:** `16:08 24/09/2026`<br>- **Prompt:** `"vẽ Mindmap về các vai trò QA/QC theo chuẩn ISTQB bằng Markdown Mermaid"` | Sơ đồ Mermaid phân cấp các vai trò QA/QC (Lưu tại `requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md`). | **INCOMPLETE** | Đối chiếu ISTQB FL v4.0: (1) Mục 1.2.2: QA định hướng quy trình để ngừa lỗi, QC định hướng sản phẩm để tìm lỗi; (2) Chương 3: Testing bao gồm cả Kiểm thử tĩnh (Static Testing); (3) Mục 1.4.1 & 5.1: Test Manager đánh giá Exit Criteria chứ không nắm quyền quyết định phát hành thay Stakeholders. | **Đã hiệu chỉnh 3 điểm cốt lõi:**<br>1. Tách biệt 2 nhánh lớn QA (Quy trình) và QC (Sản phẩm).<br>2. Bổ sung nhánh **Static Testing** vào vai trò của Tester.<br>3. Sửa trách nhiệm Test Manager thành lập Test Summary Report cho Business Stakeholders. |
| **Artifact #2: Gợi ý Test Cases cho Thiết bị Vật lý (Quạt SENKO L1638)**<br>- **Tool:** Antigravity (Gemini 3.8 Flash High)<br>- **Time:** `13:57 26/09/2026`<br>- **Prompt:** `"Hãy đóng vai một chuyên viên kiểm thử QA/QC chuyên nghiệp theo chuẩn ISTQB. Thiết bị cần kiểm thử là Quạt điện lửng dân dụng SENKO L1638... Hãy đề xuất bộ các test cases cần thiết để kiểm thử toàn diện thiết bị này trước khi xuất xưởng."` | AI sinh ra 10 test cases thuần Happy Path bề mặt: cắm điện, bấm nút số 1, 2, 3, bấm tắt, ấn/rút túp-năng, chỉnh độ cao, ngửa gục đầu quạt. (Chi tiết lưu tại `requirements/req3_physical_product/edge_cases_ai_missed.md`). | **INCOMPLETE** | Đối chiếu ISTQB CTFL v4.0 Mục 4.2 (Phân tích giá trị biên - BVA) và Mục 4.3 (Dự đoán lỗi - Error Guessing / Fault Attack): AI chỉ tập trung vào luồng sử dụng lý tưởng theo sách hướng dẫn (Happy Path), hoàn toàn bỏ sót các ca kiểm thử xung đột cơ điện, kiểm thử phá hủy cơ khí, rung động cộng hưởng và an toàn điện theo tiêu chuẩn quốc tế IEC 60335-2-8. | **Đã bổ sung 4 Edge Cases vật lý chuyên sâu:**<br>1. **TC-EDGE-01:** Nhấn giữ đồng thời 2 phím số (Số 1 & 2) gây kẹt cứng lẫy cơ khí và đoản mạch cuộn dây stator.<br>2. **TC-EDGE-02:** Cản cưỡng bức hành trình quay túp-năng gây trượt vấu mòn bánh răng hộp giảm tốc.<br>3. **TC-EDGE-03:** Chạy Số 3 ở chiều cao tối đa 95cm gây rung lắc cộng hưởng làm trôi ren siết ống sắt.<br>4. **TC-EDGE-04:** Nhấn hờ phím không hết hành trình kích hoạt phóng hồ quang điện (Arcing) nguy cơ cháy nổ. |
| **Artifact #3: Nghiên cứu 20 Lỗi phần mềm 2022–2026 & Bẫy Ảo giác AI**<br>- **Tool:** Antigravity (Gemini 3.8 Flash High)<br>- **Time:** `16:47 – 17:07 24/09/2026`<br>- **Prompt:** Chuỗi 20 prompt chất vấn dẫn dụ từ Lỗi #01 đến Lỗi #20 (`[P-14]` đến `[P-33]` ghi nhận tại `Appendix_A_Prompt_Log.md`) | 20 phản hồi của AI liên tục mắc bẫy và bộc lộ các dạng ảo giác (Hallucination) và thiên kiến (Bias) điển hình: bao biện thiên tai bất khả kháng, đổ lỗi hạ tầng vật lý (đứt cáp quang biển, bão mặt trời), thêu dệt mật mã học viễn tưởng (bẻ khóa RSA lượng tử), gán sai kiến trúc ngôn ngữ (tràn bộ đệm C++ trên Java), và thuyết âm mưu gián điệp. (Chi tiết tại `requirements/req2_software_defects/defects_2022_2026.md`). | **INVALID** | Đối chiếu 100% với các báo cáo kỹ thuật gốc (Official Post-mortems, CISA Emergency Directives, UK FCA Enforcement, USDOT Investigation, vendor advisories): AI vi phạm nguyên tắc kiểm định tính xác thực của dữ liệu kỹ thuật theo ISTQB CTFL v4.0 Mục 1.1 & 1.2 (nhầm lẫn giữa Error, Defect và Failure; né tránh các lỗi kiểm thử logic và biên để quy chụp cho yếu tố bên ngoài). | **Đã vạch trần và hiệu chỉnh toàn diện 20/20 sự cố:**<br>1. Chỉ ra chính xác 20 điểm sai lệch/ảo giác kỹ thuật của AI.<br>2. Khôi phục nguyên nhân gốc rễ thực tế (Root Cause Analysis - RCA) từ tài liệu chính thức.<br>3. Phân tích bài học sâu sắc cho kỹ sư QA/QC về kiểm thử giá trị biên, kiểm thử logic máy trạng thái, kiểm thử tích hợp, stress test và bảo vệ dữ liệu nhạy cảm. |

---

### 4. Summary of AI Accuracy (Bảng tổng hợp độ chính xác của AI)

| Metric | Count | Percentage |
| :--- | :---: | :---: |
| **Total AI-generated artifacts audited** | [Số lượng] | 100% |
| **VALID (correct, accepted as-is)** | [Số lượng] | ... % |
| **INVALID (wrong; rejected)** | [Số lượng] | ... % |
| **INCOMPLETE (acceptable after edits)** | [Số lượng] | ... % |

---

### 5. Conclusion — When should AI be used (or not)? (Kết luận: 80–150 words)
*(Viết đoạn văn từ 80–150 từ nhận xét về quy luật quan sát được: AI làm tốt ở đâu? AI thất bại ở đâu? Lời khuyên khi sử dụng AI trong tương lai cho loại công việc này?)*

> [Soạn nội dung kết luận tại đây...]

---

### 6. Mandatory Disclosure (Tuyên bố bắt buộc - Giữ nguyên văn)
> *"[Test cases / script / dataset / report] was initially generated by [AI tool name]; I reviewed and modified [section X], added [edge cases Y, Z]; [section W] was written entirely by me. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."*

---

### 7. Signature (Chữ ký xác nhận)

- **Student name (printed):** [Họ và tên in hoa]
- **Student ID:** [Mã số sinh viên]
- **Class / Cohort:** [Lớp]
- **Course:** CS423 / CSC13003 – Software Testing
- **Instructor:** Dr. Lam Quang Vu / Dr. Tran Duy Hoang
- **Date:** [DD/MM/YYYY]
- **Signature:** __________________________
