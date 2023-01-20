
def calculate_cn_S_inches(curve_number):
    """
    Return the curve number storage (S) term, in inches. Equation 2-4, Cronshey and others (1986).
    
    """

    S_inches = ( 1000.0 / curve_number ) - 10.0
    return S_inches


def calculate_cn_S_millimeters(curve_number):
    """
    Return the curve number storage (S) term, in millimeters. Equation 2-4, Cronshey and others (1986),
    with constants multiplied by 25.4 (mm to inches).
    
    """

    S_mm = ( 25400.0 / curve_number ) - 254.0
    return S_mm


def calculate_cn_runoff(inflow, storage_S, initial_abstraction_Ia = 0.05):
    """
    Return the runoff value given the inflow (precip), storage, and initial abstraction. 
    Equation 2-3, Cronshey and others (1986).
    """
 
    import numpy as np

    Ia = initial_abstraction_Ia
    runoff = np.where(inflow > Ia,
                            (inflow - Ia * storage_S)^2 / (inflow + (1.0 - Ia) * storage_S),
                            0.0
                     )

    return runoff


def calculate_cn_alternative_S_0_05(storage_S):
    """
    Return the curve number storage term, assuming that the initial abstraction is 0.05, rather than 0.2.
    Equation 8, Woodward and others, 2003.
    """
    return 1.33 * (storage_S^1.15)


def cn_references():
    """
    Cronshey, R., McCuen, R., Miller, N., Rawls, W., Robbins, S., and Woodward, D., 1986, Urban Hydrology
        for Small Watersheds - Technical release 55: US Dept. of Agriculture, Soil Conservation Service, 
        Engineering Division, accessed at http://www.nrcs.usda.gov/Internet/FSE_DOCUMENTS/16/stelprdb1044171.pdf.

    Woodward, D.E., Hawkins, R.H., Jiang, R., Hjelmfelt, J., Van Mullem, J.A., and Quan, Q.D., 2003, 
        Runoff Curve Number Method: Examination of the Initial Abstraction Ratio, 
        in World Water and Environmental Resources Congress 2003,
        American Society of Civil Engineers, Philadelphia, Pennsylvania, p. 1-10.

    """
    pass

# 