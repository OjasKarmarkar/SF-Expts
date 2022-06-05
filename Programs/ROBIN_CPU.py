ps = []
att=0
awt=0
print("**** Round Robin ****\n")
n = int(input("Enter no of processes : "))
q = int(input("Enter time quantum : "))
total_burst=0
b=0

for i in range(0,n):
  ar = int(input(f"Enter arrival of P{i+1} : "))
  burst = int(input(f"Enter burst time of P{i+1} : "))
  total_burst+=burst
  
  ps.append({
    "name":f"P{i}",
    "arrival":ar,
    "remaining": burst,
    "burst" : burst,
    "tat": -ar,
    "wt": -ar
  })

ps = sorted(ps, key = lambda i: (i['arrival']))

print('\n Gantt Chart : \n')

while b<total_burst:
  i=0
  while i < n:
    if ps[i]['remaining']!=0:
      if ps[i]['remaining'] > q:
        ps[i]['remaining'] -= q
        ps[i]['tat']+=q
        b+=q
      else:
        b+=ps[i]['remaining']
        ps[i]['remaining'] = 0
      print(f"P{i+1} : {b}")
      ps[i]['tat']= b - ps[i]['arrival']
      ps[i]['wt'] =  ps[i]['tat'] - ps[i]['burst']
      i+=1
    else:
      i+=1

for i in range (len(ps)):
  att+= ps[i]['tat']
  awt+=ps[i]['wt']


print(f"\navg waiting time {awt/n}")
print(f"avg turnaround time {att/n}")