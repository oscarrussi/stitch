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
  StructField("ORDERID", IntegerType(), nullable=False),
  StructField("PAYMENTMETHOD", StringType(), nullable=False),
  StructField("STATUS", StringType(), nullable=False),
  StructField("AMOUNT", IntegerType(), nullable=False),
  StructField("CREATED", StringType(), nullable=False)
])

df = (spark.read
      .options(header=True)
      .schema(spark_schema)
      .csv("stripe_payments.csv"))

payments = df.rdd.map(lambda row: row.asDict()).collect()
schema = {'properties': {
    'ID': {'type': 'integer'},
    'ORDERID': {'type': 'integer'},
    'PAYMENTMETHOD': {'type': 'string'},
    'STATUS': {'type': 'string'},
    'AMOUNT': {'type': 'integer'},
    'CREATED': { "type": "string", "format": "date"}
    }
  }
singer.write_schema(stream_name="payments", schema=schema, key_properties=[])
i=0
for payment in payments:
  i+=1
  singer.write_record(stream_name="payments",  record={**payment}) 