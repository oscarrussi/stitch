from pyspark.sql.session import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import DoubleType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
import singer
sc = SparkContext("local", "First App")
spark = SparkSession(sc)

spark_schema = schema = StructType([
  StructField("Film", StringType(), nullable=False),
  StructField("Genre", StringType(), nullable=False),
  StructField("Lead Studio", StringType(), nullable=False),
  StructField("Audience score %", IntegerType(), nullable=False),
  StructField("Profitability", DoubleType(), nullable=False),
  StructField("Rotten Tomatoes %", IntegerType(), nullable=False),
  StructField("Worldwide Gross", StringType(), nullable=False),
  StructField("Year", IntegerType(), nullable=False),
])

df = (spark.read
      .options(header=True)
      .schema(spark_schema)
      .csv("movies.csv"))

# rows = df.select('Film').collect()
# for row in rows:
#     print(row)
movies = df.rdd.map(lambda row: row.asDict()).collect()
# .json.loads()
# .toJSON().collect()
schema = {'properties': {
    'Film': {'type': 'string'},
    'Genre': {'type': 'string'},
    'Lead Studio': {'type': 'string'},
    'Audience score %': {'type': 'integer'},
    'Profitability': {'type': 'number'},
    'Rotten tomateos %': {'type': 'integer'},
    'Worldwide gross': {'type': 'string'},
    'Year': {'type': 'integer'},
    'Index': {'type': 'integer'}
    }
  }
singer.write_schema(stream_name="movies", schema=schema, key_properties=[])
i=0
for movie in movies:
  i+=1
  singer.write_record(stream_name="movies",  record={**movie, "index": i}) 