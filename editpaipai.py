import textwrap

import attr
from PIL import Image, ImageDraw, ImageFont

line_max_widths = [100, 120, 120, 100]
@attr.define
class Coordinates:
    x: int
    y: int

    @property
    def xy(self):
        return (self.x, self.y)

title_font = ImageFont.truetype('Metropolis-Regular.otf', 36)

centers_1 = [
    Coordinates(x=2260, y=1137),
    Coordinates(x=2660, y=1137),
    Coordinates(x=3060, y=1137),
    Coordinates(x=2260, y=1505),
    Coordinates(x=2660, y=1505),
    Coordinates(x=3060, y=1505),
    Coordinates(x=2262, y=1873),
    Coordinates(x=2662, y=1873),
    Coordinates(x=3062, y=1873),
]
centers_2 = [
    Coordinates(x=2260, y=3665),
    Coordinates(x=2660, y=3665),
    Coordinates(x=3060, y=3665),
    Coordinates(x=2260, y=4033),
    Coordinates(x=2660, y=4033),
    Coordinates(x=3060, y=4033),
    Coordinates(x=2262, y=4400),
    Coordinates(x=2662, y=4400),
    Coordinates(x=3062, y=4400),
]

bingo_oks = [
    "El ramo\nes un sable",
    "El pastel\nlleva pistacho",
    "Hay costillar",
    "Suena la\nmarcha\nimperial",
    "La novia\nlleva zapatos\nrojos",
    "Hay cochinillo",
    "Los gemelos\ndel novio\nson rojos",
    "Sirven\npollo frio",
    "Los cubiertos\nson negros",
    "Palomitas",
    "El padre\nde la novia\nva de Jedi",
    "El novio va\nen deportivas",
    "La novia\nse cambia\nde ropa",
    "Suena\nMarry me",
]
bingo_kos = [
    "El ramo\nlleva tulipanes",
    "El pastel es\nun red velvet",
    "Entran\ncon\nfuego",
    "Los cubiertos\nson dorados",
    "Hay Torreznos",
    "Llega\nDarth Vader",
    "La novia\nllega en moto",
    "Hay ostras",
    "Aparece\nChewbacca",
    "Cortan el\npastel con\nun sable",
    "Los anillos\nvan en una\npokeball",
    "Suena\nPokemon",
    "Suena\nDigimon",
    "No hay baile",
    "Sirven sushi",
    "Ramen",
    "Aparecen\nlos ewoks",
    "Aparecen\nstorm troopers",
    "Entran con\ncascos de\nMandalorian",
    "Crepes\nde postre",
    "Gofres\nde postre",
]

winner = [
    "Suena la\nmarcha\nimperial",
    "El novio va\nen deportivas",
    "Suena\nMarry me",
    "Los cubiertos\nson negros",
    "El padre\nde la novia\nva de Jedi",
    "El pastel\nlleva pistacho",
    "Hay costillar",
    "El ramo\nes un sable",
    "Sirven\npollo frio",
]
winner_2 = [
    "El padre\nde la novia\nva de Jedi",
    "Hay\nensaimadas",
    "La novia\nlleva zapatos\nrojos",
    "Suena\nMarry me",
    "Hay cochinillo",
    "Los cubiertos\nson negros",
    "El novio va\nen deportivas",
    "El pastel\nlleva pistacho",
    "El ramo\nes un sable",
    "Suena la\nmarcha\nimperial",
]

from random import sample

# population_3 = [ sample(sample(bingo_oks, 6) + sample(bingo_kos, 3), 9) for i in range(20) ]
# population_2 = [ sample(sample(bingo_oks, 7) + sample(bingo_kos, 2), 9) for i in range(60) ]
# population_1 = [ sample(sample(bingo_oks, 8) + sample(bingo_kos, 1), 9) for i in range(20) ]
# population = population_1 + population_2 + population_3

population = [ winner,  winner_2 ]

# bingo = population_3[0]
# for i in range(9):
#     img.multiline_text(
#         xy=centers[i].xy,
#         text=bingo[i], fill=(0,0,0), font=title_font,
#         align="center",spacing=25, anchor="mm"
#     )
#                  Coordinates  text     color      font
# image_editable.text((1800,750), test[0], (0, 0, 0), font=title_font)
# image_editable.text((1800,750), test[1], (0, 0, 0), font=title_font)
# my_image.save("result.png")

for n in range(0, len(population), 2):
    img = Image.open("PAIPAI_a3ai.png")
    draw = ImageDraw.Draw(img)


    print(f"Starting {n}")
    for i in range(9):
        draw.multiline_text(
            xy=centers_1[i].xy,
            text=population[n][i], fill=(0,0,0), font=title_font,
            align="center",spacing=25, anchor="mm"
        )

    print(f"Starting {n+1}")
    for i in range(9):
        draw.multiline_text(
            xy=centers_2[i].xy,
            text=population[n+1][i], fill=(0,0,0), font=title_font,
            align="center",spacing=25, anchor="mm"
        )

    print(f"Saving {n}")
    img.save(f"paipais/paipai_winners_{n}.png")

# img = Image.open("PAIPAI_a3ai.png")
# draw = ImageDraw.Draw(img)

# for i in range(9):
#     draw.multiline_text(
#         xy=centers_1[i].xy,
#         text=population[0][i], fill=(0,0,0), font=title_font,
#         align="center",spacing=25, anchor="mm"
#     )
# for i in range(9):
#     draw.multiline_text(
#         xy=centers_2[i].xy,
#         text=population[1][i], fill=(0,0,0), font=title_font,
#         align="center",spacing=25, anchor="mm"
#     )
# img.save(f"paipais/winners.png")