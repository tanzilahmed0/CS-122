''' 1: Create analysis.py.
• 2: Load expense data into a pandas DataFrame via CSV or ORM.
• 3: For a given month and year, compute total spending per category and save to
expense_summary.csv.
• 4: Plot a bar chart of the top five spending categories and save as expense_plot.png. ''' 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

from db import init_db, ExpenseModel

def main(month: int = 12, year: int = 2025):
    session = init_db()
    expenses = session.query(ExpenseModel).all()

    df = pd.DataFrame([{'amount': e.amount, 'category': e.category, 'date': e.date, 'description': e.description}  for e in expenses])
    df["date"] = pd.to_datetime(df["date"])

    df = df[(df['month'] == month) & df['year'] == year]
    
    # Total spending per category
    spending_cat = (
        df.groupby("category")["amount"]
        .sum()
        .reset_index()
        .rename(columns={"amount": "total_spent"})
        .sort_values("total_spent", ascending=False)
    )

    # Save summary CSV
    spending_cat.to_csv("expense_summary.csv", index=False)

    # Top 5 categories + plot
    top5 = spending_cat.head(5)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top5, x="category", y="total_spent")
    plt.title(f"Top 5 Spending Categories ({month:02d}/{year})")
    plt.xlabel("Category")
    plt.ylabel("Total Spent")
    plt.tight_layout()
    plt.savefig("expense_plot.png")

    session.close()


if __name__ == "__main__":
    # change these as needed
    main(month=12, year=2025)