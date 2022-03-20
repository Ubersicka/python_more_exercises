price_skumria_kg = float(input())
price_caca_kg = float(input())
palamuda_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

price_palamuda_kg = price_skumria_kg + price_skumria_kg * 0.60
total_palamuda = palamuda_kg * price_palamuda_kg
price_safrid_kg = price_caca_kg + price_caca_kg * 0.80
total_safrid = safrid_kg * price_safrid_kg

price_midi_kg = 7.50
total_midi = price_midi_kg * midi_kg

total_price = total_palamuda + total_safrid + total_midi

print(f'{total_price:.2f}')


