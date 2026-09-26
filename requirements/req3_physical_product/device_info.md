# Yêu cầu 3: Thông Tin Thiết Bị Vật Lý (Physical Product Information)

> **Mục tiêu:** Khai báo đầy đủ thông tin thiết bị gia dụng dùng để kiểm thử thực tế và bằng chứng chống gian lận.

---

## 1. Thông số Kỹ thuật Thiết bị
- **Loại thiết bị:** Quạt điện lửng ống sắt dân dụng (Pedestal / Desk-standing Mechanical Electric Fan)
- **Thương hiệu (Brand):** SENKO (Công ty TNHH Tân Tiến Senko, Việt Nam)
- **Dòng máy (Model):** L1638
- **Năm & Tháng sản xuất (Year/Month):** Tháng 09/2023 (Ghi nhận trên tem kiểm định kỹ thuật dán tại bầu motor quạt)
- **Số sê-ri (Serial Number):** `N/A` *(Dòng quạt cơ dân dụng thông dụng không quản lý bằng số serial định danh cá thể từng chiếc; thiết bị được quản lý chất lượng theo lô sản xuất tháng 09/2023 và tem kiểm định hợp quy CR).*
- **Điện áp & Tần số định mức:** 220V ~ 50Hz
- **Công suất tiêu thụ:** 47W (Tiêu chuẩn hiệu suất năng lượng 5 sao)
- **Thông số khí động học:**
  - Sải cánh: 39 cm (đường kính cánh quạt)
  - Số cánh quạt: 3 cánh cong chất liệu nhựa chịu lực
  - Lưu lượng gió: 64.4 m³/phút
  - Tốc độ gió: 3 cấp độ (Số 1: Nhẹ / Số 2: Vừa / Số 3: Mạnh)
- **Kích thước & Trọng lượng:**
  - Chiều cao điều chỉnh: Linh hoạt từ 77 cm đến 95 cm (nhờ ống sắt rút có van siết ren)
  - Khối lượng tịnh: ~ 3.8 kg
- **Cơ chế điều khiển & Cơ điện:**
  - **Bảng điều khiển:** Dãy 4 phím bấm cơ học dạng trượt liên động (Mechanical interlocking push-button switch assembly) gồm: Phím 0 (Tắt nguồn / Off), Phím 1 (Tốc độ thấp), Phím 2 (Tốc độ trung bình), Phím 3 (Tốc độ cao).
  - **Cơ chế đảo hướng gió (Tuốc-năng / Túp-năng):** Cơ cấu ly hợp cơ học bánh răng giảm tốc (Mechanical reduction gearbox & clutch) dạng núm giật/nhấn đặt tại nắp sau bầu motor; góc xoay đảo hướng ngang ~ 180°.
  - **Cơ chế gục/ngửa góc quạt (Tilt mechanism):** Khớp bản lề cơ có khấc hãm bi lò xo và ốc siết cánh bướm điều chỉnh góc phương vị đứng.
  - **Cơ chế nâng/hạ chiều cao:** Trục ống kim loại lồng kép có vòng ren siết nhựa kỹ thuật định vị.
  - **Tính năng an toàn điện:** Tích hợp cầu chì nhiệt tự ngắt (Thermal Cut-off Fuse) đặt sát cuộn dây stator motor để bảo vệ chống quá nhiệt/cháy khi kẹt cánh; lồng quạt nan kim loại đan khít sơn tĩnh điện chống kẹt ngón tay.

---

## 2. Minh chứng Chống Gian lận (Anti-cheat Evidence)
- **Thông tin sinh viên:** NGUYỄN BẢO AN — MSSV: `23120207` — Lớp/Khóa: 2023 - 2027 — Khoa Công nghệ Thông tin, Trường ĐH Khoa học Tự nhiên, ĐHQG-HCM.
- **File ảnh chụp thiết bị + Thẻ sinh viên chung khung hình:** [`photo/device_23120207.jpg`](photo/device_23120207.jpg) (và bản sao [`photo/device_student_id.jpg`](photo/device_student_id.jpg))
- **Tình trạng kiểm tra của TA:**
  - [x] Thấy rõ sản phẩm vật lý thật (Quạt lửng Senko L1638 với logo SENKO, lồng quạt, bầu motor và đế quạt).
  - [x] Thấy rõ Thẻ sinh viên (Họ tên: NGUYỄN BẢO AN, MSSV: 23120207, ảnh chân dung, logo Trường ĐH KHTN).
  - [x] Cùng nằm trong 1 bức ảnh chụp thực tế rõ nét (không qua chỉnh sửa/cắt ghép kỹ thuật số).

---

## 3. Tổng hợp Khiếm khuyết Phát hiện được (Defects Found)
> Mục tiêu trong đề bài: Hướng tới việc tìm ra **$\ge 5$ lỗi / bất thường** trong quá trình kiểm thử thực tế.

| Defect ID | Tên lỗi phát hiện trên thiết bị | Mức độ nghiêm trọng | Issue Link trên GitHub |
| :---: | :--- | :---: | :--- |
| **DEF-01** | Kẹt tiếp điểm cơ học khi ấn đồng thời 2 phím tốc độ (Số 1 & Số 2) | Major (Nguy cơ đoản mạch) | `https://github.com/.../issues/1` |
| **DEF-02** | Trượt vấu bánh răng tuốc-năng phát tiếng kêu cạch cạch khi bị cản hành trình | Medium (Hao mòn cơ khí) | `https://github.com/.../issues/2` |
| **DEF-03** | Rung lắc mất cân bằng động làm trôi ốc siết nâng hạ khi chạy số 3 ở độ cao tối đa (95cm) | Medium (Rủi ro mất ổn định) | `https://github.com/.../issues/3` |
| **DEF-04** | Lỏng khớp gục đầu quạt khi quay đảo hướng ở góc ngửa cực đại | Minor (Trải nghiệm người dùng) | `https://github.com/.../issues/4` |
| **DEF-05** | Tiếp điểm hờ sinh hồ quang điện (arcing) khi bấm phím số không hết hành trình | High (Nguy cơ an toàn điện) | `https://github.com/.../issues/5` |
