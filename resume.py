#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import errno
import json
import os
import sys

sys.path.insert(0, 'curriculum')
from curriculum.factory import setup_curriculum_vitae


class Registry:
    def __init__(self) -> None:
        self.__data = {}
        pass

    def read_from_file(self, namefile):
        if os.path.exists(namefile):
            with open(namefile) as infile:
                self.__data = json.load(infile)
        else:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), namefile)

    @property
    def information(self) -> dict:
        return self.__data

    @information.setter
    def information(self, a):
        self.__data = a

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


if __name__ == '__main__':
    with open("information.json") as f:
        data = json.load(f)

    setup_curriculum_vitae("Friggeri", data, "FrancescoArgentieri-Resume.tex")
    #setup_curriculum_vitae("europass", data, "FrancescoArgentieri-Resume-europass.tex")
    sys.exit()
