# [AI-02] Báo cáo Kiểm định AI (AI Audit Report)

> **Quy định môn học:** Mỗi sản phẩm (artifact) do AI tạo ra (danh sách test case, kịch bản, checklist, sơ đồ mindmap,...) bắt buộc phải có 1 mục đánh giá theo khung chuẩn 5 phần bên dưới. Cuối báo cáo phải có bảng tổng kết tỷ lệ chính xác và kết luận về phạm vi áp dụng AI.

---

## Mẫu Đánh giá 5 Phần (5-Section Template per Artifact)

### Artifact #...: [Tên Sản phẩm - Ví dụ: Sơ đồ tư duy vai trò QA/QC / Bộ 15 Test cases thiết bị]

#### (1) Prompt + Công cụ (Prompt + Tool)
- **Công cụ AI:** `[Ví dụ: ChatGPT 4o / Claude 3.5 Sonnet / Gemini 1.5 Pro / Antigravity / Cursor]`
- **Thời gian thực hiện (Timestamp):** `HH:MM dd/mm/yyyy`
- **Toàn văn Prompt (Full Prompt):**
```text
[Nhập nguyên văn toàn bộ nội dung prompt đã gửi cho AI tại đây]
```

#### (2) Kết quả AI phản hồi (AI Output)
> *Lưu ý: Giữ nguyên văn toàn bộ kết quả AI sinh ra hoặc đính kèm ảnh chụp màn hình viền đỏ có chú thích; không tóm tắt, không viết lại.*
```text
[Dán toàn bộ nội dung trả về của AI ở đây]
```

#### (3) Phán quyết (Verdict)
- **Đánh giá:** `[VALID / INVALID / INCOMPLETE]`
  - `VALID` (Hợp lệ): Đạt chuẩn chuyên môn, chính xác, có thể áp dụng trực tiếp.
  - `INVALID` (Không hợp lệ): Có lỗi sai về kiến thức ISTQB, thông tin bị ảo giác (hallucination) hoặc suy diễn vô căn cứ.
  - `INCOMPLETE` (Chưa đầy đủ): Đúng một phần nhưng thiếu các trường hợp biên quan trọng (edge cases), thiếu bước kiểm tra hoặc thiếu ràng buộc thực tế.

#### (4) Lập luận chuyên môn (Reasoning)
*(Viết từ 2–5 câu đối chiếu và trích dẫn chuẩn xác slide bài giảng môn học hoặc mục tương ứng trong giáo trình ISTQB Foundation Level)*:
- *Dẫn chứng:* ...
- *Phân tích:* ...

#### (5) Sinh viên hiệu chỉnh (Student Fix)
*(Nội dung sau khi sinh viên đã bổ sung, chỉnh sửa hoặc thiết kế lại — làm nổi bật/tô đậm những điểm đã cải tiến so với AI ban đầu)*:
```text
[Nội dung test case / kịch bản / checklist sau khi đã được sinh viên sửa lại hoàn chỉnh]
```

---

## Tổng kết Tỷ lệ Chính xác & Phạm vi Sử dụng AI (AI Accuracy & Usage Summary)

### Bảng Thống kê Tỷ lệ Chính xác
| Loại đánh giá | Số lượng Artifacts | Tỷ lệ (%) |
| :--- | :---: | :---: |
| **VALID (Hợp lệ)** | ... | ... % |
| **INVALID (Không hợp lệ)** | ... | ... % |
| **INCOMPLETE (Chưa đầy đủ)** | ... | ... % |
| **Tổng cộng** | **100%** |

### Kết luận: Khi nào NÊN và KHÔNG NÊN sử dụng AI trong Kiểm thử QA/QC?
* **Khi NÊN sử dụng AI:**
  - ...
* **Khi KHÔNG NÊN sử dụng AI:**
  - ...
