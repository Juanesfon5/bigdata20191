export HADOOP_STREAMING_HOME=/usr/hdp/3.0.1.0-187/hadoop-mapreduce/

hdfs dfs -rm -r /tmp/wc-out1

python wordcount-mr.py hdfs:///datasets/gutenberg-small/*.txt -r hadoop --output-dir hdfs:///tmp/wc-out1 --hadoop-streaming-jar $HADOOP_STREAMING_HOME/hadoop-streaming.jar
