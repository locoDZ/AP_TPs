cities = {}

while True:
    city = input("Enter a city name (or 'stop' to finish): ").strip()

    if city.lower() == 'stop':
        break

    population = len(city) * 1_000_000

    cities[city] = population

citiesSorted = sorted(cities.items(), key=lambda x: x[1], reverse=True)
print("\n--- Magical City Populations ---")
for city, population in citiesSorted:
    print(f"{city}: {population:,} citizens")
