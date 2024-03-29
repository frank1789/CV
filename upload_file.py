#!/usr/bin/env python3
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
            dbx.files_upload(f.read(), destination,
                             mode=dropbox.files.WriteMode.overwrite)


def parse():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Upload file to Dropbox",
        add_help=True)
    parser.add_argument("token_access", type=str, help="Token access")
    parser.add_argument(
        "file", type=str, help="File to upload", action="store")
    parser.add_argument("--destination",
                        type=str,
                        help="optional full path where upload file, without file-name",
                        action="store")
    args = parser.parse_args()
    return args


def main():
    data = parse()
    transferData = TransferData(data.token_access)
    # extract data from parse
    print(data.file)
    file_from = data.file
    # The full path to upload the file to, including the file name
    if data.destination is not None:
        file_to = "/" + data.destination + file_from
    else:
        file_to = "/" + file_from
    # API v2
    transferData.upload_file(file_from, file_to)


if __name__ == '__main__':
    main()
