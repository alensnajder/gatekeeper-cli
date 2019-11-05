![Gatekeeper](.github/logo.svg?sanitize=true "Gatekeeper logo")
# Gatekeeper CLI
A command line client to control gates connected to relay through GPIO interface.
# Installation
Clone the repository and enter directory
```
$ git clone https://github.com/alensnajder/gatekeeper-cli.git
$ cd gatekeeper-api
```
Remove python extension
```
$ mv gatekeeper.py gatekeeper
```
Make `gatekeeper` executable
```
$ chmod +x gatekeeper
```
Make `gatekeeper` globally accessible
```
$ mv gatekeeper /usr/local/bin
```
# Usage
```
$ gatekeeper --help

usage: gatekeeper [-h] -p PIN -d DURATION

optional arguments:
  -h, --help                        show this help message and exit
  -p PIN, --pin PIN                 GPIO BCM Pin number
  -d DURATION, --duration DURATION  duration of toggle
```
# License
```
Copyright (c) 2019 Alen Snajder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
