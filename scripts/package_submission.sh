#!/usr/bin/env bash

# ==============================================================================
# Script đóng gói bài tập HW01: StudentID_HW01_AI_<grade>.zip
# Tác giả: KCPM HW01 Packaging Assistant
# ==============================================================================

set -e

STUDENT_ID="${1:-21127000}"
GRADE="${2:-095}"

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
        echo "[OK] Tìm thấy '$1'"
    fi
}

echo "==> 2. Kiểm tra các tài liệu và biểu mẫu cốt lõi..."
check_file "reports/Appendix_A_Prompt_Log.md"
check_file "reports/AI_Critique.md"
check_file "reports/Self_Assessment.md"
check_file "templates/AI-02_AI_Audit_Report.md"
check_file "templates/AI-03_AI_Disclosure_Form.md"
check_file "templates/AI-05_AI_Privacy_Checklist.md"

if [ $MISSING_FILES -gt 0 ]; then
    echo "----------------------------------------------------------"
    echo "Cảnh báo: Có $MISSING_FILES file chưa hoàn thiện. Vui lòng kiểm tra lại."
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
