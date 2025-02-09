import random
import numpy as np
import matplotlib.pyplot as plt

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

# Daten für Visualisierung
demand_values = np.linspace(1, 10, 50)  # Nachfrage von 1 bis 10
supply_values = np.linspace(1, 10, 50)  # Angebot von 1 bis 10

# Preisberechnung für alle Kombinationen von Angebot und Nachfrage
prices = np.array([[dynamic_pricing(d, s) for s in supply_values] for d in demand_values])

# Erstelle ein Meshgrid für die Visualisierung
X, Y = np.meshgrid(supply_values, demand_values)
Z = np.array([[dynamic_pricing(d, s) for s in supply_values] for d in demand_values])

# Visualisierung mit Konturdiagramm
plt.figure(figsize=(8,6))
contour = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour, label='Preis (€)', orientation='horizontal', pad=0.1, location='top')
plt.xlabel('Angebot')
plt.ylabel('Nachfrage')
plt.title('Preisänderung in Abhängigkeit von Angebot und Nachfrage')
plt.grid(True)
plt.show()
