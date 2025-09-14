initial_atoms = int(input())
final_atoms = int(input())

periods = 0
while initial_atoms >= final_atoms:
    initial_atoms = initial_atoms / 2
    periods +=1

print(periods * 12)