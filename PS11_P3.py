def compute_commission_and_target(sales):
  if sales > 100000:
      commission = sales * 0.10
  else:
      commission = sales * 0.05

  next_year_target = sales * 1.05  # 5% increase for next year's target
  return commission, next_year_target


def main():
  # User inputs
  last_name = input("Enter salesperson's last name: ")
  sales = float(input("Enter sales amount: "))

  # Compute commission and next year's target
  commission, next_year_target = compute_commission_and_target(sales)

  # Display results
  print(f"\nSalesperson Last Name: {last_name}")
  print(f"Commission: ${commission:.2f}")
  print(f"Next Year's Sales Target: ${next_year_target:.2f}")


if __name__ == "__main__":
  main()
