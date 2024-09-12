#!/usr/bin/env python3

import subprocess
import time

choice = "n"

try:
    lvl=input("Enter the lvl no.: ")
    ssh_cmd=f"ssh bandit{lvl}@bandit.labs.overthewire.org -p 2220"
    choice=input(f"Are you sure  you want to login as: bandit{lvl}?\nY : to runthe following command ... \n{ssh_cmd}\nN : to start over ... \n\n(Y/n): ")

    if choice.lower() == "y":
        print(f"Running the following command\n{ssh_cmd}")
        subprocess.run(ssh_cmd, shell=True)
    elif choice.lower() == "n":
        choice2=input("Do you whish to continue? (Y/n): ")
        if choice2.lower() == "y":
            lvl=input("Enter the lvl no. : ")
            ssh_cmd=f"ssh bandit{lvl}@bandit.labs.overthewire.org -p 2220"
            choice=input(f"Are you sure  you want to login as: bandit{lvl}?\nY : to runthe following command ... \n{ssh_cmd}\nN : to start over ... \n\n(Y/n): ")
            if choice.lower() == "y":
                print(f"Running the following command\n{ssh_cmd}")
                subprocess.run(ssh_cmd, shell=True)
            else:
                print("Invalid input, please try again.")
                print("Exiting ... ")
                time.sleep(1)

        else:
            print("Invalid input, please try again.")
            print("Exiting ... ")
            time.sleep(1)
    else:
        print("Invalid input, please try again.")
        print("Exiting ... ")
        time.sleep(1)
except KeyboardInterrupt:
    print("Execution interrupted by user.\nExitting ...")
