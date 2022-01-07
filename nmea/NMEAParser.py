
from nmea.nmea_data import TALKER_ID, SENTENCE_ID
from nmea.gga import gga
from nmea.rmc import rmc
from nmea.gst import gst

myGGA = gga()
myRMC = rmc()
myGST = gst()


class NMEAParser():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1

        # Timers for each sentence, check to see if data stale when calling this class
        self.posllh_TOW = ''
        self.relposned_TOW = ''

        # Properties
        self.gps_time = ''
        self.dd_longitude_degrees = 0
        self.dd_latitude_degrees = 0
        self.altitude = 0
        self.sog = 0
        self.cmg = 0
        self.date_of_fix = 0
        self.data_validity = 0
        self.pos_mode_indicator = 0

        self.sigma_latitude = 0
        self.sigma_longitude = 0
        self.sigma_altitude = 0

        # Status values, set when updated, reset from the calling program
        self.new_position = 0
        self.new_heading = 0

        # Set the flags for local use
        self.gga_valid = False
        self.rmc_valid = False
        self.gst_valid = False

    def parser(self, CurrentNMEAString):
        # Its a comma delimited file, split values into a list
        list_of_values = CurrentNMEAString.split(',')
        try:
            # Get the talker ID
            talker_id = list_of_values[0][0:-3]
            # Check to see if its in the list of valid talker IDs
            if talker_id in TALKER_ID:
                sentence_id = list_of_values[0][2:]
                if sentence_id in SENTENCE_ID:
                    if sentence_id == 'GGA':
                        # Call a parsing function to get the required values
                        self.gps_time, self.dd_longitude_degrees, self.dd_latitude_degrees, self.altitude, self.fix_quality = myGGA.parse(CurrentNMEAString)
                        self.gga_valid = True
                    if sentence_id == 'RMC':
                        # Call a parsing function to get the required values
                        self.sog, self.cmg, self.date_of_fix, self.data_validity, self.pos_mode_indicator = myRMC.parse(CurrentNMEAString)
                        self.rmc_valid = True
                    if sentence_id == 'GST':
                        # Call a parsing function to get the required values
                        self.sigma_latitude, sigma_longitude, sigma_altitude = myGST.parse(CurrentNMEAString)
                        self.gst_valid = True
                else:
                    print(f'Bad sentence ID {sentence_id} in {CurrentNMEAString}')
            else:
                print(f'Bad talker ID {talker_id} in {CurrentNMEAString}')
        except ValueError as err:
            print(f'Error processing {CurrentNMEAString}')
        finally:
            if self.gga_valid and self.rmc_valid and self.gst_valid:
                print(self.date_of_fix, self.gps_time, self.dd_longitude_degrees, self.dd_latitude_degrees,
                      self.altitude, self.sog, self.cmg, self.sigma_latitude, self.sigma_longitude,
                      self.sigma_altitude)