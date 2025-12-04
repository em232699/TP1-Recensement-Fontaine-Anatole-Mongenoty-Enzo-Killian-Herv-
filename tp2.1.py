import csv
import matplotlib.pyplot as plt

communes_2021 = []
with open('donnees_2021.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        communes_2021.append(row)
communes_2021 = [[communes_2021[i+1][2], int(communes_2021[i+1][5])] for i in range(len(communes_2021)-1)]


communes_2008 = []
with open('donnees_2008.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        communes_2008.append(row)
communes_2008 = [[communes_2008[i+1][2]+communes_2008[i+1][5], int(communes_2008[i+1][9])] for i in range(len(communes_2008)-1)]

communes_2016 = []
with open('donnees_2016.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        communes_2016.append(row)
communes_2016 = [[communes_2016[i+1][2]+communes_2016[i+1][5], int(communes_2016[i+1][9])] for i in range(len(communes_2016)-1)]

communes_2023 = []
with open('donnees_2023.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        communes_2023.append(row)
communes_2023 = [[communes_2023[i+1][2]+communes_2023[i+1][5], int(communes_2023[i+1][10])] for i in range(len(communes_2023)-1)]


communes = []
with open('metadonnees_communes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        communes.append(row)
communes = [[communes[i+118][2], communes[i+118][3]] for i in range(len(communes)-121)]

def population_departement(departement_code, communes_data):
    total_population = 0
    for commune in communes_data:
        if commune[0].startswith(departement_code):
            total_population += commune[1]
    return total_population


dates = [2008, 2016, 2021, 2023]
populations_89 = []

pop_2008 = population_departement('89', communes_2008)
populations_89.append(pop_2008)

pop_2016 = population_departement('89', communes_2016)
populations_89.append(pop_2016)

pop_2021 = population_departement('89', communes_2021)
populations_89.append(pop_2021)

pop_2023 = population_departement('89', communes_2023)
populations_89.append(pop_2023)


plt.plot(dates, populations_89, marker='o', color='b', label="Population de l'Yonne")
plt.title("Évolution de la population de l'Yonne en fonction du temps")
plt.xlabel("Années")
plt.ylabel("Population")
plt.xticks(dates)
plt.grid(True)
plt.legend()
plt.show()
