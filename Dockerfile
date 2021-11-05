FROM python:3.9
WORKDIR /app
COPY /app .
RUN make install
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]