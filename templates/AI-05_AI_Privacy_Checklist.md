# [AI-05] Bảng Kiểm Tra Quyền Riêng Tư & Sử Dụng AI Có Trách Nhiệm
*(Privacy & Responsible AI Use Checklist)*

Bài tập: **HW01: QA/QC Jobs · 20 Defects · Test a Physical Product**  
Sinh viên thực hiện: **[Họ và tên sinh viên]** – MSSV: **[StudentID]**

---

## Danh mục Kiểm tra Tuân thủ (Checklist)

| STT | Tiêu chí Kiểm tra | Trạng thái (Đạt / Không đạt) | Ghi chú minh chứng |
| :---: | :--- | :---: | :--- |
| **1** | **Bảo vệ Dữ liệu Cá nhân & Nhạy cảm (PII):** Không đưa các dữ liệu cá nhân bí mật (mật khẩu, khóa API bí mật, thông tin tài khoản ngân hàng, thông tin cá nhân của người khác) vào prompt của AI. | `[X] ĐẠT` | Chỉ dùng thông tin sản phẩm công khai và tài liệu học thuật. |
| **2** | **Che giấu Thông tin Thiết bị (Masking Serial):** Đã che tối thiểu 4 ký tự ở giữa của số sê-ri thiết bị vật lý khi chụp ảnh và đưa vào báo cáo. | `[X] ĐẠT` | Số Serial dạng `SN-1234****9876`. |
| **3** | **Tôn trọng Bản quyền & Nguồn gốc Dữ liệu:** Các tin tuyển dụng và bài báo cáo lỗi phần mềm đều có nguồn dẫn (URL) rõ ràng, không sao chép trái phép. | `[X] ĐẠT` | Trích dẫn đầy đủ URL chính thức. |
| **4** | **Phòng ngừa và Phát hiện Ảo giác (Hallucination Control):** Mọi thông tin do AI cung cấp đều được kiểm chứng chéo với tài liệu gốc (Whitepaper, Post-mortem, ISTQB Syllabus). | `[X] ĐẠT` | Đã chỉ ra 20 điểm ảo giác/thiên vị của AI trong Yêu cầu 2. |
| **5** | **Không sử dụng Deepfake / AI giả mạo danh tính:** Video demo kiểm thử sử dụng giọng đọc thật của chính sinh viên, hình ảnh chụp thật không qua AI generated. | `[X] ĐẠT` | Video có giọng thuyết minh thật của sinh viên. |

---

## Xác nhận của Sinh viên
Tôi xác nhận đã đọc, hiểu và tuân thủ nghiêm ngặt toàn bộ các tiêu chí trong Bảng kiểm tra Quyền riêng tư và Sử dụng AI có trách nhiệm trên.

*TP. Hồ Chí Minh, ngày ..... tháng ..... năm 2026*  
**Sinh viên xác nhận**  
*(Ký và ghi rõ họ tên)*  


_________________________________  
**[Họ và tên sinh viên]**
