1. Create and initialize a new script 
```
docker run --rm -i -v $PWD:/app -u 1000 -w /app grafana/k6 new
```

2. Run k6
```
docker run --rm -i grafana/k6 run - <script.js
```
