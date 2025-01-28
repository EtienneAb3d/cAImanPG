install:
	pip install -r requirements.txt
run:
	python Vllm.py &
	uvicorn main:app --reload --reload-exclude '*script.py' --workers 2 &

