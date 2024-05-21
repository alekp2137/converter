import xml.etree.ElementTree as ET
import xmltodict

def validate(file):
    try:
        tree = ET.parse(file)
        return True
    except ET.ParseError as e:
        print('parse error: {e}')
        return False

def create(data):
    data = {'': data}
    return xmltodict.unparse(data, pretty=True)

def to_data(xml_file):
    with open(xml_file, 'r') as f:
        return xmltodict.parse(f.read())
