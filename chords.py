'''
U zasebnom repozitoriju generator akorda (ili proizvoljnog naziva) kreirajte aplikaciju
koja ce omoguciti korisniku da unese pocetni ton akorda za koji mu treba vratiti tri tona 
od kojih se sastoji durski i molski akord. 
Oktavu cine tonovi (po njemackoj notaciji)>

0, 1,  2, 3,  4, 5, 6,  7, 8,  9, 10, 11
C, C#, D, D#, E, F, F#, G, G#, A, A#, H
Durski akordi se sastoje od pocetnog tona, cetvrtog i sedmog

Primjer:
D
D dur (0, 4, 7) ili se pise samo D -> D, F#, A
D mol (0, 3, 7) ili se pise samo d -> D, F, A

H -> H, D#, F#
h -> H, D, F#
'''


notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
major = (0, 4, 7)
minor = (0, 3, 7)
root_note = input('\nIzaberite notu:\n').upper()
chord_quality = input('\nIzaberite Dur ili Mol:\n')

root_note_index = notes.index(root_note)

if chord_quality.lower() == 'dur':
   # chord = [notes[(root_note_index + j) % 12] for j in major]
    chord = []
    for i in major:
        note_index = (root_note_index + i) % 12
        chord.append(notes[note_index])

    print(chord)




    


