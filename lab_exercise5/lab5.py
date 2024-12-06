def get_student_record_single():
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        quizzes = []

        for i in range(1, 4):
            while True:
                try:
                    score = float(input(f"Enter score for Quiz {i}: "))
                    if 0 <= score <= 100:
                        quizzes.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        return {"id": student_id, "name": name, "quizzes": quizzes}
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def calculate_average(quizzes):
    try:
        return sum(quizzes) / len(quizzes)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_student_record(record):
    try:
        average = calculate_average(record["quizzes"])
        remark = "Passed" if average >= 60 else "Failed"

        print("\n--- Student Record ---")
        print(f"ID: {record['id']}")
        print(f"Name: {record['name']}")
        print(f"Quiz Scores: {record['quizzes']}")
        print(f"Average Grade: {average:.2f}")
        print(f"Remark: {remark}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_student_record_multiple():
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        quizzes = []

        for i in range(1, 4):
            while True:
                try:
                    score = float(input(f"Enter score for Quiz {i}: "))
                    if 0 <= score <= 100:
                        quizzes.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        return {"id": student_id, "name": name, "quizzes": quizzes}
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_student_records(records):
    try:
        print("\n--- Student Records ---")
        print(f"{'ID':<10} {'Name':<20} {'Quizzes':<20} {'Average':<10} {'Remark':<10}")
        print("-" * 70)

        for record in records:
            average = calculate_average(record["quizzes"])
            remark = "Passed" if average >= 75 else "Failed"
            quizzes_str = ", ".join(f"{score:.2f}" for score in record["quizzes"])
            print(f"{record['id']:<10} {record['name']:<20} {quizzes_str:<20} {average:<10.2f} {remark:<10}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_customer_info():
    try:
        print("Enter customer details:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        contact_no = input("Contact No: ")

        print("Enter order details:")
        while True:
            try:
                day = int(input("Order Date - Day: "))
                if day < 1 or day > 31:
                    print("Invalid day. Please enter a number between 1 and 31.")
                month = int(input("Order Date - Month: "))
                if month < 1 or month > 12:
                    print("Invalid month. Please enter a value between 1 and 12.")
                    continue
                year = int(input("Order Date - Year: "))
                if year < 1:
                    print("Invalid year. Please enter a positive number.")
                break
            except ValueError:
                print("Invalid input. Please enter numeric values for the date.")

        items = []

        for i in range(3):
            print(f"Enter details for Item {i + 1}:")
            item_id = input("Item ID: ")
            item_name = input("Item Name: ")
            while True:
                try:
                    item_price = float(input("Item Price: "))
                    item_quantity = int(input("Item Quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter numeric values for price and quantity.")
            items.append({"ID": item_id, "Name": item_name, "Price": item_price, "Quantity": item_quantity})

        return {
            "Name": {"FirstName": first_name, "LastName": last_name},
            "ContactNo": contact_no,
            "Order": {
                "Date": {"Day": day, "Month": month, "Year": year},
                "Items": items
            }
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_customer_info(customers):
    try:
        print("\n--- Customer Records ---")
        for idx, customer in enumerate(customers, start=1):
            print(f"\nCustomer {idx}:")
            name = customer["Name"]
            print(f"Name: {name['FirstName']} {name['LastName']}")
            print(f"Contact No: {customer['ContactNo']}")

            order = customer["Order"]
            date = order["Date"]
            print(f"Order Date: {date['Day']:02}/{date['Month']:02}/{date['Year']}")

            print("\nItems Purchased:")
            print(f"{'ID':<10} {'Name':<20} {'Price':<10} {'Quantity':<10} {'Total':<10}")
            total_order_cost = 0
            for item in order["Items"]:
                total = item["Price"] * item["Quantity"]
                total_order_cost += total
                print(f"{item['ID']:<10} {item['Name']:<20} {item['Price']:<10.2f} {item['Quantity']:<10} {total:<10.2f}")

            print(f"\nTotal Order Cost: {total_order_cost:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Single Student Record")
        print("2. Multiple Student Records")
        print("3. Customer Records")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_record = get_student_record_single()
            if student_record:
                display_student_record(student_record)
        elif choice == "2":
            student_records = []
            print("Enter details for 5 students:")
            for i in range(5):
                print(f"\nEntering record for Student {i + 1}:")
                student_record = get_student_record_multiple()
                student_records.append(student_record)
            display_student_records(student_records)
        elif choice == "3":
            customers = []
            print("Enter details for 3 customers:")
            for i in range(3):
                print(f"\nEntering details for Customer {i + 1}:")
                customer = get_customer_info()
                if customer:
                    customers.append(customer)
            display_customer_info(customers)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
