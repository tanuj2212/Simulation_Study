from functions_simulation_diff_weight import *


a_values = {
    "condoms": None,
    "internal condoms": None,
    "cervical cap": None,
    "FAM": None,
    "arm implant": None,
    "copper IUD": None,
    "hormonal IUD": None,
    "patch": None,
    "combo pill": None,
    "mini pill": None,
    "ring": None,
    "shot": None,
    "sterilization": None,
    "spermicide/vaginal gel": None,
    "withdrawal": None,
}

s_values = {
   "condoms": None,
    "internal condoms": None,
    "cervical cap": None,
    "FAM": None,
    "arm implant": None,
    "copper IUD": None,
    "hormonal IUD": None,
    "patch": None,
    "combo pill": None,
    "mini pill": None,
    "ring": None,
    "shot": None,
    "sterilization": None,
    "spermicide/vaginal gel": None,
    "withdrawal": None,
} 

x_cost_effectiveness = [-60, -40, -20, 0, 20, 40, 60]
y_acne = [3, -15, -25, -50]

for x in x_cost_effectiveness:
    condom_score = change_score_condoms()