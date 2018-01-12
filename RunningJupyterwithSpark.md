

Install Anaconda

Download extract spark, set SPARK_HOME and JAVA_HOME

'''bash
export JAVA_HOME="/usr/lib/jvm/java-8-oracle/"
export SPARK_HOME="/opt/spark"
'''

'''bash
MASTER="spark://127.0.0.1:7077" SPARK_EXECUTOR_MEMORY="8G" PYSPARK_DRIVER_PYTHON=ipython PYSPARK_DRIVER_PYTHON_OPTS="notebook" ~/spark/bin/pyspark --master local[2]
'''
