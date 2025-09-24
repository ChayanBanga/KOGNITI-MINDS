import pandas as pd

data = [
    ["Chayan Banga", "chayanbanga1978@gmail.com", "9711206083", "IT"],
    ["Amit Banga", "Amit.purchase@micronsindia.com", "9711206083", "Manager"],
    ["Harshit Banga", "harshitbanga0195@gmail.com", "9718697158" , "CA"]
] 
column = ["Name","Email","Phone_no.","Department"]
df = pd.DataFrame(data,columns=column)

df.to_csv(r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 2\data_of_custom.csv", index= False)