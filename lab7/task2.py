def alpha_beta_cards(cards, left, right, alpha, beta, maximizing, memo):
    if left > right:
        return 0
    if (left, right, maximizing) in memo:
        return memo[(left, right, maximizing)]
    if maximizing:
        pick_left = cards[left] + alpha_beta_cards(cards, left + 1, right, alpha, beta, False, memo)
        pick_right = cards[right] + alpha_beta_cards(cards, left, right - 1, alpha, beta, False, memo)
        result = max(pick_left, pick_right)
        alpha = max(alpha, result)
    else:
        # Min plays dumb, always takes lower value
        result = min(
            alpha_beta_cards(cards, left + 1, right, alpha, beta, True, memo),
            alpha_beta_cards(cards, left, right - 1, alpha, beta, True, memo)
        )
        beta = min(beta, result)
    memo[(left, right, maximizing)] = result
    return result

def card_game():
    cards = [4, 10, 6, 2, 9, 5]
    left, right = 0, len(cards) - 1
    max_score, min_score = 0, 0
    turn = "Max"
    while left <= right:
        if turn == "Max":
            left_score = cards[left] + alpha_beta_cards(cards, left + 1, right, float('-inf'), float('inf'), False, {})
            right_score = cards[right] + alpha_beta_cards(cards, left, right - 1, float('-inf'), float('inf'), False, {})
            if left_score >= right_score:
                pick = cards[left]
                left += 1
            else:
                pick = cards[right]
                right -= 1
            max_score += pick
            print(f"Max picks {pick}, Remaining Cards: {cards[left:right+1]}")
            turn = "Min"
        else:
            if cards[left] < cards[right]:
                pick = cards[left]
                left += 1
            else:
                pick = cards[right]
                right -= 1
            min_score += pick
            print(f"Min picks {pick}, Remaining Cards: {cards[left:right+1]}")
            turn = "Max"

    print(f"\nFinal Scores - Max: {max_score}, Min: {min_score}")
    print("Winner:", "Max" if max_score > min_score else "Min" if min_score > max_score else "Draw")

card_game() 
