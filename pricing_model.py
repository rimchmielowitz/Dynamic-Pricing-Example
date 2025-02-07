import random

def dynamic_pricing(demand_level, supply_level, base_price=10):
    """
    Simples Preismodell basierend auf Angebot und Nachfrage.
    - demand_level: Nachfrage (1-10, wobei 10 sehr hoch ist)
    - supply_level: Angebot (1-10, wobei 10 sehr hoch ist)
    - base_price: Ausgangspreis
    """
    demand_factor = 1 + (demand_level - 5) * 0.1
    supply_factor = 1 - (supply_level - 5) * 0.1
    final_price = base_price * demand_factor * supply_factor
    return round(final_price, 2)

# Beispielhafte Simulation
for _ in range(5):
    demand = random.randint(1, 10)
    supply = random.randint(1, 10)
    price = dynamic_pricing(demand, supply)
    print(f"Nachfrage: {demand}, Angebot: {supply} -> Preis: {price}€")
