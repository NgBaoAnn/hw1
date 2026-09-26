### 1. Thông Tin Chung (Defect Metadata)
- **Defect ID:** `DEF-04`
- **Thiết bị:** Quạt điện lửng SENKO L1638 (Sản xuất: 09/2023)
- **Mức độ nghiêm trọng (Severity):** Minor / Usability & Ergonomics Defect
- **Khả năng tái hiện (Reproducibility):** ~60% khi đầu quạt ngửa góc cực đại +15° kết hợp túp-năng
- **Mã kiểm thử liên quan:** `TC-09`
- **Video minh chứng (YouTube Unlisted):** `[Dán link Video 4 của sinh viên tại đây]`

---

### 2. Mô Tả Khiếm Khuyết (Defect Description)
Khi người dùng điều chỉnh đầu quạt ngửa lên trên ở góc tối đa (+15°) và vặn ốc cánh bướm cố định, sau đó kích hoạt chế độ quay quét đảo hướng của túp-năng:
- Khi bầu quạt quay quét đến điểm giới hạn cực đại bên phải và bắt đầu đảo chiều quay sang trái, lực quán tính và mô-men xoắn đảo chiều tác động lên bản lề gục/ngửa.
- Ốc hãm cánh bướm bị nới nhẹ, làm đầu quạt bị sụp góc ngửa xuống khoảng 5° (từ +15° xuống còn +10°), khiến hướng gió thổi không còn duy trì đúng như người dùng đã thiết lập ban đầu.

---

### 3. Các Bước Tái Hiện Lỗi (Steps to Reproduce)
1. Đẩy bầu quạt Senko L1638 ngửa lên trên ở nấc khấc lò xo tối đa (+15°).
2. Dùng tay vặn chặt ốc cánh bướm định vị bản lề.
3. Bật quạt chạy ở Tốc độ Số 2 hoặc Số 3.
4. Ấn núm túp-năng để quạt quay đảo hướng.
5. Quan sát góc ngửa của đầu quạt khi quạt đảo chiều tại góc ngoài cùng bên phải qua 5 chu kỳ.

---

### 4. Kết Quả Kỳ Vọng (Expected Result)
Khớp bản lề gục/ngửa phải duy trì góc nghiêng cố định tuyệt đối trong suốt quá trình quạt quay đảo chiều túp-năng, không bị biến dạng góc dưới tác động của lực xoắn đảo chiều.

---

### 5. Kết Quả Thực Tế (Actual Result)
Sau 3 chu kỳ đảo chiều, lực xoắn giật ở điểm biên đã làm lỏng nhẹ khớp hãm, đầu quạt bị sụp xuống 5° và thổi gió thấp hơn vị trí mong muốn.

---

### 6. Phân Tích Nguyên Nhân Gốc Rễ (Root Cause Analysis - RCA)
- Khớp bản lề gục/ngửa sử dụng bề mặt ma sát phẳng bằng nhựa trơn tiếp xúc với kim loại mà không có các răng khía dạng bánh cóc (Ratchet teeth / Serrated locking washer) để khóa góc cơ học. Lực giữ hoàn toàn phụ thuộc vào ma sát siết của ốc cánh bướm, vốn dễ bị nới lỏng khi có dao động xoắn chu kỳ.

---

### 7. Đề Xuất Giải Pháp Khắc Phục (Suggested Fix)
- Bổ sung đệm khía răng cưa (Serrated lock washer) hoặc thiết kế khớp bản lề có các rãnh răng ăn khớp định vị (Positive locking teeth) tại các góc -10°, 0°, +10°, +15°.
