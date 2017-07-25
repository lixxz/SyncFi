import argparse
from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FtpTarget
from ftpsync.synchronizers import UploadSynchronizer

def sync(ip, port, upload):
    local = FsTarget(".")
    user ="user"
    passwd = "12345"
    remote = FtpTarget("/", ip, port, username=user, password=passwd)
    opts = {"resolve": "skip", "verbose": 1, "dry_run" : False}

    if upload == True:
        s = UploadSynchronizer(local, remote, opts)
    else:
        s = UploadSynchronizer(remote, local, opts)

    s.run()


def main():
    parser = argparse.ArgumentParser(description="Sync files")

    parser.add_argument("--ip", dest="ip",
                        help="ip of ftp server running on remote machine")
    parser.add_argument("--port", dest="port", type=int,
                        help="port at which ftp server is running on remote machine")
    parser.add_argument("-u", "--upload", action="store_true", dest="upload",
                        help="upload changes from this machine to other or vice-versa")

    args = parser.parse_args()

    sync(args.ip, args.port, args.upload)

if __name__ == "__main__":
    main()
