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
artists = readLinesAndStrip("artists.txt")

# wow variables

percent = 0
score = 0
rng = random.randrange(len(songs))

# set up layout

layout = [
    [sg.Text(f"Level: {songs[rng]}", key = "levelDisp")],
    [sg.Text(f"Artist: {artists[rng]}", key = "artistDisp")],
    [sg.Text(f"Difficulty: {difficulties[rng]}", key = "diffDisp")],
    [sg.Text(f"Charter: {creators[rng]}", key = "charterDisp")],
    [sg.Text(f"Goal: {percent + 1}%", key = "percentDisp")],
    [sg.Text("Enter percent as number:"), sg.InputText(size = (5, 1))],
    [sg.Button("Submit", key = "submitButton"), sg.Button("Give Up")]
]

window = sg.Window("ADOFAI Roulette", layout)

percent = 0
score = 0

def hide_stuff_i_guess_surely_theres_a_better_way_to_do_this():
    window["artistDisp"].hide_row()
    window["diffDisp"].hide_row()
    window["charterDisp"].hide_row()
    window["percentDisp"].hide_row()
    window[0].hide_row()
    window["submitButton"].hide_row()
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
            window["levelDisp"].update(f"Congrats! Your score was {score + 1}!")
            hide_stuff_i_guess_surely_theres_a_better_way_to_do_this()
            window.read()
        
    elif event == "Give Up":
        window["levelDisp"].update(f"You failed. Your score was {score}")
        window["artistDisp"].hide_row()
        window["diffDisp"].hide_row()
        window["charterDisp"].hide_row()
        window["percentDisp"].hide_row()
        window[0].hide_row()
        window["submitButton"].hide_row()
        window.read()
        
    elif event == sg.WIN_CLOSED:
        break
    
    score += 1
    rng = random.randrange(len(songs))
    window["levelDisp"].update(f"Level: {songs[rng]}")
    window["artistDisp"].update(f"Artist: {artists[rng]}")
    window["diffDisp"].update(f"Difficulty: {difficulties[rng]}")
    window["charterDisp"].update(f"Charter: {creators[rng]}")
    window["percentDisp"].update(f"Goal: {percent + 1}%")
    del songs[rng]
        
window.close()
