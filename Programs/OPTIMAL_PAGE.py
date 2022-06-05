# << AKSHIT OP >>

frames = 3
ref_strings = "31216513"
n = len(ref_strings)
hit = 0
miss = 0
rank = [0,0,0]
Queue = ["", "", ""]

for i in range(n):
    item = ref_strings[i]
    if item not in Queue:
        #if no page hit
        miss += 1
        if "" not in Queue:
            #if queue is full
            for item_index, queue_item in enumerate(Queue):
                if queue_item not in ref_strings[i:]:
                #if queue item does not exist in ref string
                    rank[item_index] = n+1
                else:
                #if queue item does exist in ref string
                    rank[item_index] = ref_strings[i:].index(queue_item)
            #index of max rank
            insert_index = rank.index(max(rank))
            Queue[insert_index] = item
        else:
            #found empty space
            insert_index = Queue.index("")
            Queue[insert_index] = item
            
        print(f"{item} -> {Queue}")
    else:
        #page hit
        hit += 1
        print(f"{item} -> hit")
        
print(f"Hit ratio : {round(hit/n, 3)}")
print(f"Page Fault ratio : {round(miss/n, 3)}")