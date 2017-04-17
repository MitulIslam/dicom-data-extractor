import csv
import dicom
import os

dicom_dir_name = os.listdir("dicom")
print type(dicom_dir_name)
print dicom_dir_name

for dicom_file_name in dicom_dir_name:
    dicom_data = dicom.read_file("dicom/" + dicom_file_name, force=True)
    print "----------------------- dicom data -----------------------"
    # print dicom_data.dir()
    dicom_tags = dicom_data.dir()
    os.system("cd dicom && time dcm2pnm "  + dicom_file_name + " ../image/" + dicom_file_name[:-4]+".pnm")
    os.system("identify image/" + dicom_file_name[:-4]+".pnm -verbose")
    os.system("cd image && time flif " + dicom_file_name[:-4] + ".pnm ../flif/" + dicom_file_name[:-4]+".flif -V")
    with open("data/"+str(dicom_file_name[:-4]) + ".csv", "wb") as data_file:
        for dicom_tag in dicom_tags:
            # this if statement below skips PixelData and SourceImageSequence tag from adding to .csv
            # add additional skips here
            data_elem = dicom_data.data_element(dicom_tag)
            # print dicom_tag
            # print str(data_elem)
            if data_elem != None and data_elem.VM <= 1 and dicom_tag != "SourceImageSequence":
                # print data_elem
                # print str(dicom_data.ImageType).replace(",", "/")
                refined_data = str(getattr(dicom_data, str(dicom_tag))).replace(",", "/")
                writer = csv.writer(data_file, delimiter='|', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([dicom_tag, str(refined_data) if refined_data else None])
