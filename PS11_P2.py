def compute_scores(scores):
  total_points = sum(scores)
  average_score = total_points / len(scores)
  return total_points, average_score


def main():
  # User inputs
  last_name = input("Enter student's last name: ")
  scores = []
  for i in range(3):
      score = float(input(f"Enter exam score {i + 1}: "))
      scores.append(score)

  # Compute total and average scores
  total_points, average_score = compute_scores(scores)

  # Display results
  print(f"\nStudent Last Name: {last_name}")
  print(f"Total Points: {total_points:.2f}")
  print(f"Average Exam Score: {average_score:.2f}")


if __name__ == "__main__":
  main()
