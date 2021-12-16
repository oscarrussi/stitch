from pyspark.sql.session import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
sc = SparkContext("local", "First App")
spark = SparkSession(sc)

# Define the schema
schema = StructType([
  StructField("pokemon name", StringType(), nullable=False),
  StructField("url for more details", StringType(), nullable=False)
])

better_df = (spark
             .read
             .options(header=True)
             # Pass the predefined schema to the Reader
             .schema(schema)
             .csv("pokemons.csv"))
better_df.show()