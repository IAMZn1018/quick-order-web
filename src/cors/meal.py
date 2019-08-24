import json

def get_content():
    f =  open('./src/config/xiangcun.json', encoding='utf-8')
    json_data = json.load(f)
    return json_data