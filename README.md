# spark-deeplearning-examples
Deep learning examples with Apache Spark.

Installation of spark-deep-learnig https://spark-packages.org/package/databricks/spark-deep-learning on Ubuntu 16.04

# Install Python Software Properties

sudo apt-get install python-software-properties

# Add Repository

sudo add-apt-repository ppa:webupd8team/java

# Update the source list

sudo apt-get update

# Install Java

sudo apt-get install oracle-java8-installer

#Download Spark
wget https://archive.apache.org/dist/spark/spark-2.1.1/spark-2.1.1-bin-hadoop2.7.tgz

#Untar
tar xzf spark-2.1.1-bin-hadoop2.7.tgz 

#move to/opt/
sudo mv spark-2.1.1-bin-hadoop2.7 /opt/spark

#set environmental variables
export JAVA_HOME="/usr/lib/jvm/java-8-oracle/"
export SPARK_HOME="/opt/spark"


# install python packages
export LC_ALL=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
sudo apt-get install python-pip python-dev

sudo pip install tensorflow
sudo pip install nose
sudo pip install pillow
sudo pip install keras
sudo pip install h5py
sudo pip install py4j
sudo pip install pandas

# to run shell
export set JAVA_OPTS="-Xmx9G -XX:MaxPermSize=2G -XX:+UseCompressedOops -XX:MaxMetaspaceSize=512m"
$SPARK_HOME/bin/pyspark --packages databricks:spark-deep-learning:0.2.0-spark2.1-s_2.11


#To run the examples

PYSPARK_PYTHON=/usr/bin/python /opt/spark/bin/spark-submit --master local[8]  --num-executors 10 --executor-memory 16g --executor-cores 2 --driver-memory 16g  --packages databricks:spark-deep-learning:0.1.0-spark2.1-s_2.11 deepsparktest.py
