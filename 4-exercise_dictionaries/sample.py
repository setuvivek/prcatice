sample = {'name':'ushma', 'degree' : 'bca'}

if sample.get('name', 1):
    print("true")
    print()
else:
    print("false")

# if sample.items():
for key,value in sample.items():
        # print("true")
    if key == 'name':
        print(key, value)
        print()

if sample.keys():
    print("true")
    print(sample.keys())
    print()
else:
    print("false")

'name' in sample