def main():
    fatGram = float(input("Please enter fat: "))
    carbohydratesGram = float(input("Please enter carbohydrates: "))
    caloriesFromFat = getCaloriesFromFat(fatGram)
    caloriesFromCarbohydrates = getCaloriesFromCarbohydrates(carbohydratesGram)
    print(caloriesFromFat, caloriesFromCarbohydrates)


def getCaloriesFromFat(gram):
    return gram * 9

def getCaloriesFromCarbohydrates(gram):
    return gram * 4


main()