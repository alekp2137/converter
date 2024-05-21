import argparse
import os
import json_parser
import yaml_parser
import xml_parser

parser = argparse.ArgumentParser()
parser.add_argument('input', help="File for conversion")
parser.add_argument('output', help="Converted file")
args = parser.parse_args()

def ext_check(file, mustExist):
    if mustExist and not os.path.isfile(file):
        raise FileNotFoundError("file doesn't exist")

    if (file.endswith('.json')):
        return 'json'
    elif (file.endswith('.xml')):
        return 'xml'
    elif (file.endswith('.yaml')):
        return 'yaml'
    else:
        raise ValueError("wrong file extension")
    
inp_ext = ext_check(args.input, True)
out_ext = ext_check(args.output, False)

if (inp_ext == out_ext):
    raise ValueError("cannot convert to the same extension")

