#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to compile the standalone professional LaTeX report (reports/HW01_Report.tex)
into reports/HW01_Report.pdf using xelatex for FIT@HCMUS CS423 / CSC13003.
"""

import os
import sys
import subprocess

def compile_latex():
    tex_path = os.path.join("reports", "HW01_Report.tex")
    if not os.path.exists(tex_path):
        print(f"Error: {tex_path} not found!", file=sys.stderr)
        sys.exit(1)
        
    xelatex_bin = "/opt/homebrew/bin/xelatex"
    if not os.path.exists(xelatex_bin):
        xelatex_bin = "xelatex"
        
    print(f"Compiling {tex_path} with {xelatex_bin}...")
    
    cmd = [xelatex_bin, "-interaction=nonstopmode", "-output-directory=reports", tex_path]
    
    print("Running pass 1...")
    res1 = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("Running pass 2 (cross-references & LastPage)...")
    res2 = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    pdf_path = os.path.join("reports", "HW01_Report.pdf")
    if os.path.exists(pdf_path):
        print(f"Compilation successful! Generated {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    else:
        print("Compilation failed to produce PDF.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    compile_latex()
