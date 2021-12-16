from pyspark.sql.session import SparkSession
from pyspark import SparkContext
sc = SparkContext("local", "First App")
spark = SparkSession(sc)

ratings = (spark
           .read
           .options(header=True, mode="DROPMALFORMED")
           .csv("pokemons.csv"))
ratings.show()