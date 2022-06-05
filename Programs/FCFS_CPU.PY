ps = []
att=0
awt=0
n = int(input("Enter no of processes : "))

for i in range(0,n):
  ar = int(input(f"Enter arrival time of P{i+1} : "))
  burst = int(input(f"Enter burst time of P{i+1} : "))
  ps.append({
    "name":f"P{i}",
    "arrival":ar,
    "burst" : burst
  })

ps = sorted(ps, key = lambda i: i['arrival'])

for count,item in enumerate(ps) : 
  
  if count==0:
    item['tat'] = item['burst']
    item['ft'] = item['burst']
    item['wt']=0
  else:
    item['ft'] = item['burst'] + ps[count-1]['ft']
    item['tat'] = item['ft'] - item['arrival']
    item['wt']=item['tat'] - item['burst']

  att+=item['tat']
  awt+=item['wt']
  ps[count] = item


print("\n{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('Name','AT', 'BT' , 'FT' , 'TAT' , 'WT'))
for item in ps:
    x=list(item.values())
    print("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format(x[0] , x[1] , x[2] , x[4] , x[3] , x[5]))

print(f"\navg waiting time {awt/n}")
print(f"avg turnaround time {att/n}")