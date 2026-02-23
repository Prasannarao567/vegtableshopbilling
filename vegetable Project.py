import mysql.connector as db
db = db.connect(user='root',password='Mysql@123',host='localhost',database='project')
cursor = db.cursor()
choice = input("Select your choice (Owner/User): ").lower()
if choice == "owner":
    while True:
        print("\n1.Add Item\n2.Remove Item\n3.Update Inventory\n4.View Inventory\n5.View Users\n6.Total Revenue\n7.Itemized Profit\n8.Total Profit\n9.Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            name = input("Item name: ")
            cursor.execute("SELECT * FROM inventory WHERE veg_name=%s", (name,))
            if cursor.fetchone():
                print("Item already exists in inventory")
            else:
                qty = float(input("Quantity: "))
                price = int(input("Selling price per Kg: "))
                cp = int(input("Cost price Price per kg: "))
                cursor.execute(
                    "INSERT INTO inventory (veg_name, quantity, price, cost_price) VALUES (%s,%s,%s,%s)",
                    (name, qty, price, cp)
                )
                db.commit()
                print("Item added successfully")
        elif ch == 2:
            name = input("Item to remove: ")
            cursor.execute("DELETE FROM inventory WHERE veg_name=%s", (name,))
            db.commit()
            print("Item removed")
        elif ch == 3:
            name = input("Item to update: ")
            qty = float(input("New quantity: "))
            price = int(input("New price: "))
            cursor.execute(
                "UPDATE inventory SET quantity=%s, price=%s WHERE veg_name=%s",
                (qty, price, name)
            )
            db.commit()
            print("Inventory updated")
        elif ch == 4:
            cursor.execute("SELECT * FROM inventory")
            for row in cursor.fetchall():
                print(row)
        elif ch == 5:
            cursor.execute("SELECT * FROM users")
            for row in cursor.fetchall():
                print(row)
        elif ch == 6:
            cursor.execute("SELECT quantity, price FROM inventory")
            revenue = sum(q*p for q,p in cursor.fetchall())
            print("Total Revenue:", revenue)
        elif ch == 7:
            cursor.execute("SELECT veg_name, quantity, price, cost_price FROM inventory")
            for v,q,p,c in cursor.fetchall():
                print(v, "Profit:", (p-c)*q)
        elif ch == 8:
            cursor.execute("SELECT quantity, price, cost_price FROM inventory")
            profit = sum((p-c)*q for q,p,c in cursor.fetchall())
            print("Total Profit:", profit)
        elif ch == 9:
            break
elif choice == "user":
    cart = {}
    while True:
        print("\n1.Add to cart\n2.View cart\n3.Billing\n4.Exit")
        ch = input("Choose: ")
        if ch == "1":
            item = input("Vegetable: ")
            qty = float(input("Quantity: "))
            cursor.execute("SELECT quantity, price FROM inventory WHERE veg_name=%s", (item,))
            data = cursor.fetchone()
            if data is None:
                print("Item does not exist in inventory")
            elif qty > data[0]:
                print("Only", data[0], "kg available")
            else:
                cart[item] = cart.get(item, 0) + qty
                cursor.execute(
                    "UPDATE inventory SET quantity = quantity - %s WHERE veg_name=%s",
                    (qty, item)
                )
                db.commit()
                print("Item added to cart")
        elif ch == "2":
            print(cart)
        elif ch == "3":
            total = 0
            for item, qty in cart.items():
                cursor.execute("SELECT price FROM inventory WHERE veg_name=%s", (item,))
                price = cursor.fetchone()[0]
                total += qty * price
                print(item, qty, "kg =", qty*price)
            name = input("Name: ")
            phone = input("Phone: ")
            cursor.execute(
                "INSERT INTO users (username, phone) VALUES (%s,%s)",
                (name, phone)
            )
            db.commit()
            print("Total amount:", total)
            cart.clear()
        elif ch == "4":
            break
else:
    print("Invalid choice")
