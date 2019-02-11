#! python3
# Program by Caleb Goodart
# MSIS4713
# Mod04

lyrics_string = (
    "Quisiera:Ayer:cambiarle:conocí:el:un:final"
    ":cielo:al:sin:cuento|Las:sol|Y:barras:un:y"
    ":hombre:los:sin:tragos:suelo|Un:han:santo:"
    "sido:en:testigo|De:prision|Y:el:una:dolor:"
    "canción:que:triste:me:sin:causaste:dueño|Y:"
    "y:conocí:to':tus:lo:ojos:que:negros|Y:hiciste"
    ":ahora:conmigo|Un:sí:infeliz:que:en:no:el:"
    "puedo:amor,:vivir:que:sin:aun:ellos:no:yo|"
    "Le:te:pido:supera|Que:al:ahora:cielo:camina"
    ":solo:solo:un:sin:deseo|Que:nadie:en:por:tus"
    ":todas:ojos:las:yo:aceras|Preguntándole:pueda"
    ":a:vivir|He:Dios:recorrido:si:el:en:mundo:verdad"
    ":entero|te:el:vengo:amor:a:existe|:decir|")

lyrics_string = lyrics_string.replace("|", "\n")        # replaces | with newline for formatting
song_one = []
song_two = []
temp_list = lyrics_string.split(":")
same_lyric = []
del lyrics_string

for i in range(0, len(temp_list), 2):
    song_one.append(temp_list[i])
    song_two.append(temp_list[i + 1])

del temp_list       # temp list is no longer needed

for i in range(len(song_one)):      # compares all indexes of song one to all indexes of song two
    for j in range(len(song_two)):
        if song_one[i] == song_two[j]:
            if song_one[i] not in same_lyric:       # if a match is found then it check if its already in the list
                same_lyric.append(song_two[j])

# prints all everything
print(" ".join(song_one))
print(" ".join(song_two))
print("Words that are in both songs:")
for i in range(len(same_lyric)):
    print(same_lyric[i])
