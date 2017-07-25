# SyncFi

SyncFi is a cross-platform file synchronizer based on the challenge statement given in task. It synchronizes files between devices using the same network.

## Requirements
Works with python 3 and tested on python 3.4+.

### Dependencies
```
pip3 install -r requirements.txt
```
## Getting Started
1. git clone
3. Run ftp server on device A and sync the files between device A and B.
##### Device A
```
python server.py
```
##### Device B
Sync changes from device A to B
```
python sync.py --ip IP_ADDRESS --port PORT
```
Sync changes from device B to A
```
python sync.py --ip IP_ADDRESS --port PORT -u
```
IP_ADDRESS and PORT can be retrieved while running server.py on device A.
