# Dicom Data Extractor

Simple python script to extract data and image from dicom and merge data and image back to dicom.
Used flif for intermidiate image compression.

# Dependencies
  `git` 
  `make`
  `python2`
  `virtual-env`
  
# Installation
  for ubuntu run install.sh file
  
  `chmod 777 install.sh`
  
  `./install.sh`
  
  or 
  
  create this diroctories in project root
  `data` `dicom` `extracted_pnm` `flif` `image` `merged_dicom`
  
  install [dcmtk](http://support.dcmtk.org/docs/file_install.html)
  
  install [gdcm tools](http://gdcm.sourceforge.net/wiki/index.php/Main_Page)
  
  install [FLIF](https://github.com/FLIF-hub/FLIF)
  
# Usage
  just run extract_from_dcm.py or merge_to_dcm.py
