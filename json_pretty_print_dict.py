 # the standard string repr for dicts is hard to read:
my_mapping = {"a":23,"b":42,"c":0xc0ffee}
print(my_mapping)
print("_"*30)

 #the "json" module can do a much better job:
import json
print(json.dumps(my_mapping,indent=4,sort_keys=True))
