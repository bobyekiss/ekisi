person = {
    "firstname": "Théo",
    "lastname": "Dupin",
    "age": 52,
    "email": "t.dupin@gmail.com",
    "work": "Analyste SOC",
    "phones": ["0247020202", "0622334455"],
    "address": [38, "rue Jules Charpentier", 37000, "Tours"]
}
print(person)
person = {
    "firstname": "Théo",
    "lastname": "Dupin",
    "age": 52,
    "email": "t.dupin@gmail.com",
    "work": "Analyste SOC",
    "phones": ["0247020202", "0622334455"],
    "address": {
        "number": 38,
        "street": "rue Jules Charpentier",
        "postal": 37000,
        "city": "Tours"
    }
}

print(person["address"]["street"])