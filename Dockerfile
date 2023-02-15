FROM python:3.10
EXPOSE 5000
WORKDIR /app
ENV TZ=America/Manaus
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt \
  # syncing timezones
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && echo $TZ > /etc/timezone
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]