from data_cleaning import clean_data
from analysis import aggregate_sales, top_products
from visualization import plot_sales_by_month
import os
# 1. Завантаження та очищення даних
BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
file_path = os.path.join(BASE_DIR, 'online_retail.csv')
df = clean_data(file_path)

# 2. Аналіз
sales_by_month = aggregate_sales(df)
top10 = top_products(df)

# 3. Візуалізація
BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs/figures')
file_path = os.path.join(BASE_DIR, 'sales_by_month.png')
plot_sales_by_month(sales_by_month, file_path)






