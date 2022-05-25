import random

# setup song, difficulty, and creator lists

tempfile = open("songs.txt", encoding="utf-8")
songlistbad = tempfile.readlines()
tempfile2 = open("difficulties.txt", encoding="utf-8")
difficultylistbad = tempfile2.readlines()
tempfile3 = open("creators.txt", encoding = "utf-8")
creatorlistbad = tempfile3.readlines()

songlist = []
difficultylist = []
creatorlist = []

for a in songlistbad:
    songlist.append(a.strip())
for a in difficultylistbad:
    difficultylist.append(a.strip())
for a in creatorlistbad:
    creatorlist.append(a.strip())

# variable stuff

print("type 'balls' to give up, type your percentage to continue")

response = 0
oldpercent = 0
score = 0

#initial loop

rng = random.randint(1,332)
print(songlist[rng] + " - " + creatorlist[rng] + " - " + difficultylist[rng] + " - Goal: 1%")
print("")
while True:
    response = input("")
    try:
        int(response)
    except ValueError:
        continue
    break
response = int(response)
oldpercent = response
print("")

#real loop

while response < 100:
    rng = random.randint(1,332)
    print(songlist[rng] + " - " + creatorlist[rng] + " - " + difficultylist[rng] + " - Goal: " + str(response + 1) + "%")
    print("")
    print(oldpercent)
    while True:
        response = input("")
        if response == "balls":
            exit()
        try:
            int(response)
        except ValueError:
            continue
        if int(response) <= (oldpercent):
            continue
        response = int(response)
        break
    print("")
    oldpercent = response
    score += 1

print("s+")
print("good job!")
print("score: " + str(score) + " / 100")

input()
