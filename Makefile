build:
	docker run --rm -p 5000:5000 -v "$(pwd):/app" blockchain-api-uea-ru
run:
	docker build -t blockchain-api-uea-ru .