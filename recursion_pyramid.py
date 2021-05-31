# PF-Exer-32
weight_per_person = 50

b=1



def human_pyramid(WEIGHT):

     # remove pass and place the recursive code the you had written earlier for this function


def find_maximum_people(max_weight):
    global b
    if (max_weight <= 0):
        return b - 4
    else:

        max_weight = max_weight - (weight_per_person * (b))
        b = b + 2
        no_of_people=find_maximum_people(max_weight)
        return  no_of_people

    # write your logic here. You may invke recursive function human_pyramid() wherever applicable
    return no_of_people


# Provide different values for max_weight and test your program
max_people = find_maximum_people(1200)
print(max_people)