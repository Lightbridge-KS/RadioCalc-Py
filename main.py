import radcalc.BSA as BSA
import radcalc.vol as vol

# BSA for Age > 17 year
print("# BSA")
BSA.print_BSA_gt17(W_kg = 10, H_cm = 120)
print("")

# Ellipsoid Volume
print("# Volume")
vol.print_vol_ellipsoid(10, 20, 30)