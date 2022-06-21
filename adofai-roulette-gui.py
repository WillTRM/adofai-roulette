import random
import time as t
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
    [sg.Button("Submit", key = "submitButton"), sg.Button("Give Up")]
]

window = sg.Window("ADOFAI Roulette", layout)

percent = 0
score = 0

# code loop

while True:
    event, values = window.read()

    if event == "submitButton":
        try:
            parsed_response = int(values[0])
        except ValueError:
            continue
        if parsed_response <= percent:
            continue

        percent = parsed_response
        if percent == 100:
            break
        
    elif event == "Give Up":
        window["levelDisp"].update(f"Your score: {score}")
        window["percentDisp"].hide_row()
        window[0].hide_row()
        window["submitButton"].hide_row()
        window.read()
        
    elif event == sg.WIN_CLOSED:
        break
    
    score += 1
    rng = random.randrange(len(songs))
    window["levelDisp"].update(f"{songs[rng]} - {creators[rng]} - {difficulties[rng]}")
    window["percentDisp"].update(f"Goal: {percent + 1}%")
    del songs[rng]
        
window.close()
