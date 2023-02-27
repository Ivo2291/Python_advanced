def shopping_cart(*args):
    meals = {"Pizza": [], "Soup": [], "Dessert": []}
    output = []

    for elements in args:
        if elements == "Stop":
            break

        current_meal = elements[0]
        product = elements[1]

        if product not in meals[current_meal]:

            if current_meal == "Soup":
                if len(meals[current_meal]) < 3:
                    meals[current_meal].append(product)

            elif current_meal == "Pizza":
                if len(meals[current_meal]) < 4:
                    meals[current_meal].append(product)

            elif current_meal == "Dessert":
                if len(meals[current_meal]) < 2:
                    meals[current_meal].append(product)

    meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

    for meal, products in meals:
        output.append(f"{meal}:")

        for current_product in sorted(products):
            if current_product:
                output.append(f" - {current_product}")

    products_counter = 0

    for product_to_check in meals:
        if product_to_check[1]:
            products_counter += 1

    if products_counter == 0:
        return "No products in the cart!"

    else:
        return '\n'.join(output)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
