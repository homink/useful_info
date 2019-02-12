# useful_info
Archive for useful information and commands

## SoX installation for Ubuntu
```
sudo apt-get update && sudo apt-get install sox libsox-fmt-all
```

## NIVIDIA driver installation for Ubuntu
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install nvidia-410
```

## MKL installation for Ubuntu
```
cd /tmp
wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
sudo apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB

sudo sh -c 'echo deb https://apt.repos.intel.com/mkl all main > /etc/apt/sources.list.d/intel-mkl.list'
sudo apt-get update && sudo apt-get install intel-mkl-64bit-2018.2-046
```
Add to end of ~/.bashrc
```
source /opt/intel/bin/compilervars.sh intel64

export CMAKE_INCLUDE_PATH=/opt/intel/compilers_and_libraries_2018.2.199/linux/mkl/include
export MAKE_LIBRARY_PATH=/opt/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64:/opt/intel/compilers_and_libraries_2018.2.199/linux/compiler/lib/intel64
export LD_LIBRARY_PATH=$CMAKE_LIBRARY_PATH:$LD_LIBRARY_PATH
```
Then run:
```
source ~/.bashrc
```
