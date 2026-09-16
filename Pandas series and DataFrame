import pandas as pd

info = {
    "Name" : ["Rahul", "Harshita", "Pranav"],
    "CGPA" : ["9.5", "7.5", "8.2"],
    } 


df = pd.DataFrame(info)
print(df)



s = pd.Series([1, 2, 3, 4, 5])
print(s)
print(type(s))

#index


print(s[0])
print(s[4])




s = pd.Series([23, 24, 25, 26], index=["Adam", "Eve", "Bob", "Charlie"])
print(s)

print(s["Adam"])
print(s["Bob"])

print(s.iloc[1])





s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40 ,50])

print(s1 + s2)

s1[0] = 100

changed_s1 = s1.drop(0)
print(s1)
print(changed_s1)









# DataFrame

info = {

    "Name" : ["Adam", "Eve", "Bob"],
    "Age" : [23, 24, 25],
    "GPA" : [9.5, 6.8, 8.2]
}


df = pd.DataFrame(info)
print(df, type(df))

print(df.index)
print(df.columns)




df = pd.DataFrame([["Adam", 23] , ["Eve", 24], ["Bob", 25] ], columns = ["Name", "Age"])

print(df)







import numpy as np 

np_arr = np.array([[1, 2, 3], [4, 5, 6] ])

df =pd.DataFrame(np_arr, columns=["A", "B", "C"])

print(df)

print(s.index)
