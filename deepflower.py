
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os
import sys
import time
 
try:
    from pyspark import SparkConf, SparkContext
    from pyspark import sql
    from pyspark.sql import SQLContext
    from pyspark.sql import SparkSession
    from pyspark.sql.types import *
    from pyspark.sql.functions import *
    from sparkdl import readImages
    from pyspark.sql.functions import lit
    from pyspark.ml.classification import LogisticRegression
    from pyspark.ml import Pipeline
    from sparkdl import DeepImageFeaturizer
    from pyspark.ml.evaluation import MulticlassClassificationEvaluator
 
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)
 
if __name__ == "__main__" :
    # Configure Spark
    spark = SparkSession\
        .builder\
        .appName("mb_ornek_sorgu")\
        .config("spark.some.config.option", "some-value")\
        .getOrCreate()
 
    #Initialize SparkContext
    sc = spark.sparkContext
    img_dir = "/home/ubuntu/flower_photos"

    tulips_df = readImages(img_dir + "/tulips").withColumn("label", lit(1))
    daisy_df = readImages(img_dir + "/daisy").withColumn("label", lit(0))

    tulips_train, tulips_test = tulips_df.randomSplit([0.6, 0.4])
    daisy_train, daisy_test = daisy_df.randomSplit([0.6, 0.4])

    train_df = tulips_train.unionAll(daisy_train)
    test_df = tulips_test.unionAll(daisy_test)

    featurizer = DeepImageFeaturizer(inputCol="image", outputCol="features", modelName="InceptionV3")
    lr = LogisticRegression(maxIter=20, regParam=0.05, elasticNetParam=0.3, labelCol="label")
    p = Pipeline(stages=[featurizer, lr])
    p_model = p.fit(train_df)

    df = p_model.transform(test_df)
    df.show()

    predictionAndLabels = df.select("prediction", "label")
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    print("Training set accuracy = " + str(evaluator.evaluate(predictionAndLabels)))
