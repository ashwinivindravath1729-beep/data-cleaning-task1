import pandas as pd
from dateutil import parser as dateparser

print("Starting Data Cleaning...")

df = pd.read_csv('data.csv')
print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

print("\n--- Missing Values ---")
print(df.isnull().sum())
print(f"Duplicates: {df.duplicated().sum()}")

df = df.drop_duplicates()
print(f"\nAfter removing duplicates: {df.shape[0]} rows")

df['age'] = df['age'].fillna(df['age'].median())
df['purchase_amount'] = df['purchase_amount'].fillna(df['purchase_amount'].mean())
df['name'] = df['name'].fillna('Unknown')
df['city'] = df['city'].fillna('Unknown')
print("Missing values filled!")

df['name'] = df['name'].str.strip().str.title()
df['email'] = df['email'].str.strip().str.lower()
df['city'] = df['city'].str.strip().str.title()
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True).str[-10:]
df['age'] = df['age'].astype(int)
df['purchase_amount'] = df['purchase_amount'].round(2)

def fix_gender(g):
    g = str(g).strip().lower()
    if g in ['f', 'female']: return 'Female'
    elif g in ['m', 'male']: return 'Male'
    return 'Other'
df['gender'] = df['gender'].apply(fix_gender)

def fix_date(d):
    try: return dateparser.parse(str(d)).strftime('%Y-%m-%d')
    except: return None
df['purchase_date'] = df['purchase_date'].apply(fix_date)
print("All columns standardized!")

print("\n--- Clean Data ---")
print(df.to_string())

df.to_csv('cleaned_data.csv', index=False)
print("\nSaved to cleaned_data.csv!")
print("Done!")