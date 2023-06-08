lista_goala = []
dict_gol = []

# declaram si initializam un dict
note_elevi = {'Gigel': 10, "Costel": 9, 'Ana': 10, ' Sebi ': 7}

# adaugam elemente
# afisam Dictul
print(note_elevi)

# aflam note
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi[' Costel '] =10
print(note_elevi)

#aflam dimensiunea
print(len(note_elevi))

# sterg valorile
note_elevi.pop("Gigel")
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())

