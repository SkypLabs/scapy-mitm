# Scapy mitm

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f5ccc6e8643f4bd9bddfb1e4f7377fac)](https://www.codacy.com/app/skyper/scapy-mitm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SkypLabs/scapy-mitm&amp;utm_campaign=Badge_Grade)

ARP cache poisoning implementation using Scapy.

## Dependencies

 * Python 2.6 or 2.7
 * [Scapy][scapy]
 * [argparse][argparse] (included with Python >= 2.7 and >= 3.2)

### On Fedora

    yum install scapy

### On Debian

    aptitude install python-scapy

### Using pip

    pip install -r requirements.txt

## How to

Two arguments are required :

* The NIC's name to use
* The IP address you want to hijack

For example :

    sudo ./mitm.py -i eth0 -t 192.168.1.1

For more information :

    sudo ./mitm.py -h

## License

[GPL version 3][GPLv3]

 [scapy]: https://pypi.python.org/pypi/scapy "Scapy: interactive packet manipulation tool"
 [argparse]: https://pypi.python.org/pypi/argparse "argparse: Python command-line parsing library"
 [GPLv3]: https://www.gnu.org/licenses/gpl.txt "GPL version 3"
