#https://adventofcode.com/2021/day/6

import os, sys
import numpy as np

def getInput():
    with open(os.path.join(sys.path[0], "input.txt")) as file_in:
        for line in file_in:
            list_of_ages = list(map(int,(line.strip().split(','))))

    return list_of_ages

class LanternFish:
    def __init__(self,age):
        self.age = age

    def printAge(self):
        print("Age is: {0}".format(self.age))

    def getAge(self):
        return self.age

    def updateAge(self):
        self.age -= 1

    def checkIfAgeMinus1(self):
        if self.age ==  -1:
            self.age = 6 #Reset to 6
            return True
        return False

    # def collapseData(self):

def part1(list_of_ages):
    list_of_fishes = []
    for age in list_of_ages:
        fish = LanternFish(age)
        list_of_fishes.append(fish)

    days = 18
    # print(list_of_fishes)

    for i in range(1,days+1):
        fish_ages = []
        new_fishes = []
        for fish in list_of_fishes:
            fish.updateAge()
            spawn_new_fish = fish.checkIfAgeMinus1()

            fish_ages.append(fish.getAge())

            if spawn_new_fish:
                new_fish = LanternFish(8) #new Fish age
                new_fishes.append(new_fish)
                fish_ages.append(new_fish.getAge())

        list_of_fishes += new_fishes
        print("Total Fishes: {0}".format(len(list_of_fishes)))
        print("After {0} day, Total Fishes: {1}, Ages: {2}".format(i, len(list_of_fishes), fish_ages))

############################################

def part2(list_of_ages):
    '''
    Rather then storing each fish in list
    create list of fish count per age, (0,1,2,3,4,5,6,7,8)
    
    #e.g 3,4,3,1,2 is [ 0 1  1  2  1   0  0  0  0]
    #e.g [ 0 86 53 54 55 52  0  0  0]
    '''

    fish_population = np.zeros(9, dtype=np.ulonglong) #Dealing with very large numbers.

    #Get initial list_of_fishes
    for age in list_of_ages:
        fish_population[age] +=1

    # print(fish_population)

    days = 256  #18,256
    for day in range(1,days+1):
        tmp_fish_pop = np.zeros(9, dtype=np.ulonglong)

        for age in range(0,9):
            if age == 0: #Dealing with fishes with age 0
                if(fish_population[age] != 0): #Any fishes about to spawn?
                    tmp_fish_pop[8] = fish_population[age] #Spawn new fish with age 8
                    tmp_fish_pop[6] += fish_population[age] #Reset 0 age fish(s) to age 6
                # print("After spawn and reset fish_population: {0}".format(tmp_fish_pop))
            else:
                # Decrement age by 1 by left shift from orig list
                tmp_fish_pop[age-1] += fish_population[age]

        fish_population = tmp_fish_pop
        # print(fish_population)

        total_population = np.sum(fish_population)
        print("Total Population at Day {0}: {1}".format(day, total_population))


if __name__ == "__main__":
    list_of_ages = getInput()
    # print(list_of_ages)

    # part1(list_of_ages)

    part2(list_of_ages)
   



