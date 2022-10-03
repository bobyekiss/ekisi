players_count = int(input("Combien êtes-vous à jouer ? "))
score_goal = int(input("Quel est le score à atteindre ? "))

scores = {}
for i in range(players_count):
    nickname = input(f"Quel est le pseudonyme du joueur n°{i + 1} ? ")
    scores[nickname] = []

while max([sum(scores[n]) for n in scores]) <= score_goal:
    for nick in scores:
        print(f"C'est au tour de {nick} !")
        user_score = 0
        for f in range(3):
            user_score += int(input(
                f"Veuillez saisir le score de la fléchette n°{f + 1} : "
            ))
        scores[nick].append(user_score)

for nick in scores:
    print(f"Joueur {nick}", scores[nick], sum(scores[nick]))