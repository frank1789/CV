#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import sys

from curriculum.factory import setup_curriculum_vitae
from curriculum.identifying import Identifying

parser = argparse.ArgumentParser(description="Build fast your CV, Choose between template 'Friggeri' or 'Europass'")
parser.add_argument('cv', metavar='cv', type=str, help='file information JSON')
parser.add_argument('--template', dest='template', help='template name, choose between Friggeri or Europass')
parser.add_argument('--output', dest='outname', action='store', help='Output name file.')

if __name__ == '__main__':
    args = parser.parse_args()
    data_resume = Identifying()
    data_resume.read_from_file(args.cv)
    setup_curriculum_vitae(args.template, data_resume.data, args.outname)
    sys.exit()
