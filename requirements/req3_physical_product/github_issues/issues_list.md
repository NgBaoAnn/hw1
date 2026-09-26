# Hướng Dẫn & Nội Dung 5 GitHub Issues (Thay Thế Mantis Bug Tracker)

> **Mục tiêu:** Ghi nhận 5 khiếm khuyết vật lý thực tế phát hiện được trên Quạt Senko L1638 lên hệ thống GitHub Issues của repository cá nhân (`NgBaoAnn`), tuân thủ chuẩn báo cáo lỗi phần cứng/phần mềm chuyên nghiệp theo ISTQB.

---

## 1. Bảng Tổng Hợp 5 Issues

| Issue ID | Defect ID | Tiêu đề Issue (Title) | Mức độ (Severity) | Nhãn (Labels) | Test Case tương ứng | File nội dung chi tiết | Link GitHub | Minh chứng Ảnh chụp (Anti-cheat) |
| :---: | :---: | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **#1** | **DEF-01** | `[DEF-01][Major] Kẹt cơ cấu liên động và dẫn chéo dòng stator khi nhấn đồng thời 2 phím tốc độ (1 & 2)` | Major | `bug`, `safety`, `hardware` | `TC-12 (Edge Case #1)` | [`issue_01_DEF-01.md`](issue_01_DEF-01.md) | [Issue #1](https://github.com/NgBaoAnn/hw1/issues/1) | [`photo/issue_1.png`](../photo/issue_1.png) |
| **#2** | **DEF-02** | `[DEF-02][Medium] Trượt vấu bánh răng hộp số túp-năng phát tiếng kêu cạch cạch khi bị cản hành trình` | Medium | `bug`, `mechanical`, `degradation` | `TC-13 (Edge Case #2)` | [`issue_02_DEF-02.md`](issue_02_DEF-02.md) | [Issue #2](https://github.com/NgBaoAnn/hw1/issues/2) | [`photo/issue_2.png`](../photo/issue_2.png) |
| **#3** | **DEF-03** | `[DEF-03][Medium] Rung lắc cộng hưởng làm trôi van siết ren ống sắt ở độ cao 95cm & Số 3` | Medium | `bug`, `stability`, `vibration` | `TC-14 (Edge Case #3)` | [`issue_03_DEF-03.md`](issue_03_DEF-03.md) | [Issue #3](https://github.com/NgBaoAnn/hw1/issues/3) | [`photo/issue_3.png`](../photo/issue_3.png) |
| **#4** | **DEF-04** | `[DEF-04][Minor] Lỏng khớp bản lề làm sụp góc ngửa +15° khi quạt quay đảo chiều đến điểm biên` | Minor | `bug`, `usability`, `mechanical` | `TC-09` | [`issue_04_DEF-04.md`](issue_04_DEF-04.md) | [Issue #4](https://github.com/NgBaoAnn/hw1/issues/4) | [`photo/issue_4.png`](../photo/issue_4.png) |
| **#5** | **DEF-05** | `[DEF-05][High] Phóng hồ quang điện (Arcing) và khét tiếp điểm khi nhấn phím tốc độ không hết hành trình` | High | `bug`, `safety`, `electrical-hazard` | `TC-15 (Edge Case #4)` | [`issue_05_DEF-05.md`](issue_05_DEF-05.md) | [Issue #5](https://github.com/NgBaoAnn/hw1/issues/5) | [`photo/issue_5.png`](../photo/issue_5.png) |

---

## 2. Hướng Dẫn Sinh Viên Tạo Issue Trên GitHub Repository

Sinh viên thực hiện theo 1 trong 2 cách sau:

### Cách 1: Tạo trực tiếp qua giao diện Web GitHub (Khuyên dùng)
1. Truy cập vào GitHub repository của bài tập: `https://github.com/NgBaoAnn/hw1` (hoặc tên repo bài tập tương ứng).
2. Chuyển sang tab **Issues** -> Bấm nút xanh **New issue**.
3. Mở lần lượt các file `issue_01_DEF-01.md` đến `issue_05_DEF-05.md`, sao chép nguyên văn Tiêu đề và Nội dung Markdown vào Issue.
4. Gán nhãn (Labels) tương ứng rồi bấm **Submit new issue**.
5. Chụp ảnh màn hình danh sách 5 Issues trên GitHub (có hiển thị avatar / username `NgBaoAnn`) và lưu vào `requirements/req3_physical_product/github_issues/github_issues_screenshot.png`.

### Cách 2: Tạo bằng GitHub CLI (`gh`) sau khi đăng nhập
```bash
gh issue create --title "[DEF-01][Major] Kẹt cơ cấu liên động và dẫn chéo dòng stator khi nhấn đồng thời 2 phím tốc độ" --body-file requirements/req3_physical_product/github_issues/issue_01_DEF-01.md --label "bug,safety,hardware"
gh issue create --title "[DEF-02][Medium] Trượt vấu bánh răng hộp số túp-năng phát tiếng kêu cạch cạch khi bị cản hành trình" --body-file requirements/req3_physical_product/github_issues/issue_02_DEF-02.md --label "bug,mechanical"
gh issue create --title "[DEF-03][Medium] Rung lắc cộng hưởng làm trôi van siết ren ống sắt ở độ cao 95cm & Số 3" --body-file requirements/req3_physical_product/github_issues/issue_03_DEF-03.md --label "bug,stability"
gh issue create --title "[DEF-04][Minor] Lỏng khớp bản lề làm sụp góc ngửa +15° khi quạt quay đảo chiều đến điểm biên" --body-file requirements/req3_physical_product/github_issues/issue_04_DEF-04.md --label "bug,usability"
gh issue create --title "[DEF-05][High] Phóng hồ quang điện (Arcing) và khét tiếp điểm khi nhấn phím tốc độ không hết hành trình" --body-file requirements/req3_physical_product/github_issues/issue_05_DEF-05.md --label "bug,safety"
```
