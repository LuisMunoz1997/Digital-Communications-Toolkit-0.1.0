# DIGITAL TELECOMUNICATIONS TOOLKIT

Luis Muñoz & Jesús Del Mar's Final Degree Project: Design of a Digital Communication Toolkit over Software Defined Radio for Telecommunications Laboratories.

Version 0.1 - Currently in Development.

## Overview

## Getting Started
### Prerequisites

1) A computer with at least 8 GB of RAM and a procesor Intel(R) Core(TM) i5-10510U CPU @ 1.80GHz 2.30 GHz.
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
#### Option 1) Download .exe

Click on the next link to download:

Install *[PlutoSDR driver](https://github.com/analogdevicesinc/plutosdr-m2k-drivers-win/releases/download/v0.7/PlutoSDR-M2k-USB-Drivers.exe) for Windows

Also, it's necesary the following libraries:

*[libiio](https://github.com/analogdevicesinc/libiio?tab=readme-ov-file): Analog Device’s “cross-platform” library for interfacing hardware
*[libad9361-iio](https://github.com/analogdevicesinc/libad9361-iio?tab=readme-ov-file): AD9361 is the specific RF chip inside the PlutoSDR
pyadi-iio: Main library that allows users manage ADALM-PLUTO throught Python.
```
git clone https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
pip install .
```

#### Option 2) Work directly with the Python's script on Windows.



#### Option 3) Work directly with the Python's script on Linux (Any Distribution)

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


### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

