import argparse
from argparse import RawTextHelpFormatter

global queue = []


@dataclass




def fcfs():

    return
def main():
    numberOfProcess = int(input("Enter number of process(es): "))
    
    
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