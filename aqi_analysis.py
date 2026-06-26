# Step 1- Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2- Load Dataset
print("Libraries imported successfully")
# Load the dataset
df = pd.read_csv('city_day.csv')

# Check first 5 rows
print(df.head())

# Check shape
print("Rows and Columns:", df.shape)

# Check column names
print("Columns:", df.columns)

# Check basic information
print("\n--- Dataset Info ---")
print(df.info())

# Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Step 2 - Explore Data(statistics)

# Check basic statistics
print("\n--- Basic Statistics ---")
print(df.describe())

# Check missing values in percentage
print("\n--- Missing Values Percentage ---")
missing = df.isnull().sum() / len(df) * 100
print(missing)

# Check total rows
print("\n--- Total Rows ---")
print(len(df))

# Step 4 - Clean Data
# Drop columns with too many missing values
df = df.drop(columns=['Xylene'])

# Fill missing values with mean
df = df.fillna(df.mean(numeric_only=True))

# Check missing values again
print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

print("\nData Cleaning Complete!✅")

# Step 5 - Data Visulization

# Top 10 most polluted cities
plt.figure(figsize=(12,6))
city_aqi = df.groupby('City')['AQI'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=city_aqi.values, y=city_aqi.index, palette='Reds_r')
plt.title('Top 10 Most Polluted Cities in India')
plt.xlabel('Average AQI')
plt.ylabel('City')
plt.tight_layout()
plt.savefig('top10_polluted_cities.png')
plt.show()
print("Graph 1 saved successfully! ✅")

# Graph 2 - AQI Trend Over Years
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

plt.figure(figsize=(12,6))
year_aqi = df.groupby('Year')['AQI'].mean()
sns.lineplot(x=year_aqi.index, y=year_aqi.values, marker='o', color='red')
plt.title('AQI Trend Over Years in India')
plt.xlabel('Year')
plt.ylabel('Average AQI')
plt.tight_layout()
plt.savefig('aqi_trend_years.png')
plt.show()
print("Graph 2 saved successfully! ✅")

# Graph 3 - PM2.5 Analysis by City
plt.figure(figsize=(12,6))
city_pm25 = df.groupby('City')['PM2.5'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=city_pm25.values, y=city_pm25.index, palette='Blues_r')
plt.title('Top 10 Cities with Highest PM2.5 Levels')
plt.xlabel('Average PM2.5')
plt.ylabel('City')
plt.tight_layout()
plt.savefig('pm25_analysis.png')
plt.show()
print("Graph 3 saved successfully! ✅")

# Graph 4 - Seasonal AQI Analysis
df['Month'] = df['Date'].dt.month

plt.figure(figsize=(12,6))
month_aqi = df.groupby('Month')['AQI'].mean()
sns.lineplot(x=month_aqi.index, y=month_aqi.values, marker='o', color='green')
plt.title('Monthly AQI Trend in India')
plt.xlabel('Month')
plt.ylabel('Average AQI')
plt.xticks(range(1,13), ['Jan','Feb','Mar','Apr','May','Jun',
                          'Jul','Aug','Sep','Oct','Nov','Dec'])
plt.tight_layout()
plt.savefig('seasonal_aqi.png')
plt.show()
print("Graph 4 saved successfully! ✅")

# Graph 5 - Heatmap of Pollutants
plt.figure(figsize=(12,8))
correlation = df[['PM2.5','PM10','NO','NO2','NOx',
                   'NH3','CO','SO2','O3','AQI']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Pollutants')
plt.tight_layout()
plt.savefig('pollutants_heatmap.png')
plt.show()
print("Graph 5 saved successfully! ✅")

# Graph 6 - Delhi vs Mumbai Comparison
plt.figure(figsize=(12,6))
delhi = df[df['City']=='Delhi'].groupby('Year')['AQI'].mean()
mumbai = df[df['City']=='Mumbai'].groupby('Year')['AQI'].mean()

plt.plot(delhi.index, delhi.values, marker='o', color='red', label='Delhi')
plt.plot(mumbai.index, mumbai.values, marker='o', color='blue', label='Mumbai')
plt.title('Delhi vs Mumbai AQI Comparison')
plt.xlabel('Year')
plt.ylabel('Average AQI')
plt.legend()
plt.tight_layout()
plt.savefig('delhi_vs_mumbai.png')
plt.show()
print("Graph 6 saved successfully! ✅")
