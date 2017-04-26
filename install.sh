# create required directories
echo "creating directories"
mkdir -p data dicom extracted_pnm flif image merged_dicom

echo "installing dcmtk"
sudo apt-get install dcmtk

echo "installing libgdcm-tools"
sudo apt install libgdcm-tools

echo "installing flif dependencies"
sudo apt-get install libpng-dev

echo "cloning FLIF"
git clone https://github.com/FLIF-hub/FLIF.git

echo "installing FLIF"
cd FLIF/src && make
sudo make install

echo "install complete"
