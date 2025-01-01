import math

seawater_concentration = 35.0 #kg/m3 or g/L
seawater_temp = 293.15 #K
salt_molecular_mass = 58.44 # g/mol
R = 8.314463 # m3*Pa/(K*mol)
def vant_hoff_osmotic_pressure(concentration, T):
    return 2*concentration*R*T

def specific_energy_consumption(osmotic_pressure, recovery):
    return -osmotic_pressure/recovery * math.log(1- recovery)

def equilibrium_pressure_ratio(recovery):
    return 1.0/(1.0-recovery)
    