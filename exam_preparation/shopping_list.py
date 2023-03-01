def shopping_list(budget, **products_data):
    output = []
    products_bought = 0

    if budget < 100:
        return "You do not have enough budget."

    for product, product_info in products_data.items():

        if products_bought == 5:
            break

        price = float(product_info[0])
        quantity = int(product_info[1])
        total_price = price * quantity

        if budget >= total_price:
            output.append(f"You bought {product} for {total_price:.2f} leva.")
            products_bought += 1
            budget -= total_price

    return '\n'.join(output)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
