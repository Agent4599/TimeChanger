#DO NOT EDIT ANY CODE IS YOU DON"T KNOW WHAT YOUR DOING!!!

import os
import time
import pyautogui
import urllib.request

local_version = "1.1"


def check_for_updates():
    try:
        # Replace this with the raw link of your version.txt file on GitHub
        server_version_url = "https://raw.githubusercontent.com/Agent4599/TimeChanger/main/Server%20Version.txt"
        with urllib.request.urlopen(server_version_url) as response:
            server_version = response.read().decode('utf-8').strip()
            if local_version < server_version:
                return True
    except Exception as e:
        print(f"Error checking for updates: {e}")
    return False

def download_update():
    try:
        # Replace this with the raw link of your updated script on GitHub
        script_url = "https://raw.githubusercontent.com/Agent4599/TimeChanger/main/Time_Changer.py"
        with urllib.request.urlopen(script_url) as response:
            updated_script = response.read().decode('utf-8')
            with open("Time_Changer.py", 'w') as script_file:
                script_file.write(updated_script)
        print("Update successful. Please restart the script.")
    except Exception as e:
        print(f"Error downloading update: {e}")

# Check for updates and download if available
if check_for_updates():
    print("An update is available. Downloading...")
    download_update()
else:
    print("Your script is up to date.")

# Check for updates and download if available
if check_for_updates():
    print("An update is available. Downloading...")
    download_update()

def Hour_to_Min():
    while True:
        os.system('cls')
        print("Hour to Minutes Converter")
        Minutes = int(input("Enter the number of Hour ->"))
        Seconds = int(input("Enter the number of Minutes (Enter zero if none) ->"))

        # Converts min into sec and adds the seconds provided by the user.
        Final_Second = Minutes * 60 + Seconds

        # prints the Final_Second After converting it into int and adding seconds in the end.
        print(str(Final_Second) + " Minutes")

        # Made this abomination of code since the cmd prompt closes after printing the last code.
        while True:
            user_input = input("Do you want to repeat? (type 'yes' to run again, type 'no' to quit): ")

            if user_input.lower() == 'no':
                exit()
            elif user_input.lower() == 'yes':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")
        while True:
            os.system('cls')
            nd = input("Do you want to switch Mode?")
            if nd == 'yes':
                main()
            elif nd == 'no':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

def Hour_to_Sec():
    while True:
        os.system('cls')
        print("Hour to Seconds Converter")
        Minutes = int(input("Enter the number of Hour ->"))
        Seconds = int(input("Enter the number of Seconds (Enter zero if none) ->"))

        # Converts min into sec and adds the seconds provided by the user.
        Final_Second = Minutes * 3600 + Seconds

        # prints the Final_Second After converting it into int and adding seconds in the end.
        print(str(Final_Second) + " Seconds")

        # Made this abomination of code since the cmd prompt closes after printing the last code.
        while True:
            user_input = input("Do you want to repeat? (type 'yes' to run again, type 'no' to quit): ")

            if user_input.lower() == 'no':
                exit()
            elif user_input.lower() == 'yes':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

        while True:
            os.system('cls')
            nd = input("Do you want to switch Mode?")
            if nd == 'yes':
                main()
            elif nd == 'no':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

def Min_to_Hour():
    while True:
        os.system('cls')
        print("Minutes to Hour Converter")
        Minutes = int(input("Enter the number of minutes ->"))
        Hour = int(input("Enter the number of Hours (Enter zero if none) ->"))

        # Converts min into sec and adds the seconds provided by the user.
        Final_Hour = Minutes / 60 + Hour

        # prints the Final_Second After converting it into int and adding seconds in the end.
        print(str(Final_Hour) + " Hours")

        # Made this abomination of code since the cmd prompt closes after printing the last code.
        while True:
            user_input = input("Do you want to repeat? (type 'yes' to run again, type 'no' to quit): ")

            if user_input.lower() == 'no':
                exit()
            elif user_input.lower() == 'yes':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")
        while True:
            os.system('cls')
            nd = input("Do you want to switch Mode?")
            if nd == 'yes':
                main()
            elif nd == 'no':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

def Min_to_Sec():
    os.system('cls')
    while True:
        print("Minutes to Second Converter")
        Minutes = int(input("Enter the number of minutes ->"))
        Seconds = int(input("Enter the number of Seconds (Enter zero if none) ->"))

        # Converts min into sec and adds the seconds provided by the user.
        Final_Second = Minutes * 60 + Seconds

        # prints the Final_Second After converting it into int and adding seconds in the end.
        print(str(Final_Second) + " Seconds")

        # Made this abomination of code since the cmd prompt closes after printing the last code.
        while True:
            user_input = input("Do you want to repeat? (type 'yes' to run again, type 'no' to quit): ")

            if user_input.lower() == 'no':
                exit()
            elif user_input.lower() == 'yes':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

        while True:
            os.system('cls')
            nd = input("Do you want to switch Mode?")
            if nd == 'yes':
                main()
            elif nd == 'no':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

def Sec_to_Hour():
    os.system('cls')
    while True:
        print("Seconds to Hours Converter")
        Minutes = int(input("Enter the number of Seconds ->"))
        Seconds = int(input("Enter the number of Hours (Enter zero if none) ->"))

        # Converts min into sec and adds the seconds provided by the user.
        Final_Second = Minutes / 3600 + Seconds

        # prints the Final_Second After converting it into int and adding seconds in the end.
        print(str(Final_Second) + " Hours")

        # Made this abomination of code since the cmd prompt closes after printing the last code.
        while True:
            user_input = input("Do you want to repeat? (type 'yes' to run again, type 'no' to quit): ")

            if user_input.lower() == 'no':
                exit()
            elif user_input.lower() == 'yes':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

        while True:
            os.system('cls')
            nd = input("Do you want to switch Mode?")
            if nd == 'yes':
                main()
            elif nd == 'no':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

def Sec_to_Min():
    while True:
        os.system('cls')
        print("Seconds to Minutes Converter")
        Minutes = int(input("Enter the number of Seconds ->"))
        Seconds = int(input("Enter the number of Minutes (Enter zero if none) ->"))

        # Converts min into sec and adds the seconds provided by the user.
        Final_Second = Minutes / 60 + Seconds

        # prints the Final_Second After converting it into int and adding seconds in the end.
        print(str(Final_Second) + " Minutes")

        # Made this abomination of code since the cmd prompt closes after printing the last code.
        while True:
            user_input = input("Do you want to repeat? (type 'yes' to run again, type 'no' to quit): ")

            if user_input.lower() == 'no':
                exit()
            elif user_input.lower() == 'yes':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

        while True:
            os.system('cls')
            nd = input("Do you want to switch Mode?")
            if nd == 'yes':
                main()
            elif nd == 'no':
                break
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

#--IGNORE THIS--

# def start_cmd(max_executions, text_to_type):
#     execution_count = 0

#     while execution_count < max_executions:
#         os.system("start cmd")
#         print("CMD started")
#         execution_count += 1
        

#         # Allow some time for the new CMD window to open
#         time.sleep(1)

#         # Type the specified text
#         pyautogui.typewrite(text_to_type)
#         pyautogui.press('enter')

#--IGNORE THIS--


def main():
        time.sleep(1)
        print("Connecting to the main servers...")
        time.sleep(2)
        print("Successful Connected.")
        time.sleep(1)
        print("Authorizing...")
        time.sleep(2)
        print("Authorizition Completed.")
        time.sleep(1)
        print("Changing Time...")
        time.sleep(2)
        
        while True:
            os.system('cls')
            print("Welcome To Time Changer v2.0 By Aditya Rana " + "\nType 1 For Hours to Minutes" + "\nType 2 For Hours to Sec" + "\nType 3 For Minutes to Hours" + "\nType 4 For Minutes to Seconds" + "\nType 5 For Seconds to Hours" + "\nType 6 For Seconds to Minutes" + "\nType Exit To Exit")
            getinput = input()

            if getinput == '1':
                Hour_to_Min()
            elif getinput == '2':
                Hour_to_Sec()
            elif getinput == '3':
                Min_to_Hour()
            elif getinput == '4':
                Min_to_Sec()
            elif getinput == '5':
                Sec_to_Hour()
            elif getinput == '6':
                Sec_to_Min()
            elif getinput.lower() == 'exit':
                exit()
            else:
                print("Error: Invalid input.")

main()
