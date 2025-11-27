# 📊 Sales Data Analysis (EDA)

This project is a simple **Exploratory Data Analysis (EDA)** of sales data using Python.  
It demonstrates key data analytics skills: data cleaning, transformation, aggregation, and visualization using `pandas` and `matplotlib`.  
The project is structured to be professional and GitHub-ready for portfolio purposes.

---

## 🧱 Project Structure

```
Sales EDA/
├─ data/                 # CSV files with raw sales data
├─ outputs/
│  ├─ figures/           # Saved graphs
├─ src/                  # Python scripts
│  ├─ main.py
│  ├─ data_cleaning.py
│  ├─ analysis.py
│  ├─ visualization.py
├─ README.md
└─ requirements.txt
```

---

## 🎯 Project Objectives

- Load and explore the sales dataset  
- Clean the data (missing values, negative quantities)  
- Create new calculated fields (`total`, `month`)  
- Analyze sales patterns by month and product  
- Build and save visualizations using `matplotlib`  
- Summarize key business insights  

---

## 📥 Dataset Description

The dataset (CSV file) contains sales transactions:

| Column      | Description               |
| ----------- | ------------------------- |
| InvoiceNo   | Unique order identifier   |
| StockCode   | Product stock code        |
| Description | Product description       |
| Quantity    | Number of units purchased |
| InvoiceDate | Date of purchase          |
| UnitPrice   | Price per unit            |
| CustomerID  | Customer unique ID        |
| Country     | Customer’s country        |


---

## 🧹 Data Cleaning

The project cleans the data using the following steps:

### 1. Remove rows with missing critical fields
```python
df = df.dropna(subset=['Description'])
```

### 2. Fill missing categories
```python
df['Description'] = df['Description'].fillna('Unknown')
```

### 3. Remove negative quantities
```python
df = df[df['Quantity'] >= 0]
```

### 4. Add calculated columns
```python
df['total'] = df['Quantity'] * df['UnitPrice']
df['month'] = df['InvoiceDate'].dt.to_period('M')
```

---

## 🧮 Analysis

### Aggregate sales by month
```python
sales_by_month = df.groupby('month')['total'].sum().reset_index()
```

### Top 10 products by revenue
```python
top_products = df.groupby('product_id')['total'].sum().nlargest(10)
```

### Descriptive statistics
```python
df.describe()
```

---

## 📊 Visualization

### Monthly sales plot
```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.figure(figsize=(10,5))
plt.plot(sales_by_month['month'].astype(str), sales_by_month['total'])
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('outputs/figures/sales_by_month.png', dpi=300, bbox_inches='tight')
plt.show()
```

> The chart will be saved in `outputs/figures/`.

---

## 🧠 Key Insights

- Sales peak during certain months (e.g., holiday season)  
- A few products generate the majority of revenue  
- Some countries contribute more to total sales  
- Negative and missing data were cleaned for accurate analysis  

---

## 🛠 Technologies Used

- Python  
- pandas  
- numpy  
- matplotlib  
- PyCharm  

---

## 🚀 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/your-username/sales-eda.git
```

2. Install required libraries:
```bash
pip install -r requirements.txt
```

3. Run the project in PyCharm:
```bash
python src/main.py
```

4. Output charts will appear in:
```
outputs/figures/
```

---

## 📬 Contact

Author: *Shyianovskyi Andrii*  
Email: *kabelua351@gmail.com*  
GitHub: *https://github.com/your-username](https://github.com/andreyvitalievich*  
Telegram: *+380 66 409 17 94*
