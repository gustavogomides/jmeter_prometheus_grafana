#! /bin/sh

if [ -z "$1" ]
  then
    echo "Favor informar o nome do arquivo final"
    exit 1
fi

export _JAVA_OPTIONS="-Xms8g -Xmx8g -XX:MaxMetaspaceSize=8192m -Xss256k"

export HEAP="-Xms8g -Xmx8g -XX:MaxMetaspaceSize=8192m -Xss256k"

TEST_NAME=Api.jmx

REPORT_FOLDER='test_'$1

REPORT_FOLDER=$REPORT_FOLDER

rm -rf $REPORT_FOLDER

mkdir -p $REPORT_FOLDER

echo
echo "******************************"
echo "TESTE INICIADO"
echo "******************************"
echo


./apache-jmeter-4.0/bin/jmeter -n -t $TEST_NAME -l $REPORT_FOLDER/jtl -e -o $REPORT_FOLDER/report


echo
echo "******************************"
echo "TESTE CONCLUIDO"
echo "******************************"
echo



