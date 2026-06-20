def calculate_spread(volatility):
    """If-Bedingung welche den Spread je nach Marktvolatilität berechnet."""
    if volatility > 0.05:
        return 0.005
    return 0.001

def adjust_liquidity(volume, volatility):
    """Hier wird das Volumen dem Risikoprofil angepasst."""
    if volatility > 0.05:
        return volume * 0.3
    return volume

if __name__ == "__main__":
    volatility = 0.08
    spread = calculate_spread(volatility)
    volume = adjust_liquidity(10000, volatility)
    print(f"Spread: {spread}, Volumen: {volume}")
