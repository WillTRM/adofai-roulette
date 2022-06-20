import random
import PySimpleGUI as sg

# set up song, difficulty, and creator lists

def readLinesAndStrip(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

songs = readLinesAndStrip("songs.txt")
difficulties = readLinesAndStrip("difficulties.txt")
creators = readLinesAndStrip("creators.txt")

# wow variables

percent = 0
score = 0
rng = random.randrange(len(songs))

# set up layout

layout = [
    [sg.Text(f"{songs[rng]} - {creators[rng]} - {difficulties[rng]}", key = "levelDisp")],
    [sg.Text(f"Goal: {percent + 1}%", key = "percentDisp")],
    [sg.Text("Enter percent as number:"), sg.InputText(size = (5, 1))],
    [sg.Button("Submit")]
]

window = sg.Window("ADOFAI Roulette", layout)

percent = 0
score = 0

# code loop

while True:
    event, values = window.read()

    if event == "Submit":
        try:
            parsed_response = int(values[0])
        except ValueError:
            continue
        if parsed_response <= percent:
            continue

        percent = parsed_response
        if percent == 100:
            break

    score += 1
    rng = random.randrange(len(songs))
    window["levelDisp"].update(f"{songs[rng]} - {creators[rng]} - {difficulties[rng]}")
    window["percentDisp"].update(f"Goal: {percent}%")
    del songs[rng]

    if event == sg.WIN_CLOSED:
        break

window.close()
