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

class gst():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1

    def parse(self, sentence):
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

    def create(self, sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0