#FIFO - SF - Ref String

fr = int(input("Enter no of frames : "))
ref = input("Enter ref string : ")
hit =0
miss = 0
n = len(ref)
que = []
ix = 0

for i in range(0,n):

  if len(que) < fr:
    que.append(ref[i])
    print(que)
    miss+=1

  else:
    if (ref[i]) in que:
      hit+=1
      print("Hit")
    else:
      que[ix] = ref[i]
      miss+=1
      
      if ix==fr-1:
        ix=0
      else: 
        ix+=1
      print(que)

print(f"Hit ratio : {hit/n}")
print(f"Page Fault ratio : {miss/n}")
      
      
    
  


