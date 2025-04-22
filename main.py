# main.py - Simulation of Smart Food Locker Logic

def open_locker():
    print("🔓 Locker opened.")

def close_locker():
    print("🔒 Locker closed.")

def main():
    correct_pin = "1234"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        pin = input("Enter PIN to open locker: ")
        if pin == correct_pin:
            open_locker()
            break
        else:
            print("❌ Incorrect PIN.")
            attempts += 1

    if attempts == max_attempts:
        print("🚨 Access denied. Too many failed attempts.")

    close_locker()

if __name__ == "__main__":
    main()
