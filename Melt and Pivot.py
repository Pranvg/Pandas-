#Melt & Pivot

df = pd.DataFrame({
"country": ["USA", "USA", "India", "India"],
"year": [2020, 2021, 2020, 2021],
"sales": [100, 120, 90, 110],
"profit": [20, 25, 18, 22],
"tax": [10, 20, 30, 40]
})

melted_df = df.melt(
    id_vars=["country", "year"],
    value_vars=["sales", "profit", "tax"],
    var_name="metrics",
    value_name="value"
    
)


original = melted_df.pivot(
    
    index=["country", "year"],
    columns="metrics",
    values="value"


)


df = pd.read_csv("employee_data.csv")

#df["Age"].hist()

df.plot(kind="scatter", x="Age", y="Salary")




#Merging & joinoing Data


df_customers = pd.DataFrame({
"customer_id": [1, 2, 3, 4],
"name": ["Adam", "Bob", "Charlie", "Dave"]
})
df_orders = pd.DataFrame({
"order_id": [101, 102, 103, 104],
"customer_id": [2, 1, 4, 5],
"amount": [250, 120, 300, 180]
})

pd.merge(df_customers, df_orders, on="customer_id")   #inner join
pd.merge(df_customers, df_orders, on="customer_id", how="left")  #left join
pd.merge(df_customers, df_orders, on="customer_id", how="right")  #right join
pd.merge(df_customers, df_orders, on="customer_id", how="outer")  



df_customers 


df_orders




#Concatenation 

df1 = pd.DataFrame({
        "id" : [1, 2, 3],
        "name": [ "Adam", "Eve", "Bob"],
})

df2 = pd.DataFrame({
         "id" : [4, 5, 6],
        "name": [ "Charlie", "Fester", "Gilian"]
})

pd.concat([df1, df2])  #row
pd.concat([df1, df2], ignore_index=True)   

pd.concat([df1, df2], axis=1)  #col


df1 
df2






