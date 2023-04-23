import joblib
import tkinter as tk
from tkinter import filedialog

model = joblib.load('model.joblib')


def load_model():
    global model
    filepath = filedialog.askopenfilename()  # open file dialog to select the file
    model = joblib.load("seg")  # load the selected model file
    print("Model loaded successfully!")

def csgo_classification(bomb_planted, ct_health , ct_armor , t_armor , ct_helmets , t_helmets , ct_defuse_kits , ct_players_alive , ct_weapon_ak47 , t_weapon_ak47 , ct_weapon_awp ,ct_weapon_m4a4, ct_weapon_sg553 , t_weapon_sg553, ct_weapon_usps , ct_grenade_hegrenade, ct_grenade_flashbang ,t_grenade_flashbang , ct_grenade_smokegrenade , ct_grenade_incendiarygrenade):
    y_pred = model.predict([[bomb_planted, ct_health , ct_armor , t_armor , ct_helmets , t_helmets , ct_defuse_kits , ct_players_alive , ct_weapon_ak47 , t_weapon_ak47 , ct_weapon_awp ,ct_weapon_m4a4, ct_weapon_sg553 , t_weapon_sg553, ct_weapon_usps , ct_grenade_hegrenade, ct_grenade_flashbang ,t_grenade_flashbang , ct_grenade_smokegrenade , ct_grenade_incendiarygrenade]])
    if y_pred == 0:
        return "CT"
    return "T"

# Create the Tkinter window and widgets
window = tk.Tk()
window.title("CS:GO Round Winner Prediction")

#1 bomb_planted
label_bomb_planted = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_bomb_planted.grid(row=1, column=0, padx=10, pady=10)
entry_bomb_planted = tk.Entry(window)
entry_bomb_planted.grid(row=1, column=1, padx=10, pady=10)

#2 ct_health
label_ct_health = tk.Label(window, text="ct_health")
label_ct_health.grid(row=2, column=0, padx=10, pady=10)
entry_ct_health = tk.Entry(window)
entry_ct_health.grid(row=2, column=1, padx=10, pady=10)

#3 ct_armor
label_ct_armor = tk.Label(window, text="ct_armor")
label_ct_armor.grid(row=3, column=0, padx=10, pady=10)
entry_ct_armor = tk.Entry(window)
entry_ct_armor.grid(row=3, column=1, padx=10, pady=10)

#4 t_armor
label_t_armor = tk.Label(window, text="t_armor")
label_t_armor.grid(row=4, column=0, padx=10, pady=10)
entry_t_armor = tk.Entry(window)
entry_t_armor.grid(row=4, column=1, padx=10, pady=10)

#5 ct_helmets
label_ct_helmets = tk.Label(window, text="ct_helmets")
label_ct_helmets.grid(row=5, column=0, padx=10, pady=10)
entry_ct_helmets = tk.Entry(window)
entry_ct_helmets.grid(row=5, column=1, padx=10, pady=10)

#6 t_helmets
label_t_helmets = tk.Label(window, text="t_helmets")
label_t_helmets.grid(row=6, column=0, padx=10, pady=10)
entry_t_helmets = tk.Entry(window)
entry_t_helmets.grid(row=6, column=1, padx=10, pady=10)

#7 ct_defuse_kits
label_ct_defuse_kits = tk.Label(window, text="ct_defuse_kits")
label_ct_defuse_kits.grid(row=7, column=0, padx=10, pady=10)
entry_ct_defuse_kits = tk.Entry(window)
entry_ct_defuse_kits.grid(row=7, column=1, padx=10, pady=10)

#8 ct_players_alive
label_ct_players_alive = tk.Label(window, text="ct_players_alive")
label_ct_players_alive.grid(row=8, column=0, padx=10, pady=10)
entry_ct_players_alive = tk.Entry(window)
entry_ct_players_alive.grid(row=8, column=1, padx=10, pady=10)

#9 ct_weapon_ak47
label_ct_weapon_ak47 = tk.Label(window, text="ct_weapon_ak47")
label_ct_weapon_ak47.grid(row=9, column=0, padx=10, pady=10)
entry_ct_weapon_ak47 = tk.Entry(window)
entry_ct_weapon_ak47.grid(row=9, column=1, padx=10, pady=10)

#10 t_weapon_ak47
label_t_weapon_ak47 = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_t_weapon_ak47.grid(row=10, column=0, padx=10, pady=10)
entry_t_weapon_ak47 = tk.Entry(window)
entry_t_weapon_ak47.grid(row=10, column=1, padx=10, pady=10)

#11 ct_weapon_awp
label_ct_weapon_awp = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_weapon_awp.grid(row=1, column=3, padx=10, pady=10)
entry_ct_weapon_awp = tk.Entry(window)
entry_ct_weapon_awp.grid(row=1, column=4, padx=10, pady=10)

#12 ct_weapon_m4a4
label_ct_weapon_m4a4 = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_weapon_m4a4.grid(row=2, column=3, padx=10, pady=10)
entry_ct_weapon_m4a4 = tk.Entry(window)
entry_ct_weapon_m4a4.grid(row=2, column=4, padx=10, pady=10)

#13 ct_weapon_sg553
label_ct_weapon_sg553 = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_weapon_sg553.grid(row=3, column=3, padx=10, pady=10)
entry_ct_weapon_sg553 = tk.Entry(window)
entry_ct_weapon_sg553.grid(row=3, column=4, padx=10, pady=10)

#14 t_weapon_sg553
label_t_weapon_sg553 = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_t_weapon_sg553.grid(row=4, column=3, padx=10, pady=10)
entry_t_weapon_sg553 = tk.Entry(window)
entry_t_weapon_sg553.grid(row=4, column=4, padx=10, pady=10)

#15 ct_weapon_usps
label_ct_weapon_usps = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_weapon_usps.grid(row=5, column=3, padx=10, pady=10)
entry_ct_weapon_usps = tk.Entry(window)
entry_ct_weapon_usps.grid(row=5, column=4, padx=10, pady=10)

#16 ct_grenade_hegrenade
label_ct_grenade_hegrenade = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_grenade_hegrenade.grid(row=6, column=3, padx=10, pady=10)
entry_ct_grenade_hegrenade = tk.Entry(window)
entry_ct_grenade_hegrenade.grid(row=6, column=4, padx=10, pady=10)

#17 ct_grenade_flashbang
label_ct_grenade_flashbang = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_grenade_flashbang.grid(row=7, column=3, padx=10, pady=10)
entry_ct_grenade_flashbang = tk.Entry(window)
entry_ct_grenade_flashbang.grid(row=7, column=4, padx=10, pady=10)

#18 t_grenade_flashbang
label_t_grenade_flashbang = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_t_grenade_flashbang.grid(row=8, column=3, padx=10, pady=10)
entry_t_grenade_flashbang = tk.Entry(window)
entry_t_grenade_flashbang.grid(row=8, column=4, padx=10, pady=10)

#19 ct_grenade_smokegrenade
label_ct_grenade_smokegrenade = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_grenade_smokegrenade.grid(row=9, column=3, padx=10, pady=10)
entry_ct_grenade_smokegrenade = tk.Entry(window)
entry_ct_grenade_smokegrenade.grid(row=9, column=4, padx=10, pady=10)

#20 ct_grenade_incendiarygrenade
label_ct_grenade_incendiarygrenade = tk.Label(window, text="Is a bomb planted? Put 0/1 for Fale/True")
label_ct_grenade_incendiarygrenade.grid(row=10, column=3, padx=10, pady=10)
entry_ct_grenade_incendiarygrenade = tk.Entry(window)
entry_ct_grenade_incendiarygrenade.grid(row=10, column=4, padx=10, pady=10)


def prediction_of_winner():
    #gender = (entry_gender.get())
    bomb_planted = float(entry_bomb_planted.get())
    ct_health = float(entry_ct_health.get())
    ct_armor = float(entry_ct_armor.get())
    t_armor = float(entry_t_armor.get())
    ct_helmets = float(entry_ct_helmets.get())
    t_helmets = float(entry_t_helmets.get())
    ct_defuse_kits = float(entry_ct_defuse_kits.get())
    ct_players_alive  = float(entry_ct_players_alive.get())
    ct_weapon_ak47 = float(entry_ct_weapon_ak47.get())
    t_weapon_ak47 = float(entry_t_weapon_ak47.get())
    ct_weapon_awp = float(entry_ct_weapon_awp.get())
    ct_weapon_m4a4 = float(entry_ct_weapon_m4a4.get())
    ct_weapon_sg553 = float(entry_ct_weapon_sg553.get())
    t_weapon_sg553 = float(entry_t_weapon_sg553.get())
    ct_weapon_usps = float(entry_ct_weapon_usps.get())
    ct_grenade_hegrenade = float(entry_ct_grenade_hegrenade.get())
    ct_grenade_flashbang = float(entry_ct_grenade_flashbang.get())
    t_grenade_flashbang = float(entry_t_grenade_flashbang.get())
    ct_grenade_smokegrenade = float(entry_ct_grenade_smokegrenade.get())
    ct_grenade_incendiarygrenade = float(entry_ct_grenade_incendiarygrenade.get())
    

    prediction = csgo_classification(bomb_planted, ct_health , ct_armor , t_armor , ct_helmets , t_helmets , ct_defuse_kits , ct_players_alive , ct_weapon_ak47 , t_weapon_ak47 , ct_weapon_awp ,ct_weapon_m4a4, ct_weapon_sg553 , t_weapon_sg553, ct_weapon_usps , ct_grenade_hegrenade, ct_grenade_flashbang ,t_grenade_flashbang , ct_grenade_smokegrenade , ct_grenade_incendiarygrenade)
    output_label.config(text=prediction)



button = tk.Button(window, text="Predict", command = prediction_of_winner)
button.grid(row=12, column=1)

output_label = tk.Label(window, text="")
output_label.grid(row=11, column=1)

window.mainloop()