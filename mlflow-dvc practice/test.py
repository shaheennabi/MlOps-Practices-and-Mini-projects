import pandas as pd

data = [
    {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice.johnson@example.com",
        "phone": "+1-555-1234",
        "city": "San Francisco",
        "occupation": "Software Engineer"
    },
    {
        "name": "Michael Chen",
        "age": 35,
        "email": "michael.chen@example.com",
        "phone": "+1-555-5678",
        "city": "New York",
        "occupation": "Data Scientist"
    },
    {
        "name": "Sophie Brown",
        "age": 22,
        "email": "sophie.brown@example.com",
        "phone": "+1-555-9876",
        "city": "Austin",
        "occupation": "Marketing Specialist"
    },
    {
        "name": "hello Brown",
        "age": 222,
        "email": "lse.brown@example.com",
        "phone": "+1-555-9876",
        "city": "Mars",
        "occupation": "Marketing Specialist"
    },
    {
        "name": "nemo Brown",
        "age": 22,
        "email": "sophie.brown@example.com",
        "phone": "+1-5355-9876",
        "city": "Aurora",
        "occupation": "Aueronatics"
    }
]

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv("data/data.csv", index=False)
