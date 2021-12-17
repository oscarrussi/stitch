from pyspark.sql.session import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import IntegerType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
import singer
sc = SparkContext("local", "First App")
spark = SparkSession(sc)

spark_schema = schema = StructType([
  StructField("ID", IntegerType(), nullable=False),
  StructField("USER_ID", IntegerType(), nullable=False),
  StructField("ORDER_DATE", StringType(), nullable=False),
  StructField("STATUS", StringType(), nullable=False)
])

df = (spark.read
      .options(header=True)
      .schema(spark_schema)
      .csv("jaffle_shop_orders.csv"))

orders = df.rdd.map(lambda row: row.asDict()).collect()
schema = {'properties': {
    'ID': {'type': 'integer'},
    'USER_ID': {'type': 'integer'},
    'ORDER_DATE': { "type": "string", "format": "date"},
    'STATUS': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="orders", schema=schema, key_properties=[])
i=0
for order in orders:
  i+=1
  singer.write_record(stream_name="orders",  record={**order}) 