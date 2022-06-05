last_loc = int(input("Enter initial location of arm : "))
max_loc = int(input("Enter Max location of arm : "))
arm_dir = input("Enter r for right , l for left : ")
l =  [int(item) for item in input("Enter The Locations : ").split()]
t=0

l.append(last_loc)


if arm_dir == 'r':
        l.append(max_loc)
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

else:
        l.append(0)
        l=sorted(set(l))
        ix = l.index(last_loc)
        
        for item in reversed(l[0:ix]):
                t+=abs(item - last_loc)
                last_loc = item
                print("Visited " , item)
        
        for item in l[ix+1:]:
                t+=abs(item - last_loc)
                last_loc = item
                print("Visisted " , item)
        
      



print(f"\nUsing SCAN the total seek time is {t}")