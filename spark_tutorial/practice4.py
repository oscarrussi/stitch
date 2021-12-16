from pyspark.sql.session import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField

sc = SparkContext("local", "First App")
spark = SparkSession(sc)

schema = StructType([
  StructField("name", StringType(), nullable=False),
  StructField("url", StringType(), nullable=False),
  StructField("index", IntegerType(), nullable=False)
])

df = (spark.read
      .options(header=True)
      .schema(schema)
      .csv("pokemons.csv"))
df = df.fillna(-1, subset=["index"])
df.show()