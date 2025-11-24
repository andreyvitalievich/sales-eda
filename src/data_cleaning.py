import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['InvoiceDate'])
    df.shape  # кількість рядків і колонок
    print("===============================")
    print(df.head())  # перші 5 рядків
    print("===============================")
    print(df.info())  # типи колонок, порожні значення
    print("===============================")
    print(df.describe())  # описова статистика для числових колонок
    print("===============================")
    print(df.isnull().sum())   # кількість пропусків в колонках
    df = df.dropna(subset=['Description']) # Видалення рядків з пропусками в колонці конкретній
    df['Description'] = df['Description'].fillna('Unknown') # Замінює значення з пропусками на вказане
    df = df[df['Quantity'] >= 0] # Забираємо рядки з відємними значеннями кількості проданого товару
    df['total'] = df['Quantity'] * df['UnitPrice'] # Створення нової колонки для загальної суми по рядку
    df['month'] = df['InvoiceDate'].dt.to_period('M') # Колонка з місяцями замовлення
    return df