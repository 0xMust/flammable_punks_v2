import random
import pandas as pd

type_ = ["Male", "Female", "Alien", "Zombie", "Ape"]

skin_color = ["Pink", "Pale", "Fair", "Tan", "Dark"]


def get_skin_color(type_):
    if type_ in ["Male", "Female"]:
        return skin_color[random.randrange(len(skin_color))]
    else:
        return type_


head = [
    "None",
    "Red Helmet - Gold Badge",
    "Red Helmet - Silver Badge",
    "Yellow Helmet - Gold Badge",
    "Yellow Helmet - Silver Badge",
    "Fire Marshall's Cap",
    "Fire Marshall's Cap - Backwards",
    "Explosion Hair - Blonde",
    "Explosion Hair - Brown",
    "Explosion Hair - Black",
    "Explosion Hair - Red",
    "Orange Beanie",
    "Hoodie",
    "Mcdonalds Cap Red",
    "Bucket Hat - Fire",
    #'Bucket Hat - Ice',
    "Stuck Up Peak",
    "Green Mohawk",
    "Bandana",
    "Purple Cap",
    "Police Man Hat",
]

eyes = [
    "None",
    "Welding Goggles - Blue",
    "Welding Goggles - Blue - Up",
    "Welding Goggles - Pink",
    "Welding Goggles - Pink - Up",
    "Welding Goggles - Green",
    "Welding Goggles - Green - Up",
    "Reflective Goggles",
    "3D Glasses",
    "Cool Glasses",
    "Square Shades",
    "Eye Patch",
    "VR Goggles",
    "Gas Mask",
    "Gas Mask - Icy",
    "Gas Mask - Green",
    "Gas Mask - Rainbow",
    "Gas Mask - Warm",
    "Big Purple Shades",
    "Small Shades - Classic",
    "Small Shades - Dysto",
    "VR Headset - Kawaii",
    "Cyclops Visor",
    "Cybereye",
]

mouth = ["None", "Cigarette", "Covid Mask", "Pipe", "Dysto Gas Mask"]

ear = ["None", "None", "None", "None", "Earring"]

neck = ["None", "None", "None", "Silver Chain", "Silver Chain", "Gold Chain"]

soot = ["None", "None", "None", "Soot"]

beard = [
    "None",
    "Beard"
    #'Mutton Chops',
    #'Goatee'
]


def get_soot(head):
    if head == "Gas Mask":
        return "None"
    else:
        return soot[random.randrange(len(soot))]


def get_beard(type_):
    if type_ == "Male":
        return beard[random.randrange(len(beard))]
    else:
        return "None"


df = pd.DataFrame()


for t in type_:
    for h in head:
        for e in eyes:
            for m in mouth:
                df = df.append(
                    {
                        "Type": t,
                        "Head": h,
                        "Eyes": e,
                        "Mouth": m,
                        "Skin Color": get_skin_color(t),
                        "Facial Hair": get_beard(t),
                        "Earring": ear[random.randrange(len(ear))],
                        "Neck": neck[random.randrange(len(neck))],
                        "Soot": get_soot(h),
                    },
                    ignore_index=True,
                )
df = df[
    ~(
        (df["Mouth"] != "None")
        & (
            df["Eyes"].isin(
                [
                    "Gas Mask",
                    "Gas Mask - Icy",
                    "Gas Mask - Green",
                    "Gas Mask - Rainbow",
                    "Gas Mask - Warm",
                ]
            )
        )
    )
]

# shuffle rows
df = df.sample(frac=1)

df.reset_index(inplace=True, drop=True)

df.to_pickle("scripts/flammable_punks.pkl")
