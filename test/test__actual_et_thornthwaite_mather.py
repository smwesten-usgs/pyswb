import sys
from pathlib import Path
import numpy as np
sys.path.append(str(Path.cwd().parents[0]))

import pyswb.science_functions.actual_et_thornthwaite_mather as aet_tm

def test_soil_moisture_equations():

    results = []

    tol = 0.75

    # from Thornthwaite-Mather table 30: a soil with water holding capacity of 250mm and a APWL of 190 should retain 116mm of water
    sm = aet_tm.thornthwaite_mather_soil_moisture_millimeters(250, 190)
    apwl = aet_tm.thornthwaite_mather_accumulated_potential_water_loss_millimeters(250,sm)
    results.append(np.isclose(sm, 116, atol=tol))

    # from Thornthwaite-Mather table 30: a soil with water holding capacity of 250mm and a APWL of 259 should retain 87mm of water
    sm = aet_tm.thornthwaite_mather_soil_moisture_millimeters(250, 259)
    apwl = aet_tm.thornthwaite_mather_accumulated_potential_water_loss_millimeters(250,sm)
    results.append(np.isclose(sm, 87, atol=tol))

    # from Thornthwaite-Mather table 23: a soil with water holding capacity of 25mm and a APWL of 20 should retain 10mm of water
    sm = aet_tm.thornthwaite_mather_soil_moisture_millimeters(25,20)
    apwl = aet_tm.thornthwaite_mather_accumulated_potential_water_loss_millimeters(25,sm)
    results.append(np.isclose(sm, 10, atol=tol))
    
    # from Thornthwaite-Mather table 27: a soil with water holding capacity of 125mm and a APWL of 100 should retain 55mm of water
    sm = aet_tm.thornthwaite_mather_soil_moisture_millimeters(125,100)
    apwl = aet_tm.thornthwaite_mather_accumulated_potential_water_loss_millimeters(125,sm)
    results.append(np.isclose(sm, 55, atol=tol))
    
    # from Thornthwaite-Mather table 28: a soil with water holding capacity of 150mm and a APWL of 320 should retain 20mm of water
    sm = aet_tm.thornthwaite_mather_soil_moisture_millimeters(150,320)
    apwl = aet_tm.thornthwaite_mather_accumulated_potential_water_loss_millimeters(150,sm)
    results.append(np.isclose(sm, 17, atol=tol))

    assert all(test for test in results)