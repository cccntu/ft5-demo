ARG ENV_IMAGE=myorg/myenv:latest
FROM $ENV_IMAGE

WORKDIR /code_dir
COPY . repo/
WORKDIR /code_dir/repo
ENV PORT 8080
RUN ["./download_and_cache.sh"]
CMD ["./run.sh"]
