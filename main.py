from analyzer import PasswordAnalyzer
from generator import PasswordGenerator
from breach_checker import BreachChecker


def check_breach():
    password = input("\nEnter the password to check for breaches: ")

    checker = BreachChecker(password)
    count, message = checker.check_breach()

    print(f"\n{message}")

    if count is None:
        pass
    elif count > 0:
        print("  ⚠️  Do NOT use this password anywhere. Change it immediately if you do.")
    else:
        print("  💡 But still make sure it scores well on the strength checker!")

def show_menu():
    print("\n" + "="*45)
    print("       🔐 PASSWORD MANAGER TOOL")
    print("="*45)
    print("  1. Check password strength")
    print("  2. Generate a strong password")
    print("  3. Check if password was in a breach")
    print("  4. Exit")
    print("="*45)


def check_password_strength():
    password = input("\nEnter the password you want to check: ")

    analyzer = PasswordAnalyzer(password)
    score, feedback = analyzer.analyze()
    strength = analyzer.get_strength_label()

    print(f"\nStrength: {strength}  (Score: {score}/6)")

    if feedback:
        print("\nSuggestions to improve it:")
        for tip in feedback:
            print(f"  {tip}")
    else:
        print("\n✅ Great password! No suggestions.")


def generate_password():
    print("\n-- Password Generator --")

    try:
        length = int(input("How long should the password be? (min 8): "))
        if length < 8:
            print("Setting length to minimum of 8.")
            length = 8
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"
    numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"

    generator = PasswordGenerator(length=length, use_symbols=symbols, use_numbers=numbers)
    password = generator.generate()

    print(f"\n✅ Generated Password: {password}")

    # Automatically analyze the generated password
    analyzer = PasswordAnalyzer(password)
    score, _ = analyzer.analyze()
    strength = analyzer.get_strength_label()
    print(f"   Strength: {strength}  (Score: {score}/6)")


def main():
    print("\nWelcome to the Password Manager Tool!")

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            check_password_strength()
        elif choice == "2":
            generate_password()
        elif choice == "3":
            check_breach()
        elif choice == "4":
            print("\nGoodbye! Stay secure 🔐\n")
            break
        else:
            print("\n⚠️  Invalid choice. Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()