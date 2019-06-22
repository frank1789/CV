#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, source, destination):
        """
        upload a file to Dropbox using API v2
        :param source: the original file wants to upload
        :param destination: the destination folder on dropbox
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(source, 'rb') as f:
            dbx.files_upload(f.read(), destination)


def parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="Upload file to Dropbox")
    parser.add_argument("token_access",  type=str, help="Token access")
    parser.add_argument("file",  type=str, help="file to upload", action="store")
    parser.add_argument("destination",  type=str,  help="destination folder Dropbox", action="store")
    args = parser.parse_args()
    return args


def main():
    data = parse()
    print(data)
    exit()
    transferData = TransferData(data.access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(data.file, data.destination)

if __name__ == '__main__':
    main()
