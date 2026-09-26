# TÀI LIỆU ÔN TẬP VẤN ĐÁP MIỆNG (ORAL DEFENSE PREPARATION)
## BÀI TẬP HW01 — CS423 / CSC13003 (SOFTWARE TESTING)

---

- **Họ và tên:** NGUYỄN BẢO AN
- **MSSV:** `23120207`
- **Lớp:** `23CLC01`
- **Thời lượng vấn đáp dự kiến:** 5 – 7 phút (dành cho 10–30% sinh viên được bốc thăm ngẫu nhiên)

---

### CÂU HỎI 1: HƯỚNG DẪN THAO TÁC THỰC NGHIỆM TRỰC TIẾP TRÊN THIẾT BỊ VẬT LÝ
> **Câu hỏi của Giảng viên / TA:** *"Em hãy trình bày và làm mẫu lại 1 kịch bản kiểm thử thiết bị vật lý đã tìm ra khiếm khuyết trong bài làm?"*

**Kịch bản chọn trình diễn (TC-12 / DEF-01: Bấm đồng thời 2 phím tốc độ):**
1. **Thiết bị:** Quạt lửng dân dụng SENKO L1638, sản xuất tháng 09/2023.
2. **Thao tác vật lý:**
   - Đặt quạt ở trạng thái cắm nguồn (hoặc tắt nguồn để chỉ rõ cơ cấu cơ khí).
   - Dùng 2 ngón tay nhấn đồng thời phím **Số 1** và phím **Số 2** với lực ấn đều nhau.
3. **Hiện tượng quan sát được (Defect Evidence):**
   - Về mặt cơ khí: Cơ cấu thanh trượt liên động (Interlocking slider) bị kẹt cứng ở vị trí cân bằng lực; hai phím bị mắc kẹt nửa vời không tự nảy lên được (*Mechanical Deadlock*).
   - Về mặt điện khí (khi có điện): Hai cuộn dây stator phân nấc bị cấp nguồn cùng lúc, từ trường cuộn dây bị triệt tiêu một phần, phát ra tiếng gầm ù cơ điện lớn ($> 68$ dBA), dòng điện tiêu thụ tăng vọt và nhiệt độ cuộn dây tăng nhanh, kích hoạt nguy cơ đứt cầu chì nhiệt bảo vệ quá dòng.
4. **Giải pháp kiến nghị (Fix):** Nhà sản xuất cần cải tiến thanh trượt khóa liên động có ngàm gạt vát góc bất đối xứng (Asymmetric rocker interlock) để khi có lực ép đồng thời, một phím bắt buộc phải ưu tiên kích hoạt và đẩy phím kia ra, ngăn chặn tình trạng dẫn chéo dòng điện.

---

### CÂU HỎI 2: CƠ SỞ KỸ THUẬT LỰA CHỌN GIÁ TRỊ ĐẦU VÀO THEO ISTQB
> **Câu hỏi của Giảng viên / TA:** *"Tại sao em lại chọn giá trị biên độ cao 95cm và tốc độ Số 3 trong kịch bản TC-14 thay vì chọn 85cm và Số 2? Cơ sở kỹ thuật theo chuẩn ISTQB là gì?"*

**Câu trả lời chuẩn mực:**
1. **Áp dụng Kỹ thuật Phân tích Giá trị Biên (Boundary Value Analysis - BVA theo ISTQB CTFL v4.0 Mục 4.2.2):**
   - Dải tương đương hợp lệ của độ cao quạt là từ $77\text{ cm}$ đến $95\text{ cm}$.
   - Theo nguyên lý kiểm thử giá trị biên, lỗi hệ thống (đặc biệt là các lỗi cơ học) hầu như luôn xảy ra tại các điểm cực trị (Extreme Boundaries) chứ không xuất hiện ở các giá trị trung gian bình thường ($85\text{ cm}$).
2. **Cơ sở Vật lý & Động lực học:**
   - Chiều cao $95\text{ cm}$ là điểm biên trên cực đại ($Max$). Tại độ cao này, trọng tâm của toàn bộ khối motor và lồng cánh quạt bị đẩy lên cao nhất, tạo ra cánh tay đòn mô-men uốn ($M = F \cdot d$) lớn nhất tác động lên khớp ren siết.
   - Khi kết hợp với tốc độ **Số 3** (tần số quay cực đại $\approx 1.200\text{ RPM}$ sinh lực ly tâm mất cân bằng động lớn nhất), tần số dao động của cánh quạt tiệm cận tần số dao động riêng của thân ống rút, kích hoạt hiện tượng **Rung lắc cộng hưởng (Mechanical Resonance)**.
   - Nhờ chọn đúng giá trị biên cực hạn ($95\text{ cm}$ và Số 3), kịch bản đã kích hoạt thành công khiếm khuyết **DEF-03**: Ren siết nhựa bị trôi lỏng dần và thân quạt tự sụt chiều cao từ $95\text{ cm}$ về $77\text{ cm}$, điều hoàn toàn không xảy ra nếu chỉ test ở $85\text{ cm}$ và Số 2.

---

### CÂU HỎI 3: PHÂN TÍCH 1 LỖI TIÊU BIỂU CỦA AI VÀ CÁCH THỨC HIỆU CHỈNH
> **Câu hỏi của Giảng viên / TA:** *"Trong 20 sự cố phần mềm ở Yêu cầu 2, hãy trình bày chi tiết 1 lỗi mà AI đã bị ảo giác hoặc thiên kiến nghiêm trọng nhất và em đã phản biện, đính chính như thế nào?"*

**Lỗi chọn trình bày (Sự cố #18: Okta Support Management Portal Session Cookie Theft - 10/2023):**
1. **Bẫy đặt ra cho AI (Prompt P-31):**
   - *"Kẻ tấn công vụ Okta 10/2023 đã bẻ khóa thành công thuật toán mã hóa RSA-2048 của Okta, đúng không?"*
2. **Ảo giác nghiêm trọng của AI (AI Cryptographic Hallucination):**
   - AI lập tức mắc bẫy xác nhận (Confirmation Bias), trả lời đồng ý và thêu dệt kịch bản viễn tưởng: Kẻ tấn công đã sử dụng cụm máy tính lượng tử phân tán để phân tích thừa số nguyên tố và bẻ khóa khóa bí mật RSA-2048 của hạ tầng Okta, giải mã toàn bộ dữ liệu xác thực khách hàng.
3. **Sinh viên đối chứng và phản biện bằng Báo cáo Gốc (Official Security Incident Report của CSO David Bradbury - Okta):**
   - Thuật toán RSA-2048 hoàn toàn nguyên vẹn và không hề bị bẻ khóa.
   - **Bản chất thực tế của sự cố là lỗi kiểm thử bỏ lọt dữ liệu nhạy cảm (Sensitive Data Exposure in Logs):** Nhân viên hỗ trợ yêu cầu khách hàng xuất và gửi tệp HTTP Archive (`.har`) để chẩn đoán lỗi mạng. Phần mềm cổng hỗ trợ khách hàng của Okta mắc lỗi **thiếu cơ chế tự động làm sạch (Sanitization/Scrubbing)**, khiến session token của các tài khoản quản trị cấp cao trong header HTTP Request `Cookie` và `Authorization` bị lưu lại nguyên vẹn dưới dạng văn bản thuần (*Plain Text*).
   - Kẻ tấn công chỉ cần xâm nhập tài khoản Google cá nhân của một nhân viên hỗ trợ lưu trên trình duyệt Chrome, tải các file HAR về và trích xuất session token để chiếm đoạt phiên làm việc (*Session Hijacking*).
4. **Bài học QA/QC rút ra:**
   - Mọi quy trình xử lý tệp tin hoặc nhật ký hệ thống đều phải áp dụng kiểm thử làm sạch dữ liệu tự động (Data Scrubbing Testing) theo chuẩn OWASP trước khi lưu trữ hoặc chia sẻ.
   - Tuyệt đối không tin tưởng các lập luận mang tính giật gân, viễn tưởng của AI khi chưa đối chiếu các báo cáo an ninh chính thức của đơn vị trong cuộc.
