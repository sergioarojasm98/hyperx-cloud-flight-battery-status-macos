# Battery Status App for HyperX Cloud Flight on MacOS

This application enables you to monitor the battery status of your HyperX Cloud Flight headphones on macOS devices, providing real-time battery updates.

## Requirements:
- **Homebrew**: Latest version recommended.
- **Python Environment**: Conda or Virtualenv.

> **Note**: Developed on MacBook Pro M1 Max with ARM64 architecture. Compatibility with Intel processors is untested.

## Installation Instructions

### Step 1: Clone the Repository
Clone the repository using the following Git command:
```sh
git clone git@github.com:sergioarojasm98/hyperx-cloud-flight-battery.git
```
### Step 2: Verify HIDAPI Library Installation
Check if the HIDAPI library is installed:
```sh
find /usr/local -name "libhidapi*.dylib"
```
Proceed to Step 5 if files are found, otherwise continue to Step 3.

### Step 3: Manual Installation of Dependencies
Install necessary tools and the HIDAPI library:
```sh
brew install autoconf automake libtool
git clone https://github.com/libusb/hidapi.git
cd hidapi
./bootstrap
./configure
make
sudo make install
```
### Step 4: Confirm HIDAPI Installation 
```sh
find /usr/local -name "libhidapi*.dylib"
# Expected output:
# /usr/local/lib/libhidapi.dylib
# /usr/local/lib/libhidapi.0.dylib
```
### Step 5: Set Up Python Environment
Choose your environment setup:
* Conda:
```sh
conda env create -f environment.yml
```
* Virtualenv:
```sh
virtualenv -p python3.8 hyperx
source hyperx/bin/activate
pip install -r requirements.txt
```
### Step 6: Run the Application
Execute the main application script:
```sh
python main.py
````
