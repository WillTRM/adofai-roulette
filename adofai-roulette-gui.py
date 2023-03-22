import json
import random
import time as t
import numpy as np
import PySimpleGUI as sg
from tkinter import filedialog

# set up song, difficulty, and creator lists

def readLinesAndStrip(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

#what the fuck does this do
#i stole it off stack overflow
#HEY IT WORKS!

class npEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.int32):
            return int(obj)
        return json.JSONEncoder.default(self, obj)

def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, "r")
    temp = json.load(file)
    return temp["levelList"], temp["score"], temp["progress"]

songs = readLinesAndStrip("songs.txt")
difficulties = readLinesAndStrip("difficulties.txt")
creators = readLinesAndStrip("creators.txt")
artists = readLinesAndStrip("artists.txt")

# wow variables

percent = 0
score = 0
rng = list(np.random.permutation(np.arange(len(songs) + 1))[:100])

# set up layout

layout = [
    [sg.Text(f"Level: {songs[rng[percent]]}", key = "levelDisp")],
    [sg.Text(f"Artist: {artists[rng[percent]]}", key = "artistDisp")],
    [sg.Text(f"Difficulty: {difficulties[rng[percent]]}", key = "diffDisp")],
    [sg.Text(f"Charter: {creators[rng[percent]]}", key = "charterDisp")],
    [sg.Text(f"Goal: {percent + 1}%", key = "percentDisp")],
    [sg.Text("Enter percent as number:"), sg.InputText(size = (5, 1))],
    [sg.Button("Submit", key = "submitButton"), sg.Button("Give Up")],
    [sg.Button("Export", key = "exportSave"), sg.Button("Import", key = "importSave")]
]

window = sg.Window("ADOFAI Roulette", layout)

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
            score += 1
        except ValueError:
            continue

        percent = parsed_response
        if percent == 100:
            window["levelDisp"].update(f"Congrats! Your score was {score}!")
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

    elif event == "exportSave":
        dtw = {
            "levelList": rng,
            "progress": percent,
            "score": score
        }
        print(dtw)
        sd = open("adofai_roulette_save.json", "w+")
        json.dump(dtw, sd, indent = 4, cls = npEncoder)
        sd.close()

    elif event == "importSave":
        rng, score, percent = openFile()
    
    window["levelDisp"].update(f"Level: {songs[rng[percent]]}")
    window["artistDisp"].update(f"Artist: {artists[rng[percent]]}")
    window["diffDisp"].update(f"Difficulty: {difficulties[rng[percent]]}")
    window["charterDisp"].update(f"Charter: {creators[rng[percent]]}")
    window["percentDisp"].update(f"Goal: {percent + 1}%")
        
window.close()
