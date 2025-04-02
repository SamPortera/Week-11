def compute_discount(price, quantity, discount_rate):
  total_price = price * quantity
  discount_amount = total_price * (discount_rate / 100)
  discounted_price = total_price - discount_amount
  return discount_amount, discounted_price


def main():
  # User inputs
  quantity = int(input("Enter quantity: "))
  price = float(input("Enter price per item: "))
  discount_rate = float(input("Enter discount rate (in %): "))

  # Compute discount
  discount_amount, discounted_price = compute_discount(price, quantity, discount_rate)

  # Display results
  print(f"\nQuantity: {quantity}")
  print(f"Price per item: ${price:.2f}")
  print(f"Discount Amount: ${discount_amount:.2f}")
  print(f"Discounted Price: ${discounted_price:.2f}")


if __name__ == "__main__":
  main()
