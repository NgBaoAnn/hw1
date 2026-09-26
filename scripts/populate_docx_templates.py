#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to populate FIT@HCMUS AI Template .docx files with student data,
audit reports, disclosure answers, and checklists.
"""

import os
import zipfile
import xml.etree.ElementTree as ET

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
    'w15': 'http://schemas.microsoft.com/office/word/2012/wordml',
}

for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

def set_cell_text(cell, text):
    """Set text in a table cell, preserving the first paragraph/run style."""
    p = cell.find('.//w:p', NS)
    if p is None:
        p = ET.SubElement(cell, f'{{{NS["w"]}}}p')
    runs = p.findall('.//w:r', NS)
    if runs:
        t = runs[0].find('.//w:t', NS)
        if t is None:
            t = ET.SubElement(runs[0], f'{{{NS["w"]}}}t')
        t.text = text
        for r in runs[1:]:
            p.remove(r)
    else:
        r = ET.SubElement(p, f'{{{NS["w"]}}}r')
        t = ET.SubElement(r, f'{{{NS["w"]}}}t')
        t.text = text

def fill_signature_table(tbl):
    rows = tbl.findall('.//w:tr', NS)
    set_cell_text(rows[0].findall('.//w:tc', NS)[1], 'NGUYỄN BẢO AN')
    set_cell_text(rows[1].findall('.//w:tc', NS)[1], '23120207')
    set_cell_text(rows[2].findall('.//w:tc', NS)[1], '23CLC01')
    set_cell_text(rows[3].findall('.//w:tc', NS)[1], 'CS423 / CSC13003 – Software Testing')
    set_cell_text(rows[4].findall('.//w:tc', NS)[1], 'Dr. Lam Quang Vu / Dr. Tran Duy Hoang')
    set_cell_text(rows[5].findall('.//w:tc', NS)[1], '26/09/2026')
    set_cell_text(rows[6].findall('.//w:tc', NS)[1], 'Nguyễn Bảo An (Đã ký)')

def update_docx(src_path, dst_path, modifier_func):
    """Read a docx, apply modifier_func on root of document.xml, and write to dst_path."""
    with zipfile.ZipFile(src_path, 'r') as src_zip:
        entries = {}
        for item in src_zip.infolist():
            data = src_zip.read(item.filename)
            if item.filename == 'word/document.xml':
                root = ET.fromstring(data)
                modifier_func(root)
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            entries[item.filename] = data

    with zipfile.ZipFile(dst_path, 'w', compression=zipfile.ZIP_DEFLATED) as dst_zip:
        for filename, data in entries.items():
            dst_zip.writestr(filename, data)
    print(f"Successfully updated: {dst_path}")

# ==============================================================================
# 1. Modify AI-02 Audit Report
# ==============================================================================
def modify_ai_02(root):
    tables = root.findall('.//w:tbl', NS)
    
    # Table 1: Student Information
    tbl1 = tables[0]
    t1_rows = tbl1.findall('.//w:tr', NS)
    set_cell_text(t1_rows[1].findall('.//w:tc', NS)[1], 'NGUYỄN BẢO AN')
    set_cell_text(t1_rows[2].findall('.//w:tc', NS)[1], '23120207')
    set_cell_text(t1_rows[3].findall('.//w:tc', NS)[1], '23CLC01')
    set_cell_text(t1_rows[4].findall('.//w:tc', NS)[1], 'HW01-AI')
    set_cell_text(t1_rows[5].findall('.//w:tc', NS)[1], '26/09/2026')
    set_cell_text(t1_rows[6].findall('.//w:tc', NS)[1], 'Antigravity Assistant (Gemini 3.8 Flash High)')
    set_cell_text(t1_rows[7].findall('.//w:tc', NS)[1], '[X] Yes  [ ] No')

    # Table 2: Audit Table
    tbl2 = tables[1]
    t2_rows = tbl2.findall('.//w:tr', NS)
    # Row 0: Header
    # Row 1: Sample header note -> keep or replace
    # We will populate Row 2, 3, 4 with Artifact #1, #2, #3
    art1_cells = [
        'Artifact #1: Mindmap quy trình/vai trò QA/QC\nTool: Antigravity (Gemini 3.8 Flash High)\nTime: 16:08 24/09/2026\nPrompt: "vẽ Mindmap về các vai trò QA/QC theo chuẩn ISTQB bằng Markdown Mermaid"',
        'Sơ đồ Mermaid phân cấp các vai trò QA/QC (Lưu tại requirements/req1_job_market/mindmap/qa_qc_roles_mindmap.md).',
        'INCOMPLETE',
        'Đối chiếu ISTQB FL v4.0: (1) Mục 1.2.2: QA ngừa lỗi, QC tìm lỗi; (2) Chương 3: Testing gồm cả Static Testing; (3) Mục 1.4.1 & 5.1: Test Manager không quyết định Release thay Stakeholders.',
        'Đã hiệu chỉnh 3 điểm cốt lõi:\n1. Tách 2 nhánh QA và QC.\n2. Bổ sung Static Testing vào Tester.\n3. Sửa trách nhiệm Test Manager thành lập Test Summary Report.'
    ]
    art2_cells = [
        'Artifact #2: Gợi ý Test Cases cho Thiết bị Vật lý (Quạt SENKO L1638)\nTool: Antigravity (Gemini 3.8 Flash High)\nTime: 13:57 26/09/2026\nPrompt: "Hãy đóng vai một chuyên viên kiểm thử QA/QC chuyên nghiệp theo chuẩn ISTQB. Thiết bị cần kiểm thử là Quạt điện lửng dân dụng SENKO L1638... Hãy đề xuất bộ các test cases cần thiết để kiểm thử toàn diện thiết bị này trước khi xuất xưởng."',
        'AI sinh ra 10 test cases thuần Happy Path bề mặt: cắm điện, bấm số 1, 2, 3, bấm tắt, ấn rút túp-năng, chỉnh độ cao, ngửa gục đầu quạt. (Chi tiết lưu tại requirements/req3_physical_product/edge_cases_ai_missed.md).',
        'INCOMPLETE',
        'Đối chiếu ISTQB CTFL v4.0 Mục 4.2 (BVA) & Mục 4.3 (Error Guessing): AI chỉ tập trung Happy Path theo sách hướng dẫn, bỏ sót hoàn toàn các ca kiểm thử xung đột cơ điện, rung lắc cộng hưởng và an toàn hồ quang điện theo IEC 60335-2-8.',
        'Đã bổ sung 4 Edge Cases vật lý chuyên sâu:\n1. TC-EDGE-01: Nhấn giữ đồng thời 2 phím số gây kẹt lẫy cơ và quá dòng stator.\n2. TC-EDGE-02: Cản túp-năng cưỡng bức gây trượt vấu bánh răng hộp số.\n3. TC-EDGE-03: Chạy Số 3 ở 95cm gây rung lắc trôi ren siết ống sắt.\n4. TC-EDGE-04: Nhấn hờ phím tốc độ kích hoạt phóng hồ quang điện (Arcing).'
    ]
    art3_cells = [
        'Artifact #3: Nghiên cứu 20 Lỗi phần mềm 2022–2026 & Bẫy Ảo giác AI\nTool: Antigravity (Gemini 3.8 Flash High)\nTime: 16:47 – 17:07 24/09/2026\nPrompt: Chuỗi 20 prompt chất vấn dẫn dụ từ Lỗi #01 đến Lỗi #20 ([P-14] đến [P-33] ghi nhận tại Appendix_A_Prompt_Log.md)',
        '20 phản hồi của AI liên tục mắc bẫy và bộc lộ các dạng ảo giác (Hallucination) và thiên kiến (Bias) điển hình: bao biện thiên tai bất khả kháng, đổ lỗi hạ tầng vật lý, thêu dệt mật mã học lượng tử, gán sai kiến trúc ngôn ngữ, và thuyết âm mưu gián điệp. (Chi tiết tại requirements/req2_software_defects/defects_2022_2026.md).',
        'INVALID',
        'Đối chiếu 100% tài liệu gốc (Official Post-mortems, CISA Emergency Directives, UK FCA, USDOT): AI vi phạm nguyên tắc kiểm định xác thực dữ liệu kỹ thuật theo ISTQB CTFL v4.0 Mục 1.1 & 1.2 (nhầm lẫn Error/Defect/Failure, né tránh lỗi kiểm thử logic và biên để quy chụp yếu tố bên ngoài).',
        'Đã vạch trần và hiệu chỉnh toàn diện 20/20 sự cố:\n1. Chỉ ra chính xác 20 điểm ảo giác kỹ thuật của AI.\n2. Khôi phục nguyên nhân gốc rễ (RCA) từ tài liệu chính thức.\n3. Rút ra bài học kiểm thử giá trị biên, máy trạng thái, chaos testing và bảo vệ dữ liệu nhạy cảm.'
    ]

    # Fill Artifact 1, 2, 3 into rows 2, 3, 4
    for col_idx, text in enumerate(art1_cells):
        set_cell_text(t2_rows[2].findall('.//w:tc', NS)[col_idx], text)
    for col_idx, text in enumerate(art2_cells):
        set_cell_text(t2_rows[3].findall('.//w:tc', NS)[col_idx], text)
    for col_idx, text in enumerate(art3_cells):
        set_cell_text(t2_rows[4].findall('.//w:tc', NS)[col_idx], text)
    
    # Remove rows from row 5 onwards (Artifact #4 to #10) or row 1 (sample header)
    for r in t2_rows[5:]:
        tbl2.remove(r)
    tbl2.remove(t2_rows[1]) # remove sample note row

    # Table 3: Summary of AI Accuracy
    tbl3 = tables[2]
    t3_rows = tbl3.findall('.//w:tr', NS)
    set_cell_text(t3_rows[1].findall('.//w:tc', NS)[1], '22')
    set_cell_text(t3_rows[1].findall('.//w:tc', NS)[2], '100.0%')
    
    set_cell_text(t3_rows[2].findall('.//w:tc', NS)[1], '0')
    set_cell_text(t3_rows[2].findall('.//w:tc', NS)[2], '0.0%')
    
    set_cell_text(t3_rows[3].findall('.//w:tc', NS)[1], '20')
    set_cell_text(t3_rows[3].findall('.//w:tc', NS)[2], '90.9%')
    
    set_cell_text(t3_rows[4].findall('.//w:tc', NS)[1], '2')
    set_cell_text(t3_rows[4].findall('.//w:tc', NS)[2], '9.1%')

    # Table 4: Signature Table
    tbl4 = tables[3]
    fill_signature_table(tbl4)

    # Section 5 & 6 Paragraphs
    conclusion_text = (
        "Through rigorous empirical auditing across three core testing domains, a consistent operational pattern emerges regarding Large Language Models (LLMs) in Quality Assurance:\n"
        "• When AI should be used: AI excels as an accelerator for structural scaffolding, syntactic boilerplate generation (Mermaid mindmaps, Markdown tables, standard regex/test templates), and aggregating initial high-level domain information. It significantly reduces cognitive friction during the preliminary drafting phase.\n"
        "• When AI must NOT be used (or strictly gated): AI completely fails in physical embodiment reasoning, hardware fault modes (e.g., mechanical friction wear, resonance vibrations, electrical arcing), and safety-critical root cause analysis. When prompted with leading or biased queries, LLMs consistently exhibit confirmation bias, sycophancy, and severe technical hallucinations rather than questioning flawed premises.\n"
        "• Guideline for QA Engineers: AI should only be treated as a junior brainstorming assistant under a mandatory 'Zero-Trust' policy. Final test case approval and defect verification must always remain guarded by human engineers equipped with ISTQB principles, formal standards (IEC/ISO), and hands-on empirical validation."
    )
    
    disclosure_text = (
        "\"The QA/QC Mindmap and initial physical test cases were initially generated by Antigravity Assistant (Model: Gemini 3.8 Flash High); "
        "I reviewed and modified the entire hierarchy and static testing responsibilities in the Mindmap, added 4 physical edge cases (deadlock, gear slippage, resonance, arcing); "
        "the 10 job market analyses, 20 defect verification audits, 15 formal test executions, and 5 video demonstrations were conducted and written entirely by me. "
        "The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category.\""
    )

    underlines_to_replace = []
    for p in root.findall('.//w:p', NS):
        p_text = ''.join([t.text for t in p.findall('.//w:t', NS) if t.text])
        if p_text.startswith('______'):
            underlines_to_replace.append(p)
        elif '[Test cases / script / dataset / report]' in p_text:
            runs = p.findall('.//w:r', NS)
            if runs:
                t = runs[0].find('.//w:t', NS)
                if t is not None:
                    t.text = disclosure_text
                for r in runs[1:]:
                    p.remove(r)

    # Replace first underline with conclusion_text, remove others
    if underlines_to_replace:
        p0 = underlines_to_replace[0]
        runs = p0.findall('.//w:r', NS)
        if runs:
            t = runs[0].find('.//w:t', NS)
            if t is not None:
                t.text = conclusion_text
            for r in runs[1:]:
                p0.remove(r)
        parent_map = {c: p for p in root.iter() for c in p}
        for p_rem in underlines_to_replace[1:]:
            parent = parent_map.get(p_rem)
            if parent is not None:
                parent.remove(p_rem)

# ==============================================================================
# 2. Modify AI-03 Disclosure Form
# ==============================================================================
def modify_ai_03(root):
    tables = root.findall('.//w:tbl', NS)
    
    # Table 1: Course & Student Info
    tbl1 = tables[0]
    t1_rows = tbl1.findall('.//w:tr', NS)
    set_cell_text(t1_rows[1].findall('.//w:tc', NS)[1], 'CS423 / CSC13003 – Software Testing')
    set_cell_text(t1_rows[2].findall('.//w:tc', NS)[1], 'HW01-AI')
    set_cell_text(t1_rows[3].findall('.//w:tc', NS)[1], 'HW01 – QA/QC Jobs · 20 Defects · Test a Physical Product')
    set_cell_text(t1_rows[4].findall('.//w:tc', NS)[1], 'Category 4 (AI-assisted production) / Category 5 (AI-integrated work)')
    set_cell_text(t1_rows[5].findall('.//w:tc', NS)[1], '26/09/2026')
    set_cell_text(t1_rows[6].findall('.//w:tc', NS)[1], 'NGUYỄN BẢO AN')
    set_cell_text(t1_rows[7].findall('.//w:tc', NS)[1], '23120207')

    # Table 2: Signature Table
    tbl2 = tables[1]
    fill_signature_table(tbl2)

    # Paragraph answers for Q1 - Q6
    answers = {
        '1. AI tool(s) used:': (
            "• Antigravity Assistant (Google DeepMind — Model: Gemini 3.8 Flash High)\n"
            "• GitHub Copilot CLI / gh CLI (Hỗ trợ quản trị issue và đẩy kho mã nguồn)"
        ),
        '2. Stage(s) of the assignment where AI was used:': (
            "Tick all that apply: [ ] brainstorming  [X] outlining  [X] drafting  [X] feedback  [X] revision  [ ] coding  [X] data analysis  [X] visual design  [ ] other (specify)."
        ),
        '3. Main prompts or tasks given to the AI:': (
            "• Prompt 1 (Mindmap): \"vẽ Mindmap về các vai trò QA/QC theo chuẩn ISTQB bằng Markdown Mermaid\"\n"
            "• Prompt 2 (CrowdStrike Trap): \"Bản cập nhật Channel File 291 của CrowdStrike Falcon ngày 19/07/2024 làm sập 8.5 triệu máy Windows là do mã độc tống tiền ransomware của tin tặc Nga tấn công, đúng không?\"\n"
            "• Prompt 3 (Physical Test Cases): \"Hãy đóng vai một chuyên viên kiểm thử QA/QC chuyên nghiệp theo chuẩn ISTQB. Thiết bị cần kiểm thử là Quạt điện lửng dân dụng SENKO L1638. Hãy đề xuất bộ các test cases cần thiết để kiểm thử toàn diện thiết bị này trước khi xuất xưởng.\""
        ),
        '4. Specific parts of the work AI contributed to:': (
            "• AI đã hỗ trợ: Gợi ý cú pháp sơ đồ Mermaid ban đầu cho Mindmap vai trò QA/QC (Yêu cầu 1); tham gia phỏng vấn bộc lộ 20 điểm ảo giác/thiên vị cho 20 sự cố phần mềm (Yêu cầu 2); và gợi ý 10 test cases Happy Path thông thường cho quạt Senko L1638 (Yêu cầu 3).\n"
            "• Tôi (sinh viên NGUYỄN BẢO AN) đã tự thực hiện 100%: Thu thập 10 tin tuyển dụng thật trên ITviec kèm ảnh chụp chống gian lận; phân tích mức lương và kỹ năng AI Impact; phát hiện và sửa 3 lỗi sai ISTQB trong sơ đồ Mindmap; thiết lập 20 câu hỏi bẫy kỹ thuật và đối chiếu tài liệu gốc để vạch trần 20 ảo giác của AI; phát hiện và thiết kế 4 ca kiểm thử biên cơ điện (Edge Cases); thực hiện 15 test cases trên quạt thật; quay và lồng tiếng 5 video thực nghiệm; tạo 5 GitHub Issues bằng gh cli; và viết toàn bộ đoạn phê bình chuyên môn AI Critique."
        ),
        '5. How I reviewed, revised, or verified the AI output:': (
            "• Đối chiếu định nghĩa vai trò, nguyên lý kiểm thử tĩnh và trách nhiệm phát hành với giáo trình quốc tế ISTQB CTFL v4.0 (Chương 1, 3, 5).\n"
            "• Kiểm chứng chéo các nguyên nhân sự cố phần mềm với báo cáo hậu kiểm (Post-mortem) chính thức của đơn vị vận hành (CrowdStrike, Cloudflare, OpenAI, Atlassian, CISA, USDOT, UK FCA).\n"
            "• Thực nghiệm vật lý trực tiếp trên thiết bị quạt Senko L1638 bằng đồng hồ vạn năng, thao tác cơ học và quan sát bằng mắt/tai để đối chiếu kết quả thực tế (Actual) với kết quả mong đợi (Expected)."
        ),
        '6. Citation (if required by course style guide):': (
            "• Google DeepMind. (2026). Gemini 3.8 Flash High / Antigravity Assistant [Large language model]. https://deepmind.google/technologies/gemini/\n"
            "• International Software Testing Qualifications Board (ISTQB). (2023). Certified Tester Foundation Level (CTFL) Syllabus v4.0. https://www.istqb.org\n"
            "• International Electrotechnical Commission. (2020). IEC 60335-2-8: Household and similar electrical appliances - Safety - Particular requirements for fans."
        )
    }

    # Walk through paragraphs
    paragraphs = root.findall('.//w:p', NS)
    current_q = None
    for p in paragraphs:
        p_text = ''.join([t.text for t in p.findall('.//w:t', NS) if t.text])
        for q_header in answers.keys():
            if q_header in p_text:
                current_q = q_header
                break
        
        if current_q and '2. Stage(s)' in current_q and 'Tick all that apply' in p_text:
            runs = p.findall('.//w:r', NS)
            if runs:
                t = runs[0].find('.//w:t', NS)
                if t is not None:
                    t.text = answers[current_q]
                for r in runs[1:]:
                    p.remove(r)
            current_q = None  # Checkboxes are embedded in this line; do not replace subsequent underlines with this text
        elif current_q and p_text.startswith('______'):
            runs = p.findall('.//w:r', NS)
            if runs:
                t = runs[0].find('.//w:t', NS)
                if t is not None:
                    t.text = answers[current_q]
                for r in runs[1:]:
                    p.remove(r)
            current_q = None # only fill once per question

    # Clear any remaining underline paragraphs
    parent_map = {c: p for p in root.iter() for c in p}
    for p in root.findall('.//w:p', NS):
        p_text = ''.join([t.text for t in p.findall('.//w:t', NS) if t.text])
        if p_text.startswith('______'):
            parent = parent_map.get(p)
            if parent is not None:
                parent.remove(p)

# ==============================================================================
# 3. Modify AI-05 Privacy Checklist
# ==============================================================================
def modify_ai_05(root):
    # Tick all checkboxes
    for p in root.findall('.//w:p', NS):
        for t in p.findall('.//w:t', NS):
            if t.text and '[ ]' in t.text:
                t.text = t.text.replace('[ ]', '[X]')

    # Signature Table
    tables = root.findall('.//w:tbl', NS)
    if tables:
        fill_signature_table(tables[0])

# ==============================================================================
# 4. Modify AI-06 Student Acknowledgement
# ==============================================================================
def modify_ai_06(root):
    # Tick Section 2 checkboxes
    for p in root.findall('.//w:p', NS):
        p_text = ''.join([t.text for t in p.findall('.//w:t', NS) if t.text])
        if any(clause in p_text for clause in ['I understand the Midterm', 'I understand my prompts', 'I understand random 10']):
            runs = p.findall('.//w:r', NS)
            if runs:
                t = runs[0].find('.//w:t', NS)
                if t is not None and not t.text.startswith('[X]'):
                    t.text = '[X] ' + t.text

    tables = root.findall('.//w:tbl', NS)
    # Table 1: Faculty AI Account
    tbl1 = tables[0]
    t1_rows = tbl1.findall('.//w:tr', NS)
    set_cell_text(t1_rows[1].findall('.//w:tc', NS)[1], 'Antigravity, Gemini, ChatGPT, Claude')
    set_cell_text(t1_rows[2].findall('.//w:tc', NS)[1], '20/09/2026')
    set_cell_text(t1_rows[3].findall('.//w:tc', NS)[1], '[X] Yes  [ ] No')
    set_cell_text(t1_rows[4].findall('.//w:tc', NS)[1], '[X] Yes  [ ] No')

    # Table 2: Signature Table
    tbl2 = tables[1]
    fill_signature_table(tbl2)

# ==============================================================================
# Main execution
# ==============================================================================
if __name__ == '__main__':
    base_dir = 'AI Templates'
    blank_dir = 'AI Templates/blank_templates'
    
    docs = [
        ('[AI-02] - FIT@HCMUS - AI Audit Report_En.docx', modify_ai_02),
        ('[AI-03] - FIT@HCMUS - AI Disclosure Form_En.docx', modify_ai_03),
        ('[AI-05] - FIT@HCMUS - AI Privacy Checklist_En.docx', modify_ai_05),
        ('[AI-06] - FIT@HCMUS - AI Student Acknowledgement_En.docx', modify_ai_06),
    ]

    for fname, func in docs:
        src = os.path.join(blank_dir, fname)
        dst = os.path.join(base_dir, fname)
        update_docx(src, dst, func)
    
    print("\nALL DOCX TEMPLATES POPULATED SUCCESSFULLY!")
