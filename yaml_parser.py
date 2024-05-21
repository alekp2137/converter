import yaml

def validate(file):
    try:
        with open(file, 'r') as f:
            yaml.safe_load(f)
        return True
    except yaml.YAMLError as e:
        print('parse error: {e}')
        return False
    
