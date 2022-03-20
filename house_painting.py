x_visochina_house = float(input())
y_duljina_house = float(input())
h_visochina_house = float(input())
# Разход на боята
green_pain_color = 3.40
red_pain_color = 4.30
# Стени
door = 1.20 * 2
window = 1.5 * 1.5
front_wall_area = x_visochina_house * x_visochina_house
total_front_area = (2 * front_wall_area) - door
side_wall_area = x_visochina_house * y_duljina_house
total_side_area = (2 * side_wall_area) - (2 * window)
total_area_walls = total_front_area + total_side_area
green_pain_color_total_litters = total_area_walls / green_pain_color
print(f'{green_pain_color_total_litters:.2f}')
# Покрив
rectangle_roof_area = 2 * (x_visochina_house * y_duljina_house)
triangle_roof_area =  2 * (x_visochina_house * h_visochina_house / 2)
total_roof_area = rectangle_roof_area + triangle_roof_area
red_pain_color_total_litters = total_roof_area / red_pain_color
print(f'{red_pain_color_total_litters:.2f}')
