from art_generating_functions import *
import pandas as pd
from PIL import Image

df = pd.read_pickle("scripts/flammable_punks.pkl")

for i in range(len(df)):
    # for i in range(100):
    img = draw.Drawing(dim, dim, origin="center", displayInline=False)

    # draw background
    draw_background(img)

    # draw fire
    draw_fire(img)

    # draw head
    if df["Type"][i] == "Ape":
        draw_ape_head(img)
    elif df["Type"][i] == "Alien":
        draw_alien_head(img)
    elif df["Type"][i] == "Zombie":
        draw_zombie_head(img)
    elif df["Type"][i] == "Male":
        draw_male_head(img, df["Skin Color"][i])
    elif df["Type"][i] == "Female":
        draw_female_head(img, df["Skin Color"][i])

    # draw beard traits
    if df["Facial Hair"][i] == "None":
        draw_nothing(img)
    elif df["Facial Hair"][i] == "Beard":
        draw_beard(img)

    # draw neck traits
    if df["Neck"][i] == "None":
        draw_nothing(img)
    elif df["Neck"][i] == "Silver Chain":
        draw_silver_chain(img, gender=df["Type"][i])
    elif df["Neck"][i] == "Gold Chain":
        draw_gold_chain(img, df["Type"][i])

    # draw cyber eye under hat and mouth traits
    if df["Eyes"][i] == "Cybereye":
        draw_cybereye(img, gender=df["Type"][i])

    # draw soot traits
    if df["Soot"][i] == "None":
        draw_nothing(img)
    elif df["Soot"][i] == "Soot":
        draw_soot(img)

    # draw head trait
    if df["Head"][i] == "None":
        draw_nothing(img)
    elif df["Head"][i] == "Red Helmet - Gold Badge":
        draw_fireman_hat(img, hat_color="Red", badge_color="Gold")
    elif df["Head"][i] == "Red Helmet - Silver Badge":
        draw_fireman_hat(img, hat_color="Red", badge_color="Silver")
    elif df["Head"][i] == "Yellow Helmet - Gold Badge":
        draw_fireman_hat(img, hat_color="Yellow", badge_color="Gold")
    elif df["Head"][i] == "Yellow Helmet - Silver Badge":
        draw_fireman_hat(img, hat_color="Yellow", badge_color="Silver")
    elif df["Head"][i] == "Fire Marshall's Cap":
        draw_marshall_cap(img, df["Type"][i])
    elif df["Head"][i] == "Fire Marshall's Cap - Backwards":
        draw_marshall_cap_backwards(img, df["Type"][i])
    elif df["Head"][i] == "Explosion Hair - Brown":
        draw_explosion_hair(img, "#5A3825")
    elif df["Head"][i] == "Explosion Hair - Black":
        draw_explosion_hair(img, "#000000")
    elif df["Head"][i] == "Explosion Hair - Red":
        draw_explosion_hair(img, "#e5282e")
    elif df["Head"][i] == "Orange Beanie":
        draw_beanie(img)
    elif df["Head"][i] == "Hoodie":
        draw_hoodie(img, gender=df["Type"][i], alive="Alive")
    elif df["Head"][i] == "Mcdonalds Cap Red":
        draw_mcdonalds_cap(img)
    elif df["Head"][i] == "Bucket Hat - Fire":
        draw_bucket_hat(img, colors)
    elif df["Head"][i] == "Stuck Up Peak":
        draw_turned_up_peak(img)
    elif df["Head"][i] == "Green Mohawk":
        draw_green_mohawk(img, gender=df["Type"][i])
    elif df["Head"][i] == "Bandana":
        draw_bandana(img, gender=df["Type"][i])
    elif df["Head"][i] == "Purple Cap":
        draw_purple_cap(img)
    elif df["Head"][i] == "Police Man Hat":
        draw_police_hat(img)

    # draw mouth traits
    if df["Mouth"][i] == "None":
        draw_nothing(img)
    elif df["Mouth"][i] == "Cigarette":
        draw_cig(img)
    elif df["Mouth"][i] == "Covid Mask":
        draw_covid_mask(img, alive="Alive")
    elif df["Mouth"][i] == "Pipe":
        draw_pipe(img)
    elif df["Mouth"][i] == "Dysto Gas Mask":
        draw_dysto_gas_mask(img, df["Type"][i])

    # draw eyes traits
    if df["Eyes"][i] == "None":
        draw_nothing(img)
    elif df["Eyes"][i] == "Welding Goggles - Blue":
        draw_welders_goggles(img, "#23ACC4")
    elif df["Eyes"][i] == "Welding Goggles - Blue - Up":
        draw_welders_on_head(img, "#23ACC4")
    elif df["Eyes"][i] == "Welding Goggles - Pink":
        draw_welders_goggles(img, "#d25598")
    elif df["Eyes"][i] == "Welding Goggles - Pink - Up":
        draw_welders_on_head(img, "#d25598")
    elif df["Eyes"][i] == "Welding Goggles - Green":
        draw_welders_goggles(img, "#7e9a81")
    elif df["Eyes"][i] == "Welding Goggles - Green - Up":
        draw_welders_on_head(img, "#7e9a81")
    elif df["Eyes"][i] == "Reflective Goggles":
        draw_reflective_goggles(img)
    elif df["Eyes"][i] == "3D Glasses":
        draw_3d_glasses(img)
    elif df["Eyes"][i] == "Cool Glasses":
        draw_thug_life_shades(img)
    elif df["Eyes"][i] == "Square Shades":
        draw_square_shades(img)
    elif df["Eyes"][i] == "Eye Patch":
        draw_eye_patch(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "VR Goggles":
        draw_vr_headset(img)
    elif df["Eyes"][i] == "Gas Mask":
        draw_gas_mask(img, colors)
    elif df["Eyes"][i] == "Gas Mask - Icy":
        draw_gas_mask(img, ice_colors)
    elif df["Eyes"][i] == "Gas Mask - Green":
        draw_gas_mask(img, green_colors)
    elif df["Eyes"][i] == "Gas Mask - Rainbow":
        draw_gas_mask(img, rainbow_colors)
    elif df["Eyes"][i] == "Gas Mask - Warm":
        draw_gas_mask(img, warm_colors)
    elif df["Eyes"][i] == "Big Purple Shades":
        draw_big_shades(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "Small Shades - Classic":
        draw_small_shades(img, gender=df["Type"][i], dysto=False)
    elif df["Eyes"][i] == "Small Shades - Dysto":
        draw_small_shades(img, gender=df["Type"][i], dysto=True)
    elif df["Eyes"][i] == "VR Headset - Kawaii":
        draw_kawaii_vr(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "Cyclops Visor":
        draw_cyclops_visor(img)

    if (df["Head"][i] == "Stuck Up Peak") & (
        df["Eyes"][i]
        in [
            "Welding Goggles - Blue - Up",
            "Welding Goggles - Pink - Up",
            "Welding Goggles - Green - Up",
        ]
    ):
        draw_peak(img)

    # draw ear traits
    if df["Earring"][i] == "None":
        draw_nothing(img)
    elif df["Earring"][i] == "Earring":
        draw_earring(img, type_=df["Type"][i])

    # save svg images
    img.savePng(f"imgs/{i} - 0.png")

    img = draw.Drawing(dim, dim, origin="center", displayInline=False)

    # draw background
    draw_background(img)

    # draw head
    if df["Type"][i] == "Ape":
        draw_ape_head(img)
    elif df["Type"][i] == "Alien":
        draw_alien_head(img)
    elif df["Type"][i] == "Zombie":
        draw_zombie_head(img)
    elif df["Type"][i] == "Male":
        draw_male_head(img, df["Skin Color"][i])
    elif df["Type"][i] == "Female":
        draw_female_head(img, df["Skin Color"][i])

    # draw beard traits
    if df["Facial Hair"][i] == "None":
        draw_nothing(img)
    elif df["Facial Hair"][i] == "Beard":
        draw_beard(img)

    # draw neck traits
    if df["Neck"][i] == "None":
        draw_nothing(img)
    elif df["Neck"][i] == "Silver Chain":
        draw_silver_chain(img, gender=df["Type"][i])
    elif df["Neck"][i] == "Gold Chain":
        draw_gold_chain(img, df["Type"][i])

    # draw cyber eye under hat and mouth traits
    if df["Eyes"][i] == "Cybereye":
        draw_cybereye(img, gender=df["Type"][i])

    # draw soot traits
    if df["Soot"][i] == "None":
        draw_nothing(img)
    elif df["Soot"][i] == "Soot":
        draw_soot(img)

    # draw head trait
    if df["Head"][i] == "None":
        draw_nothing(img)
    elif df["Head"][i] == "Red Helmet - Gold Badge":
        draw_fireman_hat(img, hat_color="Red", badge_color="Gold")
    elif df["Head"][i] == "Red Helmet - Silver Badge":
        draw_fireman_hat(img, hat_color="Red", badge_color="Silver")
    elif df["Head"][i] == "Yellow Helmet - Gold Badge":
        draw_fireman_hat(img, hat_color="Yellow", badge_color="Gold")
    elif df["Head"][i] == "Yellow Helmet - Silver Badge":
        draw_fireman_hat(img, hat_color="Yellow", badge_color="Silver")
    elif df["Head"][i] == "Fire Marshall's Cap":
        draw_marshall_cap(img, df["Type"][i])
    elif df["Head"][i] == "Fire Marshall's Cap - Backwards":
        draw_marshall_cap_backwards(img, df["Type"][i])
    elif df["Head"][i] == "Explosion Hair - Brown":
        draw_explosion_hair(img, "#5A3825")
    elif df["Head"][i] == "Explosion Hair - Black":
        draw_explosion_hair(img, "#000000")
    elif df["Head"][i] == "Explosion Hair - Red":
        draw_explosion_hair(img, "#e5282e")
    elif df["Head"][i] == "Orange Beanie":
        draw_beanie(img)
    elif df["Head"][i] == "Hoodie":
        draw_hoodie(img, gender=df["Type"][i], alive="Dead")
    elif df["Head"][i] == "Mcdonalds Cap Red":
        draw_mcdonalds_cap(img)
    elif df["Head"][i] == "Bucket Hat - Fire":
        draw_bucket_hat(img, colors)
    elif df["Head"][i] == "Stuck Up Peak":
        draw_turned_up_peak(img)
    elif df["Head"][i] == "Green Mohawk":
        draw_green_mohawk(img, gender=df["Type"][i])
    elif df["Head"][i] == "Bandana":
        draw_bandana(img, gender=df["Type"][i])
    elif df["Head"][i] == "Purple Cap":
        draw_purple_cap(img)
    elif df["Head"][i] == "Police Man Hat":
        draw_police_hat(img)

    # draw mouth traits
    if df["Mouth"][i] == "None":
        draw_nothing(img)
    elif df["Mouth"][i] == "Cigarette":
        draw_cig(img)
    elif df["Mouth"][i] == "Covid Mask":
        draw_covid_mask(img, alive="Dead")
    elif df["Mouth"][i] == "Pipe":
        draw_pipe(img)
    elif df["Mouth"][i] == "Dysto Gas Mask":
        draw_dysto_gas_mask(img, df["Type"][i])

    # draw eyes traits
    if df["Eyes"][i] == "None":
        draw_nothing(img)
    elif df["Eyes"][i] == "Welding Goggles - Blue":
        draw_welders_goggles(img, "#23ACC4")
    elif df["Eyes"][i] == "Welding Goggles - Blue - Up":
        draw_welders_on_head(img, "#23ACC4")
    elif df["Eyes"][i] == "Welding Goggles - Pink":
        draw_welders_goggles(img, "#d25598")
    elif df["Eyes"][i] == "Welding Goggles - Pink - Up":
        draw_welders_on_head(img, "#d25598")
    elif df["Eyes"][i] == "Welding Goggles - Green":
        draw_welders_goggles(img, "#7e9a81")
    elif df["Eyes"][i] == "Welding Goggles - Green - Up":
        draw_welders_on_head(img, "#7e9a81")
    elif df["Eyes"][i] == "Reflective Goggles":
        draw_reflective_goggles(img)
    elif df["Eyes"][i] == "3D Glasses":
        draw_3d_glasses(img)
    elif df["Eyes"][i] == "Cool Glasses":
        draw_thug_life_shades(img)
    elif df["Eyes"][i] == "Square Shades":
        draw_square_shades(img)
    elif df["Eyes"][i] == "Eye Patch":
        draw_eye_patch(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "VR Goggles":
        draw_vr_headset(img)
    elif df["Eyes"][i] == "Gas Mask":
        draw_gas_mask(img, colors)
    elif df["Eyes"][i] == "Gas Mask - Icy":
        draw_gas_mask(img, ice_colors)
    elif df["Eyes"][i] == "Gas Mask - Green":
        draw_gas_mask(img, green_colors)
    elif df["Eyes"][i] == "Gas Mask - Rainbow":
        draw_gas_mask(img, rainbow_colors)
    elif df["Eyes"][i] == "Gas Mask - Warm":
        draw_gas_mask(img, warm_colors)
    elif df["Eyes"][i] == "Big Purple Shades":
        draw_big_shades(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "Small Shades - Classic":
        draw_small_shades(img, gender=df["Type"][i], dysto=False)
    elif df["Eyes"][i] == "Small Shades - Dysto":
        draw_small_shades(img, gender=df["Type"][i], dysto=True)
    elif df["Eyes"][i] == "VR Headset - Kawaii":
        draw_kawaii_vr(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "Cyclops Visor":
        draw_cyclops_visor(img)

    if (df["Head"][i] == "Stuck Up Peak") & (
        df["Eyes"][i]
        in [
            "Welding Goggles - Blue - Up",
            "Welding Goggles - Pink - Up",
            "Welding Goggles - Green - Up",
        ]
    ):
        draw_peak(img)

    # draw ear traits
    if df["Earring"][i] == "None":
        draw_nothing(img)
    elif df["Earring"][i] == "Earring":
        draw_earring(img, type_=df["Type"][i])

    img.savePng(f"imgs/{i} - 1.png")

    img = draw.Drawing(dim, dim, origin="center", displayInline=False)

    # draw background
    draw_fire_background(img)

    # draw fire
    draw_fire(img)

    # draw head
    if df["Type"][i] == "Ape":
        draw_ape_obit_head(img)
    elif df["Type"][i] == "Alien":
        draw_alien_obit_head(img)
    elif df["Type"][i] == "Zombie":
        draw_zombie_obit_head(img)
    elif df["Type"][i] == "Male":
        draw_male_obit_head(img)
    elif df["Type"][i] == "Female":
        draw_female_obit_head(img)

    # draw beard traits
    if df["Facial Hair"][i] == "None":
        draw_nothing(img)
    elif df["Facial Hair"][i] == "Beard":
        draw_beard(img)

    # draw neck traits
    if df["Neck"][i] == "None":
        draw_nothing(img)
    elif df["Neck"][i] == "Silver Chain":
        draw_silver_chain(img, gender=df["Type"][i])
    elif df["Neck"][i] == "Gold Chain":
        draw_gold_chain(img, df["Type"][i])

    # draw cyber eye under hat and mouth traits
    if df["Eyes"][i] == "Cybereye":
        draw_cybereye(img, gender=df["Type"][i])

    # draw soot traits
    if df["Soot"][i] == "None":
        draw_nothing(img)
    elif df["Soot"][i] == "Soot":
        draw_soot(img)

    # draw head trait
    if df["Head"][i] == "None":
        draw_nothing(img)
    elif df["Head"][i] == "Red Helmet - Gold Badge":
        draw_fireman_hat(img, hat_color="Red", badge_color="Gold")
    elif df["Head"][i] == "Red Helmet - Silver Badge":
        draw_fireman_hat(img, hat_color="Red", badge_color="Silver")
    elif df["Head"][i] == "Yellow Helmet - Gold Badge":
        draw_fireman_hat(img, hat_color="Yellow", badge_color="Gold")
    elif df["Head"][i] == "Yellow Helmet - Silver Badge":
        draw_fireman_hat(img, hat_color="Yellow", badge_color="Silver")
    elif df["Head"][i] == "Fire Marshall's Cap":
        draw_marshall_cap(img, df["Type"][i])
    elif df["Head"][i] == "Fire Marshall's Cap - Backwards":
        draw_marshall_cap_backwards(img, df["Type"][i])
    elif df["Head"][i] == "Explosion Hair - Brown":
        draw_explosion_hair(img, "#5A3825")
    elif df["Head"][i] == "Explosion Hair - Black":
        draw_explosion_hair(img, "#000000")
    elif df["Head"][i] == "Explosion Hair - Red":
        draw_explosion_hair(img, "#e5282e")
    elif df["Head"][i] == "Orange Beanie":
        draw_beanie(img)
    elif df["Head"][i] == "Hoodie":
        draw_hoodie(img, gender=df["Type"][i], alive="Dead")
    elif df["Head"][i] == "Mcdonalds Cap Red":
        draw_mcdonalds_cap(img)
    elif df["Head"][i] == "Bucket Hat - Fire":
        draw_bucket_hat(img, colors)
    elif df["Head"][i] == "Stuck Up Peak":
        draw_turned_up_peak(img)
    elif df["Head"][i] == "Green Mohawk":
        draw_green_mohawk(img, gender=df["Type"][i])
    elif df["Head"][i] == "Bandana":
        draw_bandana(img, gender=df["Type"][i])
    elif df["Head"][i] == "Purple Cap":
        draw_purple_cap(img)
    elif df["Head"][i] == "Police Man Hat":
        draw_police_hat(img)

    # draw mouth traits
    if df["Mouth"][i] == "None":
        draw_nothing(img)
    elif df["Mouth"][i] == "Cigarette":
        draw_cig(img)
    elif df["Mouth"][i] == "Covid Mask":
        draw_covid_mask(img, alive="Dead")
    elif df["Mouth"][i] == "Pipe":
        draw_pipe(img)
    elif df["Mouth"][i] == "Dysto Gas Mask":
        draw_dysto_gas_mask(img, df["Type"][i])

    # draw eyes traits
    if df["Eyes"][i] == "None":
        draw_nothing(img)
    elif df["Eyes"][i] == "Welding Goggles - Blue":
        draw_welders_goggles(img, "#23ACC4")
    elif df["Eyes"][i] == "Welding Goggles - Blue - Up":
        draw_welders_on_head(img, "#23ACC4")
    elif df["Eyes"][i] == "Welding Goggles - Pink":
        draw_welders_goggles(img, "#d25598")
    elif df["Eyes"][i] == "Welding Goggles - Pink - Up":
        draw_welders_on_head(img, "#d25598")
    elif df["Eyes"][i] == "Welding Goggles - Green":
        draw_welders_goggles(img, "#7e9a81")
    elif df["Eyes"][i] == "Welding Goggles - Green - Up":
        draw_welders_on_head(img, "#7e9a81")
    elif df["Eyes"][i] == "Reflective Goggles":
        draw_reflective_goggles(img)
    elif df["Eyes"][i] == "3D Glasses":
        draw_3d_glasses(img)
    elif df["Eyes"][i] == "Cool Glasses":
        draw_thug_life_shades(img)
    elif df["Eyes"][i] == "Square Shades":
        draw_square_shades(img)
    elif df["Eyes"][i] == "Eye Patch":
        draw_eye_patch(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "VR Goggles":
        draw_vr_headset(img)
    elif df["Eyes"][i] == "Gas Mask":
        draw_gas_mask(img, colors)
    elif df["Eyes"][i] == "Gas Mask - Icy":
        draw_gas_mask(img, ice_colors)
    elif df["Eyes"][i] == "Gas Mask - Green":
        draw_gas_mask(img, green_colors)
    elif df["Eyes"][i] == "Gas Mask - Rainbow":
        draw_gas_mask(img, rainbow_colors)
    elif df["Eyes"][i] == "Gas Mask - Warm":
        draw_gas_mask(img, warm_colors)
    elif df["Eyes"][i] == "Big Purple Shades":
        draw_big_shades(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "Small Shades - Classic":
        draw_small_shades(img, gender=df["Type"][i], dysto=False)
    elif df["Eyes"][i] == "Small Shades - Dysto":
        draw_small_shades(img, gender=df["Type"][i], dysto=True)
    elif df["Eyes"][i] == "VR Headset - Kawaii":
        draw_kawaii_vr(img, gender=df["Type"][i])
    elif df["Eyes"][i] == "Cyclops Visor":
        draw_cyclops_visor(img)

    if (df["Head"][i] == "Stuck Up Peak") & (
        df["Eyes"][i]
        in [
            "Welding Goggles - Blue - Up",
            "Welding Goggles - Pink - Up",
            "Welding Goggles - Green - Up",
        ]
    ):
        draw_peak(img)

    # draw ear traits
    if df["Earring"][i] == "None":
        draw_nothing(img)
    elif df["Earring"][i] == "Earring":
        draw_earring(img, type_=df["Type"][i])

    img.savePng(f"imgs/{i} - 2.png")
