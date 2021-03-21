import argparse
from argparse import RawTextHelpFormatter

def totalheadmovement(items):
    print(items)
    thm = 0
    for i, k in zip(items[0:], items[1:]):
        print("from {} to {} = {}".format(i, k, abs(i - k))) 
        thm += abs(i - k)
    return thm


def fcfs(current, items):
    print("First-come, First-served Scheduling")
    return totalheadmovement(items)


def sstf(current, items):
    print("Short Seek Time First Scheduling")

    dct = dict(zip(iter(items),iter([0]*(len(items)))))
    
    for k in dct.keys():
        dct[k] = abs(k - current)
    
    dct = {k: v for k, v in sorted(dct.items(), key=lambda x: x[1])} 
    return totalheadmovement([*dct.keys()])


def scan(current, items):
    print("Scan Disk Scheduling")
    arglist = sorted(items[:])

    if arglist.index(current) < len(arglist) - 1:
        arglist.insert(0,0)
        
    idx = arglist.index(current)
    if idx > 0:
        return totalheadmovement(arglist[idx:None:-1] + arglist[idx+1:])
    else:
        return totalheadmovement(arglist)
    


def cscan(current, items):
    print("C-Scan Disk Scheduling")
    arglist = sorted(items[:])

    if arglist.index(current) > 0: #if current tracking index is not equal to zero, we have to include the beginning track and ending track.
        arglist.insert(0,0)
        arglist.append(total - 1)
        
    idx = arglist.index(current)
    if idx > 0:
        return totalheadmovement(arglist[idx:] + arglist[:idx])
    else:
        return totalheadmovement(arglist)

def look(current, items):
    print("Look Disk Scheduling")
    arglist = sorted(items[:])
    idx = arglist.index(current) 
    if idx > 0:
        return totalheadmovement(arglist[idx:] + arglist[idx-1:None:-1])
    else:
        return totalheadmovement(arglist)
    


def clook(current, items):
    print("C-Look Disk Scheduling")
    arglist = sorted(items[:])
    idx = arglist.index(current) 
    if idx > 0:
        return totalheadmovement(arglist[idx:] + arglist[:idx]) #transform list to update track movement for computation.
    else:
        return totalheadmovement(arglist)
    


def main():
    global total
    total = int(input("Enter total tracks: "))
    current = int(input("Enter currently tracked item: "))
    
    if args.values:
        items = [int(item) for item in args.values]
    else:
        items = [int(item) for item in input("Enter the rest of the items: ").split()]
    
    items.insert(0, current)

    if args.func == 'sstf':
        thm = sstf(current, items)

    elif args.func == 'look':
        thm = look(current, items)
    
    elif args.func == 'clook':
        thm = clook(current, items)
    
    elif args.func == 'scan':
        thm = scan(current, items)
    
    elif args.func == 'cscan':
        thm = cscan(current, items)
    
    else:
        thm = fcfs(current, items)

    print("Total Head Movement = {} tracks".format(thm))


parser = argparse.ArgumentParser(
            prog="diskscheduler",
            description="Choose disk scheduling algorithm",
            formatter_class=RawTextHelpFormatter
        )


parser.add_argument(
    "-f", "--func",
    type=str,
    default="fcfs",
    help="\n\n\"fcfs\" - First-come, First-served\n"+
         "\"sstf\" - Shortest Seek Time First\n"+
         "\"scan\" - Elevator Algorithm\n" +
         "\"cscan\" - Circular SCAN\n" +
         "\"look\" - Vanilla Look Scheduling\n" +
         "\"clook\"- Circular Look Scheduling\n")

parser.add_argument(
    "-v", "--values",
    nargs="+",
    help="input a list of values. e.g. 1 2 3 4 5 6"
)

args = parser.parse_args()

if __name__ == "__main__": 
    main()
