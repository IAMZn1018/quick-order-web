import json

def get_content(filename):
    try:
        f =  open('./src/config/{}.json'.format(filename), encoding='utf-8')
    except FileNotFoundError:
        return None
        
    json_data = json.load(f)
    return json_data