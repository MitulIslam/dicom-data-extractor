import dicom
import os
import csv

directory_data = os.listdir("data/")
# print type(directory_data)
print directory_data

# f = open('attendees1.csv')
# csv_f = csv.reader(f)

# f = open("CR.1.3.51.0.7.1662753766.59086.8771.36000.27815.52340.23289.csv", "rb")
# csv_f = csv.reader(f)
#
# for row in csv_f:
#     print row

for csvfile in directory_data:
    f = open("data/" + str(csvfile), "rb")
    csv_f = csv.reader(f)

    print "--------------------------------csv data--------------------------------"
    for row in csv_f:
        print row[0]

    f.close()
    # with open("data/" + str(csvfile), "rb") as datafile:
    #     data_reader = csv.reader(datafile, delimiter='|', quotechar=' ')
    #     print data_reader
    #     for row in data_reader:
    #         print row

# for data in directory_data:
#     with open("data/" + str(data[:-4]) + ".csv", "r") as data_file:
#         print "----------------------- dicom data -----------------------"
#         print data_file
#         for data in data_file:
#             print data
