model:
	python3 download_and_cache.py
examples:
	pip3 install datasets
	python3 download_examples.py
docker: model
	docker build -t ft5-demo .
