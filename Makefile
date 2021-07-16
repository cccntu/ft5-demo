docker-env:
	docker build -t ft5-env env/
model:
	python3 download_and_cache.py
examples:
	pip3 install datasets
	python3 download_examples.py
docker: model docker-env
	docker build -t ft5-demo --build-arg ENV_IMAGE=ft5-env .
