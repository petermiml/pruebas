import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

df_gr = df.groupby("gender").agg({
                "math score": 'mean',
                "reading score": 'mean',
                "writing score": 'mean'
})

print(df_gr)


# Gráfico de línea

#df_gr["math score"].plot()
#plt.show()

# Gráfico de barras

df_gr["math score"].plot(kind="bar")
plt.show()

df_gr.to