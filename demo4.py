# players_count = int(input("Combien êtes-vous à jouer ? "))
# round_count = int(input("Très bien, et combien de tour voulez-vous faire ? "))
#
# scores = []
# for i in range(players_count):
#     scores.append([])
#
# for i in range(round_count):
#     for player_index in range(players_count):
#         user_score = 0
#         for f in range(3):
#             user_score += int(input(
#                 f"Veuillez saisir le score du joueur {player_index + 1} au tour N°{i + 1} ({f + 1}/3) : "
#             ))
#         scores[player_index].append(user_score)
#
# for i in range(players_count):
#     print(f"Joueur {i + 1}", scores[i], sum(scores[i]))

ma_list = [4, 8, 1, 2, 7, 16]
ma_chaine = "Blah"

for c in ma_chaine:
    print(c)