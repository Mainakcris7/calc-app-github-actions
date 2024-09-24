# Distorless Python docker images
FROM gcr.io/distroless/python3

WORKDIR /calculator-app

COPY . /calculator-app/

# This command is the entrypoint, and can't be changed during docker container execution
ENTRYPOINT [ "python" ]

# These commands can be changed/overridden during docker container execution (docker run ...)
CMD [ "app.py" ]

