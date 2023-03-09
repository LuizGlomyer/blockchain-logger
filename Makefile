build:
	docker build -t blockchain-api-uea-ru .
run:
	docker run --rm -p 5000:5000 -v "$(CURDIR):/app" blockchain-api-uea-ru
test:
	pytest -rP tests/unit.py