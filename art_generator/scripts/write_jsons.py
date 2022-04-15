from art_generating_functions import *
import pandas as pd
import json

df = pd.read_pickle("scripts/flammable_punks.pkl")

vital_dict = {0: "Unknown", 1: "Rescued", 2: "Murdered"}
vital_desc_dict = {
    0: "A punk who's fate is yet to be determined.",
    1: "Someone had mercy on this punk and rescued them from the flames.",
    2: "A ruthless navigator of the chain cast this punk into the flames.",
}
for i in range(len(df)):
    for vital in [0, 1, 2]:
        metadata_dict = {}

        metadata_dict["description"] = vital_desc_dict[vital]

        metadata_dict[
            "image"
        ] = f"https://ipfs.io/ipfs/QmfRy1ANL7iJzwt37DM3zdfPwwdhMHuKe3F8HaRtNMYkNV/{i}%20-%20{vital}.png"

        metadata_dict["name"] = f"Flammable Punk #{str(i).zfill(4)}"

        metadata_dict["attributes"] = {}
        for col in df.columns:
            if col != "Skin Color":
                if df[col][i] != "None":
                    metadata_dict["attributes"][col] = df[col][i]
            else:
                if df["Skin Color"][i] not in ["Ape", "Alien", "Zombie"]:
                    metadata_dict["attributes"][col] = df[col][i]
        metadata_dict["attributes"]["Fate"] = vital_dict[vital]

        out_file = open(f"./metadata/{i} - {vital}.json", "w")

        json.dump(metadata_dict, out_file)

        out_file.close()
