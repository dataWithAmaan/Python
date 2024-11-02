# code basics discord - https://github.com/codebasics/py/tree/master/Basics/Hindi

# dictionaries and tuples
captains = {
    'india': 'virat',
    'pakistan': 'sarfaraz',
    'sri lanka': 'dimuth',
}
for team in captains:
    print(f"{team} captain is {captains[team]}")

for team, captain in captains.items():
    print(team,"==>",captain)

