📊 Sales Data Analysis (EDA)
This project is a simple and clean Exploratory Data Analysis (EDA) of sales data written in Python using PyCharm.
It demonstrates key data analytics skills: data cleaning, transformation, aggregation, visualization, and extracting insights useful for business decisions.

🧱 Project Structure
project/
├─ data/
│  ├─ sales.csv
├─ outputs/
│  ├─ figures/
│  │  ├─ sales_by_month.png
├─ src/
│  ├─ main.py
│  ├─ data_cleaning.py
│  ├─ analysis.py
│  ├─ visualization.py
├─ README.md
└─ requirements.txt

🎯 Project Objectives
Load and explore the sales dataset
Clean the data (missing values, invalid rows, negative quantities)
Create new calculated fields (total, month)
Analyze sales patterns
Build visualizations using matplotlib
Save charts to /outputs/figures/
Summarize business insights

📥 Dataset Description
The dataset (CSV file) contains sales transactions.
Column	Description

| Column      | Description               |
| ----------- | ------------------------- |
| order_id    | Unique order identifier   |
| order_date  | Date of purchase          |
| customer_id | Customer unique ID        |
| product_id  | Product identifier        |
| category    | Product category          |
| price       | Price for one unit        |
| quantity    | Number of units purchased |
| country     | Customer’s country        |

🧹 Data Cleaning
The script removes or fixes problematic data:
✔ Remove rows with missing critical fields
df = df.dropna(subset=['order_id', 'order_date', 'price'])
✔ Fill missing categories
df['category'] = df['category'].fillna('Unknown')
✔ Remove rows where quantity is negative
df = df[df['quantity'] >= 0]

🧮 Feature Engineering
Total transaction revenue
df['total'] = df['price'] * df['quantity']
Extract monthly period
df['month'] = df['order_date'].dt.to_period('M')

📊 Analysis & Visualizations
Monthly sales revenue
Aggregation:
sales_by_month = df.groupby('month')['total'].sum().reset_index()
Plot:
plt.plot(sales_by_month['month'].astype(str), sales_by_month['total'])
Saved to:
/outputs/figures/sales_by_month.png
Top 10 products:
top_products = df.groupby('product_id')['total'].sum().nlargest(10)
Descriptive statistics:
df.describe()

🧠 Key Insights
(Example placeholder — replace with your real findings)
Sales have seasonal spikes in specific months
A small number of products generate a large portion of total revenue
Some countries contribute significantly more to global sales
Several data anomalies (missing values, negative quantities) were found and fixed

🛠 Technologies Used
- Python
- pandas
- numpy
- matplotlib
- PyCharm

🚀 How to Run the Project
Clone the repository:
git clone https://github.com/andreyvitalievich/sales-eda.git
Install required libraries:
pip install -r requirements.txt
Run the project in PyCharm (or any IDE) by executing:
src/main.py
Output charts will appear in:
outputs/figures/

📬 Contact
Author: Shyianovskyi Andrii
Email: kabelua351@gmail.com
GitHub: https://github.com/andreyvitalievich
Telegram: +380 66 409 17 94