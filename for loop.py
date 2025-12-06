mylist = [1,2,3]
for item in mylist:
    print ("item")

mydict  = {1:'one', 2:'two', 3:'three'}
for key in mydict:
    print ("key"), mydict[key]


for i, item in enumerate(mylist):
    mylist[i] = item**2