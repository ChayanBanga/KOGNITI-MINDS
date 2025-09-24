import pandas as pd
data = [
    ["John Smith", "john.smith@example.com", "123-456-7890", "TechNova", "Product Manager"],
    ["Sarah Johnson", "sarah.johnson@marketingworld.com", "987-654-3210", "MarketingWorld", "Sales Director"],
    ["Michael Chen", "michaelchen@invalid", "321-654-9870", "HealthPlus", "Data Analyst"],
    ["Emily Davis", "emily.davis@example.com", "555-444-3333", "DesignPro", "UI Designer"],
    ["John Smith", "john.smith@example.com", "123-456-7890", "TechNova", "Product Manager"],  # duplicate
    ["Daniel Lee", "daniel.lee@examplecom", "222-333-4444", "CodeBase", "DevOps Engineer"],
    ["Rachel Green", "rachel.green@example.com", "444-555-6666", "FashionCorp", "Brand Manager"],
    ["Monica Geller", "monica@cleaning.com", "777-888-9999", "Spotless", "Manager"],
    ["Chandler Bing", "chandler.bing@example.com", "000-111-2222", "FunnyCorp", "Copywriter"],
    ["Ross Geller", "rossgeller@dinosaurs", "111-222-3333", "MuseumTech", "Paleontologist"],
    ["Phoebe Buffay", "phoebe@example.com", "333-444-5555", "MusicLife", "Musician"],
    ["Joey Tribbiani", "joey@actor.com", "888-999-0000", "Hollywood Inc", "Actor"],
    ["Tony Stark", "tony.stark@starkindustries.com", "101-202-3030", "Stark Industries", "CEO"],
    ["Bruce Wayne", "bruce@wayneenterprises.", "909-808-7070", "Wayne Enterprises", "CEO"],
    ["Clark Kent", "clark.kent@example.com", "606-505-4040", "Daily Planet", "Reporter"],
    ["Peter Parker", "peter.parker@spiderman", "303-202-1010", "Daily Bugle", "Photographer"],
    ["Diana Prince", "diana@example.com", "111-111-1111", "Themyscira", "Ambassador"],
    ["Barry Allen", "barry.allen@example.com", "222-222-2222", "Central Labs", "Scientist"],
    ["Hal Jordan", "hal.jordan@example.com", "333-333-3333", "Air Force", "Pilot"],
    ["Bruce Wayne", "bruce@wayneenterprises.", "909-808-7070", "Wayne Enterprises", "CEO"],  # duplicate
    ["Lex Luthor", "lex@evil.com", "444-444-4444", "LuthorCorp", "Founder"],
]

# Column names
columns = ["Full Name", "Email", "Phone", "Company", "Job Title"]

# Setting columns namme here 
df = pd.DataFrame(data , columns=columns )

#Comverting Dataframe to .csv file 
df.to_csv(r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 1\company_leads.csv", index = False)
