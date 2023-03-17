import pandas as pd

data = pd.read_csv('data_C02_emission.csv')

#A
print("a)")
print(data.shape)
print("Postoji", data.isnull().sum().sum(), "redaka s izostavljenim podacima.")
data.dropna()
print("Postoji", data.duplicated().sum(), "redaka s ponovljenim podacima.")
data.drop_duplicates()
for col in ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']:
    data[col] = data[col].astype('category')

#B
#Fuel Consumption City (L/100km)
print("b)")
highest_consumption = data.sort_values(by=['Fuel Consumption City (L/100km)'], ascending=False).head(3)
lowest_consumption = data.sort_values(by=['Fuel Consumption City (L/100km)']).head(3)

print("Highest Fuel Consumption City (L/100km)")
print(highest_consumption[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print("Lowest Fuel Consumption City (L/100km)")
print(lowest_consumption[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

#C
print("c)")
engine_size_interval = data[(data['Engine Size (L)'] > 2.5) & (data['Engine Size (L)'] < 3.5)]
print("Broj ovih vozila je", engine_size_interval['Engine Size (L)'].count())
print("Prosječna emisija CO2 je ", round(engine_size_interval['CO2 Emissions (g/km)'].mean(), 2), " g/km")

#D
print("d)")
audis = data[(data['Make'] == "Audi")]
print("Postoji", audis.shape[0], "mjerenja za proizvođača Audi.")
audis_4_cilinder = audis[(audis['Cylinders'] == 4)]
print("Prosječna emisija CO2 iznosi", round(audis['CO2 Emissions (g/km)'].mean(), 2), "g/km")

#E
print("e)")
grouped_by_cilinders_count = data.groupby("Cylinders").count()
grouped_by_cilinders_mean = data.groupby("Cylinders").mean()
print(grouped_by_cilinders_count["Make"])
print(grouped_by_cilinders_mean["CO2 Emissions (g/km)"])

#F
print("f)")
using_diesel = data[(data['Fuel Type'] == 'D')]
using_gasoline = data[(data['Fuel Type'] == 'X')]
print("Prosječna potrošnja za dizelaše je", round(using_diesel["Fuel Consumption City (L/100km)"].mean(), 2), "L/100km")
print("Prosječna potrošnja za benzince je", round(using_gasoline["Fuel Consumption City (L/100km)"].mean(), 2), "L/100km")
print("Medijalna potrošnja za dizelaše je", round(using_diesel["Fuel Consumption City (L/100km)"].median(), 2), "L/100km")
print("Medijalna potrošnja za benzince je", round(using_gasoline["Fuel Consumption City (L/100km)"].median(), 2), "L/100km")

#G
print("g)")
all_with_condition = data[(data['Fuel Type'] == 'D') & (data['Cylinders'] == 4)]
uses_most = all_with_condition.sort_values(by=['Fuel Consumption City (L/100km)'], ascending=False).head(1)
print("Najveću gradsku potrošnju ima", uses_most['Make'].astype(str), uses_most['Model'].astype(str))

#H
print("h)")
manual_transmission = data[(data["Transmission"].str.startswith('M'))]
print("Postoji", manual_transmission.shape[0], "vozila s ručnim mjenjačem.")

#I
print("i)")
print(data.corr(numeric_only=True))