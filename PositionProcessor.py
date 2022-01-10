import os
import csv
from nmea.NMEAParser import NMEAParser

# Instantiate an object to parse NMEA
myNMEA = NMEAParser()

output_file_name = './processed/summary.csv'
print(f'Saving data as {output_file_name}')
# Now create the CSV file and headers
output_file = open(output_file_name, 'w', newline='')
with output_file:
    file_header = ['Date', 'UTC', 'Longitude', 'Latitude', 'Altitude', 'SOG', 'CMG', 'Sigma Latitude', 'Sigma Longitude', 'Sigma Altitude']
    writer = csv.writer(output_file)
    writer.writerow(file_header)

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
            output_file = open(output_file_name, 'a', newline='')
            with output_file:
                line_data = [myNMEA.date_of_fix, myNMEA.gps_time, myNMEA.dd_longitude_degrees,
                             myNMEA.dd_latitude_degrees, myNMEA.altitude, myNMEA.sog, myNMEA.cmg,
                             myNMEA.sigma_latitude, myNMEA.sigma_longitude, myNMEA.sigma_altitude]
                writer = csv.writer(output_file)
                writer.writerow(line_data)