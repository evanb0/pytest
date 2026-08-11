import tkinter as tk
import random
import math

# INSPIRATION TAKEN FROM STARFIELD SIMULATION
# create a list to store info about stars, then loop through list to add new ones
# create a dict to store info about planets, generic information that user will be able to click
# implement mouse tracking so that user can click on planet, and get basic info
# create info/close panels that user will see once planet is clicked
# implement click hear event that can cause panel to occur when the user has clicked the planet
# consider simulation updates i.e what happens when the star reaches the screen, how do planets rotate etc
# actually draw planets/sun onth gui and add hover labels so u can see which planet is each.




# settings -> constants that can be modified by user

NUM_STARS = 3000
STAR_SPEED = 400

# window creation

root = tk.Tk()
root.title("Space simulation")

root.state("zoomed")

canvas = tk.Canvas(
    root,
    bg="black"
)

canvas.pack(
    fill="both",
    expand=True
)

# star creation

stars = []

for star in range(NUM_STARS):

    stars.append({
        "x": random.uniform(-1000, 1000),
        "y": random.uniform(-1000, 1000),
        "z": random.uniform(1, 1000)
    })


# planet creation + NASA descriptions for all planets but earth 

planets = [

    {
        "name": "Mercury",
        "orbit": 80,
        "angle": 0,
        "speed": 0.2075,
        "size": 12,
        "color": "#888888",
        "type": "Terrestrial planet",
        "description": "Mercury is the closest planet to the Sun, and the smallest planet in our solar system. It's only slightly larger than Earth's Moon.",
        "distance": "57.9 million km or 0.387 AU",
        "moons": "0"
    },

    {
        "name": "Venus",
        "orbit": 110,
        "angle": 1,
        "speed": 0.0815,
        "size": 15,
        "color": "#d4a15c",
        "type": "Terrestrial planet",
        "description": "Venus is the second planet from the Sun, and the sixth largest planet. It’s the hottest planet in our solar system.",
        "distance": "108.2 million km or 0.723 AU",
        "moons": "0"
    },

    {
        "name": "Earth",
        "orbit": 140,
        "angle": 2,
        "speed": 0.0500,
        "size": 17,
        "color": "#3366ff",
        "type": "Terrestrial planet",
        "description": "Our home planet and the only world currently known to support life.",
        "distance": "149.6 million km or 1 AU",
        "moons": "1"
    },

    {
        "name": "Mars",
        "orbit": 175,
        "angle": 4,
        "speed": 0.0266,
        "size": 15,
        "color": "#ff6633",
        "type": "Terrestrial planet",
        "description": "The Red Planet, known for its dusty surface and enormous volcanoes.",
        "distance": "227.9 million km or 1.523 AU",
        "moons": "2"
    },

    {
        "name": "Jupiter",
        "orbit": 225,
        "angle": 1,
        "speed": 0.00420,
        "size": 27,
        "color": "#cc9933",
        "type": "Gas giant",
        "description": "Jupiter is the fifth planet from the Sun, and the largest in the solar system, by far — more than twice as massive as the other planets combined.",
        "distance": "778.5 million km or 5.204 AU",
        "moons": "95+"
    },

    {
        "name": "Saturn",
        "orbit": 280,
        "angle": 3,
        "speed": 0.001695,
        "size": 24,
        "color": "#d6b879",
        "type": "Gas giant",
        "description": "Saturn is the sixth planet from the Sun, and the second largest in the solar system. It’s surrounded by seven main rings although there are more.",
        "distance": "1.43 billion km or 9.559 AU",
        "moons": "140+"
    },

    {
        "name": "Uranus",
        "orbit": 335,
        "angle": 5,
        "speed": 0.000595,
        "size": 20,
        "color": "#66ccdd",
        "type": "Ice giant",
        "description": "Uranus is the seventh planet from the Sun, and the third largest planet in our solar system. It appears to spin sideways.",
        "distance": "2.87 billion km or 19.184 AU",
        "moons": "27"
    },

    {
        "name": "Neptune",
        "orbit": 385,
        "angle": 2,
        "speed": 0.0003035,
        "size": 20,
        "color": "#3366cc",
        "type": "Ice giant",
        "description": "Neptune is the eighth, and most distant planet from the Sun. It’s the fourth-largest, and the first planet discovered with math.",
        "distance": "4.50 billion km or 30.080 AU",
        "moons": "14"
    }
]


# sun info, once again from NASA website

sun = {
    "name": "Sun",
    "size": 45,
    "color": "#ffaa00",
    "type": "Star",
    "description": "The Sun's gravity holds the solar system together, keeping everything – from the biggest planets to the smallest particles of debris – in its orbit.",
    "distance": "",
    "moons": "N/A"
}


# mouse stuff

mouse_x = 0
mouse_y = 0


def mouse_move(event):

    global mouse_x
    global mouse_y

    mouse_x = event.x
    mouse_y = event.y


canvas.bind(
    "<Motion>",
    mouse_move
)


# panel that shows up when a planet is clicked on

info_panel = None


def close_info():

    global info_panel

    if info_panel is not None:
        info_panel.destroy()
        info_panel = None


def show_info(body):

    global info_panel

    # if a panel already exists, remove it
    # before creating the new one

    if info_panel is not None:
        info_panel.destroy()


    # creation of panel

    info_panel = tk.Frame(
        root,
        bg="#111111",
        bd=2,
        relief="solid"
    )

    info_panel.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        width=360,
        height=300
    )


    # title of planet

    title = tk.Label(
        info_panel,
        text=body["name"],
        bg="#111111",
        fg="white",
        font=("Arial", 34, "bold")
    )

    title.pack(
        pady=(20, 10)
    )


    # type of planet

    type_label = tk.Label(
        info_panel,
        text="Type: " + body["type"],
        bg="#111111",
        fg="#bbbbbb",
        font=("Arial", 16)
    )

    type_label.pack(
        pady=3
    )


    # desc of planet

    description = tk.Label(
        info_panel,
        text=body["description"],
        bg="#111111",
        fg="white",
        wraplength=310,
        justify="center",
        font=("Arial", 12)
    )

    description.pack(
        pady=10
    )


    # distance of planet from sun

    distance_label = tk.Label(
        info_panel,
        text="Distance from Sun: " + body["distance"],
        bg="#111111",
        fg="#bbbbbb",
        font=("Arial", 16)
    )

    distance_label.pack(
        pady=3
    )


    # moons the planet has (if any)

    moons_label = tk.Label(
        info_panel,
        text="Moons: " + body["moons"],
        bg="#111111",
        fg="#bbbbbb",
        font=("Arial", 16)
    )

    moons_label.pack(
        pady=3
    )


    # close button for user to exit panel

    close_button = tk.Button(
        info_panel,
        text="Close",
        command=close_info,
        bg="#333333",
        fg="black",
        activebackground="#555555",
        activeforeground="black",
        relief="flat",
        padx=20,
        pady=5
    )

    close_button.pack(
        pady=15
    )


# event to see if the user has clicked a planet

def planet_clicked(event):

    mouse_click_x = event.x
    mouse_click_y = event.y


    # get current Canvas size

    width = canvas.winfo_width()
    height = canvas.winfo_height()


    # find centre of Solar System

    sun_x = width / 2
    sun_y = height / 2



    distance_from_sun = math.sqrt(
        (mouse_click_x - sun_x) ** 2
        +
        (mouse_click_y - sun_y) ** 2
    )


    if distance_from_sun <= sun["size"]:

        show_info(sun)

        return



    for planet in planets:

        x = (
            math.cos(
                planet["angle"]
            )
            * planet["orbit"]
        )

        y = (
            math.sin(
                planet["angle"]
            )
            * planet["orbit"]
        )


        screen_x = sun_x + x
        screen_y = sun_y + y


        distance = math.sqrt(
            (mouse_click_x - screen_x) ** 2
            +
            (mouse_click_y - screen_y) ** 2
        )


        if distance <= planet["size"]:

            show_info(planet)

            return


canvas.bind(
    "<Button-1>",
    planet_clicked
)


# simulation updates

def update():

    # get actual Canvas size

    width = canvas.winfo_width()
    height = canvas.winfo_height()


    # wait until Canvas has a real size

    if width <= 1 or height <= 1:

        root.after(
            16,
            update
        )

        return


    canvas.delete("all")


    # drawing of stars

    for star in stars:

        star["z"] -= STAR_SPEED


        # reset star once close to screen

        if star["z"] <= 1:

            star["x"] = random.uniform(
                -1000,
                1000
            )

            star["y"] = random.uniform(
                -1000,
                1000
            )

            star["z"] = 1000


        # perspective projection

        screen_x = (
            width / 2
            + star["x"]
            / star["z"]
            * width
        )

        screen_y = (
            height / 2
            + star["y"]
            / star["z"]
            * height
        )


        # stars get bigger when closer

        size = max(
            1,
            5 * (
                1
                - star["z"] / 1000
            )
        )


        if (
            0 <= screen_x <= width
            and
            0 <= screen_y <= height
        ):

            brightness = int(
                255
                * (
                    1
                    - star["z"] / 1000
                )
            )

            brightness = max(
                40,
                min(
                    255,
                    brightness
                )
            )



            color = ( 
                f"#{brightness:02x}"
                f"{brightness:02x}"
                f"{brightness:02x}"
            )


            canvas.create_oval(
                screen_x - size,
                screen_y - size,
                screen_x + size,
                screen_y + size,

                fill=color,
                outline=""
            )



    sun_x = width / 2
    sun_y = height / 2


    # sun glow

    canvas.create_oval(
        sun_x - 65,
        sun_y - 65,
        sun_x + 65,
        sun_y + 65,

        outline="#664400",
        width=3
    )



    canvas.create_oval(
        sun_x - 45,
        sun_y - 45,
        sun_x + 45,
        sun_y + 45,

        fill="#ffaa00",
        outline=""
    )


    # drawing of planets

    for planet in planets:

        # move planet around orbit and calculate position

        planet["angle"] += planet["speed"]


        x = (
            math.cos(
                planet["angle"]
            )
            * planet["orbit"]
        )

        y = (
            math.sin(
                planet["angle"]
            )
            * planet["orbit"]
        )


        # screen position

        screen_x = sun_x + x
        screen_y = sun_y + y


        # saturn rings

        if planet["name"] == "Saturn":

            canvas.create_oval(
                screen_x - planet["size"] * 1.8,
                screen_y - planet["size"] * 0.55,

                screen_x + planet["size"] * 1.8,
                screen_y + planet["size"] * 0.55,

                outline="#b89b62",
                width=4
            )


        # drawing of planets

        canvas.create_oval(
            screen_x - planet["size"],
            screen_y - planet["size"],

            screen_x + planet["size"],
            screen_y + planet["size"],

            fill=planet["color"],
            outline=""
        )


        # hover label

        distance = math.sqrt(
            (mouse_x - screen_x) ** 2
            +
            (mouse_y - screen_y) ** 2
        )

        hovering = (
            distance <= planet["size"]
        )


        if hovering:

            label_x = (
                screen_x
                + planet["size"]
                + 10
            )

            label_y = (
                screen_y
                - planet["size"]
                - 10
            )


            canvas.create_rectangle(
                label_x - 5,
                label_y - 5,

                label_x + 85,
                label_y + 20,

                fill="#111111",
                outline="#555555"
            )


            canvas.create_text(
                label_x,
                label_y + 7,

                text=planet["name"],

                fill="white",

                anchor="w",

                font=(
                    "Arial",
                    20,
                    "bold"
                )
            )


    # hover label for sun

    sun_distance = math.sqrt(
        (mouse_x - sun_x) ** 2
        +
        (mouse_y - sun_y) ** 2
    )


    if sun_distance <= sun["size"]:

        canvas.create_rectangle(
            sun_x + 55,
            sun_y - 55,

            sun_x + 105,
            sun_y - 30,

            fill="#111111",
            outline="#555555"
        )


        canvas.create_text(
            sun_x + 60,
            sun_y - 42,

            text="Sun",

            fill="white",

            anchor="w",

            font=(
                "Arial",
                20,
                "bold"
            )
        )



    root.after(
        16,
        update
    )




update()

root.mainloop()



