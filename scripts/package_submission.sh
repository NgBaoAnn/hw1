#!/usr/bin/env bash

# ==============================================================================
# Script đóng gói bài tập HW01: StudentID_HW01_AI_<grade>.zip
# Khóa học: CS423 / CSC13003 - Kiểm thử phần mềm (FIT@HCMUS, 2026)
# Sinh viên: NGUYỄN BẢO AN - MSSV: 23120207
# ==============================================================================

set -e

STUDENT_ID="${1:-23120207}"
GRADE="${2:-100}"

ZIP_NAME="${STUDENT_ID}_HW01_AI_${GRADE}.zip"

echo "=========================================================="
echo "BẮT ĐẦU KIỂM TRA TÍNH ĐẦY ĐỦ CỦA BÀI NỘP HW01"
echo "MSSV: ${STUDENT_ID} | Điểm tự đánh giá: ${GRADE}"
echo "File đầu ra dự kiến: ${ZIP_NAME}"
echo "=========================================================="

# 1. Trích xuất Git log theo dặn dò của giảng viên trong note.txt
echo "==> 1. Trích xuất lịch sử Git commit..."
git log --graph --all --stat > reports/git_log.txt 2>/dev/null || echo "Chưa có git log hoặc git chưa có commit."

# 2. Kiểm tra các thư mục và file bắt buộc
MISSING_FILES=0

check_file() {
    if [ ! -f "$1" ]; then
        echo "[CẢNH BÁO THIẾU FILE]: Không tìm thấy '$1'"
        MISSING_FILES=$((MISSING_FILES + 1))
    else
        echo "[OK] $1"
    fi
}

echo "==> 2.1. Kiểm tra tài sản Yêu cầu 1 (Job Market & Mindmap)..."
check_file "requirements/req1_job_market/jobs_data.md"
check_file "requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md"
for i in $(seq -w 1 10); do
    check_file "requirements/req1_job_market/screenshots/job_${i}.png"
done

echo "==> 2.2. Kiểm tra tài sản Yêu cầu 2 (20 Lỗi phần mềm 2022-2026)..."
check_file "requirements/req2_software_defects/defects_2022_2026.md"

echo "==> 2.3. Kiểm tra tài sản Yêu cầu 3 (Kiểm thử thực nghiệm Quạt Senko L1638)..."
check_file "requirements/req3_physical_product/device_info.md"
check_file "requirements/req3_physical_product/edge_cases_ai_missed.md"
check_file "requirements/req3_physical_product/photo/device_23120207.jpg"
check_file "requirements/req3_physical_product/photo/ai_edge_cases_screenshot.png"
check_file "requirements/req3_physical_product/test_cases.md"
check_file "requirements/req3_physical_product/test_cases.csv"
check_file "requirements/req3_physical_product/test_cases_and_summary.xlsx"
for i in $(seq -w 1 5); do
    check_file "requirements/req3_physical_product/github_issues/issue_0${i}_DEF-0${i}.md"
done

echo "==> 2.4. Kiểm tra Biểu mẫu quy chuẩn AI & Báo cáo..."
check_file "templates/AI-02_AI_Audit_Report.md"
check_file "templates/AI-03_AI_Disclosure_Form.md"
check_file "templates/AI-05_AI_Privacy_Checklist.md"
check_file "templates/AI-06_AI_Student_Acknowledgement.md"
check_file "reports/HW01_Report.md"
check_file "reports/AI-02_AI_Audit_Report.md"
check_file "reports/AI_Critique.md"
check_file "reports/Self_Assessment.md"
check_file "reports/Oral_Defense_Guide.md"
check_file "reports/Appendix_A_Prompt_Log.md"
check_file "reports/git_log.txt"

if [ $MISSING_FILES -gt 0 ]; then
    echo "----------------------------------------------------------"
    echo "Cảnh báo: Có $MISSING_FILES file chưa hoàn thiện. Vui lòng kiểm tra lại."
    exit 1
else
    echo "[XÁC NHẬN HOÀN TOÀN HỢP LỆ]: Tất cả tài sản và minh chứng bắt buộc đều tồn tại đầy đủ 100%!"
fi

# Đảm bảo prompt_log.md luôn đồng bộ với reports/Appendix_A_Prompt_Log.md
cp -f reports/Appendix_A_Prompt_Log.md prompt_log.md

# 3. Tạo file nén
echo "==> 3. Tiến hành đóng gói file zip..."
rm -f "${ZIP_NAME}"
zip -r "${ZIP_NAME}" \
    requirements \
    reports \
    templates \
    "AI Templates" \
    prompt_log.md \
    PLAN_HW01.md \
    note.txt \
    -x "*.DS_Store" -x "__MACOSX*" -x "*.git*"

echo "=========================================================="
echo "ĐÃ ĐÓNG GÓI THÀNH CÔNG: ${ZIP_NAME}"
echo "Dung lượng file: $(ls -lh "${ZIP_NAME}" | awk '{print $5}')"
echo "=========================================================="
