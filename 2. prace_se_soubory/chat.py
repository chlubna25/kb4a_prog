from datetime import datetime
from pathlib import Path


def main():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    chat_path = data_dir / "chatlog.txt"

    print("Jednoduchý chat — zprávy se ukládají do:", chat_path)
    print("Pro ukončení napište 'konec' jako text zprávy.")

    while True:
        username = input("Zadej uživatelské jméno: ").strip()
        if not username:
            print("Uživatelské jméno nesmí být prázdné. Zkus to znovu.")
            continue

        message = input("Zadej zprávu (nebo 'konec' pro ukončení): ").rstrip()
        if message.lower() == "konec":
            print("Chat ukončen.")
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{timestamp} - {username}: {message}\n"

        with chat_path.open("a", encoding="utf-8") as f:
            f.write(line)

        print("Zpráva uložena.")


if __name__ == "__main__":
    main()
