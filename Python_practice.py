print("Hello World")
z= "8//5-3"
print(eval(z))
a= "8//5-3"
print(eval(a))
b= "8+22*2-4"
print(eval(b))
c= "16-3/2+7-1"
print(eval(c))
d= "3**3%5"
print(eval(d))
e= "5+9*3/2-4"
print(eval(e))
test_string = (5+2)*3
print(test_string)
a1= (8//5)-3
print(a1)
b1= 8+(22*(2-4))
print(b1)
c1= 16-3/(2+7)-1
print(c1)
d1= 3**(3%5)
print(d1)
e1= 5+(9*3/2-4)
print(e1)
f1= 5+(9*3/(2-4))
print(f1)

counties = ["Araphaoe","Denver","Jefferson"]
my_list = [ ]
print(counties)
print(counties[0])
print(counties[-1])
print(counties[-3])
print(len(counties))
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties.append("El Paso"))
print(counties)
print(counties.insert(2, "El Paso"))
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
counties.insert(1, "El Paso")
print(counties)
counties.pop(0)
print(counties)
counties.insert(1, "Jefferson")
print(counties)
counties.append("Arapahoe")
print(counties)
counties.pop(3)
print(counties)

counties_tuple = ("Arapahoe", "Denver", "Jeffereson")
print(len(counties_tuple))
print(counties_tuple)
print(counties_tuple[1])
print(counties_tuple[:-2])
print(counties_tuple[:2])
print(counties_tuple[:-1])
print(counties_tuple[1:2])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict['Arapahoe'])
print(counties_dict.get("Arapahoe"))
print(counties_dict['Arapahoe'])
print(counties_dict)
print(counties_dict['Arapahoe'])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
print(len(voting_data))
voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.pop(0)
print(voting_data)
voting_data.insert(3, {"county":"Denver", "registered_voters": 463353})
print(voting_data)
voting_data.insert(2, {"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.pop(0)
print(voting_data)
voting_data.pop(0)
print(voting_data)
voting_data.insert(0, {"county":"El Paso", "registered_voters": 461149})
print(voting_data)
voting_data.pop(2)
print(voting_data)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
voting_data

countiess = ["Arapahoe","Denver","Jefferson"]
if countiess[1] == 'Denver':
    print(countiess[1])

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
    print("Turn on the AC.")
#else:
#    print("Open the windows,")


#What is the score?
##score = int(input("What is your test score? "))

#Determine the grade.
#if score >= 90:
    print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is an B.')
#elif score >= 70:
 #   print('Your grade is an C.')
#elif score >= 60:
 #   print('Your grade is an D.')
#else:
 #   print('Your grade is an F')


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num) #same output as if using for numb in range(5): <enter> print(num)

for i in range(len(counties)):
    print(counties[i])

#    counties_tuples = ("Arapahoe","Denver","Jefferson").

#Arapahoe

#Denver

#Jefferson

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#>>> counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#>>> for county in counties_dict:
#...     print(county)


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

candidate_votes= int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the elction?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}"
    f"You recieved {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)