### 1. Thông Tin Chung (Defect Metadata)
- **Defect ID:** `DEF-03`
- **Thiết bị:** Quạt điện lửng SENKO L1638 (Sản xuất: 09/2023)
- **Mức độ nghiêm trọng (Severity):** Medium / Mechanical Instability
- **Khả năng tái hiện (Reproducibility):** Thường xuyên (~80% khi chạy quá 20 phút ở 95cm & Số 3)
- **Mã kiểm thử liên quan:** `TC-14 (Edge Case #3 - AI Missed)`
- **Video minh chứng (YouTube Unlisted):** `[Dán link Video 3 của sinh viên tại đây]`

---

### 2. Mô Tả Khiếm Khuyết (Defect Description)
Khi quạt được kéo dài ống rút lên độ cao tối đa (95 cm), vặn siết van ren nhựa ở mức tay thông thường của người tiêu dùng (~1.5 Nm) và vận hành liên tục ở Tốc độ Số 3 kết hợp túp-năng đảo hướng trên bề mặt sàn gạch men trơn bóng:
- Lực khí động của cánh quạt 39cm và dao động lệch tâm của motor tạo ra hiện tượng cộng hưởng cơ học (Resonance vibration) qua cánh tay đòn 95cm.
- Dao động cộng hưởng liên tục làm biến dạng vi mô vòng ren siết nhựa, dẫn đến hiện tượng trôi ren (vibration-induced thread loosening).
- Thân ống sắt quạt bị tụt sụt đột ngột từ 95 cm xuống 83 cm; đồng thời chân đế quạt bị trôi trượt xoay lệch khoảng 4 cm trên mặt sàn gạch men, tiềm ẩn rủi ro mất cân bằng đổ ngã quạt.

---

### 3. Các Bước Tái Hiện Lỗi (Steps to Reproduce)
1. Kéo ống sắt rút của quạt Senko L1638 lên độ cao cực đại (95 cm).
2. Dùng lực tay vặn van siết ren nhựa theo chiều kim đồng hồ vừa khít (~1.5 Nm).
3. Đặt quạt trên nền sàn gạch men bóng phẳng.
4. Bật quạt ở Tốc độ Số 3 và nhấn túp-năng đảo hướng.
5. Để quạt vận hành liên tục trong 30 phút.
6. Quan sát độ cao của quạt và vị trí của chân đế sau mỗi 10 phút.

---

### 4. Kết Quả Kỳ Vọng (Expected Result)
- Van siết ren phải có vòng đệm cao su hoặc cơ chế khóa hãm chống xoay tự do (Anti-slip locking collet).
- Độ cao quạt phải duy trì ổn định ở mức 95 cm trong suốt thời gian vận hành; đế quạt có các đệm mút cao su chống trượt bám chắc vào sàn.

---

### 5. Kết Quả Thực Tế (Actual Result)
- Sau 22 phút vận hành, van siết ren nhựa bị lỏng dần, thân quạt tự động sụt lún xuống còn 83 cm.
- Chân đế nhựa thiếu đệm cao su có độ bám dính cao nên bị rung lắc làm xê dịch trôi trượt 4 cm so với vị trí đánh dấu ban đầu.

---

### 6. Phân Tích Nguyên Nhân Gốc Rễ (Root Cause Analysis - RCA)
- **Vật liệu van ren siết:** Đai ốc siết bằng nhựa polypropylene (PP) có độ đàn hồi cao và hệ số ma sát trượt thấp trên bề mặt ống sắt mạ chrome. Khi gặp rung động tuần hoàn, ren nhựa dễ bị hiện tượng trôi ren (thread creep).
- **Trọng lượng chân đế:** Chân đế quạt lửng phân bố trọng lượng chủ yếu ở mâm nhựa mỏng, không có khối gang đối trọng đủ nặng để hạ thấp trọng tâm khi quạt vươn cao 95cm.

---

### 7. Đề Xuất Giải Pháp Khắc Phục (Suggested Fix)
1. Bổ sung một vòng đệm khía cao su nitrile (Rubber compression sleeve) bên trong khớp ren để tăng ma sát tĩnh và hấp thụ xung chấn rung động.
2. Thêm 4 chân đế cao su chống rung (Anti-vibration rubber pads) dưới đáy mâm quạt.
