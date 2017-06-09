# pipNuke
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple Script that goes and nukes multiple pip packages. This was born out of the need to uninstall *a lot* of packages from a specific source that all contained the same substring in their names. There are minimal safety measure in place, with the only real safety measure being that all substrings need to be at least 3 characters long. 

## How To Use 
This script will nuke any and all packages that contain the specified substring. **PLEASE** be very careful using this as there are no safety measure or confirmation per package. The minimum length of the substring is 3 characters to avoid you nuking all/most packages on accident. The command format is as follows: 
```
sudo python pipNuke.py <substring>
```
where any pip package that contains ```<substring>``` will be uninstalled. 

That is really all there is folks. 
