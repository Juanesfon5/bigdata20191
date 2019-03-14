# Universidad EAFIT
# Curso ST0263 Tópicos Especiales en Telemática, 2019-1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co
# Profesor: Alvaro Ospina - aeospinas@eafit.edu.co

# Demo MapReduce en Java y Python con MRJOB

# LABORATORIO:

[lab-mrjob](lab-mrjob.md)

# (1) WordCount en Java

Tomado de: https://hadoop.apache.org/docs/r2.7.3/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html

* Contador de palabras en archivos texto en Java

* Se tiene el programa ejemplo: [WordCount.java](WordCount.java), el cual despues de compilarse en la version hadoop 2.7.3, genera un jar wc.jar, el cual será el que finalmente se ejecute.

* Descargarlo, compilarlo y generar el jar (wc.jar)

[WordCount](WordCount.java)

[script-compilacion-jar](wc-gen-jar.sh)

>		user@master$ cd 02-mapreduce
>		user@master$ sh wc-gen-jar.sh

### Para ejecutar:

>		user@master$ hadoop jar wc.jar WordCount hdfs:///datasets/gutenberg-small/*.txt hdfs:///user/<username>/result1

(puede tomar varios minutos)

* el comando hadoop se este abandonando por yarn:

>		user@master$ yarn jar wc.jar WordCount hdfs:///datasets/gutenberg-small/*.txt hdfs:///user/<username>/result2


# (2) WordCount en python

* correr la versión serial / secuencial asumimiendo todos los datos locales:

    $ cd 02-mapreduce
    $ python wordcount-local.py /datasets/gutenberg-small/*.txt > salida-serial.txt
    $ more salida-serial.txt

* Hay varias librerias de python para acceder a servicios MapReduce en Hadoop

* Se usará MRJOB (https://pythonhosted.org/mrjob/)

* Se puede emplear una version de python 2.x o 3.x, del sistema (como root) o con un manejador de versiones de node (pyenv o virtualenv).

* Como parte del sistema, se instalará mrjob así:

>		user@master$ sudo yum install python-pip
>		user@master$ sudo pip install --upgrade pip
>		user@master$ sudo pip install mrjob

* (OPCIONAL) Si desea utilizar un manejador de versiones de python en su propio, puede ser así:

primero instalar pyenv (https://github.com/pyenv/pyenv-installer)

>		user@master$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
>		user@master$ pyenv update
>		user@master$ pyenv install 2.7.13
>		user@master$ pyenv local 2.7.13
>		user@master$ pip install mrjob

* Probar mrjob python local:

>		user@master$ cd 02-mapreduce
>		user@master$ python wordcount-mr.py /datasets/gutenberg-small/*.txt

* Ejecutar mrjob python en Hadoop con datos en hdfs:

Crear variable de ambiente: HADOOP_STREAMING_HOME para HORTONWORKS:

>   user@master$ export HADOOP_STREAMING_HOME=/usr/hdp/3.0.1.0-187/hadoop-mapreduce/

Crear variable de ambiente: HADOOP_STREAMING_HOME para CLOUDERA CDH 5.14:

>   user@master$ export HADOOP_STREAMING_HOME=/opt/cloudera/parcels/CDH-5.14.0-1.cdh5.14.0.p0.24/lib/hadoop-mapreduce

Ejecutar:

>		user@master$ python wordcount-mr.py hdfs:///datasets/gutenberg-small/*.txt -r hadoop --output-dir hdfs:///user/<login>/result3 --hadoop-streaming-jar $HADOOP_STREAMING_HOME/hadoop-streaming.jar

* el directorio 'result*' no puede existir)

## "-D mapred.reduce.tasks=10" para especificar el nro de reducers en MRJOB
