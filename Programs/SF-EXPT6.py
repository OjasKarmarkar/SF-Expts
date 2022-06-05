prs = []
bls = []

n = int(input("Enter no of processes : "))
b = int(input("Enter no of blocks : "))

for i in range(0, b):
    x = int(input(f"Enter size of block {i+1} : "))
    bls.append({"size":x , "available":True})

for i in range(0, n):
    x = int(input(f"Enter size of process P{i+1} : "))
    pr = {"size": x, "allocatted": False, 'frag': 0 , 'block' : None}
    prs.append(pr)


# # #First Fit
# def ff(prs):

#     for count, ele in enumerate(prs):

#         for bl_ix, bl in enumerate(bls):

#             if ele['allocatted'] != True and bl['available']==True:
#                 if ele['size'] <= bl['size']:
#                     ele['allocatted'] = True
#                     bl["available"] = False
#                     ele['frag'] = bl['size'] - ele['size']
#                     ele['block'] = bl_ix+1

#     return prs

# print(prs)

#Best Fit

def bf(prs):
    for count, ele in enumerate(prs):

        min_diff=9999
        min_diff_ix = 0
        
        if ele['allocatted'] != True:
            for bl_ix, bl in enumerate(bls):
                    if ele['size'] <= bl["size"] and bl['available']==True:
                        x = min(min_diff , abs(bl["size"]-ele['size']))
                        if x<min_diff:
                            min_diff = x
                            min_diff_ix = bl_ix
                            bl['available'] = False
                            ele["allocatted"] = True
                            ele['frag'] = min_diff
                            ele['block'] = min_diff_ix+1
    
    return prs

# #Worst fit
# def wf(prs):
#     for count, ele in enumerate(prs):

#         max_diff=0
#         max_diff_ix = 0
        
#         if ele['allocatted'] != True:
#             for bl_ix, bl in enumerate(bls):
#                     if ele['size'] <= bl["size"] and bl['available']==True:
#                         x = max(max_diff , abs(bl["size"]-ele['size']))
#                         if x>max_diff:
#                             max_diff = x
#                             max_diff_ix = bl_ix
#                             bl['available'] = False
#                             ele["allocatted"] = True
#                             ele['frag'] = max_diff
#                             ele['block'] = max_diff_ix+1
#     return prs
    

prs = bf(prs)

print("Process \t Size \t Fragmentation \t Block")
for count , pr in enumerate(prs):
    print(f"P{count+1} \t\t {pr['size']} \t {pr['frag']} \t\t{pr['block']}")
