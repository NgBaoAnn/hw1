#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to create the dedicated submission package folder '23120207_HW01_AI_100'
and zip archive '23120207_HW01_AI_100.zip' strictly complying with the
Submission Regulations from '2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf'.

Student: NGUYỄN BẢO AN
StudentID: 23120207
Class: 23CLC01
Self-Assessed Grade: 100
"""

import os
import shutil
import subprocess
import zipfile

WORKSPACE = "/Users/nguyenbaoan/codeLab/kcpm/hw1"
SUBMISSION_DIR_NAME = "23120207_HW01_AI_100"
SUBMISSION_DIR = os.path.join(WORKSPACE, SUBMISSION_DIR_NAME)
ZIP_FILE = os.path.join(WORKSPACE, f"{SUBMISSION_DIR_NAME}.zip")

def main():
    print("=" * 65)
    print(f"BẮT ĐẦU TẠO FOLDER TỔNG HỢP NỘP BÀI: {SUBMISSION_DIR_NAME}")
    print("Đối chiếu quy chuẩn: 2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf")
    print("=" * 65)

    # 1. Update git_log.txt
    print("--> 1. Cập nhật git_log.txt...")
    git_log_path = os.path.join(WORKSPACE, "reports", "git_log.txt")
    with open(git_log_path, "w", encoding="utf-8") as f:
        subprocess.run(["git", "log", "--graph", "--all", "--stat"], stdout=f, cwd=WORKSPACE)

    # 2. Compile latest PDF from reports/HW01_Report.tex
    print("--> 2. Biên dịch ấn bản PDF mới nhất từ reports/HW01_Report.tex...")
    compile_script = os.path.join(WORKSPACE, "scripts", "generate_latex_report.py")
    subprocess.run(["python3", compile_script], cwd=WORKSPACE, check=True)

    # 3. Clean and prepare submission directory
    if os.path.exists(SUBMISSION_DIR):
        shutil.rmtree(SUBMISSION_DIR)
    os.makedirs(SUBMISSION_DIR, exist_ok=True)

    # 4. Copy core requirement directories
    print("--> 3. Sao chép các thư mục thành phần...")
    shutil.copytree(os.path.join(WORKSPACE, "requirements"), os.path.join(SUBMISSION_DIR, "requirements"))
    shutil.copytree(os.path.join(WORKSPACE, "reports"), os.path.join(SUBMISSION_DIR, "reports"))
    shutil.copytree(os.path.join(WORKSPACE, "AI Templates"), os.path.join(SUBMISSION_DIR, "AI Templates"))
    shutil.copytree(os.path.join(WORKSPACE, "templates"), os.path.join(SUBMISSION_DIR, "templates"))

    # 5. Copy root standalone files for quick access by graders
    print("--> 4. Thiết lập các file truy cập nhanh tại thư mục gốc của bài nộp...")
    root_files_to_copy = [
        ("reports/HW01_Report.pdf", "HW01_Report.pdf"),
        ("reports/HW01_Report.md", "HW01_Report.md"),
        ("reports/HW01_Report.tex", "HW01_Report.tex"),
        ("reports/test_cases_and_summary.xlsx", "test_cases_and_summary.xlsx"),
        ("reports/Appendix_A_Prompt_Log.md", "Appendix_A_Prompt_Log.md"),
        ("reports/Self_Assessment.md", "Self_Assessment.md"),
        ("reports/Oral_Defense_Guide.md", "Oral_Defense_Guide.md"),
        ("reports/git_log.txt", "git_log.txt"),
        ("requirements/req3_physical_product/photo/device_23120207.jpg", "device_23120207.jpg"),
        ("requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md", "qa_qc_roles_mindmap.md"),
        ("prompt_log.md", "prompt_log.md"),
    ]

    for src, dst in root_files_to_copy:
        src_path = os.path.join(WORKSPACE, src)
        dst_path = os.path.join(SUBMISSION_DIR, dst)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)

    # 6. Create dedicated YouTube Demo Links file
    youtube_content = """# Danh sách 5 Video Demo Thực nghiệm Quạt Senko L1638 (YouTube Shorts)

Sinh viên: NGUYỄN BẢO AN
MSSV: 23120207
Lớp: 23CLC01
Môn học: CS423 / CSC13003 - Kiểm thử phần mềm (FIT@HCMUS, 2026)
Thiết bị thực nghiệm: Quạt điện lửng dân dụng SENKO L1638 (SX: 09/2023)

Toàn bộ 5 video đều được đăng tải ở chế độ Unlisted (Không công khai) trên YouTube, thời lượng <= 60 giây, có giọng thuyết minh của sinh viên phân tích nguyên nhân kỹ thuật và triệu chứng lỗi thực tế:

1. Video 1 (TC-12 / DEF-01 - Kẹt cơ cấu liên động & Quá tải dòng Stator):
   - Link YouTube: https://youtube.com/shorts/NK6kk9AF39U?feature=share
   - Mô tả: Nhấn đồng thời 2 phím tốc độ (Số 1 & 2) làm kẹt lẫy cơ khí (mechanical deadlock), cấp điện cùng lúc 2 cuộn stator gây xung đột từ trường, tiếng motor gầm ù lớn và dòng điện tăng vọt đe dọa đứt cầu chì nhiệt.
   - GitHub Issue: https://github.com/NgBaoAnn/hw1/issues/1

2. Video 2 (TC-13 / DEF-02 - Trượt vấu bánh răng hộp số túp-năng đảo hướng):
   - Link YouTube: https://youtube.com/shorts/TQMrprni0oY?feature=share
   - Mô tả: Cản cưỡng bức hành trình quay đảo gió của đầu quạt; do thiếu ly hợp trượt an toàn (slip clutch), bánh răng nhựa trượt vấu cưỡng bức phát tiếng kêu cạch cạch liên hồi và gây mòn vẹt răng hộp số.
   - GitHub Issue: https://github.com/NgBaoAnn/hw1/issues/2

3. Video 3 (TC-14 / DEF-03 - Rung lắc cộng hưởng làm trôi van siết ren ở 95cm):
   - Link YouTube: https://youtube.com/shorts/edU_0xoc_JI?feature=share
   - Mô tả: Kéo ống sắt lên chiều cao cực hạn 95cm và chạy Số 3 liên tục; trọng tâm nâng cao kết hợp rung động rotor làm ren siết nhựa bị trôi lỏng dần, khiến quạt tự sụt chiều cao từ 95cm xuống 83cm.
   - GitHub Issue: https://github.com/NgBaoAnn/hw1/issues/3

4. Video 4 (TC-09 / DEF-04 - Sụp góc ngửa cổ quạt khi quay đảo chiều):
   - Link YouTube: https://youtube.com/shorts/jCHATpMITFI?feature=share
   - Mô tả: Ngửa đầu quạt góc +15 độ và bật túp-năng đảo hướng; mô-men quán tính ở điểm đảo chiều biên làm khớp bản lề bị sụp 5 độ.
   - GitHub Issue: https://github.com/NgBaoAnn/hw1/issues/4

5. Video 5 (TC-15 / DEF-05 - Phóng hồ quang điện khi nhấn dở hành trình phím):
   - Link YouTube: https://youtube.com/shorts/NZP3v1SyXfY?feature=share
   - Mô tả: Nhấn hờ phím tốc độ chỉ 50% hành trình; khoảng cách hở giữa 2 lá đồng tiếp điểm sinh hiện tượng phóng hồ quang điện (electrical arcing) xèo xèo liên tục, sinh nhiệt cục bộ làm cháy rỗ bề mặt tiếp điểm và khét nhựa.
   - GitHub Issue: https://github.com/NgBaoAnn/hw1/issues/5
"""
    with open(os.path.join(SUBMISSION_DIR, "YouTube_Demo_Links.txt"), "w", encoding="utf-8") as f:
        f.write(youtube_content)

    # 7. Create 00_README_SUBMISSION.md
    readme_content = """# BÀI NỘP BÁO CÁO HW01 - CS423 / CSC13003 KIỂM THỬ PHẦN MỀM
## KHOA CÔNG NGHỆ THÔNG TIN - TRƯỜNG ĐH KHOA HỌC TỰ NHIÊN, ĐHQG-HCM

---

### THÔNG TIN SINH VIÊN & BÀI LÀM
- **Họ và tên:** NGUYỄN BẢO AN
- **Mã số sinh viên (MSSV):** 23120207
- **Lớp:** 23CLC01 (Khóa 2023 – 2027)
- **Tên thư mục nộp bài:** `23120207_HW01_AI_100`
- **Mã tự chấm điểm nộp bài (3 chữ số):** `100` (100 / 100 điểm)
- **Kho mã nguồn GitHub (Artifacts & Issues):** [https://github.com/NgBaoAnn/hw1](https://github.com/NgBaoAnn/hw1)

---

### BẢNG ĐỐI CHIẾU DANH MỤC NỘP BÀI (SUBMISSION REGULATIONS CHECKLIST)
Căn cứ theo mục **Submission regulations (Trang 5-6)** của đề bài `2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf`:

| STT | Thành phần bắt buộc | Đường dẫn file trong gói nộp | Định dạng | Trạng thái |
| :---: | :--- | :--- | :---: | :---: |
| **1** | **Main report (PDF)** (chứa đủ AI Audit Report, AI Critique, Mandatory Disclosure) | `HW01_Report.pdf` (và `reports/HW01_Report.pdf`) | PDF | **HOÀN TẤT** (13 trang, 0 Overfull) |
| **2** | **Main report (Markdown)** (bảo tồn nguyên vẹn bản text) | `HW01_Report.md` (và `reports/HW01_Report.md`) | Markdown | **HOÀN TẤT** |
| **3** | **Appendix A: Full prompt log** có timestamp chính xác từng giây | `Appendix_A_Prompt_Log.md` (và `prompt_log.md`) | Markdown | **HOÀN TẤT** (42 Prompts) |
| **4** | **Excel Test Cases & Summary** (3 sheets: TCs, Defects, Summary Report) | `test_cases_and_summary.xlsx` | Excel (.xlsx) | **HOÀN TẤT** (3 Sheets chuẩn) |
| **5** | **Bug Screenshots / GitHub Issues** (thay thế Mantis, hiển thị username) | `requirements/req3_physical_product/photo/issue_1.png` -> `issue_5.png` | PNG | **HOÀN TẤT** (5 Live Issues) |
| **6** | **Device photo + Student ID** (chụp chung khung hình chống gian lận) | `device_23120207.jpg` | JPG | **HOÀN TẤT** (Quạt thật + Thẻ SV) |
| **7** | **YouTube Unlisted Demo Videos** (>= 5 video <= 60s có giọng thuyết minh) | `YouTube_Demo_Links.txt` | Text / URL | **HOÀN TẤT** (5 Video Shorts) |
| **8** | **QA/QC Role Mindmap** (3 lỗi kiến thức ISTQB CTFL v4.0 được sửa) | `qa_qc_roles_mindmap.md` | Markdown / Mermaid | **HOÀN TẤT** |
| **9** | **[AI-02] AI Audit Report** (mẫu 5 phần cho 22 artifact) | `AI Templates/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx` | Word (.docx) & .md | **HOÀN TẤT** |
| **10** | **[AI-03] AI Disclosure Form** (kê khai minh bạch, ký tên cam kết) | `AI Templates/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx` | Word (.docx) & .md | **HOÀN TẤT** |
| **11** | **[AI-05] AI Privacy Checklist** (tích chọn 100% điều khoản bảo mật) | `AI Templates/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx` | Word (.docx) & .md | **HOÀN TẤT** |
| **12** | **[AI-06] Student Acknowledgement** (ký cam kết tuân thủ chính sách AI) | `AI Templates/[AI-06] - FIT@HCMUS - AI Student Acknowledgement_En.docx` | Word (.docx) & .md | **HOÀN TẤT** |
| **13** | **Self-assessment section** (tự chấm 100/100 điểm theo rubric) | `Self_Assessment.md` (và cuối báo cáo PDF/MD) | Markdown / PDF | **HOÀN TẤT** (Mã: 100) |
| **14** | **Tài liệu chuẩn bị Vấn đáp miệng** (Oral Defense Guide cho 30% sinh viên) | `Oral_Defense_Guide.md` | Markdown | **HOÀN TẤT** (3 Kịch bản chi tiết) |
| **15** | **Git Commit Log trích xuất** (theo dặn dò note.txt của giảng viên) | `git_log.txt` | Text | **HOÀN TẤT** (Full tree & stats) |

---

### HƯỚNG DẪN TRUY XUẤT NHANH CHO GIẢNG VIÊN VÀ TRỢ GIẢNG
1. **Đọc Báo cáo Tổng thể:** Mở ngay tệp `HW01_Report.pdf` tại thư mục gốc để xem ấn bản in ấn chuẩn học thuật.
2. **Kiểm tra Bảng tính Kiểm thử:** Mở tệp `test_cases_and_summary.xlsx` xem 3 sheets: (1) 15 Test Cases ISTQB, (2) Ma trận 5 Defects ánh xạ GitHub Issues & YouTube Videos, (3) Báo cáo Test Summary Report.
3. **Xem Video Thực nghiệm:** Mở `YouTube_Demo_Links.txt` để nhấp trực tiếp vào 5 đường dẫn YouTube Shorts có thuyết minh giọng thật của sinh viên.
4. **Kiểm tra 5 Biểu mẫu Quy chuẩn:** Mở thư mục `AI Templates/` chứa đầy đủ 4 tệp `.docx` chính thức đã được hoàn thiện.
"""
    with open(os.path.join(SUBMISSION_DIR, "00_README_SUBMISSION.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 8. Verification against Checklist
    print("--> 5. Kiểm tra tính toàn vẹn của tất cả tài sản...")
    critical_checks = [
        "HW01_Report.pdf",
        "HW01_Report.md",
        "HW01_Report.tex",
        "test_cases_and_summary.xlsx",
        "Appendix_A_Prompt_Log.md",
        "Self_Assessment.md",
        "Oral_Defense_Guide.md",
        "device_23120207.jpg",
        "qa_qc_roles_mindmap.md",
        "YouTube_Demo_Links.txt",
        "00_README_SUBMISSION.md",
        "AI Templates/[AI-02] - FIT@HCMUS - AI Audit Report_En.docx",
        "AI Templates/[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx",
        "AI Templates/[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx",
        "AI Templates/[AI-06] - FIT@HCMUS - AI Student Acknowledgement_En.docx",
        "requirements/req1_job_market/jobs_data.md",
        "requirements/req2_software_defects/defects_2022_2026.md",
        "requirements/req3_physical_product/device_info.md",
        "requirements/req3_physical_product/edge_cases_ai_missed.md",
        "requirements/req3_physical_product/photo/ai_edge_cases_screenshot.png",
        "requirements/req3_physical_product/photo/issue_1.png",
        "requirements/req3_physical_product/photo/issue_2.png",
        "requirements/req3_physical_product/photo/issue_3.png",
        "requirements/req3_physical_product/photo/issue_4.png",
        "requirements/req3_physical_product/photo/issue_5.png",
    ]

    for i in range(1, 11):
        critical_checks.append(f"requirements/req1_job_market/screenshots/job_{i:02d}.png")

    missing = 0
    for rel_path in critical_checks:
        full_path = os.path.join(SUBMISSION_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"  [X] THIẾU: {rel_path}")
            missing += 1
        else:
            print(f"  [V] Hợp lệ: {rel_path} ({os.path.getsize(full_path):,} bytes)")

    if missing > 0:
        print(f"\nLỖI: Phát hiện {missing} file bị thiếu trong thư mục nộp bài!")
        exit(1)

    print("\n--> 6. Tạo file nén chuẩn định dạng: StudentID_HW01_AI_<grade>.zip...")
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)

    with zipfile.ZipFile(ZIP_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SUBMISSION_DIR):
            for file in files:
                if file.startswith(".") or file.endswith(".tmp") or file.endswith(".aux") or file.endswith(".log") or file.endswith(".toc") or file.endswith(".out"):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, WORKSPACE)
                zipf.write(file_path, arcname)

    print("=" * 65)
    print(f"HOÀN TẤT THÀNH CÔNG!")
    print(f"1. Thư mục tổng hợp nộp bài: {SUBMISSION_DIR_NAME}/")
    print(f"2. File nén nộp bài chính thức: {os.path.basename(ZIP_FILE)}")
    print(f"   Dung lượng file zip: {os.path.getsize(ZIP_FILE):,} bytes (~{os.path.getsize(ZIP_FILE)/(1024*1024):.2f} MB)")
    print("=" * 65)

if __name__ == "__main__":
    main()
