#! PYTHON 25 DAN 
#! CSV data files and PANDAS library
 
#! Open the weather_data.csv file using readlines() to create a list named DATA that contains the values from the .csv file
# with open("Dan_25/weather_data.csv", mode = "r") as file:
#     data = file.readlines()
#     print(data)

#! Library for working with csv
# import csv

# with open("Dan_25/weather_data.csv", mode = "r") as data_flie:
#     data = csv.reader(data_flie)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))   
#     print(temperature)

#! Pandas data analysis library PANDAS
# savet je da se uvek procita documentation koji postoji
import pandas 

# data = pandas.read_csv("Dan_25/weather_data.csv")

# # otvara prvi row kao da je title i printa sve ispod njega
# print(data["temp"])

# # mozemo da proverimo tip podataka sa pandas
# print(type(data)) # --> ovo ce biti DataFrame, u sustini sve u tabeli sto je je DataFrame
# print(type(data["temp"])) # --> ovo ce biti Series, ovo je u sustini lista npr red ili kolona

# #! API references iz dokumentacije - sve sto mozes da radis sa PANDAS

# # Convertovanje u dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Convertovanje Series into lists
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# #TODO Zadatak pronaci AVG temperaturu
# #* peske
# avg = sum(temp_list)/len(temp_list)
# print(round(avg,2))

# #* pomocu Pandas
# avg_pandas = data["temp"].mean()
# print(round(avg_pandas,2))

# #TODO Naci maksimum temperature iz Series "temp"
# max = data["temp"].max()
# print(max)

# #! Get Data in Columns
# print(data["condition"])
# print("********************")
# print(data.condition) # --> isto sto i gore, tako da ne moras uglaste zagrade ako znas kako ti se kolone zovu, voditi racuna da ako je veliko slovo, mora i ovde veliko slovo

# #! Get Data in Row
# row = data[data.day == "Monday"]
# print(row)

# #TODO Naci row data u kome je temperatura na max
# row_max = data[data.temp == data.temp.max()]
# print(row_max)

# #TODO Convert Monday's temperature to Fahrenheit. Hint: use [] to get a single value from the pandas Series by index.
# monday_row = data[data.day == "Monday"]
# monday_temp = monday_row.temp
# monday_temp_f = (monday_temp * 9/5) + 32
# print(round(monday_temp_f,2))

# #! Create a dataframe from the scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }

# # koristimo pandas.DataFrame
# new_data = pandas.DataFrame(data_dict)
# print(new_data)

# # a ako hocemo mozemo odmah u csv da ga pretvorimo
# new_data.to_csv("Dan_25/new_data.csv")

#TODO Napraviti od squirrel_data novu tabelu u kojoj ce pisati ukupan broj veverica za svaku boju krzna

data = pandas.read_csv("Dan_25\squirrel_data.csv")
data_fur = data["Primary Fur Color"]

grey_squirrels_count = 0
cinnamon_squirrels_count = 0
black_squirrels_count = 0
nije_zabelezena_boja_krzna = 0

grey_squirrels = data[data_fur == "Grey"]
number_grey_squirrels = len(grey_squirrels)
print(grey_squirrels)

black_squirrels = data[data_fur == "Black"]
number_black_squirrels = len(black_squirrels)
print(black_squirrels)

cinnamon_squirrels = data[data_fur == "Cinnamon"]
number_cinnamon_squirrels = len(cinnamon_squirrels)
print(cinnamon_squirrels)


#? lekina verzija... komplikovanija
for color_of_fur in data_fur:
    if color_of_fur == "Gray":
        grey_squirrels_count += 1
    elif color_of_fur == "Cinnamon":
        cinnamon_squirrels_count += 1
    elif color_of_fur == "Black":
        black_squirrels_count += 1
    else:
        nije_zabelezena_boja_krzna +=1

print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("Dan_25/squirrel_count.csv")