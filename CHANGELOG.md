# Changelog

## v1.2.1 - July 14, 2019

### Improvements

* Use the parameters `inter` and `loop` of the function `sendp`
* Use commit ids instead of Git tags in the pre-commit configuration

### Fixes

* The parameter `iface` of the function `sendp` was not set

## v1.2.0 - May 25, 2019

### New Features

* Display version number with `--version`

### Improvements

* Stick to the PEP 8 style guide
* Add a `pre-commit` configuration file
* Add a Probot Settings configuration file

## v1.1.1 - Jan 12, 2018

### Improvements

* Rename `mitm.py` to `arp-mitm`
* Add `requirements.txt`
* Replace tab characters with spaces
* Remove a useless import

### Fixes

* Fix the use of objects with the same name as a built-in

## v1.1.0 - Jul 20, 2015

### New Features

* Use `argparse` module

### Improvements

* Allow to import `mitm.py` into another Python script
* Improve help messages
* Possibility to use `--help` without being root

## v1.0.0 - Jun 13, 2015

First release.
