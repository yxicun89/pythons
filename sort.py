minave=min(ave)
minindex = [i for i, x in enumerate(ave) if x == minave]
for i in minindex:
    minlist.append(list[i][0])
    minans=sorting(minlist)
    for i in minans:
        print("A"+f'{i:04}'+"{0:.2f}".format(minave))


maxave=max(ave)
maxindex = [i for i, x in enumerate(ave) if x == maxave]
for i in maxindex:
    maxlist.append(list[i][0])
    maxans=sorting(maxlist)
    for i in maxans:
        print("A"+f'{i:04}'+"{0:.2f}".format(maxave))
