
def gst(sentence):
    # GNSS pseudorange error statistics
    # GNGST, 120112.00, 34, 0.011, 0.0065, 38, 0.010, 0.010, 0.010 * 76
    # 1 - Fix taken at in UTC as hhmmss.ss
    # 2 - RMS value of the standard deviation of the ranges
    # 3 - Standard deviation of semi-major axis
    # 4 - Standard deviation of semi-minor axis
    # 5 - Orientation of semi-major axis
    # 6 - Standard deviation of latitude error
    # 7 - Standard deviation of longitude error
    # 8 - Standard deviation of altitude error

    # Return values
    sigma_latitude = '0'
    sigma_longitude = '0'
    sigma_altitude = '0'

    try:
        list_of_values = sentence.split(',')
        sigma_latitude = list_of_values[6]
        sigma_longitude = list_of_values[7]
        sigma_altitude_and_crc = list_of_values[8].split('*')
        sigma_altitude = sigma_altitude_and_crc[0]
    except ValueError:
        print(f'[GST] Error parsing {sentence}')

    return sigma_latitude, sigma_longitude, sigma_altitude