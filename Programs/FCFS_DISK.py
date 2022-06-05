n = int(input("Enter no of locations to visit : "))
last_loc = int(input("Enter initial location of arm : "))
seek_mult = int(input("Enter seek time for each cylinder : "))
t=0
l =  [int(item) for item in input("Enter The Locations : ").split()]



for item in l:
  t+= abs(last_loc-item)
  last_loc = item

print(f"\nUsing FCFS the total seek time is {t*seek_mult}")