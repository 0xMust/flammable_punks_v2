import drawSvg as draw
import random

dim = 336
p_size = int(dim / 24)
# img = draw.Drawing(dim, dim, origin="center", displayInline=False)


def hex_to_rgb(value):
    value = value.lstrip("#")
    lv = len(value)
    return tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))


def draw_pixel(img, x, y, color):
    # Draw an irregular polygon
    img.append(
        draw.Lines(
            -dim / 2 + x * dim / 24,
            dim / 2 - y * dim / 24,
            -dim / 2 + x * dim / 24,
            dim / 2 - dim / 24 - y * dim / 24,
            -dim / 2 + dim / 24 + x * dim / 24,
            dim / 2 - dim / 24 - y * dim / 24,
            -dim / 2 + dim / 24 + x * dim / 24,
            dim / 2 - y * dim / 24,
            close=False,
            fill=color,
            stroke="none",
        )
    )


skin_color_dict = {}
skin_color_dict["Pink"] = {}
skin_color_dict["Pink"]["Light"] = "#FFD6C5"
skin_color_dict["Pink"]["Midtone"] = "#E7C1B2"
skin_color_dict["Pink"]["Dark"] = "#E4BDAD"
skin_color_dict["Pale"] = {}
skin_color_dict["Pale"]["Light"] = "#FFE2C9"
skin_color_dict["Pale"]["Midtone"] = "#E7CBB5"
skin_color_dict["Pale"]["Dark"] = "#E6C8B0"
skin_color_dict["Fair"] = {}
skin_color_dict["Fair"]["Light"] = "#FFCBA3"
skin_color_dict["Fair"]["Midtone"] = "#E8B894"
skin_color_dict["Fair"]["Dark"] = "#E7B38D"
skin_color_dict["Tan"] = {}
skin_color_dict["Tan"]["Light"] = "#D8905F"
skin_color_dict["Tan"]["Midtone"] = "#C28155"
skin_color_dict["Tan"]["Dark"] = "#BE794A"
skin_color_dict["Dark"] = {}
skin_color_dict["Dark"]["Light"] = "#88513A"
skin_color_dict["Dark"]["Midtone"] = "#7B4934"
skin_color_dict["Dark"]["Dark"] = "#733E26"
skin_color_dict["Zombie"] = {}
skin_color_dict["Zombie"]["Light"] = "#597350"
skin_color_dict["Zombie"]["Midtone"] = "#72a562"
skin_color_dict["Zombie"]["Dark"] = "#000000"
skin_color_dict["Obit"] = {}
skin_color_dict["Obit"]["Light"] = "#bebebe"
skin_color_dict["Obit"]["Midtone"] = "#ffffff"
skin_color_dict["Obit"]["Dark"] = "#818181"
skin_color_dict["Alien"] = {}
skin_color_dict["Alien"]["Light"] = "#99dfe1"
skin_color_dict["Alien"]["Midtone"] = "#c8fcfc"
skin_color_dict["Alien"]["Dark"] = "#050002"
skin_color_dict["Ape"] = {}
skin_color_dict["Ape"]["Light"] = "#a98b6f"
skin_color_dict["Ape"]["Midtone"] = "#866f58"
skin_color_dict["Ape"]["Dark"] = "#a98b6f"


smoke_colors = ["#a9bad4", "#d0d0ce", "#d1e0f7"]

char_colors = ["#333333", "#414141", "#565656", "#CFCFCF", "#A8A8A8", "#777777"]

colors = ["#801100", "#B62203", "#D73502", "#FC6400", "#FF7500", "#FAC000"]

ice_colors = ["#3f7eb3", "#6ba7cc", "#aedbf0", "#fafeff", "#e2fcff", "#cbf1fa"]

green_colors = ["#006a4e", "#2e856e", "#5ca08e", "#8abaae", "#b8d5cd"]

rainbow_colors = ["#ffb3ba", "#ffdfba", "#ffffba", "#baffc9", "#bae1ff"]

warm_colors = ["#F8B195", "#F67280", "#C06C84", "#6C5B7B", "#355C7D"]


def draw_background(img):
    for a in range(24):
        for b in range(24):
            draw_pixel(img, a, b, smoke_colors[random.randrange(len(smoke_colors))])


def draw_fire_background(img):
    for a in range(24):
        for b in range(24):
            draw_pixel(img, a, b, char_colors[random.randrange(len(char_colors))])


def draw_fire(img):
    for a in range(24):
        for b in range((-2 * a ** 3 - 3 * a ** 2 + 10) % 7 + 5):
            draw_pixel(img, a, 23 - b, colors[random.randrange(len(colors))])


def draw_male_head(img, skin_color):
    skin = skin_color_dict[skin_color]["Midtone"]
    # Outline
    for h in range(10):
        draw_pixel(img, 7, 14 + h, "#000000")
    for h in range(3):
        draw_pixel(img, 6, 12 + h, "#000000")
    for h in range(5):
        draw_pixel(img, 7, 7 + h, "#000000")
    draw_pixel(img, 8, 6, "#000000")
    for w in range(7):
        draw_pixel(img, 9 + w, 5, "#000000")
    draw_pixel(img, 16, 6, "#000000")
    for h in range(13):
        draw_pixel(img, 17, 7 + h, "#000000")
    draw_pixel(img, 16, 20, "#000000")
    for w in range(5):
        draw_pixel(img, 11 + w, 21, "#000000")
    for h in range(2):
        draw_pixel(img, 11, 22 + h, "#000000")
    # Skin Color
    for h in range(2):
        draw_pixel(img, 7, 12 + h, skin)
    for h in range(17):
        draw_pixel(img, 8, 7 + h, skin)
    for h in range(18):
        for w in range(2):
            draw_pixel(img, 9 + w, 6 + h, skin)
    for h in range(15):
        for w in range(6):
            draw_pixel(img, 10 + w, 6 + h, skin)
    for h in range(13):
        draw_pixel(img, 16, 7 + h, skin)

    # Eyebrows
    for w in range(2):
        draw_pixel(img, 10 + w, 11, "#A46E32")
        draw_pixel(img, 15 + w, 11, "#A46E32")

    if skin_color in ["Zombie", "Alien"]:
        shade = "Dark"
    else:
        shade = "Light"
    # Eye Shadow
    draw_pixel(img, 11, 12, skin_color_dict[skin_color][shade])
    draw_pixel(img, 16, 12, skin_color_dict[skin_color][shade])

    # Eyes
    draw_pixel(img, 10, 12, "#000000")
    draw_pixel(img, 15, 12, "#000000")

    # Nose
    for w in range(2):
        draw_pixel(img, 13 + w, 15, "#000000")

    # Mouth
    for w in range(3):
        draw_pixel(img, 12 + w, 18, "#000000")

    # Head Shine
    for a in range(2):
        draw_pixel(img, 9 + a, 8 - a, skin_color_dict[skin_color]["Light"])


def draw_female_head(img, skin_color):
    # Outline
    for h in range(5):
        draw_pixel(img, 9, 19 + h, "#000000")
        draw_pixel(img, 8, 14 + h, "#000000")
    for h in range(3):
        draw_pixel(img, 7, 12 + h, "#000000")
    for h in range(3):
        draw_pixel(img, 8, 9 + h, "#000000")
    draw_pixel(img, 9, 8, "#000000")
    for w in range(6):
        draw_pixel(img, 10 + w, 7, "#000000")
    draw_pixel(img, 16, 8, "#000000")
    for h in range(10):
        draw_pixel(img, 17, 9 + h, "#000000")

    draw_pixel(img, 16, 19, "#000000")
    draw_pixel(img, 15, 20, "#000000")
    for w in range(3):
        draw_pixel(img, 12 + w, 21, "#000000")
    draw_pixel(img, 11, 20, "#000000")
    for h in range(2):
        draw_pixel(img, 13, 22 + h, "#000000")

    # Skin Color
    for h in range(2):
        draw_pixel(img, 8, 12 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(10):
        for w in range(8):
            draw_pixel(img, 9 + w, 9 + h, skin_color_dict[skin_color]["Midtone"])
    for w in range(6):
        draw_pixel(img, 10 + w, 8, skin_color_dict[skin_color]["Midtone"])
        draw_pixel(img, 10 + w, 19, skin_color_dict[skin_color]["Midtone"])
    for w in range(3):
        draw_pixel(img, 12 + w, 20, skin_color_dict[skin_color]["Midtone"])
    for h in range(4):
        draw_pixel(img, 10, 20 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(3):
        draw_pixel(img, 11, 21 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(2):
        draw_pixel(img, 12, 22 + h, skin_color_dict[skin_color]["Midtone"])

    # Eyebrows
    for w in range(2):
        draw_pixel(img, 10 + w, 12, "#A46E32")
        draw_pixel(img, 15 + w, 12, "#A46E32")

    # Eye Shadow
    draw_pixel(img, 11, 13, skin_color_dict[skin_color]["Dark"])
    draw_pixel(img, 16, 13, skin_color_dict[skin_color]["Dark"])

    # Eyes
    draw_pixel(img, 10, 13, "#000000")
    draw_pixel(img, 15, 13, "#000000")

    # Nose
    draw_pixel(img, 13, 16, "#000000")

    # Mouth
    for w in range(3):
        draw_pixel(img, 12 + w, 18, "#B60033")

    # Head Shine
    draw_pixel(img, 10, 9, skin_color_dict[skin_color]["Light"])


def draw_male_obit_head(img, skin_color="Obit"):
    for h in range(9):
        draw_pixel(img, 8, 15 + h, "#000000")
        draw_pixel(img, 7, 7 + h, "#000000")
    draw_pixel(img, 8, 6, "#000000")
    for w in range(7):
        draw_pixel(img, 9 + w, 5, "#000000")
    draw_pixel(img, 16, 6, "#000000")
    for h in range(10):
        draw_pixel(img, 17, 7 + h, "#000000")
    for h in range(4):
        draw_pixel(img, 16, 17 + h, "#000000")
    for w in range(6):
        draw_pixel(img, 10 + w, 21, "#000000")
    for h in range(3):
        draw_pixel(img, 10, 21 + h, "#000000")

    for h in range(8):
        draw_pixel(img, 8, 7 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(18):
        draw_pixel(img, 9, 6 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(15):
        for w in range(6):
            draw_pixel(img, 10 + w, 6 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(10):
        draw_pixel(img, 16, 7 + h, skin_color_dict[skin_color]["Midtone"])

    # for w in range(3):
    #    draw_pixel(img, 8+w,22,'#dfdfdf')

    for a in range(3):
        draw_pixel(img, 9 + a, 16 + a, "#000000")
    for w in range(2):
        draw_pixel(img, 13 + 2 * w, 18, "#000000")
        draw_pixel(img, 12 + 2 * w, 19, skin_color_dict[skin_color]["Light"])

    for h in range(2):
        draw_pixel(img, 13, 14 + h, "#000000")
    draw_pixel(img, 14, 15, skin_color_dict[skin_color]["Light"])

    for w in range(2):
        draw_pixel(img, 10 + 5 * w, 12, "#000000")
        draw_pixel(img, 11 + 5 * w, 12, skin_color_dict[skin_color]["Light"])
        for v in range(2):
            draw_pixel(img, 10 + 5 * w + v, 11, skin_color_dict[skin_color]["Dark"])


def draw_female_obit_head(img):
    for h in range(4):
        draw_pixel(img, 10, 20 + h, "#000000")
        draw_pixel(img, 9, 16 + h, "#000000")
    for h in range(8):
        draw_pixel(img, 8, 9 + h, "#000000")
    draw_pixel(img, 9, 8, "#000000")
    for w in range(6):
        draw_pixel(img, 10 + w, 7, "#000000")
    draw_pixel(img, 16, 8, "#000000")
    for h in range(8):
        draw_pixel(img, 17, 9 + h, "#000000")
    for h in range(3):
        draw_pixel(img, 16, 17 + h, "#000000")
    draw_pixel(img, 15, 20, "#000000")
    for w in range(3):
        draw_pixel(img, 12 + w, 21, "#000000")
    for h in range(3):
        draw_pixel(img, 12, 21 + h, "#000000")

    for h in range(7):
        draw_pixel(img, 9, 9 + h, "#ffffff")
    for h in range(12):
        draw_pixel(img, 10, 8 + h, "#ffffff")
    for h in range(16):
        draw_pixel(img, 11, 8 + h, "#ffffff")
    for h in range(13):
        for w in range(3):
            draw_pixel(img, 12 + w, 8 + h, "#ffffff")
    for h in range(12):
        draw_pixel(img, 15, 8 + h, "#ffffff")
    for h in range(8):
        draw_pixel(img, 16, 9 + h, "#ffffff")

    for a in range(2):
        draw_pixel(img, 10 + a, 17 + a, "#000000")
    for w in range(2):
        draw_pixel(img, 13 + 2 * w, 18, "#000000")
        draw_pixel(img, 12 + 2 * w, 19, "#bebebe")

    for h in range(2):
        draw_pixel(img, 13, 15 + h, "#000000")
    draw_pixel(img, 14, 16, "#bebebe")

    for w in range(2):
        draw_pixel(img, 10 + 5 * w, 13, "#000000")
        draw_pixel(img, 11 + 5 * w, 13, "#bebebe")
        for v in range(2):
            draw_pixel(img, 10 + 5 * w + v, 12, "#818181")


def draw_beard(img):
    draw_pixel(img, 8, 15, "#997c5a")
    for w in range(2):
        draw_pixel(img, 8 + w, 16, "#997c5a")
    for w in range(2):
        draw_pixel(img, 8 + w, 16, "#997c5a")
    draw_pixel(img, 16, 16, "#997c5a")
    for w in range(9):
        draw_pixel(img, 8 + w, 17, "#997c5a")
    for w in range(4):
        draw_pixel(img, 8 + w, 18, "#997c5a")
    for w in range(2):
        draw_pixel(img, 15 + w, 18, "#997c5a")
    for w in range(8):
        draw_pixel(img, 9 + w, 19, "#997c5a")
    for w in range(6):
        draw_pixel(img, 10 + w, 20, "#997c5a")


def draw_explosion_hair(img, hair_color):
    for w in range(5):
        for a in range(5):
            draw_pixel(img, 9 - a + 2 * w, 7 - a, hair_color)
    for h in range(2):
        for a in range(7):
            draw_pixel(img, 9 - a, 9 - a + 2 * h, hair_color)
    for h in range(2):
        for a in range(3):
            draw_pixel(img, 6 - a, 11 - a + 2 * h, hair_color)
    for a in range(5):
        draw_pixel(img, 7 - a, 10 - a, hair_color)
    for h in range(4):
        for w in range(5):
            draw_pixel(img, 9 + 2 * w, 2 + 2 * h, hair_color)
    for h in range(3):
        for w in range(3):
            draw_pixel(img, 8 + 3 * w, 2 + 3 * h, hair_color)
    for h in range(4):
        for a in range(2):
            draw_pixel(img, 17 - a, 3 - 2 * a + 2 * h, hair_color)
    for w in range(3):
        for h in range(8):
            draw_pixel(img, 6 + w, 5 + h, hair_color)
    for w in range(8):
        for h in range(2):
            draw_pixel(img, 6 + w, 4 + h, hair_color)


def draw_fireman_hat(img, hat_color, badge_color):
    # firemans hat
    if hat_color == "Red":
        color_code = "#EE4B2B"
    if hat_color == "Yellow":
        color_code = "#FFCC00"
    for w in range(3):
        for h in range(2):
            draw_pixel(img, 7 + 2 * w + h, 10 - w, color_code)
        draw_pixel(img, 13 + w, 8, color_code)
        draw_pixel(img, 16 + w, 8 + w, color_code)
    for a in range(4):
        draw_pixel(img, 7, 6 + a, color_code)
        draw_pixel(img, 17, 5 + a, color_code)
        for w in range(2):
            draw_pixel(img, 7 + 2 * a + w, 5 - a, color_code)
    for a in range(3):
        draw_pixel(img, 15 + a, 2 + a, color_code)
        draw_pixel(img, 13 + a, 3, color_code)
    for hat_fill in range(6):
        draw_pixel(img, 11 + hat_fill, 4, color_code)
    for hat_fill in range(8):
        draw_pixel(img, 9 + hat_fill, 5, color_code)
    for hat_fill in range(9):
        for hat_height in range(2):
            draw_pixel(img, 8 + hat_fill, 6 + hat_height, color_code)
    for hat_fill in range(3):
        draw_pixel(img, 8 + hat_fill, 8, color_code)
    for hat_fill in range(6):
        draw_pixel(img, 11 + hat_fill, 9, color_code)
    draw_pixel(img, 8, 9, color_code)
    draw_pixel(img, 6, 10, color_code)

    # fireman hat badge
    if badge_color == "Gold":
        color_0 = "#FDDF00"
        color_1 = "#D4AF37"
        color_2 = "#996515"
    if badge_color == "Silver":
        color_0 = "#CCCCCC"
        color_1 = "#D8D8D8"
        color_2 = "#AFB1AE"
    for w in range(4):
        draw_pixel(img, 13 + w, 7, color_0)
    for h in range(2):
        draw_pixel(img, 13, 5 + h, color_0)
        draw_pixel(img, 16, 5 + h, color_0)
    for w in range(2):
        for h in range(3):
            draw_pixel(img, 14 + w, 4 + h, color_0)
    draw_pixel(img, 15, 5, color_1)
    draw_pixel(img, 14, 6, color_1)
    draw_pixel(img, 14, 5, color_2)
    draw_pixel(img, 15, 6, color_2)


def draw_gas_mask(img, glass_colors):
    for w in range(8):
        draw_pixel(img, 10 + w, 9, "#304056")
    for w in range(10):
        draw_pixel(img, 9 + w, 10, "#304056")
    for w in range(12):
        for h in range(4):
            draw_pixel(img, 8 + w, 11 + h, "#304056")
    for w in range(10):
        draw_pixel(img, 9 + w, 15, "#304056")
    for w in range(8):
        for h in range(3):
            draw_pixel(img, 10 + w, 16 + h, "#304056")
    for w in range(6):
        draw_pixel(img, 11 + w, 19, "#304056")
    for w in range(4):
        draw_pixel(img, 12 + w, 20, "#304056")
    for w in range(2):
        draw_pixel(img, 11 + w, 10, glass_colors[0])
        draw_pixel(img, 16 + w, 10, glass_colors[0])
        draw_pixel(img, 11 + w, 14, glass_colors[4])
        draw_pixel(img, 16 + w, 14, glass_colors[4])
    for w in range(4):
        for h in range(3):
            draw_pixel(img, 10 + w, 11 + h, glass_colors[h + 1])
            draw_pixel(img, 15 + w, 11 + h, glass_colors[h + 1])
    for w in range(3):
        draw_pixel(img, 13 + w, 15, "#131313")
        draw_pixel(img, 13 + w, 19, "#131313")
    for w in range(5):
        for h in range(3):
            draw_pixel(img, 12 + w, 16 + h, "#131313")
    for h in range(2):
        draw_pixel(img, 14, 16 + h, "#253042")
    draw_pixel(img, 13, 18, "#253042")
    draw_pixel(img, 15, 18, "#253042")


def draw_welders_goggles(img, glass_color):
    for w in range(3):
        draw_pixel(img, 10 + w, 10, "#3A3B3C")
        draw_pixel(img, 15 + w, 10, "#3A3B3C")
        draw_pixel(img, 10 + w, 13, "#3A3B3C")
        draw_pixel(img, 15 + w, 13, "#3A3B3C")
    for w in range(10):
        draw_pixel(img, 9 + w, 12, "#3A3B3C")
    for w in range(12):
        draw_pixel(img, 7 + w, 11, "#3A3B3C")
    for w in range(2):
        for h in range(2):
            draw_pixel(img, 11 + w, 11 + h, glass_color)
            draw_pixel(img, 16 + w, 11 + h, glass_color)


def draw_earring(img, type_):
    # earring
    if type_ in ["Male", "Zombie", "Alien", "Ape"]:
        draw_pixel(img, 6, 14, "#ffd823")
        draw_pixel(img, 5, 14, "#000000")
        draw_pixel(img, 6, 13, "#000000")
        draw_pixel(img, 6, 15, "#000000")
    elif type_ == "Female":
        draw_pixel(img, 7, 14, "#ffd823")
        draw_pixel(img, 6, 14, "#000000")
        draw_pixel(img, 7, 13, "#000000")
        draw_pixel(img, 7, 15, "#000000")


def draw_nothing(img):
    None


def draw_soot(img):
    # soot
    for h in range(3):
        for w in range(2):
            draw_pixel(img, 10 + w, 14 + h, "#5d5c5e")
        draw_pixel(img, 16, 14 + h, "#5d5c5e")
    for w in range(3):
        draw_pixel(img, 12 + w, 10, "#5d5c5e")


def draw_cig(img):
    # cigarette
    for w in range(6):
        draw_pixel(img, 14 + w, 17, "#000000")
        draw_pixel(img, 14 + w, 19, "#000000")
    draw_pixel(img, 20, 18, "#000000")
    for w in range(5):
        draw_pixel(img, 14 + w, 18, "#ffffff")
    draw_pixel(img, 19, 18, "#e3532a")
    # for h in range(6):
    #    draw_pixel(img, 19,10+h,'#afc4d2')


def draw_marshall_cap(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    # fire marshall's cap
    for w in range(9):
        draw_pixel(img, 8 + w, 4 + num, "#eefe82")
    for w in range(11):
        for h in range(4):
            draw_pixel(img, 7 + w, 5 + h + num, "#eefe82")
    for w in range(15):
        draw_pixel(img, 7 + w, 9 + num, "#eefe82")

    for w in range(9):
        for h in range(3):
            draw_pixel(img, 9 + w, 6 + h + num, "#f2554b")

    for w in range(7):
        for h in range(1):
            draw_pixel(img, 10 + w, 7 + h + num, "#c8c7c8")


def draw_welders_on_head(img, glass_color):
    # welders goggles on head
    for w in range(3):
        draw_pixel(img, 10 + w, 5, "#3A3B3C")
        draw_pixel(img, 15 + w, 5, "#3A3B3C")
        draw_pixel(img, 10 + w, 8, "#3A3B3C")
        draw_pixel(img, 15 + w, 8, "#3A3B3C")
    for w in range(10):
        for h in range(2):
            draw_pixel(img, 9 + w, 6 + h, "#3A3B3C")
    for w in range(2):
        draw_pixel(img, 7 + w, 8 - w, "#3A3B3C")
    for w in range(2):
        for h in range(2):
            draw_pixel(img, 11 + w, 6 + h, glass_color)
            draw_pixel(img, 16 + w, 6 + h, glass_color)


def draw_reflective_goggles(img):
    for w in range(12):
        draw_pixel(img, 8 + w, 10, "#32527b")
    draw_pixel(img, 8, 11, "#32527b")
    for h in range(3):
        draw_pixel(img, 9, 11 + h, "#32527b")
        draw_pixel(img, 19, 11 + h, "#32527b")
    for w in range(3):
        draw_pixel(img, 10 + w, 14, "#32527b")
        draw_pixel(img, 16 + w, 14, "#32527b")
    for w in range(3):
        draw_pixel(img, 13 + w, 13, "#32527b")

    for h in range(3):
        draw_pixel(img, 10, 11 + h, colors[0])
        draw_pixel(img, 18, 11 + h, colors[0])
    draw_pixel(img, 11, 11, colors[0])
    draw_pixel(img, 17, 11, colors[0])

    for h in range(2):
        draw_pixel(img, 11, 12 + h, colors[1])
        draw_pixel(img, 17, 12 + h, colors[1])
    draw_pixel(img, 12, 11, colors[1])
    draw_pixel(img, 16, 11, colors[1])

    for h in range(2):
        draw_pixel(img, 12, 12 + h, colors[2])
        draw_pixel(img, 16, 12 + h, colors[2])
    for w in range(3):
        draw_pixel(img, 13 + w, 11, colors[2])
        draw_pixel(img, 13 + w, 12, colors[3])


light_colors = ["#fdfbd3", "#ffffe0", "#fff5b6"]


def draw_oxygen_helmet(img, helmet_color):
    for w in range(3):
        draw_pixel(img, 9 + w, 8, helmet_color)
    for w in range(4):
        draw_pixel(img, 11 + w, 9, helmet_color)
    for a in range(3):
        draw_pixel(img, 15 + a, 9 - a, helmet_color)

    for a in range(3):
        draw_pixel(img, 7 + a, 10 + 3 * a, helmet_color)
        draw_pixel(img, 7 + a, 11 + 3 * a, helmet_color)
        draw_pixel(img, 7 + a, 12 + 3 * a, helmet_color)
    for a in range(3):
        draw_pixel(img, 10 + a, 19 + a, helmet_color)
    for w in range(3):
        draw_pixel(img, 13 + w, 21, helmet_color)
    for a in range(2):
        draw_pixel(img, 16 + a, 20 - a, helmet_color)
    for a in range(2):
        draw_pixel(img, 7 + a, 9 - a, helmet_color)

    for h in range(8):
        draw_pixel(img, 6, 4 + h, helmet_color)
    for a in range(2):
        draw_pixel(img, 7 + 3 * a, 4 - a, helmet_color)
        draw_pixel(img, 8 + 3 * a, 4 - a, helmet_color)
        draw_pixel(img, 9 + 3 * a, 4 - a, helmet_color)
        draw_pixel(img, 10 + 3 * a, 4 - a, helmet_color)
    for a in range(4):
        draw_pixel(img, 14 + a, 3 + a, helmet_color)
    for w in range(4):
        draw_pixel(img, 11 + w, 4, helmet_color)
    for w in range(9):
        draw_pixel(img, 7 + w, 5, helmet_color)
    for w in range(10):
        for h in range(3):
            draw_pixel(img, 7 + w, 6 + h, helmet_color)
    for h in range(2):
        draw_pixel(img, 7, 13 + h, helmet_color)
    draw_pixel(img, 8, 16, helmet_color)

    for h in range(2):
        draw_pixel(img, 9, 14 + h, "#028A0F")
    for h in range(4):
        draw_pixel(img, 10, 15 + h, "#028A0F")
    for h in range(4):
        draw_pixel(img, 8, 9 + h, "#028A0F")
    for h in range(11):
        draw_pixel(img, 17, 8 + h, "#028A0F")
    for w in range(2):
        draw_pixel(img, 9 + w, 9, "#028A0F")
    for w in range(6):
        draw_pixel(img, 10 + w, 10, "#028A0F")
    draw_pixel(img, 16, 9, "#028A0F")
    draw_pixel(img, 16, 19, "#028A0F")
    draw_pixel(img, 11, 19, "#028A0F")
    for w in range(4):
        draw_pixel(img, 12 + w, 20, "#028A0F")
    draw_pixel(img, 8, 13, "#028A0F")

    # for a in range(3):
    #    draw_pixel(img, 7+a,5+a,'#D3D3D3')
    #    draw_pixel(img, 8+a,5+a,'#D3D3D3')
    #    draw_pixel(img, 9+a,5+a,'#D3D3D3')

    for h in range(2):
        draw_pixel(img, 13, 22 + h, "#000000")
        draw_pixel(img, 14, 22 + h, "#000000")

    for a in range(6):
        for h in range(3):
            draw_pixel(
                img,
                18 + a,
                6 + h + a,
                light_colors[random.randrange(len(light_colors))],
            )
    for a in range(3):
        for h in range(1):
            draw_pixel(
                img,
                18 + 2 * a,
                7 + h + a,
                light_colors[random.randrange(len(light_colors))],
            )
            draw_pixel(
                img,
                19 + 2 * a,
                7 + h + a,
                light_colors[random.randrange(len(light_colors))],
            )
    draw_pixel(img, 23, 10, light_colors[random.randrange(len(light_colors))])


def draw_marshall_cap_backwards(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    # fire marshall's cap
    for w in range(9):
        draw_pixel(img, 8 + w, 4 + num, "#eefe82")
    for w in range(11):
        for h in range(2):
            draw_pixel(img, 7 + w, 5 + h + num, "#eefe82")
    for w in range(7):
        draw_pixel(img, 7 + w, 7 + num, "#eefe82")
    for w in range(7):
        draw_pixel(img, 7 + w, 8 + num, "#eefe82")
    for h in range(2):
        draw_pixel(img, 17, 7 + h + num, "#eefe82")
    for w in range(15):
        draw_pixel(img, 3 + w, 9 + num, "#eefe82")


def draw_zombie_head(img):
    draw_male_head(img, "Zombie")
    draw_pixel(img, 10, 12, "#fb0002")
    draw_pixel(img, 15, 12, "#fb0002")
    for w in range(2):
        draw_pixel(img, 10 + w, 11, "#5f7055")
        draw_pixel(img, 15 + w, 11, "#5f7055")
    draw_pixel(img, 10, 13, "#5f7055")
    draw_pixel(img, 15, 13, "#5f7055")
    draw_pixel(img, 12, 19, "#5f7055")


def draw_zombie_obit_head(img):
    draw_male_obit_head(img, "Zombie")
    for w in range(2):
        draw_pixel(img, 10 + w, 11, "#5f7055")
        draw_pixel(img, 15 + w, 11, "#5f7055")
    draw_pixel(img, 10, 12, "#fd0002")
    draw_pixel(img, 15, 12, "#fd0002")
    draw_pixel(img, 11, 12, "#000000")
    draw_pixel(img, 16, 12, "#000000")
    draw_pixel(img, 10, 13, "#5f7055")
    draw_pixel(img, 15, 13, "#5f7055")


def draw_alien_head(img):
    draw_male_head(img, skin_color="Alien")
    for w in range(2):
        draw_pixel(img, 11 + 5 * w, 12, "#96e1e1")
        draw_pixel(img, 10 + 5 * w, 11, "#72bdbd")
        draw_pixel(img, 11 + 5 * w, 11, "#060000")
        draw_pixel(img, 11 + 4 * w, 18, "#000000")
        draw_pixel(img, 6 - w, 11 + w, "#000000")
    for h in range(3):
        draw_pixel(img, 13, 14 + h, "#9ae0e1")
    draw_pixel(img, 14, 15, "#c8fcfc")
    draw_pixel(img, 6, 12, "#c8fafe")
    draw_pixel(img, 7, 12, "#9be0de")


def draw_alien_obit_head(img):
    draw_male_obit_head(img, skin_color="Alien")
    for w in range(2):
        draw_pixel(img, 11 + 5 * w, 12, "#96e1e1")
        draw_pixel(img, 10 + 5 * w, 11, "#72bdbd")
        draw_pixel(img, 11 + 5 * w, 11, "#060000")
        draw_pixel(img, 11 + 4 * w, 18, "#000000")
    for h in range(2):
        draw_pixel(img, 13, 14 + h, "#000000")
    draw_pixel(img, 13, 16, "#9ae0e1")
    draw_pixel(img, 14, 15, "#c8fcfc")


def draw_ape_head(img):
    draw_male_head(img, skin_color="Ape")
    for w in range(2):
        draw_pixel(img, 10 + w, 11, "#69553c")
        draw_pixel(img, 15 + w, 11, "#69553c")
        draw_pixel(img, 11 + w * 4, 18, "#000000")
    draw_pixel(img, 12, 15, "#000000")
    draw_pixel(img, 13, 15, "#876f57")
    for h in range(2):
        draw_pixel(img, 7, 12 + h, "#352410")
    for h in range(17):
        draw_pixel(img, 8, 7 + h, "#352410")
    for w in range(7):
        draw_pixel(img, 9 + w, 6, "#352410")
    for w in range(8):
        for h in range(3):
            draw_pixel(img, 9 + w, 7 + h, "#352410")
    for h in range(9):
        draw_pixel(img, 9, 15 + h, "#352410")
    for h in range(3):
        draw_pixel(img, 10, 21 + h, "#352410")
    draw_pixel(img, 10, 16, "#352410")
    draw_pixel(img, 16, 16, "#352410")
    for h in range(2):
        draw_pixel(img, 9, 18 + h, "#000000")
    draw_pixel(img, 10, 20, "#000000")
    for w in range(6):
        draw_pixel(img, 10 + w, 9, "#000000")
    # for a in range(2):
    #    draw_pixel(img, 9+a,8-a,'#69553c')


def draw_ape_obit_head(img):
    skin_color = "Obit"

    draw_pixel(img, 8, 15, "#000000")
    for h in range(9):
        draw_pixel(img, 8, 15 + h, "#000000")
    for h in range(9):
        draw_pixel(img, 7, 7 + h, "#000000")
    draw_pixel(img, 8, 6, "#000000")
    for w in range(7):
        draw_pixel(img, 9 + w, 5, "#000000")
    draw_pixel(img, 16, 6, "#000000")
    for h in range(9):
        draw_pixel(img, 17, 7 + h, "#000000")
    # for h in range(2):
    #    draw_pixel(img, 17,15+h,'#000000')
    # for h in range(3):
    #    draw_pixel(img, 16,17+h,'#000000')

    # draw_pixel(img, 16,20,'#000000')
    for w in range(5):
        draw_pixel(img, 10 + w, 21, "#000000")
    for h in range(3):
        draw_pixel(img, 10, 21 + h, "#000000")

    for h in range(8):
        draw_pixel(img, 8, 7 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(18):
        draw_pixel(img, 9, 6 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(15):
        for w in range(6):
            draw_pixel(img, 10 + w, 6 + h, skin_color_dict[skin_color]["Midtone"])
    for h in range(13):
        draw_pixel(img, 16, 7 + h, skin_color_dict[skin_color]["Midtone"])
    # for h in range(3):
    #    draw_pixel(img, 16,17+h,skin_color_dict[skin_color]['Midtone'])

    for h in range(2):
        draw_pixel(img, 16, 16 + h, "#000000")

    for a in range(3):
        draw_pixel(img, 9 + a, 16 + a, "#000000")
    for w in range(2):
        draw_pixel(img, 13 + 2 * w, 18, "#000000")
        draw_pixel(img, 12 + 2 * w, 17, skin_color_dict[skin_color]["Light"])

    draw_pixel(img, 14, 15, skin_color_dict[skin_color]["Light"])

    for w in range(2):
        draw_pixel(img, 10 + 5 * w, 12, "#000000")
        draw_pixel(img, 11 + 5 * w, 12, skin_color_dict[skin_color]["Light"])
        for v in range(2):
            draw_pixel(img, 10 + 5 * w + v, 11, skin_color_dict[skin_color]["Dark"])

    draw_pixel(img, 12, 14, "#000000")
    draw_pixel(img, 14, 14, "#000000")
    draw_pixel(img, 12, 15, skin_color_dict[skin_color]["Light"])
    draw_pixel(img, 14, 15, skin_color_dict[skin_color]["Light"])

    for a in range(2):
        draw_pixel(img, 15 + a, 20 - a, "#000000")
    draw_pixel(img, 16, 18, "#000000")


def draw_beanie(img, beanie_color="#cb4d12", darker_color="#943608"):
    for w in range(7):
        draw_pixel(img, 9 + w, 6, beanie_color)
    for w in range(9):
        draw_pixel(img, 8 + w, 7, beanie_color)
    for w in range(11):
        for h in range(2):
            draw_pixel(img, 7 + w, 8 + h, beanie_color)
    for a in range(2):
        draw_pixel(img, 7 + a, 7 - a, "#000000")
    for a in range(2):
        draw_pixel(img, 16 + a, 6 + a, "#000000")
    for w in range(7):
        draw_pixel(img, 9 + w, 5, "#000000")
    for w in range(2):
        for h in range(2):
            draw_pixel(img, 6 + 12 * w, 8 + h, "#000000")
    for w in range(11):
        draw_pixel(img, 7 + w, 8, darker_color)
    for w in range(6):
        draw_pixel(img, 7 + 2 * w, 9, darker_color)


def draw_covid_mask(img, alive="Alive"):
    r = 2
    if alive == "Dead":
        r = 1
    for w in range(6):
        for h in range(5):
            draw_pixel(img, 10 + w, 15 + h, "#c9c9c9")
    for w in range(4):
        draw_pixel(img, 11 + w, 20, "#c9c9c9")

    for a in range(3 - (2 - r)):
        draw_pixel(img, 7 + (2 - r) + a, 12 + (2 - r) + a, "#c9c9c9")

    for w in range(2 - (2 - r)):
        draw_pixel(img, 8 + (2 - r) + w, 18, "#c9c9c9")

    for h in range(r):
        draw_pixel(img, 16, 14 + 4 * h, "#c9c9c9")

    for w in range(2):
        draw_pixel(img, 10 + 5 * w, 17, "#b2b1af")
    draw_pixel(img, 13, 15, "#b2b1af")


def draw_gold_chain(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    for a in range(3):
        draw_pixel(img, 8 + a + 2 * num, 20 + a + num, "#ffd823")


def draw_silver_chain(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 2
    for w in range(3):
        draw_pixel(img, 8 + num + w, 22, "#dfdfdf")


def draw_3d_glasses(img):
    glass_color = ["#328efd", "#f73535"]
    for start in range(3):
        for w in range(11 - start):
            if start == 2:
                height = 2
            else:
                height = 1
            for h in range(height):
                draw_pixel(img, 7 + start + w, 10 + start + h, "#ffffff")
    for place in range(2):
        for w in range(3):
            for h in range(2):
                draw_pixel(img, 10 + w + 4 * place, 11 + h, glass_color[place])


def draw_hoodie(img, gender="Male", alive="Alive"):
    num = 0
    if gender == "Female":
        num = 1
    # hoodie color
    for h in range(3):
        draw_pixel(img, 6 + num, 21 + h, "#4e4d4c")
    for h in range(2):
        draw_pixel(img, 5 + num, 19 + h, "#4e4d4c")
    for h in range(5):
        draw_pixel(img, 4 + num, 14 + h, "#4e4d4c")
    for h in range(3):
        draw_pixel(img, 5 + num, 11 + h, "#4e4d4c")
    for h in range(4):
        draw_pixel(img, 6 + num, 8 + h, "#4e4d4c")
    for h in range(3):
        for a in range(2):
            draw_pixel(img, 7 + a + num, 7 - a + h, "#4e4d4c")
        for w in range(7):
            draw_pixel(img, 9 + w + num, 5 + h, "#4e4d4c")
    for w in range(3):
        draw_pixel(img, 11 + w + num, 4, "#4e4d4c")
    for h in range(3):
        for a in range(2):
            draw_pixel(img, 16 + a + num, 6 + a + h, "#4e4d4c")
    for h in range(4):
        draw_pixel(img, 18 + num, 8 + h, "#4e4d4c")
    for h in range(3):
        draw_pixel(img, 19 + num, 11 + h, "#4e4d4c")
    for h in range(5):
        draw_pixel(img, 20 + num, 14 + h, "#4e4d4c")
    for a in range(3):
        draw_pixel(img, 19 - a + num, 19 + a, "#4e4d4c")
    for w in range(3):
        draw_pixel(img, 14 + w + num, 22, "#4e4d4c")
    draw_pixel(img, 13 + num, 23, "#4e4d4c")

    # inside hoodie
    for h in range(10):
        draw_pixel(img, 7 + num, 14 + h, "#000000")
    for h in range(9):
        draw_pixel(img, 6 + num, 12 + h, "#000000")
    for h in range(5):
        draw_pixel(img, 5 + num, 14 + h, "#000000")
    for h in range(2):
        draw_pixel(img, 7 + num, 10 + h, "#000000")
    draw_pixel(img, 8 + num, 9, "#000000")
    for w in range(7):
        draw_pixel(img, 9 + w + num, 8, "#000000")
    draw_pixel(img, 16 + num, 9, "#000000")
    for h in range(11):
        draw_pixel(img, 17 + num, 10 + h, "#000000")
    for h in range(8):
        draw_pixel(img, 18 + num, 12 + h, "#000000")
    for h in range(5):
        draw_pixel(img, 19 + num, 14 + h, "#000000")
    draw_pixel(img, 16 + num, 20, "#000000")
    for w in range(6):
        draw_pixel(img, 11 + w + num, 21, "#000000")
    for a in range(2):
        for w in range(3 - a - num):
            draw_pixel(img, 11 + w + 2 * num, 22 + a, "#000000")

    # outside hoodie
    for h in range(3):
        draw_pixel(img, 5 + num, 21 + h, "#000000")
    for h in range(2):
        draw_pixel(img, 4 + num, 19 + h, "#000000")
    for h in range(5):
        draw_pixel(img, 3 + num, 14 + h, "#000000")
    for h in range(3):
        draw_pixel(img, 4 + num, 11 + h, "#000000")
    for h in range(3):
        draw_pixel(img, 5 + num, 8 + h, "#000000")
    for a in range(3):
        draw_pixel(img, 6 + a + num, 7 - a, "#000000")
    for w in range(2):
        draw_pixel(img, 9 + w + num, 4, "#000000")
    for w in range(3):
        draw_pixel(img, 11 + w + num, 3, "#000000")
    for w in range(2):
        draw_pixel(img, 14 + w + num, 4, "#000000")
    for a in range(3):
        draw_pixel(img, 16 + a + num, 5 + a, "#000000")
    for h in range(3):
        draw_pixel(img, 19 + num, 8 + h, "#000000")
    for h in range(3):
        draw_pixel(img, 20 + num, 11 + h, "#000000")
    for h in range(5):
        draw_pixel(img, 21 + num, 14 + h, "#000000")
    for a in range(4):
        draw_pixel(img, 20 - a + num, 19 + a, "#000000")
    for w in range(3):
        draw_pixel(img, 14 + w + num, 23, "#000000")

    if gender == "Female":
        for a in range(2):
            draw_pixel(img, 16 + a, 20 - a, "#000000")
        if alive == "Dead":
            for h in range(2):
                draw_pixel(img, 17, 17 + h, "#000000")
            for h in range(4):
                draw_pixel(img, 9, 20 + h, "#000000")


def draw_mcdonalds_cap(img):
    for w in range(6):
        draw_pixel(img, 10 + w, 5, "#ca1011")
    for w in range(8):
        draw_pixel(img, 9 + w, 6, "#ca1011")
    for w in range(10):
        for h in range(2):
            draw_pixel(img, 8 + w, 7 + h, "#ca1011")
    for w in range(13):
        draw_pixel(img, 8 + w, 9, "#ca1011")

    for h in range(3):
        draw_pixel(img, 7, 7 + h, "#b40002")
    for a in range(2):
        draw_pixel(img, 9 - a, 5 + a, "#b40002")
    draw_pixel(img, 10, 9, "#b40002")
    for w in range(7):
        draw_pixel(img, 11 + w, 8, "#b40002")
    for a in range(5):
        draw_pixel(img, 11 + a, 7 - a % 2, "#f9c200")
    for w in range(3):
        draw_pixel(img, 11 + 2 * w, 8, "#ff9e01")


def draw_bucket_hat(img, color_set):
    for w in range(15):
        draw_pixel(img, 5 + w, 10, "#000000")
    for w in range(13):
        draw_pixel(img, 6 + w, 9, "#000000")
    for w in range(11):
        draw_pixel(img, 7 + w, 8, color_set[random.randrange(len(color_set))])
        for h in range(3):
            draw_pixel(img, 7 + w, 7 - h, "#000000")
    for w in range(9):
        draw_pixel(img, 8 + w, 4, "#000000")
    for w in range(5):
        draw_pixel(img, 8 + 2 * w, 7, color_set[random.randrange(len(color_set))])


def draw_square_shades(img, gender="Male"):
    gender_height = 0
    if gender == "Female":
        gender_height = 1
    for w in range(11 - gender_height):
        draw_pixel(img, 7 + w + gender_height, 11 + gender_height, "#000000")
    draw_pixel(img, 7 + gender_height, 12 + gender_height, "#000000")
    for w in range(2):
        for a in range(2):
            for h in range(2):
                draw_pixel(img, 11 - w + (5) * a, 12 + gender_height + h, "#000000")


def draw_thug_life_shades(img, gender="Male"):
    gender_height = 0
    if gender == "Female":
        gender_height = 1
    for w in range(12):
        draw_pixel(img, 7 + w, 11 + gender_height, "#000000")
        for i in range(2):
            for w in range(4):
                draw_pixel(img, 9 + 6 * i + w, 12 + gender_height, "#000000")
            for w in range(2):
                draw_pixel(img, 10 + 6 * i + w, 13 + gender_height, "#000000")


def draw_pipe(img):
    brown = "#855115"
    outline = "#000002"
    dark_brown = "#683c0a"
    smoke = "#dcdcdc"
    color_list = [outline, brown]
    for i in range(4):
        draw_pixel(img, 15 + i, 18 + i, outline)
    for i in range(4):
        draw_pixel(img, 15 + i, 19 + i, brown)
    for i in range(5):
        draw_pixel(img, 14 + i, 19 + i, outline)
    for h in range(3):
        draw_pixel(img, 19, 19 + h, outline)
    for w in range(3):
        draw_pixel(img, 19 + w, 23, outline)
    for w in range(4):
        draw_pixel(img, 20 + w, 19, outline)
    for h in range(2):
        draw_pixel(img, 23, 20 + h, outline)
    draw_pixel(img, 22, 22, outline)
    for w in range(3):
        draw_pixel(img, 19 + w, 22, brown)
    for w in range(3):
        for h in range(2):
            draw_pixel(img, 20 + w, 20 + h, brown)
    for w in range(3):
        draw_pixel(img, 20 + w, 21 + w % 2, dark_brown)
    for h in range(3):
        draw_pixel(img, 21, 13 + 2 * h, smoke)
    for h in range(2):
        for w in range(3):
            draw_pixel(img, 20 + w, 12 - h % 2, smoke)


def draw_turned_up_peak(img):
    for w in range(13):
        draw_pixel(img, 7 + w, 9, "#000000")
    for w in range(7):
        draw_pixel(img, 11 + w, 7, "#000000")
    for i in range(5):
        draw_pixel(img, 15 + i, 4 + i, "#000000")
    draw_pixel(img, 10, 8, "#000000")
    for h in range(3):
        draw_pixel(img, 7, 6 + h, "#000000")
    draw_pixel(img, 8, 5, "#000000")
    for w in range(6):
        draw_pixel(img, 9 + w, 4, "#000000")

    for w in range(8):
        draw_pixel(img, 11 + w, 8, "#353535")

    for w in range(7):
        draw_pixel(img, 9 + w, 5, "#515151")
    for w in range(9):
        draw_pixel(img, 8 + w, 6, "#515151")
    for w in range(3):
        draw_pixel(img, 8 + w, 7, "#515151")
    for w in range(2):
        draw_pixel(img, 8 + w, 8, "#515151")

    for i in range(2):
        draw_pixel(img, 8 + i, 6 - i, "#353535")


def draw_dysto_gas_mask(img, gender_):
    gender = 0
    if gender_ == "Female":
        gender = 1
    outline = "#12173d"
    for h in range(4):
        draw_pixel(img, 6, 16 + h + gender, outline)
        draw_pixel(img, 12, 16 + h + gender, outline)
    for w in range(11):
        draw_pixel(img, 7 + w, 21 + gender, outline)
    for w in range(5):
        draw_pixel(img, 7 + w, 15 + gender, outline)
    for h in range(5):
        draw_pixel(img, 18, 16 + h + gender, outline)
    for w in range(2):
        for h in range(2):
            draw_pixel(img, 7 + 4 * w, 16 + 4 * h + gender, outline)
    for w in range(2):
        draw_pixel(img, 10 + w, 14 + gender, outline)
    for w in range(3):
        draw_pixel(img, 12 + w, 13 + gender, outline)
    draw_pixel(img, 15, 14 + gender, outline)
    for h in range(6):
        draw_pixel(img, 16, 15 + h + gender, outline)
    draw_pixel(img, 17, 15 + gender, outline)

    for w in range(5):
        for h in range(3):
            draw_pixel(img, 7 + w, 17 + h + gender, "#283169")
    for h in range(2):
        draw_pixel(img, 9, 16 + 4 * h + gender, "#283169")

    for w in range(2):
        for h in range(2):
            draw_pixel(img, 8 + 2 * w, 16 + 4 * h + gender, "#6a74b2")
            draw_pixel(img, 7 + 4 * w, 17 + 2 * h + gender, "#454c8a")
    for w in range(2):
        for h in range(3):
            draw_pixel(img, 14 + w, 15 + 2 * h + gender, "#6a74b2")
    draw_pixel(img, 13, 15 + gender, "#6a74b2")
    draw_pixel(img, 12, 15 + gender, "#909edd")
    for h in range(2):
        draw_pixel(img, 13, 17 + 2 * h + gender, "#909edd")
    draw_pixel(img, 9, 18 + gender, "#7af9e6")
    for w in range(3):
        draw_pixel(img, 12 + w, 14 + gender, "#283169")
        for h in range(3):
            draw_pixel(img, 13 + w, 16 + 2 * h + gender, "#283169")
    draw_pixel(img, 12, 20 + gender, "#283169")
    for h in range(2):
        draw_pixel(img, 17, 17 + 2 * h + gender, "#283169")
        draw_pixel(img, 17, 16 + 4 * h + gender, "#6a74b2")
    draw_pixel(img, 17, 18 + gender, "#464b8b")


def draw_fire_mohawk(img):
    for h in range(6):
        draw_pixel(img, 13, 2 + h, colors[random.randrange(len(colors))])
    for h in range(4):
        draw_pixel(img, 12, 3 + h, colors[random.randrange(len(colors))])
    for h in range(2):
        draw_pixel(img, 11, 4 + h, colors[random.randrange(len(colors))])
    draw_pixel(img, 10, 5, colors[random.randrange(len(colors))])

    for i in range(4):
        draw_pixel(img, 10 + i, 4 - i, "#000000")
    for h in range(4):
        draw_pixel(img, 14, 1 + h, "#000000")


def draw_green_mohawk(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 3
    for h in range(6):
        draw_pixel(img, 13, 2 + h + num, "#39FF14")
    for h in range(4):
        draw_pixel(img, 12, 3 + h + num, "#39FF14")
    for h in range(2):
        draw_pixel(img, 11, 4 + h + num, "#39FF14")
    draw_pixel(img, 10, 5 + num, "#39FF14")

    for i in range(4):
        draw_pixel(img, 10 + i, 4 - i + num, "#000000")
    for h in range(4):
        draw_pixel(img, 14, 1 + h + num, "#000000")


def draw_bandana(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    main_color = "#1a44c2"
    for w in range(8):
        draw_pixel(img, 9 + w, 5 + num, main_color)
    for w in range(10):
        draw_pixel(img, 8 + w, 6 + num, main_color)
    for w in range(11):
        draw_pixel(img, 7 + w, 7 + num, main_color)
    for w in range(14):
        draw_pixel(img, 3 + w, 8 + num, main_color)
    for w in range(3):
        for i in range(2):
            draw_pixel(img, 4 + w + 9 * i, 9 + num, main_color)
    for w in range(2):
        draw_pixel(img, 4 + w, 10 + num, main_color)
    draw_pixel(img, 4, 11 + num, main_color)

    outline = "#1738a0"
    for w in range(8):
        draw_pixel(img, 9 + w, 5 + num, outline)
    for h in range(2):
        draw_pixel(img, 17, 6 + h + num, outline)
    draw_pixel(img, 16, 8, outline)
    for w in range(3):
        draw_pixel(img, 13 + w, 9 + num, outline)
    for w in range(4):
        draw_pixel(img, 9 + w, 8 + num, outline)
    for i in range(2):
        draw_pixel(img, 8 - i, 6 + i + num, outline)
        draw_pixel(img, 6 - i, 8 + i + num, "#1737a7")
    for i in range(3):
        draw_pixel(img, 7 - i, 8 + i + num, "#132e75")
    draw_pixel(img, 4, 8, "#1837a2")


def draw_eye_patch(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    for w in range(11 - num):
        draw_pixel(img, 7 + w + num, 10 + num, "#000000")
    for w in range(4):
        for h in range(2):
            draw_pixel(img, 9 + w, 11 + h + num, "#000000")
    for w in range(2):
        draw_pixel(img, 10 + w, 13 + num, "#000000")


def draw_vr_headset(img):
    for h in range(2):
        for w in range(9):
            draw_pixel(img, 9 + w, 9 + 5 * h, "#000000")
        for w in range(7):
            draw_pixel(img, 10 + w, 10 + 3 * h, "#b4b4b4")
            draw_pixel(img, 10 + w, 11 + h, "#000000")
        for w in range(2):
            draw_pixel(img, 9 + 8 * w, 10 + 3 * h, "#8c8c8c")
            draw_pixel(img, 9 + 8 * w, 11 + h, "#b4b4b4")
        draw_pixel(img, 8, 11 + h, "#8c8c8c")
        draw_pixel(img, 7, 11 + h, "#000000")
        draw_pixel(img, 8, 10 + 3 * h, "#000000")
    for h in range(4):
        draw_pixel(img, 18, 10 + h, "#000000")
    draw_pixel(img, 8, 10, "#000000")


def draw_purple_cap(img):
    for w in range(14):
        draw_pixel(img, 7 + w, 8, "#8115b5")
    for w in range(13):
        draw_pixel(img, 7 + w, 7, "#8115b5")
    for w in range(10):
        draw_pixel(img, 7 + w, 6, "#8115b5")
    for w in range(9):
        draw_pixel(img, 8 + w, 5, "#8115b5")
    for w in range(7):
        draw_pixel(img, 9 + w, 4, "#8115b5")
    for i in range(2):
        draw_pixel(img, 14 + i, 5 + i, "#b260da")


def draw_police_hat(img):
    for w in range(6):
        draw_pixel(img, 7 + 2 * w, 7, "#000000")
    for w in range(5):
        draw_pixel(img, 8 + 2 * w, 7, "#ffffff")
    for w in range(3):
        draw_pixel(img, 7 + w, 8, "#000000")
    for w in range(8):
        draw_pixel(img, 10 + w, 9, "#000000")
        draw_pixel(img, 10 + w, 8, "#26324a")
    for w in range(11):
        for h in range(2):
            draw_pixel(img, 7 + w, 5 + h, "#26324a")
    for w in range(3):
        draw_pixel(img, 11 + w, 4, "#26324a")
    for w in range(3):
        draw_pixel(img, 11 + w, 3, "#000000")
    for i in range(2):
        for w in range(4):
            draw_pixel(img, 7 + w + 7 * i, 4, "#000000")
    for h in range(2):
        draw_pixel(img, 6, 5 + h, "#000000")
        for i in range(2):
            draw_pixel(img, 18, 5 + h + 3 * i, "#000000")
    draw_pixel(img, 12, 5, "#fcd901")


def draw_big_shades(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 2
    shade_colors = ["#670d45", "#8c0e5d", "#ad2160"]
    draw_pixel(img, 7, 11, "#000000")
    for i in range(2):
        for w in range(5):
            draw_pixel(img, 8 + w + 6 * i, 9 + num, "#000000")
        for w in range(2):
            for h in range(3):
                draw_pixel(img, 8 + 4 * w + 6 * i, 10 + h + num, "#000000")
        for w in range(3):
            draw_pixel(img, 9 + w + 6 * i, 13 + num, "#000000")
        for w in range(3):
            draw_pixel(img, 9 + w + 6 * i, 13 + num, "#000000")
        for w in range(3):
            draw_pixel(img, 9 + w + 6 * i, 13 + num, "#000000")
        for w in range(3):
            for h in range(3):
                draw_pixel(img, 9 + w + 6 * i, 10 + h + num, shade_colors[h])
    draw_pixel(img, 13, 10 + num, "#000000")


def draw_medium_shades(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    for w in range(11):
        draw_pixel(img, 7 + w, 11 + num, "#000000")
    for i in range(2):
        for w in range(4):
            for h in range(4):
                draw_pixel(img, 9 + w + 5 * i, 10 + h + num, "#000000")
        for w in range(2):
            for h in range(2):
                draw_pixel(img, 10 + w + 5 * i, 11 + h + num, "#81dbdb")


def draw_small_shades(img, gender="Male", dysto="False"):
    num = 0
    if gender == "Female":
        num = 1
    glass_colors = ["#5a3a11", "#c87310"]
    if dysto == "True":
        glass_colors = ["#42bc7f", "#8cff9a"]
    for w in range(11):
        draw_pixel(img, 7 + w, 10 + num, "#000000")
    for i in range(2):
        for w in range(2):
            for h in range(2):
                draw_pixel(img, 9 + 3 * w + 5 * i, 11 + h + num, "#000000")
                draw_pixel(img, 10 + w + 5 * i, 11 + h + num, glass_colors[h])
            draw_pixel(img, 10 + w + 5 * i, 13 + num, "#000000")


def draw_kawaii_vr(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    for h in range(6):
        for w in range(9 + 2 * (((h + 2) % 7) % (h + 1))):
            draw_pixel(img, 9 - (((h + 2) % 7) % (h + 1)) + w, 9 + h + num, "#12173d")
    for i in range(2):
        for w in range(3):
            draw_pixel(img, 10 + w + 5 * i, 12 - w % 2 + num, "#8dff99")
    if gender != "Female":
        for h in range(2):
            draw_pixel(img, 7, 10 + h + num, "#12173d")


def draw_cyclops_visor(img):
    for w in range(11):
        for h in range(3):
            draw_pixel(img, 7 + w, 11 + h, "#12173d")
    for w in range(7):
        draw_pixel(img, 10 + w, 12, "#dd3745")
    draw_pixel(img, 10, 12, "#a42736")


def draw_cybereye(img, gender="Male"):
    num = 0
    if gender == "Female":
        num = 1
    for w in range(3):
        for h in range(3):
            draw_pixel(img, 14 + w, 11 + h + num, "#283168")
    draw_pixel(img, 15, 12 + num, "#e54186")
    for w in range(2):
        draw_pixel(img, 15 + w, 9 + num, "#6a74b2")
    for w in range(3):
        draw_pixel(img, 14 + w, 10 + num, "#6a74b2")
    for w in range(2):
        draw_pixel(img, 15 + w, 14 + num, "#6a74b2")
    draw_pixel(img, 16, 15 + num, "#6a74b2")
    draw_pixel(img, 15, 10 + num, "#909edd")


def draw_peak(img):
    draw_pixel(img, 11, 8, "#000000")
    draw_pixel(img, 19, 8, "#000000")
    for w in range(7):
        draw_pixel(img, 12 + w, 7, "#000000")
        draw_pixel(img, 12 + w, 8, "#353535")
    for w in range(9):
        draw_pixel(img, 11 + w, 9, "#000000")
