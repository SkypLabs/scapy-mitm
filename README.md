# Scapy mitm

ARP cache poisoning implementation using Scapy.

## Dependencies

 * Python 2.6 or 2.7
 * [Scapy][1] package

### On Fedora

    yum install scapy

### On Debian

    aptitude install python-scapy

### Using pip

    pip install scapy

## How to

This script needs two parameters with the following order :

* The NIC's name to use
* The IP address you want to hijack

For example :

    sudo ./mitm.py eth0 192.168.1.1

## License

[GPL version 3][2]

  [1]: https://pypi.python.org/pypi/scapy/2.2.0-dev "Scapy: interactive packet manipulation tool"
  [2]: https://www.gnu.org/licenses/gpl.txt "GPL version 3"
