prs = []
bls = []
w=0
max_diff = 0

n = int(input("Enter no of processes : "))
b = int(input("Enter no of blocks : "))

for i in range(0, b):
    x = int(input(f"Enter size of block {i+1} : "))
    bls.append({"size":x })

for i in range(0, n):
    x = int(input(f"Enter size of process P{i+1} : "))
    pr = {"size": x, "allocatted": False, 'name':f"P{i+1}"}
    prs.append(pr)

for pr in prs:
    for b in sorted(bls , key= lambda x : x['size'] , reverse = True):
        if b['size']>=pr['size']:
            diff = max(abs(b['size'] - pr['size']) , max_diff)
            if diff>max_diff:
                print(f"Process {pr['name']} is allocatted to block of size {b['size']}")   
                b['size'] -= pr['size']
                pr['allocatted'] = True
                max_diff = diff
                break
    max_diff = 0
    if pr["allocatted"] != True:
        # wastage+=pr["size"]
        print(f"Process {pr['name']} is not allocatted")   


for b in bls:
    w+=b['size']

print(w)
