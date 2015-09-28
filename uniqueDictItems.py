def uniqueValues(aDict):
    x=[]
    y=[]
    for i,j in aDict.items():
        count=-1
        for a,b in aDict.items():
            if j==b:
                count+=1
        if count==0:
            y.append(i)
    return sorted(y)
uniqueValues({0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3})
          