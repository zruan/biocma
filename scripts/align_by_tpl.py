#!/usr/bin/env python

"""
Script to convert PKL.cma into same length using template alignment

Usage:
    align_by_tpl.py -i infile -t template -o outfile

The `infile` and `template` should have '.cma' suffix.
"""

import sys
import subprocess
import argparse
import tempfile
import logging

from biocma import cma

AP = argparse.ArgumentParser()
AP.add_argument('-o', '--outfile')
AP.add_argument('-i', '--infile')
AP.add_argument('-t', '--template')

args = AP.parse_args()
if sum(map(bool, (args.outfile, args.infile, args.template))) != 3:
    sys.exit(__doc__)

def main(args):
    tmp_file = tempfile.mkstemp(suffix='.cma')
    p = cma.parse(args.infile+'.cma')
    for i in p:
        cma.write(i, tmp_file[1])
        logging.info('Converting %s' % i['name'])
        subprocess.call("run_convert %s %s >> %s" % (args.template, tmp_file[1].split('.')[0], args.outfile), shell=True)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main(args)

