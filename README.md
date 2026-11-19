# Compara_Soluciones_Analiticas_y_Numericas

# Enfriamiento de una pieza metálica

Una pieza sale de un proceso a 80 °C y se deja en un taller a 20 °C. ¿Qué temperatura tendrá al cabo de un minuto? Suponemos que la temperatura de la pieza es uniforme, que el ambiente permanece constante y que la rapidez de enfriamiento es proporcional a la diferencia de temperaturas.

## Modelo y solución exacta

Con el tiempo $t$ en minutos y una constante de enfriamiento de $0.5$ por minuto, la ecuación y su condición inicial son

$$
\frac{dT}{dt}=-0.5(T-20),\qquad T(0)=80.
$$

Separamos las variables dividiendo por la diferencia de temperatura. Para esta pieza, que comienza por encima de la temperatura ambiente, integramos desde el estado inicial hasta el instante de interés.

$$
\int_{80}^{T(t)}\frac{d\theta}{\theta-20}
=-0.5\int_0^t ds
\quad\Longrightarrow\quad
\ln\left(\frac{T(t)-20}{60}\right)=-0.5t.
$$

Al aplicar la exponencial y despejar, obtenemos $T(t)=20+60e^{-0.5t}$. La fórmula devuelve 80 °C en el instante inicial y tiende a 20 °C a largo plazo.

## Aproximación por Euler

Dividimos el minuto en cinco intervalos de longitud $h=0.2$. Al inicio de cada intervalo calculamos la pendiente usando la última temperatura aproximada. Avanzamos con

$$
T_{n+1}=T_n+h[-0.5(T_n-20)]=T_n-0.1(T_n-20).
$$

La primera pendiente es −30 °C/min. Durante 0.2 min Euler estima un descenso de 6 °C, por lo que llega a 74 °C. El siguiente cálculo comienza con esos 74 °C.

## Ejecutar

Con Python 3, desde la carpeta del proyecto:

```sh
python comparar.py
```

El programa utiliza solo la biblioteca estándar e imprime seis filas, una por instante, con la temperatura exacta, la aproximada y el error absoluto. Al minuto, la solución exacta da **56.3918 °C** y Euler da **55.4294 °C**. Euler estima una temperatura menor porque conserva durante cada paso la rapidez de enfriamiento inicial, aunque su magnitud disminuye conforme la pieza se enfría.
