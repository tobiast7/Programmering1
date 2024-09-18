def convert_seconds_to_hms(seconds):
    # Konverterar sekunderna till Hours,minuts och seconds
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours}H, {minutes}M, {secs}S"

def process_csv(file_path):
    with open(file_path, 'r') as file:
        # Läs in alla rader från filen
        content = file.readlines()

    # Lista för att lagra tuples med (namn, land, sekunder)
    data = []

    for line in content:
        # Ta bort newline och dela upp på kommatecken
        parts = line.strip().split(',')
        if len(parts) == 3:
            name, country, seconds_str = parts
            try:
                seconds = float(seconds_str)
                data.append((name, country, seconds))
            except ValueError:
                # Om det inte går att konvertera till float, ignorera raden
                print(f"Fel vid konvertering av sekunder: {seconds_str}")



    # Sortera listan baserat på sekunder (snabbaste tider först)
    data_sorted = sorted(data, key=lambda x: x[2])

    # Hämta de tre snabbaste tiderna
    top_3 = data_sorted[:3]

    # Skriv ut de tre snabbaste tiderna
    for name, country, seconds in top_3:
        formatted_time = convert_seconds_to_hms(seconds)
        print(f"{name} ({country}): {formatted_time}")

# Anropa funktionen med sökvägen till din CSV-fil
process_csv('TT_Olympic_2024_Men.csv')
