from ai.api.extractors.pdf_extractor import parse_metrics as parse_pdf_metrics
from ai.api.extractors.image_extractor import parse_metrics as parse_image_metrics

def test_parse_pdf_metrics():
    text = """
    Hemoglobin: 14.2
    WBC: 5600
    Platelet: 250000
    RBC: 4.8
    SGPT: 30
    SGOT: 28
    Creatinine: 1.0
    Urea: 35
    TSH: 2.5
    Glucose: 90
    Cholesterol: 180
    HDL: 50
    LDL: 100
    Triglycerides: 120
    """
    metrics = parse_pdf_metrics(text)
    assert metrics['Hemoglobin'] == 14.2
    assert metrics['WBC'] == 5600
    assert metrics['Platelet'] == 250000
    assert metrics['RBC'] == 4.8
    assert metrics['SGPT'] == 30
    assert metrics['SGOT'] == 28
    assert metrics['Creatinine'] == 1.0
    assert metrics['Urea'] == 35
    assert metrics['TSH'] == 2.5
    assert metrics['Glucose'] == 90
    assert metrics['Cholesterol'] == 180
    assert metrics['HDL'] == 50
    assert metrics['LDL'] == 100
    assert metrics['Triglycerides'] == 120

def test_parse_image_metrics():
    # Use the same text for image metrics for now
    text = """
    Hemoglobin: 14.2
    WBC: 5600
    Platelet: 250000
    RBC: 4.8
    SGPT: 30
    SGOT: 28
    Creatinine: 1.0
    Urea: 35
    TSH: 2.5
    Glucose: 90
    Cholesterol: 180
    HDL: 50
    LDL: 100
    Triglycerides: 120
    """
    metrics = parse_image_metrics(text)
    assert metrics['Hemoglobin'] == 14.2
    assert metrics['WBC'] == 5600
    assert metrics['Platelet'] == 250000
    assert metrics['RBC'] == 4.8
    assert metrics['SGPT'] == 30
    assert metrics['SGOT'] == 28
    assert metrics['Creatinine'] == 1.0
    assert metrics['Urea'] == 35
    assert metrics['TSH'] == 2.5
    assert metrics['Glucose'] == 90
    assert metrics['Cholesterol'] == 180
    assert metrics['HDL'] == 50
    assert metrics['LDL'] == 100
    assert metrics['Triglycerides'] == 120

