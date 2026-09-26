### 1. Thông Tin Chung (Defect Metadata)
- **Defect ID:** `DEF-05`
- **Thiết bị:** Quạt điện lửng SENKO L1638 (Sản xuất: 09/2023)
- **Mức độ nghiêm trọng (Severity):** High / Electrical Fire Safety Hazard
- **Khả năng tái hiện (Reproducibility):** 100% khi nhấn hờ phím khoảng 50% hành trình
- **Mã kiểm thử liên quan:** `TC-15 (Edge Case #4 - AI Missed)`
- **Video minh chứng (YouTube Unlisted):** `[Dán link Video 5 của sinh viên tại đây]`

---

### 2. Mô Tả Khiếm Khuyết (Defect Description)
Khi người dùng ấn nhẹ phím tốc độ (ví dụ: Số 1 hoặc Số 2) một cách hời hợt hoặc chậm rãi, chỉ đi được khoảng 50% hành trình (nhấn hờ - feather touch) mà không ấn dứt khoát qua điểm lẫy đàn hồi:
- Khoảng cách giữa 2 lá đồng tiếp điểm nằm ở ngưỡng cực nhỏ (Micro air gap).
- Điện áp lưới xoay chiều 220VAC kích hoạt hiện tượng **phóng hồ quang điện liên tục (Sustained Electrical Arcing)** giữa các tiếp điểm.
- Xuất hiện tia lửa điện màu xanh tím phát sáng chập chờn bên trong khe nút bấm, kèm theo tiếng nổ lách tách / xì xì (*arcing sizzle*) kéo dài và bốc mùi khét nhẹ của nhựa bị nhiệt độ hồ quang đốt nóng.
- Động cơ quạt bị cấp điện ngắt quãng chập chờn, phát tiếng rên giật cục, tiềm ẩn nguy cơ gây cháy nổ cụm phím nhựa và chập điện gia đình.

---

### 3. Các Bước Tái Hiện Lỗi (Steps to Reproduce)
1. Cắm quạt Senko L1638 vào ổ cắm nguồn điện 220V.
2. Thực hiện trong phòng tối hoặc góc thiếu sáng để dễ quan sát tia lửa điện.
3. Dùng đầu ngón tay ấn nhẹ phím Số 1 từ từ, dừng lại khi phím lún khoảng 50% hành trình (vừa chạm lá đồng nhưng chưa nảy lẫy gài).
4. Giữ nguyên vị trí ngón tay trong 5 giây.
5. Quan sát qua khe hở của vỏ nút bấm và lắng nghe âm thanh phóng điện.

---

### 4. Kết Quả Kỳ Vọng (Expected Result)
Theo tiêu chuẩn an toàn công tắc cơ điện gia dụng (IEC 61058-1 / TCVN 7826):
- Cụm công tắc phải có cơ chế nhảy tiếp điểm nhanh (Snap-action mechanism / Over-center spring): Tiếp điểm đóng hoặc ngắt tức thì với tốc độ không phụ thuộc vào tốc độ ngón tay người bấm, triệt tiêu hoàn toàn hồ quang điện.
- Hoặc vỏ buồng dập hồ quang phải kín hoàn toàn chống cháy lan.

---

### 5. Kết Quả Thực Tế (Actual Result)
- Không có cơ cấu nhảy nhanh lò xo điểm chết. Tiếp điểm đồng di chuyển tịnh tiến theo ngón tay người bấm (Slow-make, slow-break).
- Sinh hồ quang điện liên tục nổ lép bép, tia lửa xanh tím phát sáng rực rỡ trong khe phím bấm, bề mặt tiếp điểm đồng bị oxy hóa đen và nhựa chân phím bị chảy xém mùi khét nồng.

---

### 6. Phân Tích Nguyên Nhân Gốc Rễ (Root Cause Analysis - RCA)
- **Thiết kế công tắc cơ giá rẻ (Cheap Push-button Switch Design):** Dãy phím cơ Senko L1638 sử dụng tiếp điểm trượt lá đồng uốn đơn giản dạng thanh lưỡi gà (Spring-loaded sliding leaf contacts). Loại tiếp điểm này không có lò xo tích lực để bật dứt khoát (thiếu Snap-action toggle), tạo ra một vùng chết chuyển tiếp (Dead zone) nguy hiểm ở giữa hành trình.

---

### 7. Đề Xuất Giải Pháp Khắc Phục (Suggested Fix)
1. Thay thế cụm công tắc cơ bằng loại có cơ chế lẫy bật lò xo quá tâm (Over-center snap-action switch assembly).
2. Sử dụng vật liệu nhựa chống cháy tiêu chuẩn UL94-V0 cho toàn bộ vỏ cụm phím bấm để ngăn ngừa nguy cơ bén lửa khi có hồ quang.
