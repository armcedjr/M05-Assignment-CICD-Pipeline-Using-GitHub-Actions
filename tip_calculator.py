def calculate_tip(total_bill, tip_percentage):
    tip_amount = total_bill * (tip_percentage / 100)
    return tip_amount

def main():
    total_bill = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage: "))
    tip_amount = calculate_tip(total_bill, tip_percentage)
    print(f"Tip amount: ${tip_amount:.2f}")

if __name__ == "__main__":
    main()