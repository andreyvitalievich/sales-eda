def aggregate_sales(df):
     return df.groupby('month')['total'].sum().reset_index()  # Сумарні продажі по місяцях

def top_products(df, n=10):
    return df.groupby('StockCode')['total'].sum().nlargest(10) # Топ 10 продуктів