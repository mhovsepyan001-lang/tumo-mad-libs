import random

def template1():
    number = input("Input some number: ")
    measure = input("Input the measure of time: ")
    transportation = input("Input mode of transportation: ")
    adjective = input("Input some adjective(feeling): ")
    adjective2 = input("Input another adjective: ")
    noun = input("Input Noun: ")
    color = input("Input color: ")
    part_of_the_body = input("Input part of the body : ")
    verb = input("Inpute some verb: ")
    number2 = input("Input number: ")
    noun2 = input("Input noun: ")
    noun3 = input("Input noun: ")
    part_of_the_body2 = input("Input other part of the body: ")
    noun4 = input("Input noun: ")
    adjective3 = input("Input adjective: ")
    silly_word = input("Input silly_word: ")

    template_1 = (
        "It was about " + number + " " + measure +
        " ago when I arrived at the hospital in a " + transportation +
        ". The hospital is a/an " + adjective +
        " place, there are a lot of " + adjective2 + " " + noun +
        " here. There are nurses here who have " + color + " " +
        part_of_the_body +
        ". If someone wants to come into my room I told them that they have to " +
        verb + " first. I've decorated my room with " + number2 + " " +
        noun2 +
        ". Today I talked to a doctor and they were wearing a " + noun3 +
        " on their " + part_of_the_body2 +
        ". I heard that all doctors " + verb + " " + noun4 +
        " every day for breakfast. The most " + adjective3 +
        " thing about being in the hospital is the " + silly_word +
        " " + noun + "!"
    )

    print(template_1)


def template2():

    proper_noun = input("Input a proper noun: ")
    noun = input("Input a noun: ")
    adjective = input("Input an adjective: ")
    verb = input("Input a verb: ")
    adjective2 = input("Input another adjective: ")
    animal = input("Input an animal: ")
    verb2 = input("Input a verb: ")
    color = input("Input a color: ")
    verb_ing = input("Input a verb ending in 'ing': ")
    adverb_ly = input("Input an adverb ending in 'ly': ")
    number = input("Input a number: ")
    measure_of_time = input("Input a measure of time: ")
    silly_word = input("Input a silly word: ")
    noun2 = input("Input a noun: ")

    template_2 = (
        "This weekend I am going camping with " + proper_noun +
        ". I packed my lantern, sleeping bag, and " + noun +
        ". I am so " + adjective + " to " + verb +
        " in a tent. I am " + adjective2 +
        " we might see a(n) " + animal +
        ". I hear they’re kind of dangerous. While we’re camping, "
        "we are going to hike, fish, and " + verb2 +
        ". I have heard that the " + color +
        " lake is great for " + verb_ing +
        ". Then we will " + adverb_ly +
        " hike through the forest for " + number +
        " " + measure_of_time +
        ". If I see a " + color + " " + animal +
        " while hiking, I am going to bring it home as a pet! "
        "At night we will tell " + number + " " + silly_word +
        " stories and roast " + noun2 +
        " around the campfire!!"
    )

    print(template_2)


def template3():

    proper_noun = input("Input a proper noun: ")
    adjective = input("Input an adjective: ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    place = input("Input a place: ")
    adjective2 = input("Input another adjective: ")
    magical_creatures = input("Input a magical creature: ")
    adjective3 = input("Input another adjective: ")
    magical_creatures2 = input("Input another magical creature: ")
    room = input("Input a room: ")
    noun = input("Input a noun: ")
    noun2 = input("Input a noun: ")
    plural_noun3 = input("Input a plural noun: ")
    adjective4 = input("Input another adjective: ")
    plural_noun4 = input("Input a plural noun: ")
    number = input("Input a number: ")
    measure_of_time = input("Input a measure of time: ")
    verb_ing = input("Input a verb ending in 'ing': ")
    adjective5 = input("Input another adjective: ")
    noun5 = input("Input a noun: ")

    template_3 = (
        "Dear " + proper_noun +
        ", I am writing to you from a " + adjective +
        " castle in an enchanted forest. I found myself here one day "
        "after going for a ride on a " + color + " " + animal +
        " in " + place + ". There are " + adjective2 + " " +
        magical_creatures + " and " + adjective3 + " " +
        magical_creatures2 + " here! In the " + room +
        " there is a pool full of " + noun +
        ". I fall asleep each night on a " + noun2 +
        " of " + plural_noun3 +
        " and dream of " + adjective4 + " " + plural_noun4 +
        ". It feels as though I have lived here for " + number +
        " " + measure_of_time +
        ". I hope one day you can visit, although the only way "
        "to get here now is " + verb_ing +
        " on a " + adjective5 + " " + noun5 + "!"
    )

    print(template_3)
choice = input("Which template would you like to use? (1, 2, 3 or 4 for random): ")
while choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please select 1, 2, 3, or 4 for random.")
    choice = input("Which template would you like to use? (1, 2, 3 or 4 for random): ")
if choice == "1":
    template1()
elif choice == "2":
    template2()
elif choice == "3":
    template3()
elif choice == "4":
    random_template = random.choice([template1, template2, template3])
    random_template()
