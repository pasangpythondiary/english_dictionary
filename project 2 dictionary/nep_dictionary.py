import csv
with open('data.csv') as file:
    reader=csv.reader(file)

    count=0

    for row in reader:
        print(row)

        if count>5:
            break
        
        count+=1
        


print(type(data))
"""
def translate(w):
    return data[w]

word=input("Enter word: ")

print(translate(word))

"""