# Data Cleaning and Balancing from Scratch

**Autores:**
- José Gerardo Ruiz García - 23719
- Gerardo André Fernández Cruz - 23763

## Descripción

Proyecto de Ingeniería de Datos que implementa técnicas de limpieza y balanceo de datos usando Python, Pandas y NumPy sin utilizar funciones automáticas de sklearn.

### Funcionalidades:
1. **Generación de Dataset Sucio**: Crea un DataFrame con valores nulos y clases desbalanceadas
2. **Imputación de Datos Faltantes**: Rellena valores NaN con el promedio usando algoritmos manuales
3. **Undersampling Manual**: Balancea clases desbalanceadas mediante undersampling

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/jruiz002/data-cleaning-and-balancing-from-scratch.git
cd data-cleaning-and-balancing-from-scratch
```

### 2. Crear entorno virtual

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

Ejecutar el programa principal:

```bash
python main.py
```

Esto generará:
1. Un dataset sucio con 100 filas
2. Imputación de valores faltantes con el promedio
3. Un dataset balanceado con 20 filas (10 de cada clase)

## Estructura del Proyecto

```
.
├── main.py              # Archivo principal
├── utils.py             # Funciones de generación, limpieza y balanceo
├── requirements.txt     # Dependencias del proyecto
├── dataset.csv          # Dataset generado (no incluido en repo)
└── README.md           # Documentación
```

## Funciones Principales

### `generate_dataset(archivo_salida='dataset.csv')`
Genera un DataFrame con:
- 100 filas y 3 columnas (Edad, Salario, Compró_Producto)
- 10% de valores NaN en columna Edad
- Desbalance: 90 filas clase '0', 10 filas clase '1'

### `generate_df_avg_age(df)`
Recorre la columna Edad y rellena valores NaN con el promedio de edades existentes.

### `manual_undersampling(df, target_column='Compró_Producto')`
Realiza undersampling manual manteniendo todas las filas de la clase minoritaria y seleccionando aleatoriamente el mismo número de la clase mayoritaria.

## Desactivar entorno virtual

```bash
deactivate
```

