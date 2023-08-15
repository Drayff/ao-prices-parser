import wget
from tqdm import tqdm  # Импортируем библиотеку tqdm

def download_file(url, filename):
    wget.download(url, filename)

def process_items_file(input_file, output_file):
    count = 0  # Счетчик обработанных предметов
    processed_items = set()  # Множество для отслеживания уже обработанных предметов

    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in tqdm(lines, desc="Обработка предметов"):  # Используем tqdm для индикатора прогресса
            line = line.strip()
            line_parts = line.split(': ')
            
            if len(line_parts) < 2:
                continue

            item_name = line_parts[1].strip()

            if '@' in item_name:
                continue

            if item_name in processed_items:
                continue

            processed_items.add(item_name)
            f.write(item_name + '\n')

            count += 1

    print(f"\nОбработка завершена. Всего обработано {count} предметов.")

# Сначала загрузим файл
input_url = 'https://raw.githubusercontent.com/broderickhyman/ao-bin-dumps/master/formatted/items.txt'
input_file = 'items.txt'
download_file(input_url, input_file)

# Теперь обработаем загруженный файл
output_file = 'items.txt'
process_items_file(input_file, output_file)
