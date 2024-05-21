import json

def validate(file): 
    try:
        with open(file, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        print('parse error: {e}')
        return False
    
def create(data):
    return json.dumps(data, indent=2)

def to_data(json_file):
    with open(json_file, 'r') as f:
            return json.load(f)
