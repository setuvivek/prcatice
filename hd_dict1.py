#Add two dict , if both keys are present in each dict than add
# otherwise remaining key should be printed in the final dict
# def merge(dict1,dict2):
#     return(dict2.update(dict1))
dict1 = {
    "a":10,
    "b":20,
    "c":30
}
dict2 = {
    "a":5,
    "b":15,
    "d":10
}
e = {**dict1, **dict2}  #merge dictionary

for key in dict1:
    if key in dict2:
        e[key] = dict2[key] + dict1[key]
    else:
        pass

print(e)

# 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