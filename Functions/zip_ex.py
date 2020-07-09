players=('Lara','williams','John')
games=('Cricket','NBA','Football')
countries=['WI','USA','UK']
z=tuple(zip(players,games,countries)) # zipping 3 iterating variables
print(z)

p,g,c=zip(*z) # unzipping variables # generator
print(p)
print(g)
print(c)