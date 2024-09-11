usernames = ["Daylan", "Pravir", "Maharaj"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

print(type(users))
for x in users:
    print(x)