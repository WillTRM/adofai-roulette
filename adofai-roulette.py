import random

# setup song, difficulty, and creator lists

def readLinesAndStrip(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]


songs = readLinesAndStrip("songs.txt")
difficulties = readLinesAndStrip("difficulties.txt")
creators = readLinesAndStrip("creators.txt")

# variable stuff

print("type 'balls' to give up, type your percentage to continue")

percent = 0
score = 0

while percent < 100:
    rng = random.randrange(len(songs))
    print(f"{songs[rng]} - {creators[rng]} - {difficulties[rng]} - Goal: {percent + 1}%")
    print()

    while True:
        response = input("")

        if response == "balls":
            exit()
        try:
            parsed_response = int(response)
        except ValueError:
            continue
        if parsed_response <= percent:
            continue

        percent = parsed_response
        break

    print()
    score += 1
    del songs[rng]

print("s+")
print("good job!")
print(f"score: {score} / 100")

input("Press enter to continue...")
