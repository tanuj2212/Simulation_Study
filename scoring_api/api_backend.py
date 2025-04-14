from scoring_api.scoring_functions_backend import *
'''
data: {
  Condom: { '1': 'Positive', '2': 'No' },
  'Cost Effectiveness': { '1': 'Important' },
  'Pregnancy Prevention': { '1': 'Neutral' },
  'Management of Period and Side Effects': { '1': 'Neutral' },
  'Low Chance of Weight Gain/Loss': { '1': 'Neutral' },
  "Partner's Willingness to Participate in Contraception": { '1': 'Neutral/No partner' },
  'STI Prevention': { '1': 'Important' },
  'Willing to Insert Foreign Object Into Vagina': { '1': 'Neutral/No partner' },
  'Willing to Seek Consultation by a Medical Professional': { '1': 'Neutral/No partner' },
  'Willing to Undergo a Medical Procedure': { '1': 'Neutral/No partner' },
  Acne: { '1': 'Severe' },
  'Migraine with Aura': { '1': 'Mild' }
}'''

    
def parse_decision_factors(data):
    decision_factors = {
        "Condom": [data.get("Condom", {}).get('1', 'none'), data.get("Condom", {}).get('2', 'none')],
        "Internal Condom": [data.get("Internal Condom", {}).get('1', 'none'), data.get("Internal Condom", {}).get('2', 'none')],
        "Cervical Cap": [data.get("Cervical Cap", {}).get('1', 'none'), data.get("Cervical Cap", {}).get('2', 'none')],
        "Fertility Awareness Methods (FAM)": [data.get("Fertility Awareness Methods (FAM)", {}).get('1', 'none'), 
                                             data.get("Fertility Awareness Methods (FAM)", {}).get('2', 'none')],
        "Arm Implant": [data.get("Arm Implant", {}).get('1', 'none'), data.get("Arm Implant", {}).get('2', 'none')],
        "Copper IUD": [data.get("Copper IUD", {}).get('1', 'none'), data.get("Copper IUD", {}).get('2', 'none')],
        "Hormonal IUD": [data.get("Hormonal IUD", {}).get('1', 'none'), data.get("Hormonal IUD", {}).get('2', 'none')],
        "The Patch": [data.get("The Patch", {}).get('1', 'none'), data.get("The Patch", {}).get('2', 'none')],
        "Combination (Combo) Pill": [data.get("Combination (Combo) Pill", {}).get('1', 'none'), data.get("Combination (Combo) Pill", {}).get('2', 'none')],
        "Mini Pill": [data.get("Mini Pill", {}).get('1', 'none'), 
                                          data.get("Mini Pill", {}).get('2', 'none')],
        "The Ring": [data.get("The Ring", {}).get('1', 'none'), data.get("The Ring", {}).get('2', 'none')],
        "Shot": [data.get("The Shot", {}).get('1', 'none'), data.get("The Shot", {}).get('2', 'none')],
        "Sterilization": [data.get("Sterilization", {}).get('1', 'none'), data.get("Sterilization", {}).get('2', 'none')],
        "Spermicide/Vaginal Gel": [data.get("Spermicide/Vaginal Gel", {}).get('1', 'none'), 
                                  data.get("Spermicide/Vaginal Gel", {}).get('2', 'none')],
        "Withdrawal": [data.get("Withdrawal", {}).get('1', 'none'), data.get("Withdrawal", {}).get('2', 'none')],
        "Cost Effectiveness": "none",
        "Pregnancy Prevention": "none",
        "Management of Period and Side Effects": "none",
        "Low Chance of Weight Gain/Loss": "none",
        "Maintenance of Birth Control": "none",
        "Partner's Willingness to Participate in Contraception": "none",
        "STI Prevention": "none",
        "Hormones Used": "none",
        "Willing to Insert Foreign Object Into Vagina": "none",
        "Willing to Seek Consultation by a Medical Professional": "none",
        "Willing to Undergo a Medical Procedure": "none",
        "Acne": "none",
        "Anxiety": "none",
        "Depression": "none",
        "Top Gender Dysphoria": "none",
        "Bottom Gender Dysphoria for Periods": "none",
        "Bottom Gender Dysphoria for Vaginal Insertion": "none",
        "Gender Dysphoria for Pregnancy": "none",
        "Migraine with Aura": "none",
        "Smoker over 35 years old": "none",
        "Hypertension": "none",
        "Blood Clots": "none",
        "CHF or CAD": "none",
        "PCOS": "none",
        "Endometriosis": "none",
        "Breast Cancer": "none",
        "Testosterone Hormone Replacement Therapy": "none",
        "Top Surgery": "none"
    }

    compulsory = {
        "Cost Effectiveness": None,
        "Pregnancy Prevention": None,
        "Management of Period and Side Effects": None,
        "Low Chance of Weight Gain/Loss": None,
        "Maintenance of Birth Control": None,
        "Partner's Willingness to Participate in Contraception": None,
        "STI Prevention": None,
        "Hormones Used": None,
        "Willing to Insert Foreign Object Into Vagina": None,
        "Willing to Seek Consultation by a Medical Professional": None,
        "Willing to Undergo a Medical Procedure": None
    }
    method_history = {
        "Condoms": None,
        "Internal Condoms": None,
        "Cervical Cap": None,
        "Fertility Awareness Methods (FAM)": None,
        "The Arm Implant": None,
        "The Copper IUD": None,
        "The Hormonal IUD": None,
        "The Patch": None,
        "The Combo Pill": None,
        "The Mini Pill (progestin only)": None,
        "The Ring": None,
        "The Shot": None,
        "Spermicide/Vaginal Gel": None,
        "Withdrawal": None,
    }

    medical_conditions = {
        "Acne": None,
        "Anxiety": None,
        "Depression": None,
        "Top Gender Dysphoria": None,
        "Bottom Gender Dysphoria for Periods": None,
        "Bottom Gender Dysphoria for Vaginal Insertion": None,
        "Gender Dysphoria for Pregnancy": None
    }

    medical_history = {
        "Migraine with Aura": None,
        "Smoker over 35 years old": None,
        "Hypertension": None,
        "Blood Clots": None,
        "CHF or CAD": None,
        "PCOS": None,
        "Endometriosis": None,
        "Breast Cancer": None,
        "Testosterone Hormone Replacement Therapy": None,
        "Top Surgery": None

    }
    
    for key in data.keys():
        for factor in compulsory.keys():
            if key == factor:
                if data[key]['1'] == 'Very Important':
                    ans = "v_imp"
                elif data[key]['1'] == 'Important':
                    ans = "imp"
                elif data[key]['1'] == 'Neutral':
                    ans = "neutral"
                elif data[key]['1'] == 'Very Unimportant':
                    ans = "v_unp"
                elif data[key]['1'] == 'Unimportant':
                    ans = "unp"
                elif data[key]['1'] == 'Slighly Important':
                    ans = "s_imp"
                elif data[key]['1'] == 'Slightly Unimportant':
                    ans = "s_unp"
                decision_factors[key] = ans
    
    for key in data.keys():
        for factor in method_history.keys():
            if key == factor:
                experience = data[key]['1']
                use_again = data[key]['2']
                decision_factors[factor] = {
                    "experience": experience,
                    "use_again": use_again
                }
    for key in data.keys():
        for factor in medical_conditions.keys():
            if key == factor:
                if data[key]['1'] == 'Severe':
                    ans = "severe"
                elif data[key]['1'] == 'Mild':
                    ans = "mild"
                elif data[key]['1'] == 'Moderate':
                    ans = "moderate"
                else:
                    ans = "none"
                
                decision_factors[key] = ans
    
    for key in data.keys():
        for factor in medical_history.keys():
            if key == factor:
                decision_factors[key] = "yes"

        
    condoms_arr = [
        decision_factors["Condom"][0], 
        decision_factors["Condom"][1], 
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"], 
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"], 
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    internal_condoms_arr = [
        decision_factors["Internal Condom"][0],
        decision_factors["Internal Condom"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    cervical_cap_arr = [
        decision_factors["Cervical Cap"][0],
        decision_factors["Cervical Cap"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    fam_arr = [
        decision_factors["Fertility Awareness Methods (FAM)"][0],
        decision_factors["Fertility Awareness Methods (FAM)"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    arm_implant_arr = [
        decision_factors["Arm Implant"][0],
        decision_factors["Arm Implant"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    copper_iud_arr = [
        decision_factors["Copper IUD"][0],
        decision_factors["Copper IUD"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    hormonal_iud_arr = [
        decision_factors["Hormonal IUD"][0],
        decision_factors["Hormonal IUD"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    patch_arr = [
        decision_factors["The Patch"][0],
        decision_factors["The Patch"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    combo_pill_arr = [
        decision_factors["Combination (Combo) Pill"][0],
        decision_factors["Combination (Combo) Pill"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    mini_pill_arr = [
        decision_factors["Mini Pill"][0],
        decision_factors["Mini Pill"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    ring_arr = [
        decision_factors["The Ring"][0],
        decision_factors["The Ring"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    shot_arr = [
        decision_factors["Shot"][0],
        decision_factors["Shot"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    sterilization_arr = [
        decision_factors["Sterilization"][0],
        decision_factors["Sterilization"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    spermicide_arr = [
        decision_factors["Spermicide/Vaginal Gel"][0],
        decision_factors["Spermicide/Vaginal Gel"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    withdrawal_arr = [
        decision_factors["Withdrawal"][0],
        decision_factors["Withdrawal"][1],
        decision_factors["Cost Effectiveness"],
        decision_factors["Pregnancy Prevention"],
        decision_factors["Management of Period and Side Effects"],
        decision_factors["Low Chance of Weight Gain/Loss"],
        decision_factors["Maintenance of Birth Control"],
        decision_factors["Partner's Willingness to Participate in Contraception"],
        decision_factors["STI Prevention"],
        decision_factors["Hormones Used"],
        decision_factors["Willing to Insert Foreign Object Into Vagina"],
        decision_factors["Willing to Seek Consultation by a Medical Professional"],
        decision_factors["Willing to Undergo a Medical Procedure"],
        decision_factors["Acne"],
        decision_factors["Anxiety"],
        decision_factors["Depression"],
        decision_factors["Top Gender Dysphoria"],
        decision_factors["Bottom Gender Dysphoria for Periods"],
        decision_factors["Bottom Gender Dysphoria for Vaginal Insertion"],
        decision_factors["Gender Dysphoria for Pregnancy"],
        decision_factors["Migraine with Aura"],
        decision_factors["Smoker over 35 years old"],
        decision_factors["Hypertension"],
        decision_factors["Blood Clots"],
        decision_factors["CHF or CAD"],
        decision_factors["PCOS"],
        decision_factors["Endometriosis"],
        decision_factors["Breast Cancer"],
        decision_factors["Testosterone Hormone Replacement Therapy"],
        decision_factors["Top Surgery"]
    ]

    # Return all arrays in a dictionary
    return {
        "Condom": condoms_arr,
        "Internal Condom": internal_condoms_arr,
        "Cervical Cap": cervical_cap_arr,
        "Fertility Awareness Methods (FAM)": fam_arr,
        "Arm Implant": arm_implant_arr,
        "Copper IUD": copper_iud_arr,
        "Hormonal IUD": hormonal_iud_arr,
        "The Patch": patch_arr,
        "Combination (Combo) Pill": combo_pill_arr,
        "Mini Pill": mini_pill_arr,
        "The Ring": ring_arr,
        "Shot": shot_arr,
        "Sterilization": sterilization_arr,
        "Spermicide/Vaginal Gel": spermicide_arr,
        "Withdrawal": withdrawal_arr
    }




def score_contraceptives(input_arrays):
    arm_implant_arr_full = input_arrays["Arm Implant"]
    hormonal_iud_arr_full = input_arrays["Hormonal IUD"]
    patch_arr_full = input_arrays["The Patch"]
    combo_pill_arr_full = input_arrays["Combination (Combo) Pill"]
    mini_pill_arr_full = input_arrays["Mini Pill"]
    ring_arr_full = input_arrays["The Ring"]
    shot_arr_full = input_arrays["Shot"]
    condom_arr_full = input_arrays["Condom"]
    internal_condom_arr_full = input_arrays["Internal Condom"]
    cervical_cap_arr_full = input_arrays["Cervical Cap"]
    fam_arr_full = input_arrays["Fertility Awareness Methods (FAM)"]
    copper_iud_arr_full = input_arrays["Copper IUD"]
    sterilization_arr_full = input_arrays["Sterilization"]
    spermicide_arr_full = input_arrays["Spermicide/Vaginal Gel"]
    withdrawal_arr_full = input_arrays["Withdrawal"]

    arm_implant_arr = ["Arm Implant", arm_implant_arr_full[0], arm_implant_arr_full[1], arm_implant_arr_full[3], arm_implant_arr_full[4], arm_implant_arr_full[5], arm_implant_arr_full[6], arm_implant_arr_full[9], arm_implant_arr_full[11], arm_implant_arr_full[12], arm_implant_arr_full[13], arm_implant_arr_full[14], arm_implant_arr_full[15], arm_implant_arr_full[26], arm_implant_arr_full[28]]
    hormonal_iud_arr = ["Hormonal IUD", hormonal_iud_arr_full[0], hormonal_iud_arr_full[1],  hormonal_iud_arr_full[3], hormonal_iud_arr_full[4], hormonal_iud_arr_full[5], hormonal_iud_arr_full[6], hormonal_iud_arr_full[9], hormonal_iud_arr_full[10], hormonal_iud_arr_full[11], hormonal_iud_arr_full[12], hormonal_iud_arr_full[13], hormonal_iud_arr_full[14], hormonal_iud_arr_full[15], hormonal_iud_arr_full[19], hormonal_iud_arr_full[22], hormonal_iud_arr_full[23], hormonal_iud_arr_full[26], hormonal_iud_arr_full[27], hormonal_iud_arr_full[28]]
    patch_arr = ["Patch", patch_arr_full[0], patch_arr_full[1],  patch_arr_full[2], patch_arr_full[3], patch_arr_full[4], patch_arr_full[5], patch_arr_full[6], patch_arr_full[9], patch_arr_full[11], patch_arr_full[13], patch_arr_full[14], patch_arr_full[15], patch_arr_full[16], patch_arr_full[17], patch_arr_full[18], patch_arr_full[19], patch_arr_full[20], patch_arr_full[21], patch_arr_full[22], patch_arr_full[23], patch_arr_full[24], patch_arr_full[25], patch_arr_full[26], patch_arr_full[28], patch_arr_full[29]]
    combo_pill_arr = ["Combo Pill", combo_pill_arr_full[0],combo_pill_arr_full[1],combo_pill_arr_full[2], combo_pill_arr_full[3], combo_pill_arr_full[4],combo_pill_arr_full[5],combo_pill_arr_full[6],combo_pill_arr_full[9],combo_pill_arr_full[11],combo_pill_arr_full[13],combo_pill_arr_full[14],combo_pill_arr_full[15],combo_pill_arr_full[16],combo_pill_arr_full[17],combo_pill_arr_full[18],combo_pill_arr_full[19],combo_pill_arr_full[20],combo_pill_arr_full[21],combo_pill_arr_full[22],combo_pill_arr_full[23],combo_pill_arr_full[24],combo_pill_arr_full[25],combo_pill_arr_full[26],combo_pill_arr_full[28],combo_pill_arr_full[29]]
    mini_pill_arr = ["Mini Pill", mini_pill_arr_full[0], mini_pill_arr_full[1],  mini_pill_arr_full[2], mini_pill_arr_full[3], mini_pill_arr_full[4], mini_pill_arr_full[5], mini_pill_arr_full[6], mini_pill_arr_full[9], mini_pill_arr_full[11], mini_pill_arr_full[13], mini_pill_arr_full[14], mini_pill_arr_full[15], mini_pill_arr_full[19], mini_pill_arr_full[22], mini_pill_arr_full[23], mini_pill_arr_full[26], mini_pill_arr_full[28]]
    ring_arr = ["Ring", ring_arr_full[0], ring_arr_full[1],  ring_arr_full[2], ring_arr_full[3], ring_arr_full[4], ring_arr_full[5], ring_arr_full[6], ring_arr_full[9], ring_arr_full[11], ring_arr_full[12], ring_arr_full[13], ring_arr_full[14], ring_arr_full[15], ring_arr_full[16], ring_arr_full[17], ring_arr_full[18], ring_arr_full[19], ring_arr_full[20], ring_arr_full[21], ring_arr_full[22], ring_arr_full[23], ring_arr_full[24], ring_arr_full[25], ring_arr_full[26], ring_arr_full[28], ring_arr_full[29]]
    shot_arr = ["Shot", shot_arr_full[0], shot_arr_full[1],  shot_arr_full[2], shot_arr_full[4], shot_arr_full[5], shot_arr_full[6], shot_arr_full[9], shot_arr_full[11], shot_arr_full[12], shot_arr_full[13], shot_arr_full[14], shot_arr_full[15], shot_arr_full[16], shot_arr_full[17], shot_arr_full[18], shot_arr_full[19], shot_arr_full[20], shot_arr_full[21], shot_arr_full[22], shot_arr_full[23], shot_arr_full[24], shot_arr_full[25], shot_arr_full[26], shot_arr_full[28], shot_arr_full[29]]
    condom_arr = ["Condom", condom_arr_full[0], condom_arr_full[1],  condom_arr_full[2], condom_arr_full[3], condom_arr_full[6], condom_arr_full[7], condom_arr_full[8], condom_arr_full[9], condom_arr_full[28]]
    internal_condom_arr = ["Internal Condom", internal_condom_arr_full[0], internal_condom_arr_full[1], internal_condom_arr_full[2], internal_condom_arr_full[3], internal_condom_arr_full[6], internal_condom_arr_full[7], internal_condom_arr_full[8], internal_condom_arr_full[9], internal_condom_arr_full[10], internal_condom_arr_full[27], internal_condom_arr_full[28]]
    cervical_cap_arr = ["Cervical Cap", cervical_cap_arr_full[0], cervical_cap_arr_full[1],  cervical_cap_arr_full[2], cervical_cap_arr_full[6], cervical_cap_arr_full[9], cervical_cap_arr_full[10], cervical_cap_arr_full[11], cervical_cap_arr_full[27], cervical_cap_arr_full[28]]
    fam_arr = ["FAM", fam_arr_full[0], fam_arr_full[1],  fam_arr_full[2], fam_arr_full[6], fam_arr_full[7], fam_arr_full[9], fam_arr_full[28]]
    copper_iud_arr = ["Copper IUD", copper_iud_arr_full[0], copper_iud_arr_full[1],  copper_iud_arr_full[3], copper_iud_arr_full[6], copper_iud_arr_full[9], copper_iud_arr_full[10], copper_iud_arr_full[11], copper_iud_arr_full[12], copper_iud_arr_full[26], copper_iud_arr_full[27], copper_iud_arr_full[28]]
    sterilization_arr = ["Sterilization", sterilization_arr_full[0], sterilization_arr_full[1],  sterilization_arr_full[3], sterilization_arr_full[4], sterilization_arr_full[9], sterilization_arr_full[11], sterilization_arr_full[12], sterilization_arr_full[22], sterilization_arr_full[23], sterilization_arr_full[26], sterilization_arr_full[28]]
    gel_arr = ["Spermicide", spermicide_arr_full[0], spermicide_arr_full[1],  spermicide_arr_full[2], spermicide_arr_full[6], spermicide_arr_full[7], spermicide_arr_full[9], spermicide_arr_full[10]]
    withdrawal_arr = ["Withdrawal", withdrawal_arr_full[0], withdrawal_arr_full[1], withdrawal_arr_full[2], withdrawal_arr_full[6], withdrawal_arr_full[7], withdrawal_arr_full[9], withdrawal_arr_full[28]]
    # Calculate scores using the updated weights
    condom_score = change_score_condoms(condom_arr, original_weight_condoms)
    internal_condom_score = change_internal_condoms(internal_condom_arr, original_weight_internal_condoms)
    cervical_cap_score = change_score_cervical_cap(cervical_cap_arr, original_weight_cervical_cap)
    fam_score = change_fam(fam_arr, original_weight_FAM)
    arm_implant_score = change_arm_implant(arm_implant_arr, original_weight_arm_implant)
    copper_iud_score = change_copper_iud(copper_iud_arr, original_weight_copper_IUD)
    hormonal_iud_score = change_score_hormonal_iud(hormonal_iud_arr, original_weight_hormonal_IUD)
    patch_score = change_score_patch(patch_arr, original_weight_patch)
    combo_pill_score = change_score_combo_pill(combo_pill_arr, original_weight_combo_pill)
    mini_pill_score = change_scoring_mini_pill(mini_pill_arr, original_weight_mini_pill)
    ring_score = score_ring(ring_arr, original_weight_ring)
    shot_score = change_score_shot(shot_arr, original_weight_shot)
    sterilization_score = change_score_sterilization(sterilization_arr, original_weight_sterilization)
    gel_score = change_score_gel(gel_arr, original_weight_spermicide)
    withdrawal_score = change_score_withdrawal(withdrawal_arr, original_weight_withdrawl)

    # Create a dictionary of contraceptive methods and their scores
    # 1. Map contraceptive names to their scores
    contraceptive_scores = {
        "Condom": condom_score,
        "Internal Condom": internal_condom_score,
        "Cervical Cap": cervical_cap_score,
        "Fertility Awareness Method (FAM)": fam_score,
        "Arm Implant": arm_implant_score,
        "Copper IUD": copper_iud_score,
        "Hormonal IUD": hormonal_iud_score,
        "The Patch": patch_score,
        "Combination (Combo) Pill": combo_pill_score,
        "Mini Pill": mini_pill_score,
        "The Ring": ring_score,
        "Shot": shot_score,
        "Sterilization": sterilization_score,
        "Spermicide/Vaginal Gel": gel_score,
        "Withdrawal": withdrawal_score
    }
    contraceptive_ids = {
    "Condom": 0,
    "Internal Condom": 1,
    "Cervical Cap": 2,
    "Fertility Awareness Method (FAM)": 3,
    "Arm Implant": 4,
    "Copper IUD": 5,
    "Hormonal IUD": 6,
    "The Patch": 7,
    "Combination (Combo) Pill": 8,
    "Mini Pill": 9,
    "The Ring": 10,
    "Shot": 11,
    "Sterilization": 12,
    "Spermicide/Vaginal Gel": 13,
    "Withdrawal": 14
}

    # 2. Sort by score (descending) and get top 3 names
    sorted_scores = sorted(contraceptive_scores.items(), key=lambda x: x[1], reverse=True)
    top_3_names = [method for method, score in sorted_scores[:3]]
    top_3_ids = [contraceptive_ids[name] for name in top_3_names]
    return top_3_ids



data = {
  'Condom': { '1': 'Positive', '2': 'No' },
  'Cost Effectiveness': {'1': 'Important' },
  'Pregnancy Prevention': { '1': 'Neutral' },
  'Management of Period and Side Effects': { '1': 'Neutral' },
  'Low Chance of Weight Gain/Loss': { '1': 'Neutral' },
  "Partner's Willingness to Participate in Contraception": { '1': 'Neutral/No partner' },
  'STI Prevention': { '1': 'Important' },
  'Willing to Insert Foreign Object Into Vagina': { '1': 'Neutral/No partner' },
  'Willing to Seek Consultation by a Medical Professional': { '1': 'Neutral/No partner' },
  'Willing to Undergo a Medical Procedure': { '1': 'Neutral/No partner' },
  'Acne': { '1': 'Severe' },
  'Migraine with Aura': { '1': 'Mild' }
}
#print(parse_decision_factors(data))
results = parse_decision_factors(data)
print(score_contraceptives(results))
