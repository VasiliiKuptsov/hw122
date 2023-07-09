
#data = {}
#collections = data
#key = 0
#defolt = 'good'
# файл dicts.py
def get_val(collection, key, default='git'):
    if key == None:
        return 'git'
    if collection == {}:
        return default

    return collection[key]
