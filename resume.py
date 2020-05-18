#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import jinja2
import os
import errno
from jinja2 import Template
import json
import re
from shutil import copyfile
import subprocess


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
	def set_data(self, a):
		self.__data = a


class TemplateTheme:

	def __init__(self, theme) -> None:

		assert (type(theme) is str), "argument must be a string"
		self.__template = ()
		self.__base_template_dir = os.path.join(os.getcwd(), "cv_template")
		# check theme wants build
		if theme is "friggeri":
			self.set_theme(theme)

		elif theme is "europass":
			print("Not Implemented yet")

		else:
			print("invalid selection, not implemented yet")

	@property
	def theme(self) -> tuple:
		return self.__template

	def set_theme(self, theme) -> None:
		path = os.path.join(self.__base_template_dir, theme)
		f = "template_{}_resume.tex".format(theme)
		self.__template = (path, os.path.join(path, f))


class BuildResume:
	def __init__(self, theme) -> None:
		self.cv = ""
		self.filename = None
		self.theme_dir, self.template = TemplateTheme(str(theme)).theme
		self.collect_information = Registry()
		# initialize jinja2 env
		self.latex_jinja_env = jinja2.Environment(
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

	@property
	def CV(self):
		return self.cv

	@CV.setter
	def CV(self, s) -> None:
		self.cv = s

	def prepare(self, filename):
		self.collect_information.read_from_file(filename)
		data_resume = self.collect_information.information
		if os.path.exists(self.template):
			template = self.latex_jinja_env.get_template(
				os.path.realpath(self.template))
		else:
			raise FileNotFoundError(
				errno.ENOENT, os.strerror(errno.ENOENT), self.template)

		# generate file to compile
		print("rendering template")
		# alias
		pers = self.collect_information.personal_data
		skills = list(map(lambda d: (d.get('skill'), ", ".join(
			d.get('type'))), self.collect_information.skills))

		self.CV = template.render(
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
			education=self.collect_information.education,
			experience=self.collect_information.experience,
			skills=skills,
			certificate=self.collect_information.certificates
		)

	def build(self, outname="FrancescoArgentieri-Resume.tex") -> None:
		print("copy files...", "start compile")
		# make build dir if not exist and copy source files
		if not os.path.exists(os.path.join(os.getcwd(), "build")):
			os.mkdir("build")
			dest = os.path.join(os.getcwd(), "build")
			for root, _, files in os.walk(self.theme_dir):
				for f in files:
					if not f.startswith(".DS_Store") and not re.match(r"(template).*", f):
						src = (os.path.join(root, f))
						copyfile(src, os.path.join(dest, f))
			# save CV
			filename = os.path.join(dest, outname)
			with open(filename, "w+") as fout:
				fout.write(self.CV)

	def compile(self) -> None:
		# run process xelatex command
		CC = "xelatex"
		flags = "-shell-escape -halt-on-error -synctex=1 -interaction=nonstopmode"
		flags += " -output-directory=build"
		# enter build dir
		for i in range(0,3):
			os.system(f'{CC} {flags} {"FrancescoArgentieri-Resume.tex"}')



if __name__ == '__main__':
	print("Hello world")
	with open("information.json") as f:
		data = json.load(f)

	print(type(data))
	a = BuildResume("friggeri")
	a.prepare("information.json")
	a.build()
	a.compile()
