from random import randint
import time


# create a shopping cart and the categories

shopping_cart_items = []
shopping_cart_prices = []

categories = ["1.Dairy", "2.Meats", "3.Vegetables", "4.Fruits", "5.Bakery", "6.Snacks"]

dairy = {
    "liter milk": 5.99,
    " dozen eggs": 11.99,
    "feta cheese": 8.99,
}
dairy_list = [
    "1) liter milk: 5.99 AED ",
    "2) dozen eggs: 11.99 AED",
    "3) feta cheese: 8.99 AED",
]

meats = {
    "kg chicken breast": 39.99,
    "kg chicken thighs": 35.99,
    "kg beef tomahawk": 30.99,
}
meats_list = [
    "1) kg chicken breast: 39.99 AED",
    "2) kg chicken thighs: 35.99 AED",
    "3) kg beef tomahawk: 30.99 AED",
]

vegs = {"kg carrots": 3.99, "kg broccoli": 4.99, "kg lettuce": 5.99}
vegs_list = [
    "1) kg carrots: 3.99 AED",
    "2) kg broccoli: 4.99 AED",
    "3) kg lettuce: 5.99 AED",
]

fruits = {"kg apples": 4.99, "kg oranges": 5.99, "kg blueberries": 3.99}
fruits_list = [
    "1) kg apples: 4.99 AED",
    "2) kg oranges: 5.99 AED",
    "3) kg blueberries: 3.99 aed",
]

bakery = {"al arz bread": 1.99, "buns": 2.99, "croissants": 5.99}
bakery_list = [
    "1) al arz bread: 1.99 AED",
    "2) buns: 2.99 AED",
    "3) croissants: 5.99 AED",
]

Snacks = {"chocolate bars": 2.99, "lays chips": 1.99, "gummy worms": 3.99}
Snacks_list = [
    "1) chocolate bars: 2.99 AED",
    "2) lays chips: 1.99 AED",
    "3) gummy worms: 3.99 AED",
]


# welcome message
print("Hello! welcome to Safi's grocery!")
time.sleep(2)


# start the shopping process with the customer
while True:
    start_shop = input(
        "Would you like to continue shopping with us, please answer with a y or n:"
    )

    # if customer replies yes the shopping process starts/continues
    if start_shop.lower() == "y":
        time.sleep(1)

        # show the buyer the categories our grocery offers
        print(
            "Safi Grocerys offers a wide variety of shopping items in the following categories:"
        )
        for x in categories:
            time.sleep(0.3)
            print(x)

        # Ask the customer what category he wants to buy from and shop from the respective category
        i = 0
        while i == 0:
            user_category = int(
                input(
                    "Please state the number of the category that you would like to shop from:"
                )
            )

            if user_category == 1:
                print(dairy_list)

                # this loop recives the first item from the customer of the respective category
                while True:
                    while (
                        True
                    ):  # while loop that makes sure the number of the item the user entered is valid
                        cat1_item_number = int(
                            input(
                                "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                            )
                        )
                        dairy_keys_list = list(
                            dairy.keys()
                        )  # creates a list for the keys of the dictonary

                        if cat1_item_number <= 3 and cat1_item_number >= 1:
                            cat1_item = dairy_keys_list[
                                cat1_item_number - 1
                            ]  # the index of the number the user entered minus 1 becomes the new varabile
                            break

                        else:
                            print("Invalid selection please try again.")

                    if cat1_item.lower() in dairy.keys():
                        price1 = dairy.get(
                            cat1_item.lower()
                        )  # create a new varabile that correspondes to the items price
                        # Created a new varabile that correspondes with the quantity of the item
                        while True:
                            quantity_item1 = int(
                                input("How many pieces would you like?")
                            )
                            if quantity_item1 <= 7:
                                quantity_item1_str = str(quantity_item1)
                                quantity_item1_amount = (
                                    quantity_item1_str + " " + cat1_item
                                )

                                # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                shopping_cart_items.append(
                                    quantity_item1_amount.upper()
                                )
                                shopping_cart_prices.append(price1 * quantity_item1)
                                break
                            else:
                                print(
                                    "We do not have this amount in stock. Please input a smaller amount"
                                )
                    break

                # this loop would start after the customer buys his first item from the category
                while True:
                    Mcat1_item = input(
                        "Would you like to shop more from this category, please answer with a y or n:"
                    )

                    if Mcat1_item.lower() == "y":
                        time.sleep(1)
                        print(dairy_list)

                        while True:
                            while (
                                True
                            ):  # while loop that makes sure the number of the item the user entered is valid
                                cat1_item_number = int(
                                    input(
                                        "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                                    )
                                )
                                dairy_keys_list = list(
                                    dairy.keys()
                                )  # creates a list for the keys of the dictonary

                                if cat1_item_number <= 3 and cat1_item_number >= 1:
                                    cat1_item = dairy_keys_list[
                                        cat1_item_number - 1
                                    ]  # the index of the number the user entered minus 1 becomes the new varabile
                                    break

                                else:
                                    print("Invalid selection please try again.")

                            if cat1_item.lower() in dairy.keys():
                                price1 = dairy.get(cat1_item.lower())
                                # Created a new varabile that correspondes with the quantity of the item
                            while True:
                                quantity_item1 = int(
                                    input("How many pieces would you like?")
                                )
                                if quantity_item1 <= 7:
                                    quantity_item1_str = str(quantity_item1)
                                    quantity_item1_amount = (
                                        quantity_item1_str + " " + cat1_item
                                    )

                                    # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                    shopping_cart_items.append(
                                        quantity_item1_amount.upper()
                                    )
                                    shopping_cart_prices.append(price1 * quantity_item1)
                                    break

                                else:
                                    time.sleep(1)
                                    print(
                                        "We do not have this amount in stock. Please input a smaller amount"
                                    )
                            break
                    # if the customer dosent want to buy more items from the category the loop would break
                    elif Mcat1_item.lower() == "n":
                        break

                    else:
                        print("That was an invalid option please try again")

                i += 1

            elif user_category == 2:
                print(meats_list)

                # this loop recives the first item from the customer of the respective category
                while True:
                    while (
                        True
                    ):  # while loop that makes sure the number of the item the user entered is valid
                        cat2_item_number = int(
                            input(
                                "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                            )
                        )
                        meats_keys_list = list(
                            meats.keys()
                        )  # creates a list for the keys of the dictonary

                        if cat2_item_number <= 3 and cat2_item_number >= 1:
                            cat2_item = meats_keys_list[
                                cat2_item_number - 1
                            ]  # the index of the number the user entered minus 1 becomes the new varabile
                            break

                        else:
                            print("Invalid selection please try again.")

                    if cat2_item.lower() in meats.keys():
                        price2 = meats.get(
                            cat2_item.lower()
                        )  # create a new varabile that correspondes to the items price
                        # Created a new varabile that correspondes with the quantity of the item
                        while True:
                            quantity_item2 = int(
                                input("How many kilograms would you like?")
                            )
                            if quantity_item2 <= 10:
                                quantity_item2_str = str(quantity_item2)
                                quantity_item2_amount = (
                                    quantity_item2_str + " " + cat2_item
                                )

                                # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                shopping_cart_items.append(
                                    quantity_item2_amount.upper()
                                )
                                shopping_cart_prices.append(price2 * quantity_item2)
                                break
                            else:
                                print(
                                    "We do not have this amount in stock. Please input a smaller amount"
                                )
                    break

                # this loop would start after the customer buys his first item from the category
                while True:
                    Mcat2_item = input(
                        "Would you like to shop more from this category, please answer with a y or n:"
                    )

                    if Mcat2_item.lower() == "y":
                        time.sleep(1)
                        print(meats_list)

                        while True:
                            while (
                                True
                            ):  # while loop that makes sure the number of the item the user entered is valid
                                cat2_item_number = int(
                                    input(
                                        "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                                    )
                                )
                                meats_keys_list = list(
                                    meats.keys()
                                )  # creates a list for the keys of the dictonary

                                if cat2_item_number <= 3 and cat2_item_number >= 1:
                                    cat2_item = meats_keys_list[
                                        cat2_item_number - 1
                                    ]  # the index of the number the user entered minus 1 becomes the new varabile
                                    break

                                else:
                                    print("Invalid selection please try again.")

                            if cat2_item.lower() in meats.keys():
                                price2 = meats.get(cat2_item.lower())
                                # Created a new varabile that correspondes with the quantity of the item
                            while True:
                                quantity_item2 = int(
                                    input("How many pieces would you like?")
                                )
                                if quantity_item2 <= 10:
                                    quantity_item2_str = str(quantity_item2)
                                    quantity_item2_amount = (
                                        quantity_item2_str + " " + cat2_item
                                    )

                                    # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                    shopping_cart_items.append(
                                        quantity_item2_amount.upper()
                                    )
                                    shopping_cart_prices.append(price2 * quantity_item2)
                                    break

                                else:
                                    time.sleep(1)
                                    print(
                                        "We do not have this amount in stock. Please input a smaller amount"
                                    )
                            break
                    # if the customer dosent want to buy more items from the category the loop would break
                    elif Mcat2_item.lower() == "n":
                        break

                    else:
                        print("That was an invalid option please try again")

                i += 1

            elif user_category == 3:
                print(vegs_list)

                # this loop recives the first item from the customer of the respective category
                while True:
                    while (
                        True
                    ):  # while loop that makes sure the number of the item the user entered is valid
                        cat3_item_number = int(
                            input(
                                "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                            )
                        )
                        vegs_keys_list = list(
                            vegs.keys()
                        )  # creates a list for the keys of the dictonary

                        if cat3_item_number <= 3 and cat3_item_number >= 1:
                            cat3_item = vegs_keys_list[
                                cat3_item_number - 1
                            ]  # the index of the number the user entered minus 1 becomes the new varabile
                            break

                        else:
                            print("Invalid selection please try again.")

                    if cat3_item.lower() in vegs.keys():
                        price3 = vegs.get(
                            cat3_item.lower()
                        )  # create a new varabile that correspondes to the items price
                        # Created a new varabile that correspondes with the quantity of the item
                        while True:
                            quantity_item3 = int(
                                input("How many kilograms would you like?")
                            )
                            if quantity_item3 <= 10:
                                quantity_item3_str = str(quantity_item3)
                                quantity_item3_amount = (
                                    quantity_item3_str + " " + cat3_item
                                )

                                # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                shopping_cart_items.append(
                                    quantity_item3_amount.upper()
                                )
                                shopping_cart_prices.append(price3 * quantity_item3)
                                break
                            else:
                                print(
                                    "We do not have this amount in stock. Please input a smaller amount"
                                )
                    break

                # this loop would start after the customer buys his first item from the category
                while True:
                    Mcat3_item = input(
                        "Would you like to shop more from this category, please answer with a y or n:"
                    )

                    if Mcat3_item.lower() == "y":
                        time.sleep(1)
                        print(vegs_list)

                        while True:
                            while (
                                True
                            ):  # while loop that makes sure the number of the item the user entered is valid
                                cat3_item_number = int(
                                    input(
                                        "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                                    )
                                )
                                vegs_keys_list = list(
                                    vegs.keys()
                                )  # creates a list for the keys of the dictonary

                                if cat3_item_number <= 3 and cat3_item_number >= 1:
                                    cat3_item = vegs_keys_list[
                                        cat3_item_number - 1
                                    ]  # the index of the number the user entered minus 1 becomes the new varabile
                                    break

                                else:
                                    print("Invalid selection please try again.")

                            if cat3_item.lower() in vegs.keys():
                                price3 = vegs.get(cat3_item.lower())
                                # Created a new varabile that correspondes with the quantity of the item
                            while True:
                                quantity_item3 = int(
                                    input("How many kilograms would you like?")
                                )
                                if quantity_item3 <= 10:
                                    quantity_item3_str = str(quantity_item3)
                                    quantity_item3_amount = (
                                        quantity_item3_str + " " + cat3_item
                                    )

                                    # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                    shopping_cart_items.append(
                                        quantity_item3_amount.upper()
                                    )
                                    shopping_cart_prices.append(price3 * quantity_item3)
                                    break

                                else:
                                    time.sleep(1)
                                    print(
                                        "We do not have this amount in stock. Please input a smaller amount"
                                    )
                            break
                    # if the customer dosent want to buy more items from the category the loop would break
                    elif Mcat3_item.lower() == "n":
                        break

                    else:
                        print("That was an invalid option please try again")

                i += 1
            elif user_category == 4:
                print(fruits_list)

                # this loop recives the first item from the customer of the respective category
                while True:
                    while (
                        True
                    ):  # while loop that makes sure the number of the item the user entered is valid
                        cat4_item_number = int(
                            input(
                                "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                            )
                        )
                        fruits_keys_list = list(
                            fruits.keys()
                        )  # creates a list for the keys of the dictonary

                        if cat4_item_number <= 3 and cat4_item_number >= 1:
                            cat4_item = fruits_keys_list[
                                cat4_item_number - 1
                            ]  # the index of the number the user entered minus 1 becomes the new varabile
                            break

                        else:
                            print("Invalid selection please try again.")

                    if cat4_item.lower() in fruits.keys():
                        price4 = fruits.get(
                            cat4_item.lower()
                        )  # create a new varabile that correspondes to the items price
                        # Created a new varabile that correspondes with the quantity of the item
                        while True:
                            quantity_item4 = int(
                                input("How many kilograms would you like?")
                            )
                            if quantity_item4 <= 10:
                                quantity_item4_str = str(quantity_item4)
                                quantity_item4_amount = (
                                    quantity_item4_str + " " + cat4_item
                                )

                                # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                shopping_cart_items.append(
                                    quantity_item4_amount.upper()
                                )
                                shopping_cart_prices.append(price4 * quantity_item4)
                                break
                            else:
                                print(
                                    "We do not have this amount in stock. Please input a smaller amount"
                                )
                    break

                # this loop would start after the customer buys his first item from the category
                while True:
                    Mcat4_item = input(
                        "Would you like to shop more from this category, please answer with a y or n:"
                    )

                    if Mcat4_item.lower() == "y":
                        time.sleep(1)
                        print(fruits_list)

                        while True:
                            while (
                                True
                            ):  # while loop that makes sure the number of the item the user entered is valid
                                cat4_item_number = int(
                                    input(
                                        "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                                    )
                                )
                                fruits_keys_list = list(
                                    fruits.keys()
                                )  # creates a list for the keys of the dictonary

                                if cat4_item_number <= 3 and cat4_item_number >= 1:
                                    cat4_item = fruits_keys_list[
                                        cat4_item_number - 1
                                    ]  # the index of the number the user entered minus 1 becomes the new varabile
                                    break

                                else:
                                    print("Invalid selection please try again.")

                            if cat4_item.lower() in fruits.keys():
                                price4 = fruits.get(cat4_item.lower())
                                # Created a new varabile that correspondes with the quantity of the item
                            while True:
                                quantity_item4 = int(
                                    input("How many kilograms would you like?")
                                )
                                if quantity_item4 <= 15:
                                    quantity_item4_str = str(quantity_item4)
                                    quantity_item4_amount = (
                                        quantity_item4_str + " " + cat4_item
                                    )

                                    # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                    shopping_cart_items.append(
                                        quantity_item4_amount.upper()
                                    )
                                    shopping_cart_prices.append(price4 * quantity_item4)
                                    break

                                else:
                                    time.sleep(1)
                                    print(
                                        "We do not have this amount in stock. Please input a smaller amount"
                                    )
                            break
                    # if the customer dosent want to buy more items from the category the loop would break
                    elif Mcat4_item.lower() == "n":
                        break

                    else:
                        print("That was an invalid option please try again")

                i += 1

            elif user_category == 5:
                print(bakery_list)

                # this loop recives the first item from the customer of the respective category
                while True:
                    while (
                        True
                    ):  # while loop that makes sure the number of the item the user entered is valid
                        cat5_item_number = int(
                            input(
                                "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                            )
                        )
                        bakery_keys_list = list(
                            bakery.keys()
                        )  # creates a list for the keys of the dictonary

                        if cat5_item_number <= 3 and cat5_item_number >= 1:
                            cat5_item = bakery_keys_list[
                                cat5_item_number - 1
                            ]  # the index of the number the user entered minus 1 becomes the new varabile
                            break

                        else:
                            print("Invalid selection please try again.")

                    if cat5_item.lower() in bakery.keys():
                        price5 = bakery.get(
                            cat5_item.lower()
                        )  # create a new varabile that correspondes to the items price
                        # Created a new varabile that correspondes with the quantity of the item
                        while True:
                            quantity_item5 = int(
                                input("How many pieces would you like?")
                            )
                            if quantity_item5 <= 15:
                                quantity_item5_str = str(quantity_item5)
                                quantity_item5_amount = (
                                    quantity_item5_str + " " + cat5_item
                                )

                                # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                shopping_cart_items.append(
                                    quantity_item5_amount.upper()
                                )
                                shopping_cart_prices.append(price5 * quantity_item5)
                                break
                            else:
                                print(
                                    "We do not have this amount in stock. Please input a smaller amount"
                                )
                    break

                # this loop would start after the customer buys his first item from the category
                while True:
                    Mcat5_item = input(
                        "Would you like to shop more from this category, please answer with a y or n:"
                    )

                    if Mcat5_item.lower() == "y":
                        time.sleep(1)
                        print(bakery_list)

                        while True:
                            while (
                                True
                            ):  # while loop that makes sure the number of the item the user entered is valid
                                cat5_item_number = int(
                                    input(
                                        "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                                    )
                                )
                                bakery_keys_list = list(
                                    bakery.keys()
                                )  # creates a list for the keys of the dictonary

                                if cat5_item_number <= 3 and cat5_item_number >= 1:
                                    cat5_item = bakery_keys_list[
                                        cat5_item_number - 1
                                    ]  # the index of the number the user entered minus 1 becomes the new varabile
                                    break

                                else:
                                    print("Invalid selection please try again.")

                            if cat5_item.lower() in bakery.keys():
                                price5 = bakery.get(cat5_item.lower())
                                # Created a new varabile that correspondes with the quantity of the item
                            while True:
                                quantity_item5 = int(
                                    input("How many pieces would you like?")
                                )
                                if quantity_item5 <= 10:
                                    quantity_item5_str = str(quantity_item5)
                                    quantity_item5_amount = (
                                        quantity_item5_str + " " + cat5_item
                                    )

                                    # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                    shopping_cart_items.append(
                                        quantity_item5_amount.upper()
                                    )
                                    shopping_cart_prices.append(price5 * quantity_item5)
                                    break

                                else:
                                    time.sleep(1)
                                    print(
                                        "We do not have this amount in stock. Please input a smaller amount"
                                    )
                            break
                    # if the customer dosent want to buy more items from the category the loop would break
                    elif Mcat5_item.lower() == "n":
                        break

                    else:
                        print("That was an invalid option please try again")

                i += 1

            elif user_category == 6:
                print(Snacks_list)

                # this loop recives the first item from the customer of the respective category
                while True:
                    while (
                        True
                    ):  # while loop that makes sure the number of the item the user entered is valid
                        cat6_item_number = int(
                            input(
                                "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                            )
                        )
                        Snacks_keys_list = list(
                            Snacks.keys()
                        )  # creates a list for the keys of the dictonary

                        if cat6_item_number <= 3 and cat6_item_number >= 1:
                            cat6_item = Snacks_keys_list[
                                cat6_item_number - 1
                            ]  # the index of the number the user entered minus 1 becomes the new varabile
                            break

                        else:
                            print("Invalid selection please try again.")

                    if cat6_item.lower() in Snacks.keys():
                        price6 = Snacks.get(
                            cat6_item.lower()
                        )  # create a new varabile that correspondes to the items price
                        # Created a new varabile that correspondes with the quantity of the item
                        while True:
                            quantity_item6 = int(
                                input("How many pieces would you like?")
                            )
                            if quantity_item6 <= 10:
                                quantity_item6_str = str(quantity_item6)
                                quantity_item6_amount = (
                                    quantity_item6_str + " " + cat6_item
                                )

                                # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                shopping_cart_items.append(
                                    quantity_item6_amount.upper()
                                )
                                shopping_cart_prices.append(price6 * quantity_item6)
                                break
                            else:
                                print(
                                    "We do not have this amount in stock. Please input a smaller amount"
                                )
                    break

                # this loop would start after the customer buys his first item from the category
                while True:
                    Mcat6_item = input(
                        "Would you like to shop more from this category, please answer with a y or n:"
                    )

                    if Mcat6_item.lower() == "y":
                        time.sleep(1)
                        print(Snacks_list)

                        while True:
                            while (
                                True
                            ):  # while loop that makes sure the number of the item the user entered is valid
                                cat6_item_number = int(
                                    input(
                                        "Please enter the number that corresponds with the items place that you would like to purchase in the list:"
                                    )
                                )
                                Snacks_keys_list = list(
                                    Snacks.keys()
                                )  # creates a list for the keys of the dictonary

                                if cat6_item_number <= 3 and cat6_item_number >= 1:
                                    cat6_item = Snacks_keys_list[
                                        cat6_item_number - 1
                                    ]  # the index of the number the user entered minus 1 becomes the new varabile
                                    break

                                else:
                                    print("Invalid selection please try again.")

                            if cat6_item.lower() in Snacks.keys():
                                price6 = Snacks.get(cat6_item.lower())
                                # Created a new varabile that correspondes with the quantity of the item
                            while True:
                                quantity_item6 = int(
                                    input("How many pieces would you like?")
                                )
                                if quantity_item6 <= 10:
                                    quantity_item6_str = str(quantity_item6)
                                    quantity_item6_amount = (
                                        quantity_item6_str + " " + cat6_item
                                    )

                                    # The items quanity and total qualitive price is added to the lists created at the beginging of the code
                                    shopping_cart_items.append(
                                        quantity_item6_amount.upper()
                                    )
                                    shopping_cart_prices.append(price6 * quantity_item6)
                                    break

                                else:
                                    time.sleep(1)
                                    print(
                                        "We do not have this amount in stock. Please input a smaller amount"
                                    )
                            break
                    # if the customer dosent want to buy more items from the category the loop would break
                    elif Mcat6_item.lower() == "n":
                        break

                    else:
                        print("That was an invalid option please try again")

                i += 1

            else:
                print("invalid input, please try again")

    elif start_shop.lower() == "n":
        time.sleep(2)
        break

    else:
        print("that was an invalid statment please try again")
        time.sleep(1)


# list out the customers final shopping cart details
time.sleep(0.5)
print("The items that are in your shopping cart are:", shopping_cart_items)
time.sleep(0.5)

rounded_item = 0
for z in shopping_cart_prices:
    z = round(z, 2)
    shopping_cart_prices[rounded_item] = z
    rounded_item += 1

print(
    "The prices for the items that are in your shopping cart in respective order are:",
    shopping_cart_prices,
)
time.sleep(1)
final_price = round(sum(shopping_cart_prices), 2)
final_price_tax = (
    final_price + final_price * 0.05
)  # this varabile calculates the final price with 5% vat


def invoice(
    n,
):  # the following function creates a random number that would be the reciept invoice
    range_start = 10 ** (n - 1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)


print("The following is the final shopping recipet of your order:")
time.sleep(3)
print("The total price of your items is: ", round(final_price, 2))
time.sleep(3)
print("The final price of your items inclusive of 5% VAT is", round(final_price_tax, 2))
time.sleep(3)
print("The recipet invoice of your order is ", invoice(10))
time.sleep(3)
print("We hope you enjoyed the time shopping with us.")
