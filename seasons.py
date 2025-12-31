from datetime import datetime, date
import inflect

p = inflect.engine()


def main():
    while True:
        input_txt = input("Date of Birth (YYYY-MM-DD):  ").strip()
        try:
            date_of_birth = datetime.strptime(input_txt, "%Y-%m-%d").date()
            if date_of_birth > date.today():
                print("Date of birth cannot be in the future.")
                continue
            break
        except ValueError:
            print("Invalid date format, try again.")

    today = date.today()
    delta = today - date_of_birth
    total_min_from_birth = delta.days * 24 * 60
    words = p.number_to_words(total_min_from_birth)
    print(words)


if __name__ == "__main__":
    main()
