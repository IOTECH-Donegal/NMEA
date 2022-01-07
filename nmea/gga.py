'''
GNGGA,120113.00,5510.0019168,N,00726.0946454,W,4,12,0.60,109.635,M,53.911,M,1.0,0000*73
1 - Fix taken at in UTC as hhmmss.ss
2 - Latitude (Northing) in DM
3 - NS Hemisphere
4 - Longitude (Easting) in DM
5 - EW Hemisphere
6 - Fix quality, see GGA_Quality
7 - Number of satellites being tracked
8 - Horizontal dilution of position (HDOP)
9 - Altitude, Metres, above mean sea level
10 - Altitude Unit
11 - Separation of geoid between mean sea level and WGS84 ellipsoid()
12 - Separation Unit
13 - Time in seconds since last DGPS update, SC104
14 - DGPS station ID number
'''


class gga():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1

    @staticmethod
    def parse(self, sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0

        try:
            list_of_values = sentence.split(',')
            gps_time = list_of_values[1]

            # Get the decimal degree values of position
            latitude_dm = (list_of_values[2])
            dm_latitude_degrees = int(latitude_dm[0:2])
            dm_latitude_minutes = float(latitude_dm[2:])
            dm_latitude_minutes_fraction = float(dm_latitude_minutes / 60)
            dd_latitude_degrees = round(dm_latitude_degrees + dm_latitude_minutes_fraction, 8)

            # Longitude converts to negative, edit this if working east of Greenwich
            longitude_dm = (list_of_values[4])
            dm_longitude_degrees = int(longitude_dm[0:3])
            dm_longitude_minutes = float(longitude_dm[3:])
            dm_longitude_minutes_fraction = float(dm_longitude_minutes / 60)
            dd_longitude_degrees = round(-dm_longitude_degrees - dm_longitude_minutes_fraction, 8)

            # To get the true altitude, add height above MSL to HoG and then convert to OSGM15 externally.
            msl = list_of_values[9]
            hog = list_of_values[11]
            altitude = float(msl) + float(hog)
            # Limit to 3 decimal places (mm)
            altitude3 = round(altitude, 3)

            # Verify the quality of the solution
            number_satellites_tracked = list_of_values[7]
            fix_quality = list_of_values[6]

        except ValueError:
            print(f'[GGA] Error parsing {sentence}')

        return gps_time, dd_longitude_degrees, dd_latitude_degrees, altitude3, fix_quality

    @staticmethod
    def create(self, sentence):
        # Default, invalid fix
        fix_quality = '0'
        gps_time = ''
        dd_longitude_degrees = 0
        dd_latitude_degrees = 0
        altitude3 = 0