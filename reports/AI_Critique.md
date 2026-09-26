# Đánh Giá & Phê Bình AI (AI Critique: 200–300 words)

> **Yêu cầu đề bài:** Viết một đoạn văn từ 200–300 từ phê bình AI. AI đã sai, thiên vị hoặc thiếu sót ở đâu? Tại sao AI không phát hiện ra lỗi đó? Bạn rút ra nguyên tắc gì khi cộng tác với AI trong bài tập này?

---

### Phê Bình Chuyên Môn: Năng Lực & Giới Hạn Của AI Trong Kiểm Thử (291 từ)

Trong quá trình thực hiện bài tập kiểm thử HW01, việc kiểm chứng các phản hồi của AI đã bộc lộ những khiếm khuyết hệ thống của mô hình ngôn ngữ lớn (LLM).

Thứ nhất, AI mắc thiên kiến xác nhận (Confirmation Bias) và chứng "xu nịnh" (Sycophancy) nghiêm trọng. Khi sinh viên đưa ra các câu hỏi bẫy có tính dẫn dụ sai lệch về 20 sự cố phần mềm nổi tiếng (như quy chụp sự cố CrowdStrike do tin tặc Nga, lỗi Confluence do tràn bộ đệm C++, hay lỗi Citigroup do bot HFT), AI lập tức đồng thuận và thêu dệt các chi tiết kỹ thuật giả mạo có vẻ hợp lý nhưng hoàn toàn sai sự thật (AI Hallucination). AI không có khả năng tự phản biện tiền đề sai.

Thứ hai, trong kiểm thử thiết bị vật lý (quạt Senko L1638), AI chỉ gợi ý các ca kiểm thử bề mặt (Happy Path). AI hoàn toàn bỏ sót các ca biên cơ điện nguy hiểm như kẹt lẫy cơ gây dẫn chéo cuộn stator, trượt vấu bánh răng hộp số, hay phóng hồ quang điện (Arcing). Nguyên nhân là LLM chỉ hoạt động trên xác suất thống kê văn bản tĩnh, thiếu tri giác vật lý (embodiment) và trải nghiệm nhân quả trong thế giới thực.

Nguyên tắc cộng tác rút ra cho kỹ sư QA/QC là: "Zero-Trust AI" (Tuyệt đối không tin tưởng, luôn luôn kiểm chứng). AI chỉ đóng vai trò trợ lý tăng tốc tạo khung tài liệu sơ bộ. Kỹ sư con người bắt buộc phải là chốt chặn kiểm thử tối hậu, luôn đối chiếu chuẩn mực kỹ thuật (ISTQB, RFC, IEC) và trực tiếp thực nghiệm trên thiết bị thật.

---

### Thống Kê & Xác Nhận
- **Độ dài đoạn văn:** 291 từ (thỏa mãn tiêu chí 200–300 từ).
- **Sinh viên thực hiện:** NGUYỄN BẢO AN — MSSV: 23120207
- **Môn học:** CS423 / CSC13003 – Kiểm thử phần mềm (FIT@HCMUS, Khóa 2026)
