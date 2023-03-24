import json
import random
import requests
import time as t
import numpy as np
import PySimpleGUI as sg
from tkinter import filedialog

#what the fuck does this do
#i stole it off stack overflow
#HEY IT WORKS!

class npEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.int32):
            return int(obj)
        return json.JSONEncoder.default(self, obj)

#import save file selection

def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, "r")
    temp = json.load(file)
    return temp["levelList"], temp["score"], temp["progress"]

#ok so uhhhhh
#1. set rng to max song id or something idk what i'm doing

def song_count():
    high = requests.get("https://be.t21c-adofai.kro.kr/levels?limit=1&random=false&seed=621").json()
    return high["results"][0]["id"]

def request_song(song_id):
    song_data = json.loads(requests.get(f"https://be.t21c-adofai.kro.kr/levels/{song_id}").text)
    return song_data

# wow variables

percent = 0
score = 0
rng = random.sample(range(1, song_count()), 100)
song_data = request_song(rng[percent])

# set up layout

layout = [
    [sg.Text(f"Level: {song_data['song']}", key = "levelDisp")],
    [sg.Text(f"Artist: {song_data['artist']}", key = "artistDisp")],
    [sg.Text(f"Difficulty: {song_data['diff']}", key = "diffDisp")],
    [sg.Text(f"Charter: {song_data['creator']}", key = "charterDisp")],
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
        sd = open("adofai_roulette_save.json", "w+")
        json.dump(dtw, sd, indent = 4, cls = npEncoder)
        sd.close()

    elif event == "importSave":
        rng, score, percent = openFile()

    song_data = request_song(rng[percent])
    
    window["levelDisp"].update(f"Level: {song_data['song']}")
    window["artistDisp"].update(f"Artist: {song_data['artist']}")
    window["diffDisp"].update(f"Difficulty: {song_data['diff']}")
    window["charterDisp"].update(f"Charter: {song_data['creator']}")
    window["percentDisp"].update(f"Goal: {percent + 1}%")
        
window.close()
