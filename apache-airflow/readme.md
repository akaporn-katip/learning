### Create custom image
```
docker build -f Dockerfile -t airflow-project:0.0.1 .
```

### Get an docker-compose 
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.3/docker-compose.yaml'
```

### Creat .env file
```
cat <<EOF > .env
AIRFLOW_PROJ_DIR=./airflow
AIRFLOW_IMAGE_NAME=airflow-project:0.0.1
AIRFLOW_UID=$(id -u)
EOF
```

### Running compose file
```
docker compose up -d
```

### Clean up
```
docker compose down --volumes --remove-orphans
sudo rm -r ./airflow
```

