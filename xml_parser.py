import xml.etree.ElementTree as ET
import xml.dom
    
def _dict_to_element(parent, value):
    if isinstance(value, dict):
        if 'attributes' in value:
            for key, val in value['attributes'].items():
                parent.set(key, val)
        if 'text' in value and value['text']:
            parent.text = value['text']
        for child in value.get('children', []):
            for tag, child_value in child.items():
                elem = ET.Element(tag)
                parent.append(elem)
                _dict_to_element(elem, child_value)

def _element_to_dict(element):
    return {
        element.tag: {
            'attributes': element.attrib,
            'text': element.text.strip() if element.text else None,
            'children': [_element_to_dict(child) for child in list(element)]
        } if element else element.text
    }
    
def validate(file):
    try:
        tree = ET.parse(file)
        return True
    except ET.ParseError as e:
        print('parse error: {e}')
        return False

def create(data):
    root_name, root_value = next(iter(data.items()))
    root = ET.Element(root_name)
    _dict_to_element(root, root_value)
    xml_str = ET.tostring(root, encoding='unicode')
    return xml.dom.parseString(xml_str).toprettyxml(indent="  ")

def to_data(xml_file):
    tree = ET.ElementTree(ET.fromstring(xml_file))
    root = tree.getroot()
    return {root.tag: _element_to_dict(root)}
