# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_name(star_dict):
    for star in star_dict.keys():
        print(star)

print_star_name(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_spectral(star_dict):
    for star, info in star_dict.items():
        print(f"Name: {star}, Type: {info['Spectral Type']}")

print_spectral(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_stars(star_dict):
    for star, info in star_dict.items():
        if info["Magnitude"] > 0.1:
            print(star)

find_stars(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Arcturus"] = {
    "RA": "14h 15m 39.7s",
    "Dec": "+19° 10′ 56″",
    "Magnitude": -0.05,
    "Spectral Type": "K1.5III"
}

print(targets)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_brightest(star_dict):
    
    closest = None
    min_difference = None

    for star, info in star_dict.items():
        dec_string = info["Dec"].split("°")[0]
        dec_string = dec_string.replace("−", "-").replace("+", "").strip() #had to google this function because it wouldn't convert negative numbered strings into integers
        dec_degree = int(dec_string)

        difference = abs(dec_degree - 20)

        if min_difference == None or difference < min_difference:
            min_difference = difference
            closest = star

    return closest

print(find_brightest(targets))

# 6) What is your favorite constellation?
print("My favorite constellation is the Libra (which is my zodiac sign!!)")