.PHONY: \
	install \
	run \
	tests

install:
	pip install --no-cache-dir --upgrade -r ./requirements.txt

run:
	uvicorn main:app --host 0.0.0.0 --port 80 --reload

tests:
	pytest -v