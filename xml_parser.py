import xml.etree.ElementTree as ET

def validate(file):
    try:
        tree = ET.parse(file)
        return True
    except ET.ParseError as e:
        print('parse error: {e}')
        return False
    
    