import json

def validate(file): 
    try:
        with open(file, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        print('parse error: {e}')
        return False
    
    