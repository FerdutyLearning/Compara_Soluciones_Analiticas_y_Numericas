"""Compara la ley de enfriamiento de Newton con Euler explícito."""
from math import exp

TEMPERATURA_AMBIENTE = 20.0  # °C
TEMPERATURA_INICIAL = 80.0   # °C
K = 0.5                      # min⁻¹
H = 0.2                      # min
PASOS = 5                    # desde t = 0 hasta t = 1 min


def rapidez(temperatura):
    """Rapidez de enfriamiento en °C/min."""
    return -K * (temperatura - TEMPERATURA_AMBIENTE)


def exacta(t):
    """Solución obtenida por separación de variables."""
    return TEMPERATURA_AMBIENTE + (TEMPERATURA_INICIAL - TEMPERATURA_AMBIENTE) * exp(-K * t)


def comparar():
    """Genera el estado inicial y los cinco estados calculados por Euler."""
    temperatura = TEMPERATURA_INICIAL
    for paso in range(PASOS + 1):
        t = paso * H
        referencia = exacta(t)
        yield t, referencia, temperatura, abs(referencia - temperatura)
        if paso < PASOS:
            temperatura += H * rapidez(temperatura)


if __name__ == "__main__":
    print("t (min) | Exacta (°C) | Euler (°C) | Error absoluto (°C)")
    for t, referencia, temperatura, error in comparar():
        print(f"{t:7.1f} | {referencia:11.4f} | {temperatura:10.4f} | {error:19.4f}")
