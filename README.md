# blockchain-api-uea-ru

An auditing system for the app _Restaurante Universitário da UEA_ that logs messages securely over the Ethereum Network and generates reports of user's interactions. To run this project, you will need Docker. Firstly, build an image with the following command:

```sh
docker build -t blockchain-api-uea-ru .
```

Next, copy the file ```.env.example``` as ```.env``` and insert the needed environment variables.

Then run a Docker container based on the built image.
```sh
docker run --rm -p 5000:5000 -v "$(CURDIR):/app" blockchain-api-uea-ru
```

Alternatively, you can just run:
```sh
make build
make run
```

The API's documentation can be seen and used on this url:
>http://localhost:5000/swagger-ui