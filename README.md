# Scapy mitm

ARP cache poisoning implementation using Scapy.

## Dependencies

 * Python 2.6 or 2.7
 * [Scapy][1]
 * [argparse][2] (included with Python >= 2.7 and >= 3.2)

### On Fedora

    yum install scapy

### On Debian

    aptitude install python-scapy

### Using pip

    pip install scapy

## How to

Two arguments are required :

* The NIC's name to use
* The IP address you want to hijack

For example :

    sudo ./mitm.py -i eth0 -t 192.168.1.1

For more information :

    sudo ./mitm.py -h

## License

[GPL version 3][3]

  [1]: https://pypi.python.org/pypi/scapy "Scapy: interactive packet manipulation tool"
  [2]: https://pypi.python.org/pypi/argparse "argparse: Python command-line parsing library"
  [3]: https://www.gnu.org/licenses/gpl.txt "GPL version 3"
