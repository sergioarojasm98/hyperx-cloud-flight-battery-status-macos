# Battery Status App for HyperX Cloud Flight on MacOS

## Requirements:
Ensure you have Homebrew and either Conda or Virtualenv installed on your system.

Note: This application was developed on a MacBook Pro M1 Max using an ARM64 architecture. Compatibility with Intel processors has not been tested, and behavior on non-ARM64 environments may vary.

## Step 1: Clone the Repository
Clone the repository using the following Git command:
```sh
git clone git@github.com:sergioarojasm98/hyperx-cloud-flight-battery.git
```
## Step 2: Verify HIDAPI Library Installation
Check if the HIDAPI library is installed:
```sh
find /usr/local -name "libhidapi*.dylib"
```
If nothing appears, you will need to manually install the dependencies. If you get results, jump to Step 5.

## Step 3: Manual Installation of Dependencies
```sh
brew install autoconf automake libtool
git clone https://github.com/libusb/hidapi.git
cd hidapi
./bootstrap
./configure
make
sudo make install
```
## Step 4: Double Check Installation 
```sh
find /usr/local -name "libhidapi*.dylib"
```
You should see output indicating the presence of the library files.
```sh
/usr/local/lib/libhidapi.dylib
/usr/local/lib/libhidapi.0.dylib
```
## Step  5: Install Requirements
Set up your Python environment and install dependencies.
* If you are using Conda:
```sh
conda env create -f environment.yml
```
* If you are using Virtualenv:
```sh
virtualenv -p python3.8 hyperx
source hyperx/bin/activate
pip install -r requirements.txt
```
## Step 6: Run the Application
Execute the main application script:
```sh
python main.py
````
