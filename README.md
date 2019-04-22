# Useful_info
Archive for useful information and commands

## Coding

### [Bits peration](https://github.com/homink/useful_info/blob/master/BitsOperation.py)
### [Tree traversal](https://github.com/homink/useful_info/blob/master/TreeTraversal.py)
### [Word Search](https://github.com/homink/useful_info/blob/master/WordSearch.py)

## SoX installation for Ubuntu
```
sudo apt-get update && sudo apt-get install sox libsox-dev libsox-fmt-all
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

## CUDA installation with deb(network) for Ubuntu 16.04 [(link)](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=debnetwork)
```
sudo dpkg -i cuda-repo-ubuntu1604_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```
## CUDNN installation with deb(network) for Ubuntu 16.04 [(link)](https://developer.nvidia.com/rdp/cudnn-download)
```
sudo dpkg -i libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.4.2.24-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-doc_7.4.2.24-1+cuda10.0_amd64.deb
```

## NCCL installation with deb(network) for Ubuntu 16.04 [(link)](https://developer.nvidia.com/nccl/nccl-download)
```
sudo dpkg -i nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb
sudo apt update
sudo apt install libnccl2
```
