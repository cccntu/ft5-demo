ARG ENV_IMAGE=myorg/myenv:latest
FROM $ENV_IMAGE

WORKDIR /code_dir
COPY . repo/
WORKDIR /code_dir/repo
ENV PORT 8080
CMD ["./run.sh"]
