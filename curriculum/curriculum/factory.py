import sys
from abc import ABC, abstractmethod

from curriculum.curriculumvitae import CurriculumVitae
from curriculum.curriculumvitae import EuropassTheme
from curriculum.curriculumvitae import FriggeriTheme


class AbstractFactory(ABC):

    @abstractmethod
    def compile_cv(self):
        pass


class FriggeriCurriculumVitae(AbstractFactory):

    def compile_cv(self) -> FriggeriTheme:
        return FriggeriTheme()


class EuropassCurriculumVitae(AbstractFactory):

    def compile_cv(self) -> EuropassTheme:
        return EuropassTheme()


def mycv(cv: AbstractFactory) -> CurriculumVitae:
    f = cv.compile_cv()
    return f


def setup_curriculum_vitae(style, data, filename="curriculumvitae.tex"):
    assert (type(style) is str), "To define a template style must be enter a string"
    assert (type(filename) is str), "argument \"filename\" must be a string"
    assert (filename.endswith(".tex")), "argument 'filename' must be end with .tex"
    print("Check setup curriculum vitae")

    if style is "friggeri" or style is "Friggeri":
        cv = mycv(FriggeriCurriculumVitae())
        print("Initialize...\nReady")
    elif style is "europass" or style is "Europass":
        cv = mycv(EuropassCurriculumVitae())
        print("Initialize...\nReady")
    else:
        print("Template request is not implemented yet")
        sys.exit(0)

    print("Prepare CV\nTake a while...")
    cv.build_theme(style.lower())
    cv.prepare(data)
    cv.write_on_file(filename)
    cv.compile(filename=filename)
    print("Done")


if __name__ == "__main__":
    setup_curriculum_vitae("friggeri")
