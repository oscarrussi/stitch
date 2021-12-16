from pyspark.sql.session import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import col
sc = SparkContext("local", "First App")
spark = SparkSession(sc)
movies = (spark.read
      .options(header=True)
      .csv("movies.csv")
      .select([col("Film"), col("Genre"), col("Profitability"), col("Year")])
      )
      
from pyspark.sql.functions import avg, stddev_samp, max as sfmax

aggregated = (movies
              .groupBy(col('Genre'))
              .agg(
                avg('Profitability').alias('average_profitability'),
                stddev_samp('Profitability'),
                sfmax('Profitability').alias('highest_profitability'))
             )

aggregated.show()