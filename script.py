import json, os, sys, msvcrt

if os.path.splitext(sys.argv[0])[1].lower() != ".exe":
    print("not an .exe")
else:
    current_dir = os.path.dirname(os.path.abspath(sys.executable))
    os.chdir(current_dir)
    

with open("modifiers.json", "r") as file:
    modifiers = json.load(file)

modeinput = str(input("Please input the mode\n(\"ground\", \"air\", \"naval\")\nUser input: "))
if modeinput not in ["ground", "air", "naval"]:
    raise Exception("Not valid mode")
submodeinput = str(input("Input the selected sub-mode\n(\"AB\", \"RB\", \"SB\")\nUser input: "))
if submodeinput not in ["AB", "RB", "SB"]:
    raise Exception("Not valid sub-mode")
rankinput = int(input("Please select what rank you want to play in\n(1-7)\nUser input: "))
if ((rankinput <= 0 or rankinput >= 8) and modeinput != "naval") or ((rankinput <= 0 or rankinput >= 6) and modeinput == "naval"):
    raise Exception("Outside of range")
scoreinput = int(input("How much score is the whole event requiring?\nUser input: "))
if scoreinput < 0 or scoreinput > 100000:
    raise Exception("Too much.")

modes = modifiers["mode"]
ranks = modifiers["rank"]
if modeinput == "naval":
    currentmode = modes["naval"]
    rankmode = ranks["naval"]
elif modeinput in ["air", "ground"]:
    currentmode = modes[modeinput]
    rankmode = ranks["normal"]

if modeinput == "naval" and submodeinput == "SB":
    raise Exception("No such gamemode")
elif submodeinput in ["AB", "RB", "SB"]:
    submode = currentmode[submodeinput]

maths1 = scoreinput/submode/rankmode[str(rankinput)]
output = round(maths1)
print(output)
print("\n\npress any key to exit")
while not msvcrt.kbhit():
    pass
msvcrt.getch()
print("Closing...")
os._exit(0)
