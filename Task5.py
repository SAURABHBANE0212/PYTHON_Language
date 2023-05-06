import functools
import schedule
import time
from sys import *

def Script_Task(No):
    if(No%2==0):
        print("It is Even")
    else:
        print("It is Odd")

def main():
    print("------------Automation---------")

    print("Automation Scrpt started With name ",argv[0])

    if(len(argv)!=2):
        print("Error : Insufficient Argument")
        print("Use -h for Help and -u for usage of the script")
        exit()

    if(argv[1]=="-h"):
        print("Help : Script is Used To perform ---------")
        exit()

    elif(argv[1]=="-u"):
        print("Usage : provide ___ Number o Argument as")
        print("First Argument As _____")
        print("Second Argument As _____")
        exit()

    else:
        schedule.every().day.at("10:19").do(Script_Task, int(argv[1]))

        while (True):
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()