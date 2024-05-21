# Galgje spel

# Vraag speler 1 om een woord in te voeren en zet het om naar kleine letters
woord = input("Speler 1, voer een woord in: ").lower()

# Maak een lijst om de geraden letters bij te houden. Begin met underscores voor elke letter in het woord
geraden_letters = ['_'] * len(woord)

# Zet het aantal toegestane fouten op 0 en stel het maximale aantal fouten in op 9
fouten = 0
max_fouten = 9

# Blijf letters raden totdat het woord is geraden of de foutenlimiet is bereikt
while fouten < max_fouten and '_' in geraden_letters:
    # Toon de huidige status van het geraden woord
    print("\nHuidige status: ", " ".join(geraden_letters))
    
    # Vraag speler 2 om een letter te raden en zet het om naar kleine letters
    letter = input("Speler 2, raad een letter: ").lower()

    # Controleer of de geraden letter in het woord zit
    if letter in woord:
        # Als de letter in het woord zit, update de geraden letters lijst
        for i in range(len(woord)):
            if woord[i] == letter:
                geraden_letters[i] = letter
    else:
        # Als de letter niet in het woord zit, verhoog het aantal fouten met 1
        fouten += 1
        # Geef de speler een bericht met het aantal resterende pogingen
        print(f"Fout! Je hebt nog {max_fouten - fouten} pogingen over.")

# Controleer of het woord volledig is geraden
if '_' not in geraden_letters:
    # Als het woord volledig is geraden, feliciteer de speler
    print("\nGefeliciteerd, je hebt het woord geraden: ", woord)
else:
    # Als de speler 9 fouten heeft gemaakt, laat weten dat het spel verloren is en toon het woord
    print("\nHelaas, je hebt verloren. Het woord was: ", woord)
