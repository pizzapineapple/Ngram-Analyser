from redditFetch import setLoad
import time
import click
import queue
from multiprocessing import Process
from threading import Thread
import threading
import sys
import os


class job :
    def __init__(self, scheduling, timeQued):
        self.scheduling = scheduling
        self.timeQued = timeQued
        

    def startJob(self) :
        self.timeStarted = time.time()

    def logJob(self) :
        pass


class redditJob(job) :
    def __init__(self, timeStarted, subreddit, sorting, size) :
        super().__init__("onetime", time.time())
        self.subreddit = subreddit
        self.sorting = sorting
        self.size = size

    def startJob(self) :
        self.time = time.time()
        setLoad(self.subreddit, self.sorting, self.size)

"""
class instaJob:
class fbJob:
class 4chanJob

Schedule different types of jobs:
    one time parse of subreddit
    regularly scheuled parses :
        different time intervals
    


"""
jobQue = queue.Queue(maxsize=0)

def runner() :
    print("Runner ran")
    jobQue.get().startJob()
    

def cli() :
    breakVar = False

    print("Nalytics Runner")
    
    while True :
        print(thread.is_alive())
        string = input(">").split()  
        print("waited for io")
        
        for each in string :
            if each == "exit" :
                print("bye bye")
                breakVar = True
                sys.exit()
                
            elif each == "addjob" :
                subreddit = input()
                method = input()
                size = input()
                jobQue.put(redditJob(time.time, subreddit, method, size))
                print("Job added")
                
            elif each == "completedjobs" :
                print(
                    "Command List: \r\n " + 
                    "exit: exits"
                )
            
            elif each == "activejobs" :
                pass
                    # "Command List: \r\n " 
                    #qualityList = []
                    # for job in jobQue :
                    #     print(job.source)
                    #     print(job.timeStarted)
                    #     print(job.name)


            elif each == "pausedjobs" :
                print(
                    "Command List: \r\n " + 
                    "exit: exits"
                )

            elif each == "help" :
                print(
                    "Command List: \r\n " + 
                    "exit: exits"
                )

            else :
                print("Command not recognised")
                
        if breakVar == True:
            break


def main() :
    runner()


if __name__ == "__main__" :

    thread = Thread(target=cli, name="CLI")
    thread.start()
    thread.join()
    print(thread.getpid + "cli")
    print(threading.activeThread.getpid() + "runner")
    
    # exitTime = time.time()
    print(time.time())
    while True:

        print(thread.is_alive())
        main()
        # if breakVar == True
        #     break
        # print("wehile True")

    print(thread.ident)

    