from pyspark.sql.session import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
import singer
sc = SparkContext("local", "First App")
spark = SparkSession(sc)

spark_schema = schema = StructType([
  StructField("ID", IntegerType(), nullable=False),
  StructField("FIRST_NAME", StringType(), nullable=False),
  StructField("LAST_NAME", StringType(), nullable=False)
])

df = (spark.read
      .options(header=True)
      .schema(spark_schema)
      .csv("jaffle_shop_customers.csv"))

customers = df.rdd.map(lambda row: row.asDict()).collect()
schema = {'properties': {
    'ID': {'type': 'integer'},
    'FIRST_NAME': {'type': 'string'},
    'LAST_NAME': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="customers", schema=schema, key_properties=[])
i=0
for customer in customers:
  i+=1
  singer.write_record(stream_name="customers",  record={**customer}) 