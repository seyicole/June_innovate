countries = {
    "France":"Paris",
    "England":"London",
    "Spain":"Madrid",
    "Germany":"Berlin",
    "Italy":"Rome",
}

countries.setdefault("Nigeria","Abuja") 
countries.setdefault("Ghana","Accra")
print(countries)

# for x, y in countries.items():
#     print(x,y)

# for x in countries.keys():
#     print(x + " : " + countries[x])
    
countries["England"]="English"
countries.update({"Nigeria":"Yoruba"})

print(countries)

fav_songs = [{
    "Artist":"Asa",
    "Song Name":"Jailer",
    "Genre":"Pop Afro",
    "Release Year":"2005"
},
{
    "Artist":"Coldplay",
    "Song Name":"Clocks",
    "Genre":"Alternative",
    "Release Year":"2003"
},
{
    "Artist":"Post Malone",
    "Song Name":"On the road",
    "Genre":"Hip hop",
    "Release Year":"2016"
}]

fav_songs.append(
    {
    "Artist":"Dave",
    "Song Name":"Gone",
    "Genre":"Rap",
    "Release Year":"n/a"
}
)

print(fav_songs)

fav_songs.pop()

print(fav_songs)

fav_songs[2].update({"Song Name":"Fly"})

print(fav_songs)

for dictionary in fav_songs:
    for k,v in dictionary.items():
        print(k + " : " + v)
    print("------")