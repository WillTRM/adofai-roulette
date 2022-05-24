import random

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

print("type 'balls' to give up, type your percentage to continue")

response = 0
score = 0

while response < 100:
    rng = random.randint(1,332)
    print(songlist[rng] + " - " + creatorlist[rng] + " - " + difficultylist[rng] + " - Goal: " + str(response + 1) + "%")
    print("")
    response = int(input(""))
    if response == "balls":
        exit()
    print("")
    score += 1

print("s+")
print("good job!")
print("score: " + str(score )+ " / 100")

input()
