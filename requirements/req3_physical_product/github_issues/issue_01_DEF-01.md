### 1. Thông Tin Chung (Defect Metadata)
- **Defect ID:** `DEF-01`
- **Thiết bị:** Quạt điện lửng SENKO L1638 (Sản xuất: 09/2023)
- **Mức độ nghiêm trọng (Severity):** Major / High Safety Risk
- **Khả năng tái hiện (Reproducibility):** 100% (luôn xảy ra khi ấn lực cân bằng)
- **Mã kiểm thử liên quan:** `TC-12 (Edge Case #1 - AI Missed)`
- **Video minh chứng (YouTube Unlisted):** `[Dán link Video 1 của sinh viên tại đây]`

---

### 2. Mô Tả Khiếm Khuyết (Defect Description)
Khi người dùng vô tình hoặc cố ý dùng 2 ngón tay ấn đồng thời hai phím tốc độ (ví dụ: Số 1 và Số 2) với lực đều nhau, cụm phím bấm cơ học dạng trượt liên động (Mechanical interlocking rocker switch assembly) rơi vào trạng thái kẹt cứng (Deadlock). Cả hai phím đều bị gài ở vị trí đóng tiếp điểm lưng chừng mà không phím nào tự nảy lên để giải phóng phím kia.

Về mặt điện khí, cả hai cuộn dây số 1 (cuộn phụ tốc độ thấp) và cuộn dây số 2 (cuộn phụ tốc độ trung bình) trên cuộn cảm stator motor đồng thời bị cấp điện pha 220VAC. Dòng điện dẫn chéo (Cross-conduction) làm sai lệch từ trường, động cơ phát ra tiếng rên rung từ trường (loud humming noise) rất lớn, cánh quạt quay chậm giật cục và nhiệt độ stator tăng vọt bất thường trong vòng 10 giây.

---

### 3. Các Bước Tái Hiện Lỗi (Steps to Reproduce)
1. Cắm phích cắm quạt Senko L1638 vào nguồn điện xoay chiều 220V.
2. Đặt ngón trỏ lên phím Số 1 và ngón giữa lên phím Số 2 của quạt.
3. Dùng lực ấn dứt khoát và đều tay lên cả 2 phím cùng một lúc.
4. Thả tay ra và quan sát vị trí của 2 phím bấm.
5. Lắng nghe âm thanh động cơ và quan sát chuyển động của cánh quạt.

---

### 4. Kết Quả Kỳ Vọng (Expected Result)
Hệ thống cơ cấu trượt khóa liên động phải có cơ chế ngàm độc quyền (Exclusive toggle latch):
- Chỉ cho phép 1 phím duy nhất chìm xuống và khóa tiếp điểm, phím còn lại phải bị trượt ra hoặc bị chặn lại.
- Hoặc hệ thống phải tự động nhả cả hai phím về vị trí an toàn (Fail-safe release) để bảo vệ cuộn dây stator khỏi quá dòng đoản mạch.

---

### 5. Kết Quả Thực Tế (Actual Result)
- Cả hai phím Số 1 và Số 2 đều bị lún sâu và kẹt cứng vào rãnh trượt, không thể tự nhả nếu không ấn mạnh phím Số 0 để đẩy bung lẫy.
- Động cơ quạt rên to bất thường, cánh quay chậm giật cục, cuộn dây motor nóng lên nhanh chóng, tiềm ẩn nguy cơ nổ cầu chì nhiệt hoặc chập cháy cuộn stator nếu duy trì quá 60 giây.

---

### 6. Phân Tích Nguyên Nhân Gốc Rễ (Root Cause Analysis - RCA)
- **Thiết kế cơ khí (Mechanical Flaw):** Thanh trượt lẫy liên động sử dụng tấm trượt kim loại phẳng đục lỗ đơn giản. Góc xiên của vấu hãm (Cam angle) không đủ dốc để đẩy phím thứ hai ra ngoài khi cả hai phím cùng đi xuống đồng thời, dẫn đến điểm cân bằng lực chết (Mechanical force deadlock).
- **Thiết kế điện khí (Electrical Safety Flaw):** Không có rơ-le ngắt bảo vệ hoặc cơ chế điện tử chống cấp nguồn đa cuộn dây (thiếu Electrical Interlocking).

---

### 7. Đề Xuất Giải Pháp Khắc Phục (Suggested Fix)
1. Cải tiến khuôn dập tấm trượt cơ khí với góc vát cam dốc hơn ($\ge 45^\circ$) để đảm bảo nguyên tắc cơ học: hễ có 1 phím di chuyển thì phím kia bắt buộc bị đẩy bật lên ngay lập tức.
2. Bổ sung gờ phân cách cơ học nổi rõ giữa các nút bấm để giảm thiểu rủi ro ngón tay người dùng bấm đè lên 2 nút cùng lúc.
