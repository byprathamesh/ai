import pdfplumber
import re

def extract_metrics_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
    return parse_metrics(text)

def parse_metrics(text):
    metrics = {}
    # Hemoglobin
    match = re.search(r'Hemoglobin\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['Hemoglobin'] = float(match.group(1))
    # WBC
    match = re.search(r'WBC\s*[:\-]?\s*([\d,\.]+)', text, re.IGNORECASE)
    if match:
        metrics['WBC'] = float(match.group(1).replace(',', ''))
    # Platelet
    match = re.search(r'Platelet\s*[:\-]?\s*([\d,\.]+)', text, re.IGNORECASE)
    if match:
        metrics['Platelet'] = float(match.group(1).replace(',', ''))
    # RBC
    match = re.search(r'RBC\s*[:\-]?\s*([\d,\.]+)', text, re.IGNORECASE)
    if match:
        metrics['RBC'] = float(match.group(1).replace(',', ''))
    # SGPT
    match = re.search(r'SGPT\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['SGPT'] = float(match.group(1))
    # SGOT
    match = re.search(r'SGOT\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['SGOT'] = float(match.group(1))
    # Creatinine
    match = re.search(r'Creatinine\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['Creatinine'] = float(match.group(1))
    # Urea
    match = re.search(r'Urea\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['Urea'] = float(match.group(1))
    # TSH
    match = re.search(r'TSH\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['TSH'] = float(match.group(1))
    # Glucose
    match = re.search(r'Glucose\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['Glucose'] = float(match.group(1))
    # Cholesterol
    match = re.search(r'Cholesterol\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['Cholesterol'] = float(match.group(1))
    # HDL
    match = re.search(r'HDL\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['HDL'] = float(match.group(1))
    # LDL
    match = re.search(r'LDL\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['LDL'] = float(match.group(1))
    # Triglycerides
    match = re.search(r'Triglycerides\s*[:\-]?\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        metrics['Triglycerides'] = float(match.group(1))
    return metrics 