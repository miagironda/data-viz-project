# import statements
import pandas as pd

# create pandas dataframe from data
df = pd.read_csv("/Users/miagironda/Data_Visualization_Project/data-viz-project/original_dataset.csv")

# convert the date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# extract "Year" from the date
df["Year"] = df["Date"].dt.year

# filter the dataframe to include only dates from the years 2012 to 2022
df_filtered_time = df[(df["Year"] >= 2012) & (df["Year"] <= 2022)]

# group by "Year" and "RegionName", then calculate the mean of each group
aggregated_df = df_filtered_time.groupby(["Year", "RegionName"]).mean().reset_index()

# create a list of borough names in London
london_boroughs = [
    "Barking and Dagenham", "Barnet", "Bexley", "Brent", "Bromley", "Camden",
    "Croydon", "Ealing", "Enfield", "Greenwich", "Hackney", "Hammersmith and Fulham",
    "Haringey", "Harrow", "Havering", "Hillingdon", "Hounslow", "Islington",
    "Kensington and Chelsea", "Kingston upon Thames", "Lambeth", "Lewisham",
    "Merton", "Newham", "Redbridge", "Richmond upon Thames", "Southwark",
    "Sutton", "Tower Hamlets", "Waltham Forest", "Wandsworth", "Westminster"
]

# filtering the dataframe to include only boroughs in London
london_df = aggregated_df[aggregated_df["RegionName"].isin(london_boroughs)]

# create a subset of columns to use and check for nan values
columns_to_check = [
    "Year", "RegionName", "AveragePrice", "12m%Change", "SalesVolume", 
    "FlatPrice", "Flat12m%Change", "MortgagePrice", "Mortgage12m%Change", "FTBPrice", 
    "FTB12m%Change", "FOOPrice", "FOO12m%Change"
    ]

# drop any missing values in the specified columns
df_london_cleaned = london_df.dropna(subset=columns_to_check)

# drop any othercolumns not wanted
df_london_cleaned = df_london_cleaned[columns_to_check]
print(df_london_cleaned)

# check to make sure there are no missing values
nan_count_per_column = df_london_cleaned.isna().sum()
print(nan_count_per_column)

# convert filtered dataframe into a new csv file to use in html file
output_directory = "/Users/miagironda/Data_Visualization_Project/data-viz-project/"
df_london_cleaned.to_csv(output_directory + "filtered_data.csv", index = False)



