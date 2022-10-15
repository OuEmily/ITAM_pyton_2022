dict1 = {"a":"b", "b":"a",  "c": "a"}
dict2 = {"a":"b", "b":"a"}
dict3 = { }
len1 = len(dict1)
len2 = len(dict2)
def key_difference(dict1, dict2):
    for key in list(dict1.keys()) + list(dict2.keys()):
        if dict1.get(key) != None  and dict2.get(key) != None:
            if dict1.get(key) == dict2.get(key):
                dict3[key] = 'equel'
            elif dict1.get(key) == dict2.get(key):
                dict3[key] = 'changed'
        elif dict1.get(key) == None and dict2.get(key) != None:
            dict3[key] = 'added'
        elif dict2.get(key) == None and dict1.get(key) != None:
            dict3[key] = 'deleted'           
    print(dict3)
key_difference(dict1, dict2)


