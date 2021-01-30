# unicorn-sort
A tool for sorting and backing up RAW photo files between a drive/NAS

Requires [exiftool](https://exiftool.org/)
Requires [exempi](https://libopenraw.freedesktop.org/exempi/) >= 2.2.0
Requries [libnfs](https://github.com/sahlberg/libnfs)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

`make black`

## Setup

CLI installable, or docker runable.  Designed and tested on a mac.

```bash
unicorn --source-dir=... --stars=... --nfs=...
```

Point unicorn at a volume mount, give it filter criteria, and a place to backup.  `unicorn` will then:
1) copy all files whos EXIF data matches the `stars` criteria
2) copy `source-dir` to a nfs or smb location

`unicorn` is a dumb script made for personal use.  Will stomp files if your naming scheme isn't unique.
