#AQI Data Set

df = pd.read_csv("globalAirQuality.csv")


df.head()

df.describe()

#selecting the data

#columns
df["city"]
df[["city", "aqi"] ]

#rows
df.loc[2]
df.loc[0:2]  #start idx : end idx (inclusive)

#cells
df.iloc[2]
df.iloc[0:2]    #start idx : end idx (exclusive)


#cells - row and column
df.loc[0:2, ["city","aqi", "latitude", "longitude" ] ]
df.columns

#df.iloc[0:3, 2]





df.loc[0:2, ["city","aqi", "latitude", "longitude" ] ]

df.iloc[0:3, 1:5 ]


#cell

df.at[0, "city"]

df.iat[0, 2]


cities = df["city"] #view

cities[0] = "New York"




#Filtering the data
df[ df["aqi"] > 100]

df[ (df["aqi"]) > 100 & (df["temperature"] > 30) ]

df[ (df["aqi"]) > 100 & (df["temperature"] < 30) ]




aqi_data = df[ (df["aqi"] > 100) &  (df["temperature"] > 30)]  [["city", "aqi"] ]

aqi_data
aqi_data.iloc[0]
aqi_data.loc[6]


#Query
aqi_val = 100


df.query("aqi > 100 & temperature > 30") [["city", "country"]]
aqi_data = df.query("aqi > @aqi_val & temperature > 30") [["city", "country", "aqi"]].copy

aqi_data


date_str = pd.Series([pd.to_datetime("2026-12-31")])
type(date_str.dtypes)



df["gender"].str.capitalize()


df["name"].str.split(" ")

#pranav@gmail.com
#shradha@gmail.com
#df["name"].str.split(" ")

df["country"].str.contains("india", case=False)












