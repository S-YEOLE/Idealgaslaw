# Define constants
R = 0.08206  # L*atm/mol*K
# R = 8.314  # J/mol*K (if using SI units)

# Define variables
P = float(input("Enter pressure in atm: "))
V = float(input("Enter volume in liters: "))
n = float(input("Enter amount of substance in moles: "))
T = float(input("Enter temperature in Kelvin: "))

# Calculate missing variable
if not P:
    P = n*R*T/V
    print(f"Pressure is {P:.2f} atm")
elif not V:
    V = n*R*T/P
    print(f"Volume is {V:.2f} L")
elif not n:
    n = P*V/(R*T)
    print(f"Amount of substance is {n:.2f} moles")
elif not T:
    T = P*V/(n*R)
    print(f"Temperature is {T:.2f} K")
else:
    print("Not enough information given to solve for a variable.")


