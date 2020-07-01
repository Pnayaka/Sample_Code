names=(('Tom','Cat'),('Jerry','Mouse'), ('Donald', 'Duck'))
number=[3561, 4014, 9813]
telDir={}
for i in range(len(number)):
    telDir[names[i]]=number[i]
for fn, ln in telDir:
    print(fn, ln, telDir[fn,ln])
