# Week 1 — App Containerization

## Completed all assigned tasks

## Homework Challenges

- Implemented healthcheck in [the V3 Docker compose file](https://github.com/zhangcheng/aws-bootcamp-cruddur-2023/blob/week-1/docker-compose.yml)

- Research best practices of Dockerfiles and attempt to implement it in your Dockerfile
    - [Use user 'app' to run process in Docker](https://github.com/zhangcheng/aws-bootcamp-cruddur-2023/blob/week-1/backend-flask/Dockerfile), instead of the default 'root'.

## Misc Notes

- Docker networking
```sh
docker run --rm -it curlimages/curl "-X GET http://localhost:4567/api/activities/home -H \"Accept: application/json\" -H \"Content-Type: application/json\""
```
This command won't work due to docker networking, need to specify host's IP, as:
```sh
docker run --rm -it curlimages/curl -X GET http://10.0.5.2:4567/api/activities/home -H "Accept: application/json" -H "Content-Type: application/json"
```

- Typo: 'busybosy' should be 'busybox'

- `npm i` on host
> We have to run NPM Install before building the container since it needs to copy the contents of node_modules

I think the reason for this step, is because we mount the app directory onto the container, and if not done this step on host, the mounted directory won't contain `node_modules` to run the app.
