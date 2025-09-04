import os

def main():
    print("📁 Создание папок по годам и месяцам")
    print("—" * 50)

    # Ввод года
    year_input = input("Введите год (например, 2025): ").strip()
    if not year_input.isdigit():
        print("❌ Неверный формат года. Используем 2025.")
        year = 2025
    else:
        year = int(year_input)

    # Имена месяцев
    months = [
        "Январь", "Февраль", "Март", "Апрель",
        "Май", "Июнь", "Июль", "Август",
        "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ]

    # Папка для года
    year_folder = str(year)
    if not os.path.exists(year_folder):
        os.mkdir(year_folder)
        print(f"✅ Создана папка: {year_folder}")
    else:
        print(f"ℹ️  Папка {year_folder} уже существует.")

    # Создаём подпапки: 01 - Январь, 02 - Февраль и т.д.
    for i, month in enumerate(months, 1):
        folder_name = f"{i:02d} - {month}"
        full_path = os.path.join(year_folder, folder_name)
        
        if not os.path.exists(full_path):
            os.mkdir(full_path)
            print(f"✅ {folder_name}")
        else:
            print(f"ℹ️  Пропущено: {folder_name} (уже есть)")

    print("—" * 50)
    print(f"🎉 Структура папок для {year} создана!")
    print("Теперь можно сортировать фото, документы и т.д.")

if __name__ == "__main__":
    main()
