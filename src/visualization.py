import matplotlib.pyplot as plt

def plot_sales_by_month(sales_by_month, save_path):
    plt.figure(figsize=(10, 5))  # Полотно графіка 10х5 дюймів
    plt.plot(sales_by_month['month'].astype(str), sales_by_month['total'])  # Будуємо графік х, y
    plt.xticks(rotation=45)  # Повертаємо підписи на 45 градусів щоб вони не накладались
    plt.title('Sales by month')  # Заголовок
    plt.xlabel('Month')  # Назва осі х
    plt.ylabel('Total sales')  # Назва осі у
    plt.tight_layout()  # Робить графік акуратним без накладень
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # Зберігаємо у папку
    plt.show()
    print(sales_by_month.head(12))
