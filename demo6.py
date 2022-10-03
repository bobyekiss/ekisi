players_count = int(input("Combien êtes-vous à jouer ? "))
score_goal = int(input("Quel est le score à atteindre ? "))

scores = [[] for i in range(players_count)]

while max([sum(s) for s in scores]) <= score_goal:
    for player_index in range(players_count):
        user_score = 0
        for f in range(3):
            user_score += int(input(
                f"Veuillez saisir le score du joueur {player_index + 1} ({f + 1}/3) : "
            ))
        scores[player_index].append(user_score)

for i in range(players_count):
    print(f"Joueur {i + 1}", scores[i], sum(scores[i]))

    -------------------------------------------------------
    players_count = int(input("Combien êtes-vous à jouer ? "))
    score_goal = int(input("Quel est le score à atteindre ? "))

    scores = {}
    for i in range(players_count):
        nickname = input(f"Quel est le pseudonyme du joueur n°{i + 1} ? ")
        scores[nickname] = []

        *******************************

        my_custom_dns = {
            "1.2.3.4": "perdu.com",
            "123.45.67.89": "cefim.eu",
            "8.8.8.8": "gougeule.com"
        }

        for ip in my_custom_dns:
            print(ip, my_custom_dns[ip])