last_loc = int(input("Enter initial location of arm : "))
l =  [int(item) for item in input("Enter The Locations : ").split()]
t=0

l.append(last_loc)
l=sorted(set(l))
ix = l.index(last_loc)

for item in l[ix+1:]:
        t+=abs(item - last_loc)
        last_loc = item
        print("Visisted " , item)
    
for item in reversed(l[0:ix]):
        t+=abs(item - last_loc)
        last_loc = item
        print("Visited " , item)



print(f"\nUsing LOOK the total seek time is {t}")