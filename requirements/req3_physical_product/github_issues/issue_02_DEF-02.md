### 1. Thông Tin Chung (Defect Metadata)
- **Defect ID:** `DEF-02`
- **Thiết bị:** Quạt điện lửng SENKO L1638 (Sản xuất: 09/2023)
- **Mức độ nghiêm trọng (Severity):** Medium / Hardware Degradation
- **Khả năng tái hiện (Reproducibility):** 100% khi gặp vật cản trong hành trình quay
- **Mã kiểm thử liên quan:** `TC-13 (Edge Case #2 - AI Missed)`
- **Video minh chứng (YouTube Unlisted):** `[Dán link Video 2 của sinh viên tại đây]`

---

### 2. Mô Tả Khiếm Khuyết (Defect Description)
Khi quạt đang vận hành ở chế độ đảo hướng gió (túp-năng đang ấn xuống), nếu lồng quạt va chạm vào chướng ngại vật cố định trong phòng (như mép bàn, góc tường, tủ quần áo) hoặc bị ngoại lực giữ chặt bầu quạt:
- Quạt không có cơ cấu ly hợp trượt bảo vệ an toàn (Slip clutch protection).
- Bộ bánh răng trục vít truyền động giảm tốc bằng nhựa trong hộp số túp-năng bị kẹt và trượt vấu cưỡng bức, phát ra tiếng kêu *cạch... cạch... cạch...* liên tục với âm lượng lớn.
- Sau 30 giây kẹt, các vấu răng nhựa bị mài mòn khuyết góc (Gear stripping), gây hỏng vĩnh viễn tính năng đảo hướng gió tự động.

---

### 3. Các Bước Tái Hiện Lỗi (Steps to Reproduce)
1. Cắm điện và bật quạt ở Tốc độ Số 2.
2. Ấn núm túp-năng xuống để kích hoạt quay quét đảo hướng 180°.
3. Khi đầu quạt đang quay sang bên trái, dùng tay chặn cứng bầu quạt lại trong 30 giây (mô phỏng quạt quay chạm tường).
4. Quan sát chuyển động và lắng nghe âm thanh phát ra từ hộp số sau bầu motor.
5. Thả tay ra và kiểm tra hoạt động quay tiếp theo của túp-năng.

---

### 4. Kết Quả Kỳ Vọng (Expected Result)
Theo tiêu chuẩn an toàn cơ học quạt điện gia dụng (IEC 60335-2-8 / TCVN 7826):
- Bộ truyền động túp-năng phải tích hợp ly hợp trượt ma sát lò xo (Spring-loaded friction slip clutch): Khi mô-men xoắn cản vượt ngưỡng an toàn, trục quay tự trượt trơn nhẹ nhàng mà không làm mẻ vấu bánh răng.
- Hoặc cơ cấu tự động đảo chiều quay khi gặp vật cản.

---

### 5. Kết Quả Thực Tế (Actual Result)
- Bộ bánh răng nhựa không có cơ cấu trượt ly hợp lò xo, bị trượt ép vấu trực tiếp lên nhau phát ra tiếng va đập *cạch... cạch... cạch...* chát chúa.
- Răng nhựa bị mài mòn nhanh chóng, sinh nhiệt ma sát cao làm biến dạng ngàm giữ, dẫn đến hiện tượng sau này quạt quay túp-năng bị giật cục và kẹt góc.

---

### 6. Phân Tích Nguyên Nhân Gốc Rễ (Root Cause Analysis - RCA)
- Để tối ưu hóa chi phí sản xuất quạt dân dụng giá rẻ, nhà sản xuất đã lược bỏ cụm ly hợp trượt lò xo (Slip clutch assembly) trong hộp số túp-năng. Hộp giảm tốc chỉ sử dụng cụm bánh răng trục vít nhựa POM đơn giản gắn cứng với tay đòn biên.

---

### 7. Đề Xuất Giải Pháp Khắc Phục (Suggested Fix)
- Bổ sung đĩa ly hợp ma sát có lò xo ép (Friction clutch with spring tension) trên trục bánh răng túp-năng để tự động trượt bảo vệ khi mô-men cản vượt quá $0.8 \text{ N}\cdot\text{m}$.
