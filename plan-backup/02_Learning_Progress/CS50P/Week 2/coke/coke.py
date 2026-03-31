amount_due = 50
#insert_coin = int(input("Insert Coin: "))
#print(f"Amount_due: {amount_due}")


while amount_due > 0:
    print(f"Amount_due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in [25, 10, 5]:
        amount_due = amount_due - insert_coin
if amount_due < 0:
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

else:
    print(f"Change Owed: {0}")


