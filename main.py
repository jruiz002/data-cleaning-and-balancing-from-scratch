# Inteligencia Articial
# José Gerardo Ruiz García - 23719
# Gerardo André Fernández Cruz - 23763

from utils import generate_dataset, generate_df_avg_age, manual_undersampling


# Generate Dataset
df = generate_dataset()

# New dataframe with avg age
# Answering Question: ¿En qué situación usar el promedio sería una mala idea y sería mejor usar la mediana?
# Usar el promedio no es una buena opción cuando existen valores extremos que se 
# alejan mucho del resto de los datos, porque estos valores pueden 
# distorsionar el resultado. En estos casos, la mediana es mejor, ya qno se ve 
# afectada por esos valores extremos y representa mejor a la mayoría de los datos.
df_avg_age = generate_df_avg_age(df)

print("Dataset with average age filled:")
print(df_avg_age.head(20))

# Apply manual undersampling to balance the dataset
print("\n" + "="*50)
df_balanced = manual_undersampling(df_avg_age)

print("\nBalanced dataset:")
print(df_balanced.head(20))