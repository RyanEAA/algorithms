arr = [1,2,2,1,1,3]

dictArr = {}

print("doing for loop")
for intValue in arr:
    #print(intValue)
    if(str(intValue) in dictArr.keys()):
        dictArr[str(intValue)] += 1
    else:
        dictArr[str(intValue)] = 0


#for values in dictArr.values():
#    print(values)
arrDictValues = list(dictArr.values())
setDictValues = set(arrDictValues)

print(len(arrDictValues)==len(setDictValues))

#print((arrDictValues.size() == setDictValues.length()))

