import dicom
import os
import csv

dicom_dir_name = os.listdir("dicom")
print type(dicom_dir_name)
print dicom_dir_name

for dicom_file_name in dicom_dir_name:
    dicom_data = dicom.read_file("dicom/" + dicom_file_name)
    print "----------------------- dicom data -----------------------"
    # print dicom_data.dir()
    dicom_tags = dicom_data.dir()
    os.system("cd dicom && time dcm2pnm "  + dicom_file_name + " ../image/" + dicom_file_name[:-4]+".pnm -v")
    os.system("cd image && time flif " + dicom_file_name[:-4] + ".pnm ../flif/" + dicom_file_name[:-4]+".flif -V")

    with open("data/"+str(dicom_file_name[:-4]) + ".csv", "wb") as data_file:
        for dicom_tag in dicom_tags:
            if dicom_tag != "PixelData" and dicom_tag != "SourceImageSequence":
                # print str(dicom_data.ImageType).replace(",", "/")
                refined_data = str(getattr(dicom_data, str(dicom_tag))).replace(",", "/")
                writer = csv.writer(data_file, delimiter='|', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([dicom_tag, str(refined_data) if refined_data else None])
