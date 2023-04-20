
df_parquet = spark.read.load("parquet_dir")
df_parquet.createOrReplaceTempView("parquet_table");
teenagers = spark.sql("SELECT name from parquet_table where age >= 13 AND age <= 19")



df_parquet.write.json("myjson_dir")
df_parquet.write.format("json").save("myjson_dir2")


df_parquet.write.mode("append").json("myjson_dir")
df_parquet.write.mode("append").save("parquet_dir")



df_parquet.write.saveAsTable("hive_parquet_table")


df_parquet = spark.read.option("mergeSchema", "true").parquet("parquet_partitioned")

