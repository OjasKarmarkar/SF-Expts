#LRU - SF - Ref String

capacity = 3
processList = [ 7, 0, 2,1,0,5,4,6,0,1]
                 
s = []
 
pageFaults = 0
 
for i in processList:
 
    if i not in s:
 
        if(len(s) == capacity):
            s.remove(s[0])
            s.append(i)
 
        else:
            s.append(i)
 
        pageFaults +=1
 
    else:
         
        s.remove(i)
 
        s.append(i)
     
print("Page Faults : {}".format(pageFaults))