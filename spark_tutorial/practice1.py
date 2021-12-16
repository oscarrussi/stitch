from pyspark.sql.session import SparkSession
from pyspark import SparkContext
sc = SparkContext("local", "First App")
spark = SparkSession(sc)

df = (spark.read
      .options(header=True)
      .csv("pokemons.csv"))

df.show()