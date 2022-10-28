def linear_search_dictionary(the_dictionary, target_value):
    for key in the_dictionary:
        if the_dictionary[key] == target_value:
            print("Success: your value was found at key", key)
            return key

    print ("Target value is not in the dictionary")
    return -1

#state_capitols = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}
#linear_search_dictionary(state_capitols, "Olympia")

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)