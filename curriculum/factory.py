import sys
from abc import ABC, abstractmethod

from curriculum.curriculumvitae import FriggeriTheme, EuropassTheme, CurriculumVitae


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
    # compare value of template and build
    if style == "friggeri" or style == "Friggeri":
        cv = mycv(FriggeriCurriculumVitae())
        print("Initialize...\nReady")
    elif style == "europass" or style == "Europass":
        cv = mycv(EuropassCurriculumVitae())
    else:
        print("Template request is not yet implemented.")
        sys.exit(-1)

    print("Prepare CV")
    print("Take a while...")
    cv.build_theme(style.lower())
    cv.prepare(data)
    cv.write_on_file(filename)
    cv.compile(filename=filename)
    print("Done")
