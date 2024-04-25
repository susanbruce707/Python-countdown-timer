# some timer counting thing writen in python 3X.
import time
# integer input function
def int_input(text):
    try:
        x = int(input(text))
    except ValueError:
        print("Only integers as input please")
        x = 0
        x = int_input(text)
    return x
def ent_hms():
    try:
        hours = int_input("Enter hours>")
        minutes = int_input("Enter minutes>")
        seconds = int_input("Enter seconds>")
    except ValueError:
        hours, minutes, seconds = 0
    return hours, minutes, seconds
q = ""
while q != "Y":
    hours, minutes, seconds = ent_hms()
    print("Hours =", hours, "Minutes =", minutes, "Seconds =", seconds)
    q = input("Is this correct y or n?").upper()
print("Timer =", hours, "Hours", minutes, "Minutes", seconds, "Seconds")
total_timer = (hours * 3600) + (minutes * 60) + seconds
t = total_timer
print("total timer time in seconds is ", total_timer)
for h in range(60):
    if total_timer == 0:
        break
    for m in range(60):
        if total_timer == 0:
            break
        for s in range(60):
            if s == 0 and total_timer == t:
                u = input("Press Return to start timer")
                s = 1
                continue
            time.sleep(1)
            print(h, "Hours ", m, "Minutes ", s, "Seconds ")
            total_timer -= 1
            if total_timer == 0:
                print("Timer time up")
                break
