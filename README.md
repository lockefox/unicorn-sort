# unicorn-sort
A tool for sorting and backing up RAW photo files between a drive/NAS

## Setup

CLI installable, or docker runable.  Designed and tested on a mac.

```bash
unicorn --source-dir=... --stars=... --nfs=...
```

Point unicorn at a volume mount, give it filter criteria, and a place to backup.  `unicorn` will then:
1) copy all files whos EXIF data matches the `stars` criteria
2) copy `source-dir` to a nfs or smb location

`unicorn` is a dumb script made for personal use.  Will stomp files if your naming scheme isn't unique.
