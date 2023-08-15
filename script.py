import json, os, sys
import tkinter as tk
import tkinter.font as tkFont

if os.path.splitext(sys.argv[0])[1].lower() != ".exe":
    print("not an .exe")
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
    
    modeinputtext = tk.Label(text="Please input the gamemode\n(\"ground\", \"air\", \"naval\")")
    modeinput = tk.Entry(root)
    submodeinputtext = tk.Label(text="Input the selected sub-mode\n(\"AB\", \"RB\", \"SB\")")
    submodeinput = tk.Entry(root)
    rankinputtext = tk.Label(text="Please select what rank you want to play in\n(1-7)")
    rankinput = tk.Entry(root)
    scoreneededinputtext = tk.Label(text="How much score is required?")
    scoreinput = tk.Entry(root)

    result_label = tk.Label(root, text="", fg="green", font=font_size(16))


    def validate():
        print("validation")
        scoreinput2 = int(scoreinput.get())
        submodeinput2 = submodeinput.get().upper()
        rankinput2 = int(rankinput.get())
        modeinput2 = modeinput.get().lower()
        if modeinput2 not in ["ground", "air", "naval"]:
            result_label.config(text="Not valid mode", fg="red")
            return
        if scoreinput2 < 0 or scoreinput2 > 100000:
            result_label.config(text="Too much.", fg="red")
            return
        if ((rankinput2 <= 0 or rankinput2 >= 8) and modeinput2 != "naval") or ((rankinput2 <= 0 or rankinput2 >= 6) and modeinput2 == "naval"):
            result_label.config(text="Outside of range", fg="red")
            return
        if submodeinput2 not in ["AB", "RB", "SB"]:
            result_label.config(text="Not valid sub-mode", fg="red")
            return

        try:
            calculated_result = scorebased(modeinput2, submodeinput2, rankinput2, scoreinput2)
            result_label.config(text=f"Calculated Result: {calculated_result}", fg="green", font=font_size(16))
        except Exception as e:
            result_label.config(text=str(e), fg="red", font=font_size(14))

    confirmbutton = tk.Button(text="Calculate", command=validate)
    confirmbutton.pack()
    def resetfields():
        print("reset fields")
        modeinput.delete(0, tk.END)
        submodeinput.delete(0, tk.END)
        rankinput.delete(0, tk.END)
        scoreinput.delete(0, tk.END)
        result_label.config(text="")

    resetfield = tk.Button(text="Reset", command=resetfields)
    modeinputtext.pack()
    modeinput.pack()
    submodeinputtext.pack()
    submodeinput.pack()
    rankinputtext.pack()
    rankinput.pack()
    scoreneededinputtext.pack()
    scoreinput.pack()
    result_label.pack()
    resetfield.pack()
    back_button = tk.Button(root, text="Back to Main", command=reset_main_window, width=20, height=5, font=font_size(14))
    back_button.pack(side=tk.BOTTOM)

def clear_main_window():
    print("clear main window")
    for widget in root.winfo_children():
        widget.pack_forget()

main_window_open = False

def open_main_window():
    global main_window_open
    root = tk.Tk()
    # ... (rest of your main window setup)
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