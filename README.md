# ft5 demo code



Project template based on https://github.com/cccntu/ml-docker

Original README:

---



# Project template for machine learning model deployment using Docker

* Edit `env/Dockerfile`  and `env/requirements.txt`.
  * Change base image in env/Dockerfile for cuda, etc...

* Build env docker
  * This will re-run `pip install -r requirements.txt` everytime, so
    only re-run this when you need to update the env, e.g. update `requirements.txt`
```
export ENV_IMAGE_NAME ='myorg/myenv:latest'
export APP_IMAGE_NAME ='myorg/myapp:latest'
docker build -t $ENV_IMAGE_NAME env
```

* Put everything insidee this repo root, run.sh should be able to run even if the repo root is moved around.
* Build another docker image based on env docker:
  * This will copy the entire repo to the docker image, and run `run.sh` on start-up.
```
docker build -t $APP_IMAGE_NAME --build-arg ENV_IMAGE=$ENV_IMAGE_NAME .
```

* run on local machine for testing
```
docker run --rm -it -p 8080:8080 $APP_IMAGE_NAME
```
