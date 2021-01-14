sentence="jsgfjgfj jfbkjsfk uttui bkjbkb"
count={}
for i in "jsgfjgfj jfbkjsfk uttui bkjbkb":
    count[i]=0
for i in sentence:
    count[i]=count[i]+1
for i,j in count.items():
    print(i,":",j)

#in operator
print("@" in count)
print("p" in count)
    
    

#2 method
sentence="jgdjgb sjkgkjgk kugekqwgk kjgkwg"
counts={}
for letter in sentence:
    if letter in counts:
        counts[letter]=counts[letter]+1
    else:
        counts[letter]=1
print(counts)        


