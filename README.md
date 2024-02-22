## Crt-Parse
Crt-Parse is a simple Python3 script which parses and saves certificate information from crt.sh for a given domain.
## Installation & Setup
```
git clone https://github.com/napnapnapster/Crt-Parse.git
cd Crt-Parse
pip install -r requirements.txt
```
## Usage:
```
python3 certparse.py -h
usage: certparse.py [-h] [-m {out,honly,hout}] domain

positional arguments:
  domain                Parse certificate information for the domain.

options:
  -h, --help            show this help message and exit
  -m {out,honly,hout}, --mode {out,honly,hout}
                        Change mode of the parser.
                        
Example: python3 certparse.py example.com
```
