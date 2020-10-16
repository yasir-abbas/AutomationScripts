#This is python api for Hunter.io. Given domain as input it searches for all the emails in that domain


from pyhunter import PyHunter

hunter = PyHunter('3f5fa87a9141779d8bcc92b13a923069edb5d586')

emailsData = hunter.domain_search('https://www.palmchip.com/')

# print(emailsData)

for key,value in emailsData.items():
    print(key," ", value)

# for value in emailsData["emails"]:
#     for key,values in value.items():
#         if key == "sources":
#             pass
#         else:
#             print(key," ",values)