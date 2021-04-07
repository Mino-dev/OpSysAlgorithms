import argparse
from argparse import RawTextHelpFormatter
from dataclasses import dataclass

queue = []

def computeNonPreemptive(n, prio = False):

    global queue
    
    time = total_turn = total_wait = 0

    temp = [queue.pop(0)]
    res = []
    
    while len(res) != n:
        temp[0]._burst -= 1
        time += 1
        if len(queue) > 0:
            temp.append(queue.pop(0))

        if temp[0]._burst <= 0:
            
            temp[0].isCompleted = True
            temp[0].completion = time
            temp[0].turnaround = abs(temp[0].completion - temp[0].arrival)               
            temp[0].waiting = abs(temp[0].turnaround - temp[0].burst)
            temp[0].isCompleted = True
            
            total_wait += temp[0].waiting
            total_turn += temp[0].turnaround
            res.append(temp.pop(0))
            
            if prio:
                temp = sorted(temp, key=lambda l: l.priority)
            else:
                temp = sorted(temp, key=lambda l: l.burst)
            

    
    queue = res
    return total_wait, total_turn

def fcfs(n):

    queue[0].completion = queue[0].burst + queue[0].arrival

    total_turn = queue[0].turnaround = abs(queue[0].completion - queue[0].arrival)

    total_wait = queue[0].waiting = abs(queue[0].turnaround - queue[0].burst)

    queue[0].isCompleted = True
    queue[0]._burst = 0
    for i in range(1, n):

        queue[i].completion = queue[i - 1].completion + queue[i].burst
        queue[i].turnaround = abs(queue[i].completion - queue[i].arrival)
        queue[i].waiting = abs(queue[i].turnaround - queue[i].burst)

        total_wait += queue[i].waiting
        total_turn += queue[i].turnaround

        queue[i].isCompleted = True
        queue[i]._burst = 0
    
    return total_wait, total_turn


def main():

    global queue
    numberOfProcess = int(input("Enter number of process(es): "))
    
    for i in range(numberOfProcess):
        arrival = int(input("Enter the arrival time: "))
        burst = int(input("Enter the burst time: "))

        process = Process(i, arrival, burst, _burst=burst)
        if args.func == "prio" or args.func == "nprio":
            process.priority = int(input("Enter the priority: "))

        queue.append(process)

    #sort by arrival
    queue = sorted(queue, key=lambda l: l.arrival)

    if args.func == "sjf":
        wait, turn = computeNonPreemptive(numberOfProcess)
    elif args.func == "nprio":
        wait, turn = computeNonPreemptive(numberOfProcess, True)
    else:
        wait, turn = fcfs(numberOfProcess)
    
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(numberOfProcess):
        print(f"{queue[i].P}\t\t{queue[i].arrival}\t\t{queue[i].burst}\t\t{queue[i].waiting}\t\t{queue[i].turnaround}")

    print("Average Waiting Time: {:.2f} ms".format(wait / numberOfProcess))
    print("Average Turnaround Time: {:.2f} ms".format(turn / numberOfProcess))
@dataclass
class Process:
    P: int
    arrival: int
    burst: int
    priority: int = 0
    completion: int = 0
    waiting: int = 0
    turnaround: int = 0
    isCompleted: bool = False
    _burst: int = 0
    
parser = argparse.ArgumentParser(
            prog="cpu process scheduler",
            description="Choose cpu scheduling algorithm",
            formatter_class=RawTextHelpFormatter
        )


parser.add_argument(
    "-f", "--func",
    type=str,
    default="fcfs",
    help="\n\n\"fcfs\" - First-come, First-served\n"+
         "\"sjf\" - Shortest Job First\n"+
         "\"nprio\" - Non Preemptive Priority\n" +
         "\"srtf\" - Shortest Remaining Time First\n" +
         "\"pprio\" - Preemptive Priority\n" +
         "\"rr\"- Round Robin\n")
args = parser.parse_args()

if __name__ == "__main__": 
    main()