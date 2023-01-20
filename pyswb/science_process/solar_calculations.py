def daylight_hours( omega_s ):
    """
    Calculate the number of daylight hours at a location.

    omega_s   Sunset hour angle in Radians.

    Implementation follows equation 34, Allen and others (1998).
    """
    from math import pi
    return 24.0 / pi * omega_s


def day_angle__Gamma(day_of_year, number_of_days_in_year):
    """
    Return the day angle in Radians.  

    day _of_year             Integer day of the year (January 1 = 1)
    number_of_days_in_year   Number of days in the current year

    Implementation follows equation 1.2.2 in Iqbal (1983)
    """

    from math import pi

    return 2.0 * pi * ( day_of_year - 1.0 ) / number_of_days_in_year



def solar_declination__delta(day_of_year, number_of_days_in_year):
    """
    Return the solar declination for a given day of the year in Radians.

    day _of_year             Integer day of the year (January 1 = 1)
    number_of_days_in_year   Number of days in the current year

    Implementation follows equation 1.3.1 in Iqbal (1983).
    Iqbal (1983) reports maximum error of 0.0006 radians; if the last two terms are omitted,
      the reported accuracy drops to 0.0035 radians.
    """
    
    from math import sin, cos

    Gamma = day_angle__Gamma( day_of_year, number_of_days_in_year )

    delta =   0.006918                                        \
             - 0.399912 * cos( Gamma )                        \
             + 0.070257 * sin( Gamma )                        \
             - 0.006758 * cos( 2.0 * Gamma )                  \
             + 0.000907 * sin( 2.0 * Gamma )                  \
             - 0.002697 * cos( 3.0 * Gamma )                  \
             + 0.00148  * sin( 3.0 * Gamma )

    return delta


def relative_earth_sun_distance__D_r(day_of_year, number_of_days_in_year):
    """
    Return the inverse relative Earth-Sun distance (unitless) for a given day of the year.

    day_of_year              Integer day of the year (January 1 = 1)
    number_of_days_in_year   Number of days in the current year

    Implementation follows equation 23, Allen and others (1998). 
    See also Equation 1.2.3 in Iqbal, Muhammad (1983-09-28).
    """
    from math import cos, pi

    D_R = 1.0 + 0.033                                   \
            * cos( 2.0 * pi * day_of_year )                \
            / number_of_days_in_year      

    return D_R


def references():
    """    
    Allen, R.G., Pereira, L.S., Raes, D., and Smith, M., 1998, Crop evapotranspiration-Guidelines for 
        computing crop water requirements-FAO Irrigation and drainage paper 56: Food and Agriculture Organization
        of the United Nations, Rome, 333 p.

    Iqbal, M., 1983, An Introduction To Solar Radiation: Academic Press Canada, Ontario, Canada, 617 p.

    """
    pass