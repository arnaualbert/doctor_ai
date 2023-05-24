# doctor_ai

Docker: https://hub.docker.com/repository/docker/arnaualbert/doctor_ai/general


First download the docker

```shell
docker pull arnaualbert/doctor_ai:v
```

Then use the database

```
doctor_ai.sql
```

Run the docker

```shell
docker run -d -p 5001:80 --net=host arnaualbert/doctor_ai:v
```

