import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv"

df = pd.read_csv(url)

if 'Industry' in df.columns:
    df['Industry'] = df['Industry'].fillna(df['Industry'].mode()[0])
    industry_counts = df["Industry"].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=industry_counts.values, y=industry_counts.index, palette="viridis")
    plt.title("Distribution of Respondents by Industry")
    plt.xlabel("Number of Respondents")
    plt.ylabel("Industry")
    plt.tight_layout()
    plt.show()

    print("\nNotable trends:")
    if len(industry_counts) > 0:
        print(f"The most represented industry is '{industry_counts.idxmax()}' with {industry_counts.max()} respondents.")
    if len(industry_counts) > 1:
        print(f"The least represented industry is '{industry_counts.idxmin()}' with {industry_counts.min()} respondents.")

else:
    print("Unable to find 'Industry' in column")


if 'ConvertedCompYearly' in df.columns:
    df['ConvertedCompYearly'] = df['ConvertedCompYearly'].fillna(df['ConvertedCompYearly'].mode()[0])
    cleaned_Comp = df['ConvertedCompYearly']
    mean_compensation = cleaned_Comp.mean() #mean
    median_compensation = cleaned_Comp.median() #median
    standevia_compensation = cleaned_Comp.std() #standard deviation

    print(f'Mean compensation: {mean_compensation}')
    print(f'Median compensation: {median_compensation}')
    print(f'Standard deviation compensation: {standevia_compensation}')

    threshold = mean_compensation + standevia_compensation * 3

    outliers = cleaned_Comp[cleaned_Comp>threshold]

    print(f"\nNumber of respondents with high compensation outliers: {len(outliers)}")
    print(outliers.head())  
else:
    print("Unable to find 'ConvertedCompYearly' in column")


if 'ConvertedCompYearly' in df.columns:

    #Calculate Q1, Q3, IQR
    Q1 = cleaned_Comp.quantile(0.25)
    Q3 = cleaned_Comp.quantile(0.75)
    IQR = Q3 - Q1

    # upper and lower bound
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR

    print(f"Q1: {Q1}")
    print(f"Q3: {Q3}")
    print(f"IQR: {IQR}")
    print(f"Lower Bound: {lower_bound}")
    print(f"Upper Bound: {upper_bound}")

    plt.figure(figsize=(10, 6))
    sns.boxplot(x=cleaned_Comp, whis=1.5, orient='h', color='skyblue')
    plt.title("Box Plot of ConvertedCompYearly with Outliers")
    plt.xlabel("Compensation (Yearly)")
    plt.show()
else:
    print("The dataset does not contain a 'ConvertedCompYearly' column.")


if 'Age' in df.columns:
    # Map Age ranges to approximate numeric values
    age_mapping = {
        'Under 18 years old': 15,
        '18-24 years old': 21,
        '25-34 years old': 30,
        '35-44 years old': 40,
        '45-54 years old': 50,
        '55-64 years old': 60,
        '65 years or older': 70
    }
    
    df['AgeNumeric'] = df['Age'].map(age_mapping)

    numerical_columns = df.select_dtypes(include=['number']).columns

    correlation_matrix = df[numerical_columns].corr()

    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title("Correlation Matrix")
    plt.show()

    print("Correlations with Age (transformed):")
    print(correlation_matrix['AgeNumeric'].sort_values(ascending=False))
else:
    print("The dataset does not contain an 'Age' column.")