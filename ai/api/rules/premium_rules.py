def evaluate_customer(metrics):
    # Reject if any metric is in the ineligible range
    if 'Hemoglobin' in metrics and (metrics['Hemoglobin'] < 11 or metrics['Hemoglobin'] > 18):
        return {'eligible': False, 'reason': 'Hemoglobin out of insurable range'}
    if 'Glucose' in metrics and metrics['Glucose'] > 125:
        return {'eligible': False, 'reason': 'Glucose indicates diabetes'}
    if 'Cholesterol' in metrics and metrics['Cholesterol'] > 240:
        return {'eligible': False, 'reason': 'Cholesterol too high'}
    if 'WBC' in metrics and (metrics['WBC'] < 3000 or metrics['WBC'] > 12000):
        return {'eligible': False, 'reason': 'WBC out of insurable range'}
    if 'Platelet' in metrics and (metrics['Platelet'] < 100000 or metrics['Platelet'] > 450000):
        return {'eligible': False, 'reason': 'Platelet count out of insurable range'}
    if 'RBC' in metrics and (metrics['RBC'] < 3.5 or metrics['RBC'] > 6.0):
        return {'eligible': False, 'reason': 'RBC out of insurable range'}
    if 'Creatinine' in metrics and metrics['Creatinine'] > 1.5:
        return {'eligible': False, 'reason': 'High creatinine (possible kidney issue)'}
    if 'Urea' in metrics and metrics['Urea'] > 50:
        return {'eligible': False, 'reason': 'High urea (possible kidney issue)'}
    if 'SGPT' in metrics and metrics['SGPT'] > 50:
        return {'eligible': False, 'reason': 'High SGPT (possible liver issue)'}
    if 'SGOT' in metrics and metrics['SGOT'] > 50:
        return {'eligible': False, 'reason': 'High SGOT (possible liver issue)'}
    if 'TSH' in metrics and (metrics['TSH'] < 0.4 or metrics['TSH'] > 5.0):
        return {'eligible': False, 'reason': 'TSH out of insurable range'}
    if 'HDL' in metrics and metrics['HDL'] < 40:
        return {'eligible': False, 'reason': 'Low HDL (bad cholesterol)'}
    if 'LDL' in metrics and metrics['LDL'] > 160:
        return {'eligible': False, 'reason': 'High LDL (bad cholesterol)'}
    if 'Triglycerides' in metrics and metrics['Triglycerides'] > 200:
        return {'eligible': False, 'reason': 'High triglycerides'}
    # Substandard risk (higher premium)
    risk_factor = 1.0
    if 'Hemoglobin' in metrics and (11 <= metrics['Hemoglobin'] < 13 or 17 < metrics['Hemoglobin'] <= 18):
        risk_factor += 0.3
    if 'Glucose' in metrics and 101 <= metrics['Glucose'] <= 125:
        risk_factor += 0.5
    if 'Cholesterol' in metrics and 200 <= metrics['Cholesterol'] <= 240:
        risk_factor += 0.4
    if 'WBC' in metrics and (3000 <= metrics['WBC'] < 4000 or 11000 < metrics['WBC'] <= 12000):
        risk_factor += 0.2
    if 'Platelet' in metrics and (100000 <= metrics['Platelet'] < 150000 or 400000 < metrics['Platelet'] <= 450000):
        risk_factor += 0.2
    if 'RBC' in metrics and (3.5 <= metrics['RBC'] < 4.5 or 5.5 < metrics['RBC'] <= 6.0):
        risk_factor += 0.2
    if 'Creatinine' in metrics and 1.2 < metrics['Creatinine'] <= 1.5:
        risk_factor += 0.2
    if 'Urea' in metrics and 40 < metrics['Urea'] <= 50:
        risk_factor += 0.2
    if 'SGPT' in metrics and 40 < metrics['SGPT'] <= 50:
        risk_factor += 0.2
    if 'SGOT' in metrics and 40 < metrics['SGOT'] <= 50:
        risk_factor += 0.2
    if 'TSH' in metrics and (0.4 <= metrics['TSH'] < 0.5 or 4.5 < metrics['TSH'] <= 5.0):
        risk_factor += 0.2
    if 'HDL' in metrics and 40 <= metrics['HDL'] < 50:
        risk_factor += 0.2
    if 'LDL' in metrics and 130 < metrics['LDL'] <= 160:
        risk_factor += 0.2
    if 'Triglycerides' in metrics and 150 < metrics['Triglycerides'] <= 200:
        risk_factor += 0.2
    base_premium = 5000
    premium = base_premium * risk_factor
    # Market premium is 20% higher (mock)
    market_premium = premium * 1.2
    if premium < market_premium:
        return {
            'eligible': True,
            'premium': premium,
            'market_premium': market_premium,
            'savings': market_premium - premium
        }
    else:
        return {'eligible': False, 'reason': 'Unprofitable for insurer'} 