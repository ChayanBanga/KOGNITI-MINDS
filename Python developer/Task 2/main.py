import pandas  as pd 
import smtplib 
templates = {
    "Welcome": """Subject: Welcome to Our Service

Hi {name},

Thanks for joining us! We're excited to have you.

Best regards,
{post}  
Your Company""",

    "Thank you": """Subject: Thank You from Our Team

Hi {name},

We appreciate your business. Thank you for choosing us!

Warm wishes,  
Your Company
{post}"""

}


customers = pd.read_csv(r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 2\data_of_custom.csv")
print(customers["Name"])

message = templates["Thank you"].format(name=customers['Name'],post = customers['Department'])
size_of_list = (customers["Name"].count())
listing = customers['Email']




smt = smtplib.SMTP("smtp.gmail.com", 587)

smt.starttls()
smt.login("chayanbanga19042004@gmail.com","hmna wbpe urjk kpky")#Add a new app password or ask user to enter it 

for i in range(size_of_list):
    name = customers['Name'][i]
    email = listing[i]
    post = customers['Department'][i]
    message = templates["Thank you"].format(name=name , post = post)

    smt.sendmail("chayanbanga19042004@gmail.com", email, message)
    print(f"Sent to {name} - {email}")
smt.quit()