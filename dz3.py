import collections
phones=[{'fabricator':'Realme','country-fabricator':'China','model':'realme 9 Pro'},
        {'fabricator':'Xiaomi','country-fabricator':'China','model':'Xiaomi PRO 12'},
        {'fabricator':'Xiaomi','country-fabricator':'China','model':'Xiaomi Redmi Note 10S'},
        {'fabricator':'Xiaomi','country-fabricator':'China','model':'Xiaomi Redmi Note 10 Pro'},
        ]

added=[['6.67','3GB'],['5','3GB'],['6.3','3GB'],['4.3','4GB']]
phones[0]["Screen"] = added[0][0]
phones[0]["Memory"] = added[0][1]
phones[1]["Screen"] = added[1][0]
phones[1]["Memory"] = added[1][1]
phones[2]["Screen"] = added[2][0]
phones[2]["Memory"] = added[2][1]
phones[3]["Screen"] = added[3][0]
phones[3]["Memory"] = added[3][1]

count = collections.Counter([phones[x]['fabricator'] for x in range(len(phones))])
print(count)
for i in count.items():
    print(i)
for i in count.values():
    print(i)

count = collections.Counter([phones[x]['Memory'] for x in range(len(phones))])
print('-------------')
for i in sorted(count.items()):
    print(i)
for i in sorted(count.values()):
    print(i)
    
