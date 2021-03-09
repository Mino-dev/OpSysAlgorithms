import argparse
from collections import Counter # Count occurences in a collection

#Optimal Algorithm
def optimal(items, frames):
    print("Optimal: \n")

    pageframe = {}#page frames    
    miss = 0 # page faults   

    for i, value in enumerate(items):
       
        if miss < frames:
            if value not in pageframe.keys():   
                miss += 1
        else:
            if value not in pageframe.keys():
                flag = False
                values = list(pageframe.keys())[:frames]
                restOfItems = items[i:len(items)]
                restOfItems.remove(restOfItems[0])
                for val in values:
                    if val not in restOfItems:
                        pageframe.pop(val, None)
                        flag = True
                        break

                if not flag:

                    indexOfval1 = restOfItems.index(values[0])
                    indexOfval2 = restOfItems.index(values[1])
                    indexOfval3 = restOfItems.index(values[2])

                    #print("Index of {} is {}".format(values[0], indexOfval1))
                    #print("Index of {} is {}".format(values[1], indexOfval2))
                    #print("Index of {} is {}".format(values[2], indexOfval3))

                    if indexOfval1 >= indexOfval2 and indexOfval1 >= indexOfval3:
                        furthest = indexOfval1
                    elif indexOfval2 >= indexOfval1 and indexOfval2 >= indexOfval3:
                        furthest = indexOfval2
                    else:   
                        furthest = indexOfval3

                    #print("Removing {} in index {}".format(restOfItems[furthest], furthest))
                    pageframe.pop(restOfItems[furthest], None)
            
                miss += 1
        
        #Create a new item or update the existing one to zero.
        pageframe[items[i]] = 0  
        # Add 1 to all the values
        pageframe.update((k, v + 1) for k, v in pageframe.items())
        # Sort the items by values in ascending order. 
        pageframe = {k: v for k, v in sorted(pageframe.items(), key=lambda x: x[1])}

        print(pageframe)
    
    return miss, len(items) - miss


#Least Recently Used Algorithm
def lru(items, frames):
    print("LRU: \n")

    pageframe = {} # page frames
    miss = 0 # page faults
    
    for item in items:
        if miss < frames:
            if item not in pageframe.keys():
                miss += 1
            
        else:
            if item not in pageframe.keys():
                pageframe.popitem()
                miss += 1

        #Create a new item or update the existing one to zero.
        pageframe[item] = 0  
        # Add 1 to all the values
        pageframe.update((k, v + 1) for k, v in pageframe.items())
        # Sort the items by values in ascending order. 
        pageframe = {k: v for k, v in sorted(pageframe.items(), key=lambda x: x[1])}     
        
        print(pageframe)
    
    return miss, len(items) - miss

#First In, First Out Algorithm
def fifo(items, frames):
    print("FIFO: \n")
    queue = [] # page frame
    miss = 0 # page faults

    for item in items:
        
        if miss < frames:
            if item not in queue:
                queue.append(item)
                miss += 1

        else:
            if item not in queue:
                queue.pop(0)
                queue.append(item)  
                miss += 1
        print(queue)
    return miss, len(items) - miss

def main():

    items = [int(item) for item in input("Enter the list of items: ").split()]
    frames = int(input("Enter number of page frames: "))
    
    print("Page reference string: ", items)
    print("No. of Page Frame:", frames)
    
    if args.func == 'lru':
        hit, miss = lru(items, frames)
        print("Number of miss : {}\nNumber of hits: {}".format(hit, miss))
    elif args.func == 'optimal':
        hit, miss = optimal(items, frames)
        print("Number of miss : {}\nNumber of hits: {}".format(hit, miss))
    else:
        hit, miss = fifo(items, frames)
        print("Number of miss : {}\nNumber of hits: {}".format(hit, miss))

parser = argparse.ArgumentParser("Choose replacement algorithm")
parser.add_argument(
    "-f", "--func",
    type=str,
    default="fifo",
    help="fifo -First In, First Out"+
         "lru - Least Recently Used"+
         "optimal - Yes"
    )
args = parser.parse_args()


if __name__ == "__main__": 
    main()


