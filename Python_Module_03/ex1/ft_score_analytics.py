import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    scores = []

    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            scores.append(num)
        except:
            print(f"Invalid parameter:'{arg}'")

    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")

        total_players = len(scores)
        total_score = sum(scores)
        average = total_score / total_players
        high = max(scores)
        low = min(scores)
        score_range = high - low

        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {score_range}")