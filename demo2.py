score = [15,5,5,9,16,1,0,0,17,11,7,4,9,3,1,6]

print("score au 1er tour:", score[0])
print("score au 5e tour:", score[4])

print("nbre de score saisi:", len(score))
print("score au dernier tour:", score[-1])
print("score à l'avant dernier tour:", score[-2])

print("Scores de l'index 5 à 9 :", score[5:10])
print("Scores sans le premier et le dernier :", score[1:-1])
print("Les 5 premiers scores :", score[:5])
print("Les 5 derniers scores :", score[-5:])

# Write

print(score)
score[8] = 12
print(score)

print("Scores de l'index 5 à 9 :", score[5:10])
print("Scores sans le premier et le dernier :", score[1:-1])
print("Les 5 premiers scores :", score[:5])
print("Les 5 derniers scores :", score[-5:])

# Write
print(score)
score[8] = 12
print(score)

print()

score = []
print(score)

score.append(15)
score.append(1)
score.append(7)
print(score)

score.pop()
print(score)

score.pop(0)
print(score)

score.append(14)
score.append(18)
score.append(20)
score.append(25)
print(score)

score.insert(3, 19)
print(score)