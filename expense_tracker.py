expenses = []

def add_expenses():

  try:
    amount = float(input("Enter amount:"))
    note = input("Enter note:")
    expenses.append({"amount": amount,"note": note})
    print("Expenses add\n")
  except ValueError:
    print("Please enter a valid number.\n")

def view_expenses():
     if not expenses:
       print("No expenses yet./n")
       return
     total = 0
     print("\n Expenses:")
     for e in expenses:
         print(f"₹{e['amount']} - {e['note']}")
         total += e['amount']
     print(f"\nTotal = ₹{total}\n")

while True:

  print(" 1. Add Expenses")
  print(" 2. View Expenses")
  print(" 3. Exit")

  choice = input("choose option:")

  if choice == "1":
      add_expenses()
  elif  choice == "2":
      view_expenses()
  elif choice == "3":
      print("Goodbye")
      break
  else:
      print("Invalid choice\n")
