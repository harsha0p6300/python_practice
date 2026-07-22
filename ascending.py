#Given a dictionary, sort it based on values in ascending order
dict1={
    "ma":5,
    "ha":3,
    "na":1,
    "ti":2,
    "oh":4
}

sort=dict(sorted(dict1.items(), key=lambda item: item[1]))
print(sort)