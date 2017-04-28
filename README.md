# Dicom Data Extractor

Simple python script to extract data ,put them in .csv file and .pnm image. Also merge data and image back to dicom file.
Used flif for intermidiate image compression.
  
# Dependencies
  `git` 
  `make`
  `python2`
  `virtual-env`
  
# Installation
  for ubuntu run install.sh file, needs permission to globally install packages
  
  `chmod 777 install.sh`
  
  `./install.sh`
  
  or 
  
  create this diroctories in project root
  `data` `dicom` `extracted_pnm` `flif` `image` `merged_dicom`
  
  install [dcmtk](http://support.dcmtk.org/docs/file_install.html)
  
  install [gdcm tools](http://gdcm.sourceforge.net/wiki/index.php/Main_Page)
  
  install [FLIF](https://github.com/FLIF-hub/FLIF)
  
# Usage
  make a virtualenv `virtualenv env`
  activate `source env/bin/activate`
  install python dependencies `pip install -r requirements.txt`
  just run extract_from_dcm.py or merge_to_dcm.py
