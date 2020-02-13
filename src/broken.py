from pyspark.sql import SparkSession

class Extract(object):
    spark = SparkSession.builder.getOrCreate()