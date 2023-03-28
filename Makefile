build:
	docker build -t blockchain-api-uea-ru .
run:
	docker run --rm -p 5000:5000 -v "$(CURDIR):/app" blockchain-api-uea-ru
test-unit:
	pytest -rP tests/unit.py
test-integration:
	pytest -rP tests/integration.py