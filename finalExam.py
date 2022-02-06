# READ THE DIRECTIONS GIVEN IN THE PDF FILE!!!!
# READ THE DIRECTIONS GIVEN IN THE PDF FILE!!!!
# COMMENT ON YOUR CODE!
#Jake adding a comment
# ______________________________________________________

#Function 1 [40 points]
def displayInfo(petDictionary):
    #function iterates through keys of dictionary
    # This function inputs petDictionary
    for key in petDictionary:
        #inner loop iterates through values of each dictionary key
        for value in petDictionary[key]:
            #seperating values into readable informative sentence
            if value == 'name':
                print(petDictionary[key][value], 'is a', end =' ')
            if value == 'type':
                print(petDictionary[key][value], 'and is', end = ' ')
            if value == 'age':
                print(petDictionary[key][value], 'years old')


#Function 2 [30 points] 
def getUniquePetTypes(petDictionary):
    '''
    This function takes the pet dictionary as the input (parameter).
    It returns a list of unique pet types in the shelter.
    '''
    #creating empty list
    typelist = []
    #creating a list of pet types
    for key in petDictionary:
        typelist.append(petDictionary[key]['type'])
    #counting number of the pet type
    for el in typelist:
        count1 = typelist.count(el)
        #if there is more than one of that type, remove it from the list
        if count1 > 1:
            typelist.remove(el)
                
    return typelist
    

#Function 3 [20 points]
def getPetCount(petDictionary, petType):
    '''
    This function takes the pet dictionary and a type as the input (parameter).
    It returns a count of that type of pets in the shelter.
    If the pet type is not in the shelter return 0.
    For example, if the petType is Dog, this function returns how many Dogs in the petDictionary.
    '''
    #empty list
    typelist = []
    #creating a list of pet types
    for key in petDictionary:
        typelist.append(petDictionary[key]['type'])
    #counting number of given pet type
    count1 = typelist.count(petType)
    return count1
    

#Function 4 [10 points]
def getoldest(petDictionary):
    '''
    This function takes the pet dictionary as the input (parameter).
    It returns a list of the oldest pet ids (the keys).
    Hint: First find the maximum age of the pets.
    Then create a list of pet ids with the maximum age and return it.
    '''
    #empty age list
    agelist = []
    #adding ages to list
    for key in petDictionary:
        agelist.append(petDictionary[key]['age'])
    #finding the max age
    max1 = max(agelist)
    old = []
    #interating through dictionary keys
    for key in petDictionary:
        #if the pet's age matches the max age it's ID is added to the list
        if petDictionary[key]['age'] == 5:
            old.append(key)
    return old
    
    
    


#Testing functions [DO NOT DELETE/MODIFY]   
if __name__ == '__main__':

    petDictionary = {'p1': {'name': 'Lucky', 'type': 'Dog', 'age': 3},
                     'p2': {'name': 'Kitty', 'type': 'Cat', 'age': 2},
                     'p3': {'name': 'Coco', 'type': 'Dog', 'age': 5},
                     'p4': {'name': 'Doughnut', 'type': 'Hamster', 'age': 1},
                     'p5': {'name': 'Snowball', 'type': ' Rabbit', 'age': 1},
                     'p6': {'name': 'Loki', 'type': 'Cat', 'age': 1},
                     'p7': {'name': 'Buddy', 'type': 'Dog', 'age': 2},
                     'p8': {'name': 'Biscuit', 'type': 'Hamster', 'age': 1},
                     'p9': {'name': 'Yertle', 'type': ' Turtle', 'age': 5},
                     'p10': {'name': 'Red', 'type': 'Cat', 'age': 2}}


    print('Display information')
    displayInfo(petDictionary)

    print('\n\nUnique Types')
    uniTypes = getUniquePetTypes(petDictionary)
    print(uniTypes)

    print('\n\nShelter Pet Count')
    for t in uniTypes:
        count = getPetCount(petDictionary, t)
        print('{} {}s'.format(count,t))

    print('\n\nOlderst Pets')
    oldList = getoldest(petDictionary)
    print(oldList)

