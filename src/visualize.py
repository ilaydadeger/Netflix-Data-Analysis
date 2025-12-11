import seaborn as sns
import matplotlib.pyplot as plt

def plot_type_distribution(df):
    sns.countplot(data=df, x="type", palette="pastel")
    plt.title("Movie vs TV Show Distribution")
    plt.show()

def plot_release_year_trend(df):
    sns.histplot(df['release_year'], kde=True, color="skyblue")
    plt.title("Release Year Distribution")
    plt.show()

def plot_top_countries(df):
    top_countries = df['country'].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, palette="mako")
    plt.title("Top Content-Producing Countries")
    plt.show()
