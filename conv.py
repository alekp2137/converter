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
    elif (file.endswith('.yaml') or file.endswith('.yml')):
        return 'yaml'
    else:
        raise ValueError("wrong file extension")
    
inp_ext = ext_check(args.input, True)
out_ext = ext_check(args.output, False)

if (inp_ext == out_ext):
    raise ValueError("cannot convert to the same extension")


if (inp_ext == 'json'):
    json_parser.validate(args.input)
    data = json_parser.to_data(args.input)
elif (inp_ext == 'xml'):
    xml_parser.validate(args.input)
    data = xml_parser.to_data(args.input)
elif (inp_ext == 'yaml'):
    yaml_parser.validate(args.input)
    data = yaml_parser.to_data(args.input)
else:
    raise ValueError("wtf") # nie powinno się zdarzać


if (out_ext == 'json'):
    converted = json_parser.create(data)
elif (out_ext == 'xml'):
    converted = xml_parser.create(data)
elif (out_ext == 'yaml'):
    converted = yaml_parser.create(data)
else:
    raise ValueError("wtf") # nie powinno się zdarzać

with open(args.output, 'w') as file:
    file.write(converted)
