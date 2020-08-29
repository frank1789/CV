import os
import re
from abc import ABC, abstractmethod
from datetime import date
from shutil import copyfile

import jinja2


def now_to_date(data: dict) -> dict:
    if data["end"] == "NOW" or data["end"] == "now" or data["end"] == "Now":
        data["end"] = "\MakeUppercase{present}"
    else:
        pass
    return data


def dict_to_list_tuple(data: dict) -> list:
    return list(map(lambda d: (d.get('skill'), ", ".join(d.get('type'))), data))


class CurriculumVitae(ABC):

    @abstractmethod
    def build_theme(self, theme) -> None:
        pass

    @abstractmethod
    def prepare(self, data) -> None:
        pass

    @abstractmethod
    def write_on_file(self, filename="curriculumvitae.tex") -> None:
        pass

    @abstractmethod
    def compile(self, filename) -> None:
        pass


class FriggeriTheme(CurriculumVitae):

    def __init__(self):
        super(CurriculumVitae, self).__init__()
        self.dir_template = ""
        self.theme = ()
        self.rawcv = None
        self.latex_environment = None

    def build_theme(self, theme) -> None:
        self.dir_template = os.path.join(os.getcwd(), "cv_template", f"{theme}")
        self.theme = (self.dir_template, f"template_{theme}_resume.tex")

    def prepare(self, data) -> None:
        self.latex_environment = jinja2.Environment(
            block_start_string='\BLOCK{',
            block_end_string='}',
            variable_start_string='\VAR{',
            variable_end_string='}',
            comment_start_string='\#{',
            comment_end_string='}',
            line_statement_prefix='%%',
            line_comment_prefix='%#',
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(os.path.abspath('/'))
        )

        # check template folder
        template = self.latex_environment.get_template(os.path.join(self.theme[0], self.theme[1]))

        # alias data fields
        pers = data["data"]
        education = data["data"]["education"]
        skills = dict_to_list_tuple(data["skillset"])
        certificate = data["certificate"]
        update_exp = [now_to_date(d) for d in data["experience"]]
        experience = update_exp

        # fill template
        self.rawcv = template.render(
            name=pers["name"],
            surname=pers["surname"],
            title=pers["title"],
            languages=pers["languages"],
            address=pers["contact"]["address"],
            city=pers["contact"]["city"],
            province=pers["contact"]["province"],
            zip=pers["contact"]["zip"],
            country=pers["contact"]["country"],
            phone=pers["contact"]["phone"],
            email=pers["social"]["e-mail"],
            linkedin=pers["social"]["linkedin"],
            skype=pers["social"]["skype"],
            github=pers["social"]["github"],
            education=education,
            experience=experience,
            skills=skills,
            certificate=certificate
        )

    def write_on_file(self, filename="curriculumvitae.tex") -> None:
        print("copy files...", "start compile")
        # make build dir if not exist and copy source files
        if not os.path.exists(os.path.join(os.getcwd(), "build")):
            os.mkdir("build")
            dest = os.path.join(os.getcwd(), "build")
            for root, _, files in os.walk(self.dir_template):
                for f in files:
                    if not f.startswith(".DS_Store") and not re.match(r"(template).*", f):
                        src = (os.path.join(root, f))
                        copyfile(src, os.path.join(dest, f))
            # save CV
            outname = os.path.join(dest, filename)
            with open(outname, "w+") as fout:
                fout.write(self.rawcv)

    def compile(self, filename) -> None:
        # run process xelatex command
        cc = "xelatex"
        flags = "-shell-escape -halt-on-error -synctex=1 -interaction=nonstopmode"
        flags += " -output-directory=build"
        # enter build dir
        for i in range(0, 3):
            os.system(f'{cc} {flags} {filename}')


class EuropassTheme(CurriculumVitae):
    def __init__(self):
        super(CurriculumVitae, self).__init__()
        self.dir_template = ""
        self.theme = ()
        self.rawcv = None
        self.latex_environment = None

    def build_theme(self, theme) -> None:
        self.dir_template = os.path.join(os.getcwd(), "cv_template", f"{theme}")
        self.theme = (self.dir_template, f"template_{theme}_resume.tex")

    def prepare(self, data) -> None:
        self.latex_environment = jinja2.Environment(
            block_start_string='\BLOCK{',
            block_end_string='}',
            variable_start_string='\VAR{',
            variable_end_string='}',
            comment_start_string='\#{',
            comment_end_string='}',
            line_statement_prefix='%%',
            line_comment_prefix='%#',
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(os.path.abspath('/'))
        )

        # check template folder
        template = self.latex_environment.get_template(os.path.join(self.theme[0], self.theme[1]))

        # alias data fields
        pers = data["data"]
        education = data["data"]["education"]
        skills = dict_to_list_tuple(data["skillset"])
        certificate = data["certificate"]
        experience = data["experience"]

        # fill template
        self.rawcv = template.render(
            name=pers["name"],
            surname=pers["surname"],
            title=pers["title"],
            languages=pers["languages"],
            address=pers["contact"]["address"],
            city=pers["contact"]["city"],
            province=pers["contact"]["province"],
            zip=pers["contact"]["zip"],
            country=pers["contact"]["country"],
            phone=pers["contact"]["phone"],
            email=pers["social"]["e-mail"],
            linkedin=pers["social"]["linkedin"],
            skype=pers["social"]["skype"],
            github=pers["social"]["github"],
            education=education,
            experience=experience,
            skills=skills,
            certificate=certificate
        )

    def write_on_file(self, filename="curriculumvitae.tex") -> None:
        print("copy files...", "start compile")
        # make build dir if not exist and copy source files
        if not os.path.exists(os.path.join(os.getcwd(), "build")):
            os.mkdir("build")
            dest = os.path.join(os.getcwd(), "build")
            for root, _, files in os.walk(self.dir_template):
                for f in files:
                    if not f.startswith(".DS_Store") and not re.match(r"(template).*", f):
                        src = (os.path.join(root, f))
                        copyfile(src, os.path.join(dest, f))
            # save CV
            outname = os.path.join(dest, filename)
            with open(outname, "w+") as fout:
                fout.write(self.rawcv)

    def compile(self, filename) -> None:
        # run process pdflatex command
        cc = "pdflatex"
        flags = "-shell-escape -halt-on-error -synctex=1 -interaction=nonstopmode"
        flags += " -output-directory=build"
        # enter build dir
        for i in range(0, 3):
            os.system(f'{cc} {flags} {filename}')
