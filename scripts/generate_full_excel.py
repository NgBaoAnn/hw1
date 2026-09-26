#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to generate the complete multi-sheet test_cases_and_summary.xlsx
workbook for FIT@HCMUS CS423 / CSC13003 HW01.
Includes:
- Sheet 1: 15 Test Cases
- Sheet 2: Defects & Issues (GitHub Issues mapping)
- Sheet 3: Test Summary Report (Executive metrics & ISTQB sign-off)
"""

import os
import csv
import zipfile
import xml.sax.saxutils as saxutils

def make_sheet_xml(rows):
    xml_rows = []
    for r_idx, row in enumerate(rows, 1):
        cells = []
        for c_idx, val in enumerate(row, 1):
            temp = c_idx
            col_letter = ''
            while temp > 0:
                temp, rem = divmod(temp - 1, 26)
                col_letter = chr(65 + rem) + col_letter
            ref = f'{col_letter}{r_idx}'
            escaped = saxutils.escape(str(val))
            cells.append(f'<c r="{ref}" t="inlineStr"><is><t>{escaped}</t></is></c>')
        xml_rows.append(f'<row r="{r_idx}">' + ''.join(cells) + '</row>')
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>' + ''.join(xml_rows) + '</sheetData></worksheet>'

def generate():
    # 1. Sheet 1: 15 Test Cases
    s1_rows = []
    with open('requirements/req3_physical_product/test_cases.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for r in reader:
            s1_rows.append(r)

    # 2. Sheet 2: Defects & Issues
    s2_rows = [
        ['Defect ID', 'GitHub Issue', 'Mức độ (Severity)', 'Tiêu đề khiếm khuyết (Defect Title)', 'Test Case kích hoạt', 'Nguyên nhân kỹ thuật (RCA)', 'Link GitHub Issue', 'Video minh chứng', 'Ảnh màn hình minh chứng'],
        ['DEF-01', 'Issue #1', 'Major', 'Kẹt cơ cấu liên động và dẫn chéo dòng stator khi nhấn đồng thời 2 phím tốc độ (1 & 2)', 'TC-12 (Edge Case 1)', 'Lẫy cơ khí thanh trượt bị deadlock; cấp nguồn song song 2 cuộn stator gây đoản mạch chéo và quá tải', 'https://github.com/NgBaoAnn/hw1/issues/1', 'https://youtube.com/shorts/NK6kk9AF39U?feature=share', 'requirements/req3_physical_product/photo/issue_1.png'],
        ['DEF-02', 'Issue #2', 'Medium', 'Trượt vấu bánh răng hộp số túp-năng phát tiếng kêu cạch cạch khi bị cản hành trình', 'TC-13 (Edge Case 2)', 'Thiếu bộ ly hợp trượt an toàn (slip clutch); bánh răng nhựa trượt cưỡng bức gây mài mòn răng', 'https://github.com/NgBaoAnn/hw1/issues/2', 'https://youtube.com/shorts/TQMrprni0oY?feature=share', 'requirements/req3_physical_product/photo/issue_2.png'],
        ['DEF-03', 'Issue #3', 'Medium', 'Rung lắc cộng hưởng làm trôi van siết ren ống sắt ở độ cao 95cm & Số 3', 'TC-14 (Edge Case 3)', 'Trọng tâm nâng cao kết hợp rung động rotor ở Số 3 làm ren siết nhựa bị trôi lỏng dần', 'https://github.com/NgBaoAnn/hw1/issues/3', 'https://youtube.com/shorts/edU_0xoc_JI?feature=share', 'requirements/req3_physical_product/photo/issue_3.png'],
        ['DEF-04', 'Issue #4', 'Minor', 'Lỏng khớp bản lề làm sụp góc ngửa +15° khi quạt quay đảo chiều đến điểm biên', 'TC-09', 'Mô-men quán tính khi đảo chiều vượt quá lực ma sát khấc bản lề khi ngửa cực đại', 'https://github.com/NgBaoAnn/hw1/issues/4', 'https://youtube.com/shorts/jCHATpMITFI?feature=share', 'requirements/req3_physical_product/photo/issue_4.png'],
        ['DEF-05', 'Issue #5', 'High (Safety)', 'Phóng hồ quang điện (Arcing) và khét tiếp điểm khi nhấn phím tốc độ không hết hành trình', 'TC-15 (Edge Case 4)', 'Cơ cấu phím bấm thiếu tính năng nhảy tiếp điểm nhanh (Snap-action); khoảng cách khe hở nhỏ sinh hồ quang', 'https://github.com/NgBaoAnn/hw1/issues/5', 'https://youtube.com/shorts/NZP3v1SyXfY?feature=share', 'requirements/req3_physical_product/photo/issue_5.png']
    ]

    # 3. Sheet 3: Test Summary Report
    s3_rows = [
        ['BÁO CÁO TỔNG KẾT KIỂM THỬ THIẾT BỊ VẬT LÝ (TEST SUMMARY REPORT)', ''],
        ['Chuẩn thực hiện:', 'ISTQB CTFL v4.0 & IEC 60335-2-8'],
        ['Thiết bị kiểm thử:', 'Quạt lửng ống sắt SENKO L1638 (Tháng 09/2023)'],
        ['Kỹ sư kiểm thử:', 'NGUYỄN BẢO AN (MSSV: 23120207) - Lớp 23CLC01'],
        ['Môn học:', 'CS423 / CSC13003 – Software Testing (FIT@HCMUS)'],
        ['Ngày hoàn tất thực nghiệm:', '26/09/2026'],
        ['', ''],
        ['CHỈ SỐ ĐO LƯỜNG (TEST METRICS)', 'SỐ LƯỢNG', 'TỶ LỆ (%)', 'ĐÁNH GIÁ CHUYÊN MÔN'],
        ['Tổng số Test Cases thiết kế & thực thi', '15', '100.0%', 'Bao quát toàn diện cơ khí, điện, chức năng, an toàn và biên'],
        ['Số Test Cases ĐẠT (PASS)', '10', '66.7%', 'Các chức năng cơ bản, tĩnh, hành trình và an toàn đạt chuẩn'],
        ['Số Test Cases KHÔNG ĐẠT (FAIL)', '5', '33.3%', 'Phát hiện chính xác 5 khiếm khuyết cơ điện (DEF-01 -> DEF-05)'],
        ['Ca kiểm thử biên do AI bỏ sót (AI Missed)', '4', '26.7%', 'Bắt trọn 4/4 ca biên cơ điện: Deadlock, Ly hợp, Rung lắc, Hồ quang'],
        ['Số khiếm khuyết log lên GitHub Issues', '5', '100.0%', 'Đầy đủ nhãn dán, mô tả, video demo và ảnh chụp màn hình'],
        ['Video demo thực nghiệm có thuyết minh', '5', '100.0%', 'Minh chứng trực quan 5 video YouTube Shorts chính chủ'],
        ['', ''],
        ['PHÂN BỔ MỨC ĐỘ KHIÊM KHUYẾT (DEFECT SEVERITY)', 'SỐ LƯỢNG', 'MÃ DEFECT'],
        ['High / Safety-Critical', '1', 'DEF-05 (Phóng hồ quang điện tiếp điểm)'],
        ['Major', '1', 'DEF-01 (Kẹt lẫy phím và quá tải dòng stator)'],
        ['Medium', '2', 'DEF-02 (Trượt bánh răng túp-năng), DEF-03 (Trôi ren siết 95cm)'],
        ['Minor', '1', 'DEF-04 (Lỏng khớp ngửa khi đảo hướng)'],
        ['', ''],
        ['KẾT LUẬN & KIẾN NGHỊ KIỂM THỬ (TEST CONCLUSION)', ''],
        ['Đánh giá tổng thể:', 'Thiết bị đáp ứng tốt các yêu cầu vận hành tiêu chuẩn hàng ngày. Tuy nhiên, thiết kế cơ khí phím bấm và van siết ren cần được bổ sung cơ cấu chống kẹt kép và snap-action tiếp điểm để triệt tiêu nguy cơ phóng hồ quang và quá nhiệt cuộn dây stator.'],
        ['Khuyến nghị phát hành:', 'CONDITIONAL PASS - Đề xuất khắc phục DEF-01 và DEF-05 trước khi xuất xưởng số lượng lớn.']
    ]

    sheets = [
        ('15 Test Cases', s1_rows),
        ('Defects & Issues', s2_rows),
        ('Test Summary Report', s3_rows)
    ]

    def write_xlsx(target_path):
        content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>'''

        pkg_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>'''

        wb_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="15 Test Cases" sheetId="1" r:id="rId1"/>
    <sheet name="Defects &amp; Issues" sheetId="2" r:id="rId2"/>
    <sheet name="Test Summary Report" sheetId="3" r:id="rId3"/>
  </sheets>
</workbook>'''

        wb_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet3.xml"/>
</Relationships>'''

        with zipfile.ZipFile(target_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr('[Content_Types].xml', content_types)
            z.writestr('_rels/.rels', pkg_rels)
            z.writestr('xl/workbook.xml', wb_xml)
            z.writestr('xl/_rels/workbook.xml.rels', wb_rels)
            z.writestr('xl/worksheets/sheet1.xml', make_sheet_xml(sheets[0][1]))
            z.writestr('xl/worksheets/sheet2.xml', make_sheet_xml(sheets[1][1]))
            z.writestr('xl/worksheets/sheet3.xml', make_sheet_xml(sheets[2][1]))
        print(f'Successfully generated: {target_path}')

    write_xlsx('reports/test_cases_and_summary.xlsx')
    write_xlsx('requirements/req3_physical_product/test_cases_and_summary.xlsx')

if __name__ == '__main__':
    generate()
