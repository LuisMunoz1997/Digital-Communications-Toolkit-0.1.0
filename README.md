# DIGITAL TELECOMUNICATIONS TOOLKIT

Luis Muñoz & Jesús Del Mar's Final Degree Project: Design of a Digital Communication Toolkit over Software Defined Radio for Telecommunications Laboratories.

Version 0.1.0 - Currently in Development.

## Overview

## Getting Started
### Prerequisites

1) A computer with at least 8 GB of RAM and a Intel(R) Core(TM) i5-10510U CPU @ 1.80GHz 2.30 GHz procesor.
2) A unit of the ADALM - PLUTO module (By Analog Devices).
3) Python installed*.
4) The following libraries*:
   - PySide 2
   - pyqtgraph
   - Spicy
   - Os
   - Numpy
   - Matplotlib
   - Commpy.filters
   - matplotlib.backends.backend_qt5agg
   - PIL
   - gc
   - Random
   - Threading
   - Time
   - Zipfile

*Just when working directly with Python's scripts (Option 2 and 3).

### Installing
#### Option 1) Download .exe for Windows.

 - [Download] .exe of the program.

 - Install [PlutoSDR driver](https://github.com/analogdevicesinc/plutosdr-m2k-drivers-win/releases/download/v0.7/PlutoSDR-M2k-USB-Drivers.exe) for Windows.

 - Also, it's necesary the following libraries:

[libiio](https://github.com/analogdevicesinc/libiio?tab=readme-ov-file): Analog Device’s “cross-platform” library for interfacing hardware.

[libad9361-iio](https://github.com/analogdevicesinc/libad9361-iio?tab=readme-ov-file): AD9361 is the specific RF chip inside the PlutoSDR.

#### Option 2) Work directly with the Python's script on Windows (RECOMMENDED).

  - It's necessary to install all the libraries mentioned at Prerequisites and Python.
  - Install [PlutoSDR driver](https://github.com/analogdevicesinc/plutosdr-m2k-drivers-win/releases/download/v0.7/PlutoSDR-M2k-USB-Drivers.exe) for Windows.
  - Also, it's necesary the following libraries:

[libiio](https://github.com/analogdevicesinc/libiio?tab=readme-ov-file): Analog Device’s “cross-platform” library for interfacing hardware.

[libad9361-iio](https://github.com/analogdevicesinc/libad9361-iio?tab=readme-ov-file): AD9361 is the specific RF chip inside the PlutoSDR.

pyadi-iio: Main library that allows users manage ADALM-PLUTO throught Python.
```
git clone https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
pip install .
```

#### Option 3) Work directly with the Python's script on Linux (Any Distribution) (RECOMMENDED).

  - It's necessary to install all the libraries mentioned at Prerequisites and Python.
  - As previously, it's necesary to download: libiio, libad9361-iio and pyadi-iio. Which you do, as follows:

```
sudo apt-get install build-essential git libxml2-dev bison flex libcdk5-dev cmake python3-pip libusb-1.0-0-dev libavahi-client-dev libavahi-common-dev libaio-dev
cd ~
git clone --branch v0.23 https://github.com/analogdevicesinc/libiio.git
cd libiio
mkdir build
cd build
cmake -DPYTHON_BINDINGS=ON ..
make -j$(nproc)
sudo make install
sudo ldconfig

cd ~
git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install

cd ~
git clone --branch v0.0.14 https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
pip3 install --upgrade pip
pip3 install -r requirements.txt
sudo python3 setup.py install
```


### Testing Code

To test ADALM-PLUTO libraries related, type the following commands while having the module conected to your computer. This will allow the module to start the reception mode until until it's forced to stop. 

```
python3
import adi
sdr = adi.Pluto('ip:192.168.2.1')
sdr.sample_rate = int(2.5e6)
sdr.rx()
```

## Deployment

Any Information related to the deployment and way of usage can be looked up on the [User's Manual](https://github.com/LuisMunoz1997/Tesis/blob/main/Digital%20Communications%20Toolkit%20-%20User's%20Manual%20(Spanish%20Version).pdf) or the youtube channel, which has some explanation videos.

## Built With

* [Python](https://www.python.org/) - Programming Language used.
* [PySide - Qt](https://wiki.qt.io/Qt_for_Python) - Main library to develop the GUI.
* [Adi](https://github.com/analogdevicesinc/pyadi-iio.git) -  Main library that allows users manage ADALM-PLUTO throught Python.

## Version

0.1.0 (In Development)

## Authors

* **Luis Muñoz** - *Initial work*
* **Jesús Del Mar** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

