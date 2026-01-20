import pandas as pd
import numpy as np

def generate_dataset(archivo_salida='dataset.csv'):    
    # Set seed for reproducibility
    np.random.seed(42)
    
    # Generate data
    n_filas = 100
    
    # Age: values between 18 and 65 years
    edad = np.random.randint(18, 66, size=n_filas)
    
    # Salary: values between 20000 and 100000
    salario = np.random.randint(20000, 100001, size=n_filas)
    
    # Purchased_Product: imbalanced (90 zeros, 10 ones)
    compro_producto = np.array([0] * 90 + [1] * 10)
    np.random.shuffle(compro_producto)  # Shuffle randomly
    
    # Create DataFrame
    df = pd.DataFrame({
        'Edad': edad,
        'Salario': salario,
        'Compró_Producto': compro_producto
    })
    
    # Introduce NaN values in 10% of the Age column
    num_nulos = int(n_filas * 0.10)  # 10 null values
    indices_nulos = np.random.choice(df.index, size=num_nulos, replace=False)
    df.loc[indices_nulos, 'Edad'] = np.nan
    
    # Save the dataset (overwrite if it already exists)
    df.to_csv(archivo_salida, index=False)
        
    return df

def generate_df_avg_age(df: pd.DataFrame) -> pd.DataFrame:
    # Calculate average age from existing (non-null) values
    avg_age = df["Edad"].mean()
    
    for index in df.index:
        # If a missing value is found
        if pd.isna(df.loc[index, 'Edad']):
            # Fill it with the average of existing ages
            df.loc[index, 'Edad'] = avg_age
    
    return df
