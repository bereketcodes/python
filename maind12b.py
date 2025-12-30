import time


def cli_menu_example():
    # The 'while True' creates an infinite loop, ensuring the menu always returns
    while True:
        # --- 1. Display Menu and Get Input ---
        print("\n " + "=" * 30)
        print("    Main Menu Application    ")
        print("=" * 30)
        print("1. View Data")
        print("2. Edit Settings")
        print("3. Exit Program")
        print("-" * 30)

        # Prompt the user for a choice
        choice = input("Enter your choice (1-3): ")

        # --- 2. Process Input ---

        # Option 3: Exit Program (Uses break)
        if choice == '3':
            print("\n👋 Exiting program. Goodbye!")
            # The 'break' statement immediately terminates the 'while True' loop.
            break

            # Invalid Input (Uses continue)
        elif choice not in ('1', '2'):
            print("\n❌ Invalid choice: Please enter 1, 2, or 3.")
            # The 'continue' statement skips the rest of the current loop iteration
            # and immediately jumps back to the start (re-displaying the menu).
            time.sleep(1)
            continue

        # Option 1: View Data (Successful Action)
        elif choice == '1':
            print("\n🔬 Viewing Data...")
            print("Data loaded: User reports for Q3 are ready.")
            time.sleep(2)
            # The loop naturally continues after this code runs,
            # restarting at the top and redisplaying the menu.

        # Option 2: Edit Settings (Successful Action)
        elif choice == '2':
            print("\n⚙️  Entering Settings Editor...")
            print("Settings updated successfully.")
            time.sleep(2)
            # The loop naturally continues after this code runs.


# Start the menu application
if __name__ == "__main__":
    cli_menu_example()