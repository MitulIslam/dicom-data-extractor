import dicom
import os
import csv

directory_data = os.listdir("data/")
dicom_dir = os.listdir("image/")
print dicom_dir
print directory_data
dicom_file = []

# f = open('attendees1.csv')
# csv_f = csv.reader(f)

# f = open("CR.1.3.51.0.7.1662753766.59086.8771.36000.27815.52340.23289.csv", "rb")
# csv_f = csv.reader(f)
#
# for row in csv_f:
#     print row
for dicoms in dicom_dir:
    if str(dicoms).endswith(".dcm"):
        dicom_file.append(dicoms[:-4])
print dicom_file

for csvfile in directory_data:
    # f = open("data/" + str(csvfile), "rb")
    # csv_f = csv.reader(f)
    #
    # print "--------------------------------csv data--------------------------------"
    # for row in csv_f:
    #     print row[0]
    #
    # f.close()
    if csvfile[:-4] in dicom_file:
        dcm_file_path = "image/" + str(csvfile[:-4]) + ".dcm"
        read_dicom_file = dicom.read_file(dcm_file_path)
        all_tags = read_dicom_file.dir()
        print str(read_dicom_file.dir())
        with open("data/" + str(csvfile), "rb") as datafile:
            data_reader = csv.reader(datafile, delimiter='|', quotechar=' ')
            # print data_reader
            print "--------------------------------csv data--------------------------------"
            for row in data_reader:
                if(row[0] in all_tags):
                    print 'dcmodify -m "%s=%s" %s' % (str(row[0]), str(row[1]), dcm_file_path)
                    try:
                        dcmmod = os.system('dcmodify -m "%s=%s" %s -v' % (str(row[0]), str(row[1]), dcm_file_path))
                        print "Dicom modiy code: " + str(dcmmod)
                        print "Existing tags " + str(row[0]) + " , " + str(row[1])
                    except Exception as e:
                        print "Cannot modify dicom. Reason: " + str(e)
                else:
                    print 'dcmodify -i "%s=%s" %s' % (str(row[0]), str(row[1]), dcm_file_path)
                    try:
                        dcmmod = os.system('dcmodify -i "%s=%s" %s -v' % (str(row[0]), str(row[1]), dcm_file_path))
                        print "Dicom insert code: " + str(dcmmod)
                        print "New Tags " + str(row[0]) + " , " + str(row[1])
                    except Exception as e:
                        print "Cannot insert new tag to dicom. Reason: " + str(e)


# for data in directory_data:
#     with open("data/" + str(data[:-4]) + ".csv", "r") as data_file:
#         print "----------------------- dicom data -----------------------"
#         print data_file
#         for data in data_file:
#             print data
