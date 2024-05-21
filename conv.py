import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('input', help="File for conversion")
parser.add_argument('output', help="Converted file")
args = parser.parse_args()

def ext_check(file):
    if not os.path.isfile(file):
        raise FileNotFoundError("file doesn't exist")

    if (file.endswith('.json')):
        return 'json'
    elif (file.endswith('.xml')):
        return 'xml'
    elif (file.endswith('.yaml')):
        return 'yaml'
    else:
        raise ValueError("wrong file extension")
    
inp_ext = ext_check(args.input)
out_ext = ext_check(args.output)

if (inp_ext == out_ext):
    raise ValueError("cannot convert to a file with the same extension")

