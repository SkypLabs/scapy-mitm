# Scapy MITM

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f5ccc6e8643f4bd9bddfb1e4f7377fac)](https://www.codacy.com/app/skyper/scapy-mitm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SkypLabs/scapy-mitm&amp;utm_campaign=Badge_Grade) [![Known Vulnerabilities](https://snyk.io/test/github/skyplabs/scapy-mitm/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/skyplabs/scapy-mitm?targetFile=requirements.txt)

[ARP cache poisoning][arp cache poisoning] implementation using [Scapy][scapy website].

## Dependencies

* Python 2.7 or 3.2+
* [Scapy][scapy PyPI]

### Using pip

    sudo pip install --upgrade -r requirements.txt

## How to

    usage: arp-mitm [-h] -i INTERFACE -t TARGET [-I INTERVAL]

    ARP cache poisoning implementation using Scapy

    optional arguments:
      -h, --help            show this help message and exit
      -i INTERFACE, --interface INTERFACE
                            network interface to use
      -t TARGET, --target TARGET
                            target's IP address
      -I INTERVAL, --interval INTERVAL
                            seconds between two ARP frames (default: 10.0s)

For example:

    sudo ./arp-mitm -i eth0 -t 192.168.1.1

## License

[GPL version 3][GPLv3]

 [arp cache poisoning]: https://en.wikipedia.org/wiki/ARP_spoofing "ARP spoofing"
 [GPLv3]: https://www.gnu.org/licenses/gpl.txt "GPL version 3"
 [scapy PyPI]: https://pypi.org/project/scapy/ "Scapy: interactive packet manipulation tool"
 [scapy website]: https://scapy.net/ "Scapy - Packet crafting for Python2 and Python3"
