import json, os, sys, re
import tkinter as tk
import tkinter.font as tkFont

if os.path.splitext(sys.argv[0])[1].lower() != ".exe":
    print("not an .exe")
    current_dir = os.path.dirname(os.path.abspath(__file__))
else:
    current_dir = os.path.dirname(os.path.abspath(sys.executable))
os.chdir(current_dir)

def font_size(size:int):
    print("font size def")
    return tkFont.Font(size=size)

def open_score_based_window():
    print("open score based window")
    clear_main_window()
    label.config(text="Score Based Window Content")

    mode_var = tk.StringVar(value="hidden")
    submode_var = tk.StringVar(value="hidden")  
    tk.Label(root, text="Select the gamemode:").grid(row=1,column=0)
    tk.Radiobutton(root, text="Ground", variable=mode_var, value="ground").grid(row=2, column=0)
    tk.Radiobutton(root, text="Air", variable=mode_var, value="air").grid(row=3, column=0)
    tk.Radiobutton(root, text="Naval", variable=mode_var, value="naval").grid(row=4, column=0)
    tk.Label(root, text="Select the sub-mode:").grid(row=5,column=0)
    tk.Radiobutton(root, text="AB", variable=submode_var, value="AB").grid(row=6, column=0)
    tk.Radiobutton(root, text="RB", variable=submode_var, value="RB").grid(row=7, column=0)
    tk.Radiobutton(root, text="SB", variable=submode_var, value="SB").grid(row=8, column=0)
    tk.Label(root, text="Please select what rank you want to play in\n(1-7)").grid(row=1,column=3)
    rankinput = tk.Spinbox(root, from_=1, to=7)
    tk.Label(root, text="How much score is required?").grid(row=3,column=3)
    scoreinput = tk.Entry(root)
    result_label = tk.Label(root, text="", fg="green", font=font_size(20))

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
        scoreinputreplace = re.sub(r'[^0-9]', '', scoreinputreplace)
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
        if ((rankinput2 < 1 or rankinput2 > 5) and modeinput2 == "naval") or (rankinput2 > 7 or rankinput2 < 1):
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
    confirmbutton.grid(row=5, column=3, columnspan=2, pady=10)
    resetfield.grid(row=6, column=3)
    scoreinput.grid(row=4,column=3)
    rankinput.grid(row=2, column=3)
    result_label.grid(row=10,column=0,columnspan=10)

def clear_main_window():
    print("clear main window")
    for widget in root.winfo_children():
        widget.pack_forget()

main_window_open = False
def open_main_window():
    global main_window_open
    root = tk.Tk()
    main_window_open = True
    root.mainloop()
    main_window_open = False
def reset_main_window():
    global main_window_open
    if main_window_open:
        clear_main_window()
        label.config(text="Select the event type")
        label.pack()
        button.pack()
        button2.pack()

root = tk.Tk()
root.title("Event score Calculator")
root.geometry("800x600")

label = tk.Label(root, text="Select the event type")
label.pack()

button = tk.Button(root, text="Score based", command=open_score_based_window, width=50, height=20)
button2 = tk.Button(root, text="Crafting (Crates)\n[DOES NOT WORK FOR NOW]", width=50, height=20)

button.pack(padx=10)
button2.pack(padx=10)

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

def craftingevent():
    print("Open crafting event window")
    print("Coming soon:tm:")

root.mainloop()