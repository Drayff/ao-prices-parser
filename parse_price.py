import requests
import json
import configparser

# Чтение параметра из INI-файла
config = configparser.ConfigParser()
config.read('config.ini')

if 'Game' in config and 'locations' in config['Game']:
    location = config['Game']['locations']
else:
    print("Параметр 'locations' не найден в INI-файле.")
    exit()

# URL базового эндпоинта API
base_url = "https://west.albion-online-data.com/api/v2/"

# Функция для получения цен предметов
def get_item_prices(item_id):
    # Конструируем URL для эндпоинта получения цен предметов
    url = base_url + "stats/Prices/" + item_id + "?locations=" + location

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем JSON-ответ
        json_data = response.json()

        # Обрабатываем JSON-ответ и извлекаем цены предметов
        for item in json_data:
            item_name = item["item_id"]
            item_prices = item["sell_price_min"], item["sell_price_max"], item["buy_price_min"], item["buy_price_max"]
            print(f"Предмет: {item_name}, Минимальная цена продажи: {item_prices[0]}, Максимальная цена продажи: {item_prices[1]}, Минимальная цена покупки: {item_prices[2]}, Максимальная цена покупки: {item_prices[3]}")
    else:
        print("Ошибка при получении цен предметов.")

output_file = "items.txt"  # Путь к файлу с обработанными предметами

with open(output_file, 'r') as f:
    for line in f:
        item_id = line.strip()  # Удаляем лишние пробелы и символы перевода строки
        get_item_prices(item_id)
