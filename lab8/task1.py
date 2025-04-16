# Probability of drawing a red card (hearts or diamonds)
total_cards = 52
red_cards = 26
print(f"Probability of drawing a red card: {red_cards/total_cards:.2f}")

# Given a red card, probability it's a heart
hearts_in_red = 13
print(f"Probability red card is a heart: {hearts_in_red/red_cards:.2f}")

# Given a face card, probability it's a diamond
face_cards = 12  # 3 per suit (Jack, Queen, King) * 4 suits
diamond_face_cards = 3
print(f"Probability face card is a diamond: {diamond_face_cards/face_cards:.2f}")

# Given a face card, probability it's a spade or a queen
spade_face_cards = 3
queens = 4  # one per suit
# We need to subtract the queen of spades to avoid double counting
spade_or_queen_face = spade_face_cards + queens - 1
print(f"Probability face card is spade or queen: {spade_or_queen_face/face_cards:.2f}")
