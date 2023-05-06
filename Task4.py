import time
import schedule
import datetime

def fun_Minute():
    print("Current Time is : ")
    print(datetime.datetime.now())
    print("scheduler executed after minute")

def fun_Hour():
    print("Current Time Is : ")
    print(datetime.datetime.now())
    print("Scheduler Executed After Hour")

def fun_Day():
    print("Current Time is : ")
    print(datetime.datetime.now())
    print("Scheduler Executed After Day")

def fun_Afternoon():
     print("Current Time is :")
     print(datetime.datetime.now())
     print("Scheduler Executed At 12")

def main():
    print("Python AUTOMATION")
    print("Python Job Scheduler")
    print(datetime.datetime.now())

    schedule.every(1).minutes.do(fun_Minute)
    schedule.every().hour.do(fun_Hour)
    schedule.every().day.at("00:00").do(fun_Afternoon)
    schedule.every().sunday.do(fun_Day)
    schedule.every().friday.at("18:00").do(fun_Day)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()