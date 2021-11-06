.PHONY: \
	check \
	format \
	install \
	run \
	tests

check:
	python -m black --check .

format:
	python -m black . 

install:
	pip install --no-cache-dir --upgrade -r ./requirements.txt

run:
	uvicorn main:app --host 0.0.0.0 --port 80 --reload

tests:
	pytest -v