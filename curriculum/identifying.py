#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import errno
import json
import os


class Identifying(object):
    def __init__(self) -> None:
        self.__data = {}

    def read_from_file(self, namefile) -> None:
        if os.path.exists(namefile):
            with open(namefile) as infile:
                self.__data = json.load(infile)
        else:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), namefile)

    def write_empty_structure(self, filename="outfile.json") -> None:
        print("Not Implemented yet")
        pass

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def personal_data(self) -> dict:
        return self.__data["data"]

    @property
    def education(self) -> list:
        return self.__data["data"]["education"]

    @property
    def experience(self) -> list:
        return self.__data["experience"]

    @property
    def skills(self) -> list:
        return self.__data["skillset"]

    @property
    def certificates(self) -> list:
        return self.__data["certificate"]

    @data.setter
    def data(self, a):
        self.__data = a


class Linkedin:
    pass
