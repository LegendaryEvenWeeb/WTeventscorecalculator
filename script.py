import json, os, sys, re
import tkinter as tk
import tkinter.font as tkFont
from tktooltip import ToolTip

if os.path.splitext(sys.argv[0])[1].lower() != ".exe":
    print("not an .exe")
    current_dir = os.path.dirname(os.path.abspath(__file__))
else:
    current_dir = os.path.dirname(os.path.abspath(sys.executable))
os.chdir(current_dir)

score_list = []
time_list = []

def font_size(size:int):
    return tkFont.Font(size=size)

def open_score_based_window():
    tk.Label(root, text="Select your rank you will play").grid(row=1,column=3)
    rankinput = tk.Spinbox(root, from_=1, to=8)
    ToolTip(rankinput, msg="Only goes in a range from 1 to 8")
    tk.Label(root, text="How much score is required?").grid(row=3,column=3)
    scoreinput = tk.Entry(root)
    with open("modifiers.json", "r") as file:
        modifiers = json.load(file)
        modifiers = modifiers["scorebased"]
    mode_var = tk.StringVar(value="hidden")
    submode_var = tk.StringVar(value="hidden")  
    tk.Label(root, text="Select the gamemode").grid(row=1,column=0)
    tk.Radiobutton(root, text="Ground", variable=mode_var, value="ground").grid(row=2, column=0)
    tk.Radiobutton(root, text="Air", variable=mode_var, value="air").grid(row=3, column=0)
    tk.Radiobutton(root, text="Naval", variable=mode_var, value="naval").grid(row=4, column=0)
    tk.Label(root, text="Select the sub-mode").grid(row=5,column=0)
    tk.Radiobutton(root, text="AB", variable=submode_var, value="AB").grid(row=6, column=0)
    tk.Radiobutton(root, text="RB", variable=submode_var, value="RB").grid(row=7, column=0)
    tk.Radiobutton(root, text="SB", variable=submode_var, value="SB").grid(row=8, column=0)
    ToolTip(scoreinput, msg="typing '+m' will add the modifiers\nonto the number you wrote the +m after\nSupports arithmetic with *,+,() and -")
    result_label = tk.Label(root, text="", fg="green", font=font_size(20))
    average_result_label = tk.Label(root, text="", fg="green", font=font_size(20))

    tk.Label(root, text="Inputted Modifiers").grid(row=12, column=3)
    tk.Label(root, text="Air and Ground").grid(row=13, column=3)
    tk.Label(root, text="Naval").grid(row=13, column=4)
    tk.Label(root, text="Ranks").grid(row=13, column=2)
    tk.Label(root, text="1").grid(row=14, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['1']}").grid(row=14, column=3)
    tk.Label(root, text=f"{modifiers['rank']['naval']['1']}").grid(row=14, column=4)
    tk.Label(root, text="2").grid(row=15, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['2']}").grid(row=15, column=3)
    tk.Label(root, text=f"{modifiers['rank']['naval']['2']}").grid(row=15, column=4)
    tk.Label(root, text="3").grid(row=16, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['3']}").grid(row=16, column=3)
    tk.Label(root, text=f"{modifiers['rank']['naval']['3']}").grid(row=16, column=4)
    tk.Label(root, text="4").grid(row=17, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['4']}").grid(row=17, column=3)
    tk.Label(root, text=f"{modifiers['rank']['naval']['4']}").grid(row=17, column=4)
    tk.Label(root, text="5").grid(row=18, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['5']}").grid(row=18, column=3)
    tk.Label(root, text=f"{modifiers['rank']['naval']['5']}").grid(row=18, column=4)
    tk.Label(root, text="6").grid(row=19, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['6']}").grid(row=19, column=3)
    tk.Label(root, text="-").grid(row=19, column=4)
    tk.Label(root, text="7").grid(row=20, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['7']}").grid(row=20, column=3)
    tk.Label(root, text="-").grid(row=20, column=4)
    tk.Label(root, text="8").grid(row=21, column=2)
    tk.Label(root, text=f"{modifiers['rank']['normal']['8']}").grid(row=21, column=3)
    tk.Label(root, text="-").grid(row=21, column=4)

    tk.Label(root, text="Calculate the average", font=font_size(16)).grid(row=10, column=10)
    tk.Label(root, text="Enter your time").grid(row=11, column=10)
    timegiven = tk.Entry(root)
    timegiven.grid(row=12,column=10)
    ToolTip(timegiven, msg="'h' converts hours to minutes(1h30 will return 90 minutes)")
    tk.Label(root, text="Enter your score").grid(row=13, column=10)
    scoregiven = tk.Spinbox(root, from_=0, to=40000)
    scoregiven.grid(row=14,column=10)
    ToolTip(scoregiven, msg="Without the additional modifiers")

    def validate_avg():
        scoregiven2 = scoregiven.get()
        timegiven2 = timegiven.get()
        print("validation (avg)")
        scoregiven2 = re.sub(r'[^0-9]', '', scoregiven2)
        timegiven2 = re.sub(r'[^0-9h]', '', timegiven2)
        timegiven2 = timegiven2.replace('h', "*60+")
        if timegiven2.split('+')[-1]=='':
            timegiven2+="0"
        timegiven2 = eval(timegiven2)
        global time_list
        global score_list
        score_list.append(int(scoregiven2))
        time_list.append(int(timegiven2))
        print(score_list)
        print(time_list)
    def reset_avg():
        print("reset (avg)")
        global score_list
        score_list = []
        time_list = []
        print(score_list)
        print(time_list)
    def calc_game_avg(time_avg, score_avg):
        average_ppm = score_avg/time_avg
        average_games = print("WIP")
        average_result_label.config(text=f"Calculated Result:", fg="green", font=font_size(20))
    def calc_score_avg():
        global score_list
        temp_num = 0
        for i in score_list:
            temp_num+=i
        temp_div = len(score_list)
        return temp_num/temp_div
    def calc_time_avg():
        global time_list
        temp_num = 0
        for i in time_list:
            temp_num+=i
        temp_div = len(time_list)
        return temp_num/temp_div

    def validate():
        print("validation")
        submodeinput2 = submode_var.get().upper()
        rankinput2 = int(rankinput.get())
        modeinput2 = mode_var.get().lower()
        with open("modifiers.json", "r") as file:
            modifiers = json.load(file)
            modifiers = modifiers["scorebased"]
        if modeinput2 == "naval":
            modetouse = "naval"
        else:
            modetouse = "normal"
        scoreinputreplace = scoreinput.get().replace("+m", f'*{float(modifiers["rank"][modetouse][f"{rankinput2}"])}*{float(modifiers["mode"][f"{modeinput2}"][f"{submodeinput2}"])}')
        scoreinputreplace = re.sub(r'[^0-9+().*\-m]', '', scoreinputreplace)
        print(scoreinputreplace)
        scoreinput_value = eval(scoreinputreplace)
        if mode_var.get() == "hidden":
            result_label.config(text="Select a mode", fg="red")
            return
        if submode_var.get() == "hidden":
            result_label.config(text="Select a sub-mode", fg="red")
            return
        if not scoreinput_value:
            result_label.config(text="Please enter the score required", fg="red")
            return
        try:
            scoreinput2 = int(scoreinput_value)
        except ValueError:
            result_label.config(text="Invalid score value", fg="red")
            return
        if modeinput2 not in ["ground", "air", "naval"]:
            result_label.config(text="Not valid mode", fg="red")
            return
        if scoreinput2 > 100000:
            result_label.config(text="Too much.", fg="red")
            return
        elif scoreinput2 <= 0:
            result_label.config(text="Done.", fg="green")
        if ((rankinput2 < 1 or rankinput2 > 5) and modeinput2 == "naval") or (rankinput2 > 8 or rankinput2 < 1):
            result_label.config(text="No Such rank.", fg="red")
            return
        if submodeinput2 not in ["AB", "RB", "SB"] or (submodeinput2 == "SB" and modeinput2 == "naval"):
            result_label.config(text="Not valid sub-mode", fg="red")
            return
        try:
            calculated_result = scorebased(modeinput2, submodeinput2, rankinput2, scoreinput2)
            if calculated_result <= 0:
                result_label.config(text="Done", fg="green", font=font_size(20))
            else:
                result_label.config(text=f"Calculated Result: {calculated_result}", fg="green", font=font_size(20))
        except Exception as e:
            result_label.config(text=str(e), fg="red", font=font_size(20))
        average_score = calc_score_avg()
        average_time = calc_time_avg()
        try:
            calc_game_avg(average_time, average_score)
        except Exception as e:
            average_result_label.config(text=str(e), fg="red", font=font_size(20))

    def resetfields():
        print("reset fields")
        mode_var.set(value="hidden")
        submode_var.set(value="hidden")
        rankinput.delete(0, tk.END)
        scoreinput.delete(0, tk.END)
        result_label.config(text="")
        rankinput.delete(0, tk.END)
        rankinput.insert(0, "1")

    confirmbutton = tk.Button(root, text="Calculate", command=validate)
    resetfield = tk.Button(root, text="Reset", command=resetfields)
    confirmbutton.grid(row=5, column=3, columnspan=1, sticky="ew")
    resetfield.grid(row=6, column=3, sticky="ew")
    scoreinput.grid(row=4,column=3, sticky="ew")
    rankinput.grid(row=2, column=3, sticky="ew")
    result_label.grid(row=9,column=0,columnspan=10)
    average_result_label.grid(row=10,column=0,columnspan=10)
    tk.Button(root, text="Add", command=validate_avg).grid(row=15,column=10)
    tk.Button(root, text="Reset", command=reset_avg).grid(row=16,column=10)
root = tk.Tk()
root.title("Event score Calculator")
root.geometry("1024x720")

def scorebased(modeinput:str, submodeinput:str, rankinput:int, scoreinput:int):
    print("score based calculator")
    with open("modifiers.json", "r") as file:
        modifiers = json.load(file)
        modifiers = modifiers["scorebased"]

    modes = modifiers["mode"]
    ranks = modifiers["rank"]
    if modeinput == "naval":
        currentmode = modes["naval"]
        rankmode = ranks["naval"]
        if submodeinput == "SB":
            raise Exception("No such gamemode")
        else:
            submode = currentmode[submodeinput]
    elif modeinput in ["air", "ground"]:
        currentmode = modes[modeinput]
        rankmode = ranks["normal"]
        submode = currentmode[submodeinput]

    maths1 = scoreinput/submode/rankmode[str(rankinput)]
    output = round(maths1)
    return output

open_score_based_window()
root.mainloop()