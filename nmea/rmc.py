def rmc(sentence):
    # RMC - Recommended minimum specific GPS/Transit data
    # GNRMC,120112.00,A,5510.0019172,N,00726.0946444,W,0.017,,070921,,,R,V*1E
    # 1 - Fix taken at in UTC as hhmmss.ss
    # 2 - Data validity, A=Valid, V=Invalid
    # 2 - Latitude (Northing) in DM
    # 3 - NS Hemisphere
    # 4 - Longitude (Easting) in DM
    # 5 - EW Hemisphere
    # 7 - Speed over ground in Knots
    # 8 - Course Made Good in Degrees, True
    # 9 - Date of fix DDMMYY
    # 10 - Magnetic variation
    # 11 - Magnetic variation hemisphere
    # 12 - posMode indicator (from NMEA 2.3 onwards)
    # 13 - navStatus, fixed field (from NMEA 4.1 onwards), always V

    # Default, invalid fix
    data_validity = 'V'

    # Return values
    pos_mode_indicator = 'N'
    sog = '0'
    cmg = '0'
    date_of_fix = ''

    try:
        list_of_values = sentence.split(',')
        data_validity = list_of_values[2]
        sog = (list_of_values[7])
        cmg = (list_of_values[8])
        date_of_fix = (list_of_values[9])
        pos_mode_indicator = (list_of_values[12])
    except ValueError:
        print(f'[RMC] Error parsing {sentence}')

    return sog, cmg, date_of_fix, data_validity, pos_mode_indicator
