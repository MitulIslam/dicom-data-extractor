import dicom
import os
import csv

directory_data = os.listdir("dicom")
print type(directory_data)
print directory_data

for data in directory_data:
    dicom_data = dicom.read_file("dicom/" + data)
    # print "----------------------- dicom data -----------------------"
    print dicom_data.dir()
    dicom_tags = dicom_data.dir()

    # file= open("data/"+data[:-4] + ".csv","wb")
    # writer = csv.writer(file, dialect='excel')
    # for row in dicom_data:
    #     with file
        # writer.writerow(row)
    with open("data/"+str(data[:-4]) + ".csv", "wb") as data_file:
        for dicom_tag in dicom_tags:
            if dicom_tag != "PixelData" and dicom_tag != "SourceImageSequence":
                print str(dicom_data.ImageType).replace(",", "/")
                refined_data = str(getattr(dicom_data, str(dicom_tag))).replace(",", "/")
                writer = csv.writer(data_file, delimiter='|', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([dicom_tag, str(refined_data) if refined_data else None])

        # file.close()
    # with open("data/"+data[:-4] + '.csv', 'wb') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    #     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
