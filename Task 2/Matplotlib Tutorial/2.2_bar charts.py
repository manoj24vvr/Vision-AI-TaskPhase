import csv
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd

plt.style.use("fivethirtyeight")

#with open('data.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file)

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
        language_counter.update(response.split(';'))

languages=[]
popularity=[]

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)


languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)


plt.title("Most Popular Languages ")
#plt.ylabel("Programming Languaages")
plt.xlabel("Number of people who Use")

plt.tight_layout()

plt.show()

