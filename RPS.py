import random


# Enhanced player function to adapt against different bot strategies.
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Initialize a dictionary to track the count of patterns
    pattern_count = {"RR": 0, "RP": 0, "RS": 0,
                     "PR": 0, "PP": 0, "PS": 0,
                     "SR": 0, "SP": 0, "SS": 0}

    # Update pattern counts based on the opponent's history
    if len(opponent_history) > 1:
        for i in range(1, len(opponent_history)):
            pattern = opponent_history[i - 1] + opponent_history[i]
            if pattern in pattern_count:
                pattern_count[pattern] += 1

    # Predict the next move based on the most common pattern
    if len(opponent_history) > 1:
        last_play = opponent_history[-1]
        potential_patterns = {key: pattern_count[key] for key in pattern_count if key.startswith(last_play)}
        most_common_pattern = max(potential_patterns, key=potential_patterns.get, default="R")
        predicted_next = most_common_pattern[1] if len(most_common_pattern) > 1 else "R"

        # Counter the predicted move
        if predicted_next == "R":
            return "P"
        elif predicted_next == "P":
            return "S"
        elif predicted_next == "S":
            return "R"

    # Fallback strategy for the first move or if history is too short
    return random.choice(["R", "P", "S"])
