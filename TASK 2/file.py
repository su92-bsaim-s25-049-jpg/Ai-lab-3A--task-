        # Question no 1 
for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
        
                                            # Question no 2 
                                            
        
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]


total_budget = 0

for movie in movies:
    total_budget += movie[1]

average_budget = total_budget / len(movies)

print("Average budget:", average_budget)
print()


count = 0

for movie in movies:
    name = movie[0]
    budget = movie[1]

    if budget > average_budget:
        print(name, "is above average")

        difference = budget - average_budget
        print("It is", difference, "more than average")
        print()

        count += 1

print("Total movies above average:", count)