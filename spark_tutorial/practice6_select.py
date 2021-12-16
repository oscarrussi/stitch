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
ratings = (spark.read
      .options(header=True)
      .schema(schema)
      .csv("pokemons.csv"))
from pyspark.sql.functions import col
# Select the columns and rename the "absorption_rate" column
result = ratings.select([col("name"),
                       col("index").alias("id")])
# Show only unique values
result.distinct().show()