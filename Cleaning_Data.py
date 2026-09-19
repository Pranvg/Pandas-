#feature engineering

df2 = df.copy()

df2["tax"] = df2["income"].apply(lambda x: "20%" if x >= 50000 else "10%" )
#Male =>M, Female=> F, Unknown => U

gender_map = {"Male" : "M", "Female" : "F", "Unknown" : "U"}
              
df2["gender"] = df2["gender"].map(gender_map)


df2.assign(new_income = df2["income"] * 1.1)



df2["country"] = df2["country"].replace("USA", "UK")

#rename

df2.columns = ["id", "Name", "Age", "Country", "Gender", "Income","Tax"] 
df2.rename(columns={"Income":"Salary"})

df2.rename(index={1:"First"}, inplace = True)

df2.sort_values(["Income"])
df2 = df2.fillna(50) 
#df2.sort_values("Income", ascending=False)
sorted_df = df2.sort_values(["Income", "Age"])
sorted_df.sort_index()

#reset
sorted_df.reset_index()
sorted_df.reset_index(drop=True)


#sorted_df["Ranking"] = sorted_df["Income"].rank(ascending=True)
sorted_df[["id", "Name", "Age", "Country", "Gender", "Tax","Income"]] 



sorted_df







df2 = df.copy()

new_col_order = [col for col in df2.columns if col != "id"] + ["id"]

print(new_col_order)


df2[new_col_order]









df2 = df.copy()

df2 = df2.drop_duplicates()
df2 = df2.fillna(0)


df2 = df2.sort_values("income")

df2 = df2.reset_index(drop=True)

df2.to_csv("sorted_data.csv")



df.groupby("country")["income"].mean()
df.groupby("country")["income"].min()
df.groupby("country")["income"].max()


df.groupby("gender")["income"].mean()
df.groupby("gender")["income"].max()

df.groupby("country")["income"].agg(["mean", "min", "max"])
df.groupby("country")["income"].aggregate(avg_salary="mean", min_salary="min", max_salary="max")



df.groupby("country").agg({

     "income" : "mean",
     "age" : "mean"
 })



df.groupby("country").agg(

   max_salary =  ("income" , "max"),
     avg_age = ("age" , "mean")
 )






max_salary	avg_age
country		
Canada	62000.0	NaN
China	51000.0	27.000000
India	73000.0	45.000000
Mexico	45000.0	NaN
Spain	NaN	34.000000
USA	62000.0	29.666667
