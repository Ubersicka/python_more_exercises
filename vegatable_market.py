price_vegatable = float(input())
price_fruit = float(input())
total_kg_vegetable = int(input())
total_kg_fruit = int(input())

total_vegatable = price_vegatable * total_kg_vegetable
total_fruit = price_fruit * total_kg_fruit
total_in_bgn = total_vegatable + total_fruit
total_in_eur = total_in_bgn / 1.94
print (f'{total_in_eur:.2f}')
