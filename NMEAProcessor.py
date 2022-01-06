import os
import csv
from nmea.NMEAParser import NMEAParser
from nmea.nmea_data import TALKER_ID, SENTENCE_ID

# Instantiate an object to parse NMEA
myNMEA = NMEAParser()

# Raw data files
directory = './logfiles'
# Open every file in sequence
for file in os.listdir(directory):
    input_filename = directory + '/' + file
    print("Found" + input_filename)
    # Process each file individually
    with open(input_filename) as nmea_file:
        # one line at a time, parse
        for CurrentNMEAString in nmea_file:
            myNMEA.parser(CurrentNMEAString)