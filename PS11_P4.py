def compute_bowling_scores(scores, handicap):
  average_score = sum(scores) / len(scores)
  average_with_handicap = average_score + handicap
  return average_score, average_with_handicap


def main():
  # User inputs
  last_name = input("Enter bowler's last name: ")
  scores = []
  for i in range(3):
      score = float(input(f"Enter game score {i + 1}: "))
      scores.append(score)

  handicap = float(input("Enter handicap: "))

  # Compute average scores
  average_score, average_with_handicap = compute_bowling_scores(scores, handicap)

  # Display results
  print(f"\nBowler Last Name: {last_name}")
  print(f"Average Score: {average_score:.2f}")
  print(f"Average Score with Handicap: {average_with_handicap:.2f}")


if __name__ == "__main__":
  main()
