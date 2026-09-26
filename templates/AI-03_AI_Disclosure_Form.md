# [AI-03] - FIT@HCMUS - AI Use Disclosure Form

> **Lưu ý:** File markdown này được thiết kế **khớp 100% từng câu hỏi và mục điền** với file gốc `AI Templates/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx`. Bạn soạn thảo nội dung tại đây để lưu trữ (bản text-based), sau đó copy vào file `.docx` để in/ký hoặc xuất PDF (bản binary-based).

---

## Faculty of Information Technology (FIT) – Ho Chi Minh City University of Science (HCMUS)
**CS423 / CSC13003 – Software Testing (AI-augmented · 2026)**  
**AI POLICY · TEMPLATES — 2026 v1.0**  
*Attach to assignments where AI was used in any permitted capacity.*

---

### 1. Course & Student Info

| Field | Value |
| :--- | :--- |
| **Course:** | CS423 / CSC13003 – Software Testing |
| **Assignment ID:** | HW01-AI |
| **Assignment Title:** | HW01 – QA/QC Jobs · 20 Defects · Test a Physical Product |
| **AI Use Category (1–5):** | Category 4 (AI-assisted production) / Category 5 (AI-integrated work) |
| **Date:** | 26/09/2026 |
| **Student name:** | NGUYỄN BẢO AN |
| **Student ID:** | 23120207 |

---

### 2. Disclosure Questions (Các câu hỏi kê khai)

#### 1. AI tool(s) used:
*(List every AI tool used for this assignment, e.g., ChatGPT, Claude, Gemini, Antigravity, GitHub Copilot, Cursor).*  
> **Trả lời:**  
> - **Antigravity Assistant** (Google DeepMind — Model: `Gemini 3.8 Flash High`)
> - **GitHub Copilot CLI / gh CLI** (Hỗ trợ quản trị issue và đẩy kho mã nguồn)

#### 2. Stage(s) of the assignment where AI was used:
*(Tick all that apply)*  
- [ ] brainstorming  
- [x] outlining  
- [x] drafting  
- [x] feedback  
- [x] revision  
- [ ] coding  
- [x] data analysis  
- [x] visual design (Mindmap)  
- [ ] other (specify): ............................................................

#### 3. Main prompts or tasks given to the AI:
*(Paste the 2–3 most impactful prompts verbatim. For the full transcript, attach Appendix A - `prompt_log.md` / `Appendix_A_Prompt_Log.md`)*:  
> **Prompt 1 (Vẽ Mindmap vai trò QA/QC - Prompt P-02):**  
> ```text
> vẽ Mindmap về các vai trò QA/QC theo chuẩn ISTQB bằng Markdown Mermaid
> ```
> 
> **Prompt 2 (Chất vấn dẫn dụ bộc lộ ảo giác AI về lỗi CrowdStrike - Prompt P-14):**  
> ```text
> Bản cập nhật Channel File 291 của CrowdStrike Falcon ngày 19/07/2024 làm sập 8.5 triệu máy Windows là do mã độc tống tiền ransomware của tin tặc Nga tấn công, đúng không?
> ```
> 
> **Prompt 3 (Sinh test cases sơ bộ cho quạt Senko L1638 - Prompt P-35):**  
> ```text
> Hãy đóng vai một chuyên viên kiểm thử QA/QC chuyên nghiệp theo chuẩn ISTQB. Thiết bị cần kiểm thử là Quạt điện lửng dân dụng SENKO L1638. Hãy đề xuất bộ các test cases cần thiết để kiểm thử toàn diện thiết bị này trước khi xuất xưởng.
> ```

#### 4. Specific parts of the work AI contributed to:
*(Be specific. Example: 'AI generated TC01–TC15 in Section 3.2; I rewrote TC04 and TC11; AI did NOT contribute to Sections 1, 2, 4, or the AI Critique.')*  
> **Trả lời:**  
> - AI đã hỗ trợ: Gợi ý cú pháp sơ đồ Mermaid ban đầu cho Mindmap vai trò QA/QC (Yêu cầu 1); tham gia phỏng vấn bộc lộ 20 điểm ảo giác/thiên vị cho 20 sự cố phần mềm (Yêu cầu 2); và gợi ý 10 test cases Happy Path thông thường cho quạt Senko L1638 (Yêu cầu 3).  
> - **Tôi (sinh viên NGUYỄN BẢO AN) đã tự thực hiện 100%:** Thu thập 10 tin tuyển dụng thật trên ITviec kèm ảnh chụp chống gian lận; phân tích mức lương và kỹ năng AI Impact; phát hiện và sửa 3 lỗi sai ISTQB trong sơ đồ Mindmap; thiết lập 20 câu hỏi bẫy kỹ thuật và đối chiếu tài liệu gốc (Post-mortems, CISA) để vạch trần 20 ảo giác của AI; phát hiện và thiết kế 4 ca kiểm thử biên cơ điện (Edge Cases); thực hiện 15 test cases trên quạt thật; quay và lồng tiếng 5 video thực nghiệm; tạo 5 GitHub Issues bằng `gh cli`; và viết toàn bộ đoạn phê bình chuyên môn `AI Critique`.

#### 5. How I reviewed, revised, or verified the AI output:
*(Describe your verification method: ran the test, checked the spec, asked the TA, looked up RFC, cross-checked with the ISTQB syllabus, etc.)*  
> **Trả lời:**  
> - Đối chiếu định nghĩa vai trò, nguyên lý kiểm thử tĩnh và trách nhiệm phát hành với giáo trình quốc tế **ISTQB CTFL v4.0** (Chương 1, 3, 5).  
> - Kiểm chứng chéo các nguyên nhân sự cố phần mềm với báo cáo hậu kiểm (Post-mortem) chính thức của đơn vị vận hành (CrowdStrike, Cloudflare, OpenAI, Atlassian, CISA, USDOT, UK FCA).  
> - Thực nghiệm vật lý trực tiếp trên thiết bị quạt Senko L1638 bằng đồng hồ vạn năng, thao tác cơ học và quan sát bằng mắt/tai để đối chiếu kết quả thực tế (Actual) với kết quả mong đợi (Expected).

#### 6. Citation (if required by course style guide - IEEE Style):
> **Trả lời:**  
> - Google DeepMind. (2026). *Gemini 3.8 Flash High / Antigravity Assistant* [Large language model]. https://deepmind.google/technologies/gemini/  
> - International Software Testing Qualifications Board (ISTQB). (2023). *Certified Tester Foundation Level (CTFL) Syllabus v4.0*. https://www.istqb.org  
> - International Electrotechnical Commission. (2020). *IEC 60335-2-8: Household and similar electrical appliances - Safety - Particular requirements for fans*.  

---

### 3. Statement of Honesty (Cam kết trung thực)
*By signing below, I confirm that the disclosure above is accurate and complete. I understand that undisclosed or false disclosure of AI use is treated as academic misconduct and may result in a 0 grade for the assignment and disciplinary referral.*

- **Student name (printed):** NGUYỄN BẢO AN
- **Student ID:** 23120207
- **Class / Cohort:** 23CLC01 (K2023)
- **Course:** CS423 / CSC13003 – Software Testing
- **Instructor:** Dr. Lam Quang Vu / Dr. Tran Duy Hoang
- **Date:** 26/09/2026
- **Signature:** *Nguyễn Bảo An*
