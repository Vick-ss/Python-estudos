
import pandas  as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#importando e entendendo dados
df = pd.read_csv("student_habits_performance.csv")

#visualizando dados
df.info()

#colunas numéricas 
cols = [
     "study_hours_per_day",
     "social_media_hours",
     "netflix_hours",
     "sleep_hours",
     "attendance_percentage",
     "exercise_frequency",
     "mental_health_rating",
     "exam_score",            
]


#Plotar map de calor-heatmap

sns.heatmap(df[cols].corr(), annot=True, cmap= "coolwarm")
plt.title("correlação entre hábitos e nota final")
plt.show()

#Alunos que estudam mais tem melhor desenpenho? ---> Gráfico de dispersão com linha de regressão
# x="study_hours_per_day" / y="exam_score"
sns.lmplot(data=df, x="study_hours_per_day", y="exam_score", hue="gender", palette="coolwarm")
plt.title("Mais etudo -->  notas mais altas?")
plt.show()  
          

# Comparando médias: quem estuda 5h vs 2hrs

filtro_estudo_alto = df ["study_hours_per_day"] > 5
filtro_estudo_baixo = df ["study_hours_per_day"] < 2

grupo_estudo_alto = df[filtro_estudo_alto]["exam_score"]
grupo_estudo_baixo= df[filtro_estudo_baixo]["exam_score"]


print("Média notas (estuda >5h):", grupo_estudo_alto.mean())
print("Média notas (estuda <2h):", grupo_estudo_baixo.mean())

#Redes sociais: distibuição geral (Histograma )

sns.histplot(data=df, x="social_media_hours", hue="gender", palette="coolwarm")
plt.title("Distribuição de tempo em redes sociais")
plt.show()

#Avaliando notas médias por diferentes intervalos de (bins) de periodo gasto em rede sociais ["0-2h", "2h-4h", "4h-6h"]

df["social_media_bin" ] = pd.cut(
   df["social_media_hours"],
   bins=[0, 2, 4, 6],
   labels=["0-2h", "2h-4h", "4h-6h"]
)

#PLOTAR Gráfico de Caixa (boxplot)

sns.boxplot(x="social_media_bin", y="exam_score", data=df, hue="gender", palette="coolwarm")
plt.title("Notas por tempo em redes sociais")
plt.show()

# Frequência de exercícios físicos

for col in ["exercise_frequency", "mental_health_rating", "diet_quality"]:
    sns.boxenplot(x=col, y="exam_score", data=df, hue="gender", palette="coolwarm")
    plt.show()

# Estatistica por gênero (média a desvio padrçao)
df.groupby(["gender"]) ["exam_score"].agg(["mean", "std"])

# Avaliar distribuição de gênero 
df ["gender"].value_counts(normalize=True)
