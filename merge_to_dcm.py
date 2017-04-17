import csv
import dicom
import os

# flif to pnm
flif_dir = os.listdir("flif/")
print flif_dir

for flif_file in flif_dir:
    # print "flif flif/%s extracted_pnm/%spnm -V" % (flif_file, flif_file[:-4])
    os.system("flif flif/%s extracted_pnm/%spnm -V" % (flif_file, flif_file[:-4]))

# pnm to dcm
img_dir = os.listdir("extracted_pnm/")
print img_dir

for img in img_dir:
    os.system("gdcmimg extracted_pnm/%s merged_dicom/%s.dcm" % (img, img[:-4]))

# csv to dcm
csv_dir = os.listdir("data/")
print csv_dir

dicom_dir = os.listdir("merged_dicom/")
print dicom_dir

dicom_file = []

for dicoms in dicom_dir:
    if str(dicoms).endswith(".dcm"):
        dicom_file.append(dicoms[:-4])
print dicom_file

for csvfile in csv_dir:
    if csvfile[:-4] in dicom_file:
        dcm_file_path = "merged_dicom/" + str(csvfile[:-4]) + ".dcm"
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
