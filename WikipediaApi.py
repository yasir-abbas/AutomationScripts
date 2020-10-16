#Returns wikipedia page and parse it also

import wikipedia

# print(wikipedia.summary("ashar aziz"))

page = wikipedia.page("Jeff bezos")

tokens = page.content.split('\n')
tokens = [x for x in tokens if not (x == '')]
final_data = {}
string = "Summary"
final_data[string] = []


for token in tokens:
    if token[0]=="=":
        string = ""
        temp = token.split()
        for i in range(1,len(temp)-1):
            string = string + temp[i] + " "
        final_data[string] = []
    else:
        final_data[string].append(token)

for key,values in final_data.items():
    print(key)
    for value in values:
        print(value)



