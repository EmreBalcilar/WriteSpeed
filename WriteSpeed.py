import time
import datetime
import random

Bold = '\033[1m' # to make the font of the post bold
End = '\033[0m' # End the Color or bold
RED = '\033[91m' # to make the color of the post Red


rand = random.randint(1, 5)


print("Write the Text Below After 3 Seconds")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("GO")
if (rand == 1):
    print(Bold+"The book is in front of the table.Wisdom is easily acquired when hiding under the bed with a saucepan on your head"+End)

if (rand == 2):
    print(Bold+"The lyrics of the song sounded like fingernails on a chalkboard.His son quipped that power bars were nothing more than adult candy bars."+End)

if (rand == 3):
    print(Bold+"The tears of a clown make my lipstick run, but my shower cap is still intact.Her life in the confines of the house became her new normal."+End)

if (rand == 4):
    print(Bold+"You bite up because of your lower jaw.There were three sphered rocks congregating in a cubed room."+End)

if (rand == 5):
    print(Bold+"Nobody has encountered an explosive daisy and lived to tell the tale.The sky is clear; the stars are twinkling."+End)


time.sleep(0.02) # stop the seconds variable
before = datetime.datetime.now() # takes the current time and adds it to the before variable

text = input(RED+"Type Here...."+End)
after = datetime.datetime.now() # takes the time of the now and adds it to the after variable

speed = after - before # subtract before and after to find speed

seconds = round(speed.total_seconds(), 2) # convert our time to seconds with the total_seconds () function.
                                          # round our values ​​with the # round function. Second in parenthesis
                                          # shows value after point as much as value..
letter_per_second = round(len(text) / seconds,1) # To find the number of words per second find the length of the text and divide it by the second.

print(RED+"You typed in : {} seconds.".format(seconds))
print("{} letters per second.".format(letter_per_second))