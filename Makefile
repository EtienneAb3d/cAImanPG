install:
	pip install -r requirements.txt
run:
	uvicorn main:app --reload --reload-exclude '*script.py' --workers 2
