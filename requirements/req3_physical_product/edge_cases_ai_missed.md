# Yêu Cầu 3: Các Trường Hợp Biên AI Bỏ Sót (Edge Cases AI Could NOT Find)

> **Ràng buộc:** Phải có ít nhất **$\ge 3$ test cases là edge cases mà AI KHÔNG THỂ tìm ra**.  
> Sinh viên phải cung cấp **CẢ HAI**:  
> (a) Ảnh chụp màn hình đoạn chat với AI chứng minh AI không sinh ra các test cases này.  
> (b) Lời giải thích kỹ thuật bằng văn bản lý do vì sao AI lại bỏ sót.

---

## 1. Edge Case #1: [Tên kịch bản kiểm thử biên #1]
* **Mô tả kịch bản:** [Ví dụ: Rút phích cắm đột ngột khi thiết bị đang ở đỉnh chu trình gia nhiệt, sau đó cắm lại sau 2 giây]
* **Bằng chứng AI không sinh ra được (Evidence):**
  - Prompt gửi cho AI: `[Prompt yêu cầu sinh toàn bộ test cases cho thiết bị]`
  - Ảnh chụp màn hình kết quả AI: Đính kèm hình ảnh đoạn chat chứng minh AI chỉ sinh ra các luồng thông thường (Normal / Happy path) hoặc các lỗi giao diện cơ bản.
* **Giải thích chuyên môn vì sao AI bỏ sót (Root cause explanation):**
  - *Phân tích:* AI (LLM) được huấn luyện chủ yếu trên văn bản sách hướng dẫn sử dụng (User Manual) và các tài liệu mô tả tính năng lý tưởng. Các trường hợp lỗi vật lý gián đoạn nguồn đột ngột, độ trễ tụ điện xả nguồn (capacitive discharge delay), và trạng thái bộ nhớ đệm EEPROM không được ghi rõ trong sách hướng dẫn nên AI không có dữ liệu để suy diễn.

---

## 2. Edge Case #2: [Tên kịch bản kiểm thử biên #2]
* **Mô tả kịch bản:** [Ví dụ: Nhấn giữ đồng thời 2 nút chức năng xung đột trong trạng thái đang khóa an toàn]
* **Bằng chứng AI không sinh ra được:**
  - ...
* **Giải thích chuyên môn vì sao AI bỏ sót:**
  - *Phân tích:* ...

---

## 3. Edge Case #3: [Tên kịch bản kiểm thử biên #3]
* **Mô tả kịch bản:** [Ví dụ: Vận hành thiết bị khi nhiệt độ vỏ ngoài đang quá nhiệt do vừa hoàn thành chu trình trước đó mà không có nước bên trong]
* **Bằng chứng AI không sinh ra được:**
  - ...
* **Giải thích chuyên môn vì sao AI bỏ sót:**
  - *Phân tích:* ...
