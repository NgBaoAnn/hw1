# Danh Sách 15 Test Cases Kiểm Thử Thiết Bị Vật Lý

> **Yêu cầu:** Thiết kế 15 test cases hoàn chỉnh theo chuẩn ISTQB.  
> **Cột bắt buộc:** Objective / Input / Steps / Expected / Actual / Verdict.  
> **Thực nghiệm:** Quay $\ge 5$ video demo ngắn ($\le 60$s) có giọng nói thuyết minh. Có $\ge 3$ edge cases AI bỏ sót.

---

## Bảng 15 Test Cases

| TC ID | Nhóm kiểm thử | Mục tiêu (Objective) | Dữ liệu đầu vào (Input) | Các bước thực hiện (Steps) | Kết quả mong đợi (Expected) | Kết quả thực tế (Actual) | Đánh giá (Verdict) | Có Video Demo? |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **TC-01** | Khởi động & Nguồn | Kiểm tra đóng cắt điện an toàn | Cắm dây nguồn 220V | 1. Cắm phích<br>2. Quan sát LED | Màn hình sáng, có tiếng bíp báo hiệu | ... | Pass / Fail | [ ] |
| **TC-02** | Chức năng cơ bản | ... | ... | ... | ... | ... | ... | [ ] |
| ... | | | | | | | | |
| **TC-13** | **Edge Case (AI missed)** | Kiểm tra sụt áp / mất điện đột ngột | Rút phích khi đang gia nhiệt | 1. Bật nấu<br>2. Rút phích<br>3. Cắm lại sau 3s | Thiết bị phục hồi trạng thái chu trình nấu tiếp tục, không reset lỗi | ... | ... | [X] Video 1 |
| **TC-14** | **Edge Case (AI missed)** | Nhấn giữ đồng thời nút | Nút A + Nút B giữ 5s | 1. Bật nguồn<br>2. Đè 2 nút cùng lúc | Ưu tiên nút an toàn hoặc bỏ qua tín hiệu xung đột | ... | ... | [X] Video 2 |
| **TC-15** | **Edge Case (AI missed)** | Thao tác khi không có tải | Bật gia nhiệt khi rỗng | 1. Không cho nước<br>2. Bấm bắt đầu | Cảm biến ngắt sau 15s và báo lỗi E01 | ... | ... | [X] Video 3 |

---

## Danh Sách Video Demo Thực Nghiệm (YouTube Unlisted)

1. **Video 1 (TC-13):** `[Link YouTube Unlisted]` (Thời lượng: ... giây) - Nội dung: ...
2. **Video 2 (TC-14):** `[Link YouTube Unlisted]` (Thời lượng: ... giây) - Nội dung: ...
3. **Video 3 (TC-15):** `[Link YouTube Unlisted]` (Thời lượng: ... giây) - Nội dung: ...
4. **Video 4 (TC-...):** `[Link YouTube Unlisted]` (Thời lượng: ... giây) - Nội dung: ...
5. **Video 5 (TC-...):** `[Link YouTube Unlisted]` (Thời lượng: ... giây) - Nội dung: ...
