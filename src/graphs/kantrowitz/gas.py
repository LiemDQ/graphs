
from math import sqrt
from scipy.optimize import brentq
from CoolProp import CoolProp as cp

def get_gamma(name):
    temperature = 293 #room temperature
    pressure = 101325 #atmospheric pressure
    CP = cp.PropsSI("CPMASS", 'T', temperature, 'P', pressure, name)
    CV = cp.PropsSI("CVMASS", 'T', temperature, 'P', pressure, name)
    return CP/CV

def mach_to_area_throat_ratio(m, gamma):
    """
    Area ratio (w.r.t to throat) for a given mach number and isentropic expansion factor.
    """
    return 1/m * ((1+ (gamma-1)/2*m**2) /((gamma+1)/2))**((gamma+1)/(2*(gamma-1)))

def mass_flow_rate_through_nozzle(p0, t0, gamma, R, A_throat):
    """
    Calculate mass flow rate through a choked nozzle given stagnation pressure, stagnation temperature, 
    isentropic expansion factor, gas constant and throat area.
    """
    return p0*A_throat/sqrt(t0)*sqrt(gamma/R*(2/(gamma+1))**((gamma+1)/(gamma-1)))

def area_ratio_to_accelerated_mach_subsonic(m, gamma, ratio):
    """
    For a given area ratio, calculate the mach in the smaller area given the mach number in the larger area.
    There are two possible solutions for a given ratio (one subsonic, one supersonic).
    This always returns the subsonic solution.
    """
    ratio1 = mach_to_area_throat_ratio(m, gamma)
    target_ratio = ratio/ratio1
    return brentq(lambda mach: mach_to_area_throat_ratio(mach, gamma), 0, 1.0)

def mach_to_area_ratio(m1, m2, gamma):
    """
    Get the constriction-to-inlet area ratio for two arbitrary subsonic mach numbers. 
    m2 should be the higher mach number.
    """
    return mach_to_area_throat_ratio(m2, gamma)/mach_to_area_throat_ratio(m1, gamma)

def normal_shock_stagnation_pressure_ratio(m, gamma):
    """
    For a given Mach number and isentropic expansion factor, calculates
    the total pressure drop across the shock. Note that this only results in physically 
    meaning full numbers for M > 1.0!
    """
    term1 = (2*gamma/(gamma+1)*m**2 - (gamma-1)/(gamma+1))**(-1/(gamma-1)) 
    term2 = (((gamma+1)/2*m**2)/(1+(gamma-1)/2*m**2))**(gamma/(gamma-1))
    return term1*term2

def normal_shock_post_mach(m, gamma):
    """
    Determine the Mach number after a normal shock for a given mach number. 
    """
    return sqrt((m**2*(gamma-1)+2)/(2*gamma*m**2 - (gamma - 1)))

def wikipedia_bypass_ratio(m, gamma):
    """
    This equation was found in the Wikipedia article on the Kantrowitz limit.
    I am frankly not sure where it comes from or what it means.
    """
    term1 = (gamma-1)/(gamma+1)**(0.5) * (2*gamma/(gamma+1))**(1/(gamma-1))
    term2 = (1 + 2/(gamma-1)/m**2)**(0.5) * (1 - (gamma-1)/(2*gamma)/m**2)**(1/(gamma-1))
    return  term1*term2

def kantrowitz_area_ratio(m, gamma):
    """
    Calculate the throat area ratio for a given mach number under the classical Kantrowitz limit.
    Note that only supersonic Mach numbers (M> 1.0) result in physically meaningful results!
    """
    return normal_shock_stagnation_pressure_ratio(m, gamma)*mach_to_area_throat_ratio(m, gamma)

def kantrowitz_overspeed(m, gamma):
    """
    Calculate the overspeed mach number required to start an inlet
    with a design mach number of m.
    """
    cr = mach_to_area_throat_ratio(m, gamma)
    subsonic_mach = brentq(lambda mach: mach_to_area_throat_ratio(mach, gamma) - cr, 0.01, 1.0)
    return brentq(lambda mach: normal_shock_post_mach(mach, gamma) - subsonic_mach, 1.0, 10.0)