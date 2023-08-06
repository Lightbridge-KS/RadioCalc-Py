# Body Surface Area (CVS Rotation)
# Source: https://www.calculator.net/body-surface-area-calculator.html

def print_BSA_gt17(W_kg, H_cm):
    """Body Surface Area for Age > 17 yr"""
    bsa_Haycock = round(calc_Haycock(W_kg, H_cm), 3)
    bsa_Mosteller = round(calc_Mosteller(W_kg, H_cm), 3)
    print(f"BSA (Haycock): {bsa_Haycock} m2")
    print(f"BSA (Mosteller): {bsa_Mosteller} m2")
    return({"Haycock": bsa_Haycock, "Mosteller": bsa_Mosteller})


def calc_Haycock(W_kg, H_cm):
    """Body Surface Area by Haycock (Age > 17 yr)"""
    BSA = 0.024265 * (W_kg**0.5378) * (H_cm**0.3964)
    return(BSA)


def calc_Mosteller(W_kg, H_cm):
    """Body Surface Area by Mosteller (Age > 17 yr)"""
    import math
    BSA = math.sqrt(W_kg * H_cm/3600)
    return(BSA)

