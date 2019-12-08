import os
import time
import requests

print("""
    _________________________________________________
    |                                               |
    |             Fix INTERNET V.1.0                |
    |                                               |
    |          - Press "s" to start                 |
    |          - Press "q" to exit                  |
    |                                               |
    _________________________________________________
""")
st = input("Enter operation: ").lower()
if st == "q":
    exit(0)
elif st == "s":
    try:
        chc = requests.get("https://www.google.com", timeout=5)
        print("Your internet connection is on")
    except requests.ConnectionError:
        print("Starting internet fixer...")
        time.sleep(0.5)
        os.system("netsh int ip reset")
        os.system("netsh winsock reset")
        os.system("netsh winhttp reset proxy")
        os.system("ipconfig/flushdns")
        os.system("ipconfig/release")
        os.system("ipconfig/renew")
    try:
        chc = requests.get("https://www.google.com", timeout=5)
        print("Your internet connection is on")
    except requests.ConnectionError:
        print("\nPlease reset your network.\nPlease wait, opening network settings.When it open please go to Network Reset and reset your network")
        print("If you already did this step you should call your isp.")
        time.sleep(3)
        os.system("start ms-settings:network-status")
else:
    print("Invalid input!")
