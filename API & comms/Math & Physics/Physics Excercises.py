'''
Coulomb force
'''
import math

def calculate_coulomb_force(q1, q2, r):

    # Электрическая постоянная
    k = 8.85418782e-12

    # Calculate force using Coulomb's Law
    force = (q1 * q2) / (4*math.pi * k * r**2)

    # Output the result with three decimal places
    print(f"Coulomb Force: {force:.3f} Newtons")

calculate_coulomb_force(1, 1, 1000)
calculate_coulomb_force(1e-4, 1e-4, 1) # 1e-4 = 1*10**-4
calculate_coulomb_force(2.3e-6, 3.5e-5, 0.017)

single_charge = -1.6021892e-19
print(8.0e-20/single_charge)
print(2.4e-19/single_charge)
print(2.4e-18/single_charge)
print(4.8e-19/single_charge)
print(1/single_charge)