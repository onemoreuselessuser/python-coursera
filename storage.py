import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

key = args.key
value = args.value

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

#create file if not exists
with open(storage_path, 'a') as f:
    f.close()

#read file contents
with open(storage_path, 'r+') as f:
    try:
        content = json.loads(f.read())
    except:
        content={}
    #if value is defined we need to update our dict
    if value:
        if key not in content.keys():
            content[key] = [value]
        else:
            content[key].append(value)
    #otherwise print values for current keys
    else:
        print(*content.get(key, ""), sep=', ')


#overwrite file with updated dict
with open(storage_path, 'w') as f:
    f.write(json.dumps(content))