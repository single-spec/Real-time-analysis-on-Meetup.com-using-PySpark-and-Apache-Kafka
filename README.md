# Real-time-analysis-on-Meetup.com-using-PySpark-and-Apache-Kafka

Initializing the Zookeeper, Kafka, Pyspark:

Start zookeeper with the below command(First for windows and second for Linux).
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
bin/zookeeper-server-start.sh config/zookeeper.properties
	
kafka started using the below command(First for windows and second for Linux), our version is 2.7.0.
.\bin\windows\kafka-server-start.bat .\config\server.properties
bin/kafka-server-start.sh config/server.properties

#Description about python codes
	
kafka.producer.ipynb - Kafka producer program which will connect to web socket and sends to topic meetup.
kafka_consumer.ipynb - Kafka consumer consumes messages from the topic meetup.
	
python_spark_meetup.ipynb - Spark application program to do some analysis
The above program submitted using 
bin\spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.1 python_spark_meetup.ipynb localhost:2181 meetup
	
meetup_visualization.ipynb - Produces visualizations using matplotlib.
