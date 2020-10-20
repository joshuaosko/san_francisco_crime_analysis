# san_francisco_crime_analysis

## How to run

1. /usr/bin/zookeeper-server-start config/zookeeper.properties
2. /usr/bin/kafka-server-start config/server.properties 
3. ./start.sh
4. python producer_server.py
5. python kafka_server.py
6. spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py


Using the default settings 3 tasks were able to be active at the same time at an average completion of 4 seconds for a 200 task job. 
After exploring different parameter tuning options such as enabling caching to a cache table, changing the number of RDDs I was unable
to identify a discernable difference in throughput for some reason.

