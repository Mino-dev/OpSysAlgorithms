import argparse
from argparse import RawTextHelpFormatter
from dataclasses import dataclass

queue = []

def sjf(n):

    global queue
    

    queue[0].completion = queue[0].arrival + queue[0].burst
    total_turn = queue[0].turnaround = abs(queue[0].completion - queue[0].arrival)
    total_wait = queue[0].waiting = abs(queue[0].turnaround - queue[0].burst)
    
    queue[0].isCompleted = True
    queue[0]._burst = 0

    for i in range(1, n):
        low = queue[i].burst
        for j in range(1, n):
            if not queue[j].isCompleted and queue[i - 1].completion >= queue[j].arrival and low >= queue[j].burst: # do
                low = queue[j].burst
                idx = j

        #print(queue[idx])
        queue[idx].completion = queue[i - 1].completion + queue[idx].burst
        queue[idx].turnaround = abs(queue[idx].completion - queue[idx].arrival)
        queue[idx].waiting = abs(queue[idx].turnaround - queue[idx].burst)

        total_wait += queue[idx].waiting
        total_turn += queue[idx].turnaround

        queue[idx].isCompleted = True
        queue[idx]._burst = 0
        
            

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
        wait, turn = sjf(numberOfProcess)
    else:
        wait, turn = fcfs(numberOfProcess)
    
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(numberOfProcess):
        print(f"{queue[i].P}\t\t{queue[i].arrival}\t\t{queue[i].burst}\t\t{queue[i].waiting}\t\t{queue[i].turnaround}")

    print(f"Average Waiting Time: {wait / numberOfProcess} ms")
    print(f"Average Turnaround Time: {turn / numberOfProcess} ms")
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