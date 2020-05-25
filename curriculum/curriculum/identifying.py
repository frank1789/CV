
import os
import json
import errno


class IdentifyingFactory:
    factories = {}

    def addFactory(id, shapeFactory):
        ShapeFactory.factories.put[id] = shapeFactory
        addFactory = staticmethod(addFactory)

    # A Template Method:
    def createShape(id):
        if not ShapeFactory.factories.has_key(id):
            ShapeFactory.factories[id] = \
                eval(id + '.Factory()')
        return ShapeFactory.factories[id].create()
    createShape = staticmethod(createShape)

    def create_identifying(type):
        pass


class Identifying(object):
    pass


class Linkedin(Identifying):
    pass



class File(Identifying):
    def __init__(self) -> None:
        self.__data = {}

    def read_from_file(self, namefile):
        if os.path.exists(namefile):
            with open(namefile) as infile:
                self.__data = json.load(infile)
        else:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), namefile)

    def write_empty_structure(self, filename) -> None:
        print("Not Implemented yet")
        pass

    @property
    def information(self) -> dict:
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

    @information.setter
    def data(self, a):
        self.__data = a
