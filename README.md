# Teste de Performance utilizando JMeter, Prometheus e Grafana

Passo a passo:

1) entre na pasta monitoring:
```sh
cd monitoring
```

2) realize o build das ferramentas e aguarde alguns minutos:
```sh
sudo docker-compose up --build -d
```

3) entre na pasta matmul-api:
```sh
cd ../matmul-api
```

4) realize o build da API e aguarde alguns minutos:
```sh
sudo docker-compose up --build -d
```

5) entre na pasta jmeter:
```sh
cd ../jmeter
```

6) permita a execução do arquivo:
```sh
sudo chmod +x run_test_jmeter.sh
```

7) execute o arquivo para iniciar o teste:
```sh
sudo ./run_test_jmeter.sh PASTA_FINAL
```

8) após a finalização do teste, verifica-se a criação dos relatórios na PASTA_FINAL