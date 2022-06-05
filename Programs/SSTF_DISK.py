n = int(input("Enter no of locations to visit : "))
last_loc = int(input("Enter initial location of arm : "))
min_time = 9999
l =  [int(item) for item in input("Enter The Locations : ").split()]
visited=[]
t=0

for i in range(0, len(l)):
    ix=0
    for index , item in enumerate(l):
        if(item not in visited):
            mt=abs(last_loc-item)
            if min_time>mt:
                min_time = mt
                ix = index
    print("Visited " , l[ix])
    t+=min_time
    last_loc = l[ix]
    visited.append(l[ix])
    min_time=9999

print(f"\nUsing SSTF the total seek time is {t}")