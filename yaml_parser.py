import yaml

def validate(file):
    try:
        with open(file, 'r') as f:
            yaml.safe_load(f)
        return True
    except yaml.YAMLError as e:
        print('parse error: {e}')
        return False
    
def create(data):
    return yaml.safe_dump(data, default_flow_style=False)

def to_data(yaml_file):
    with open(yaml_file, 'r') as f:
            return yaml.safe_load(f)
