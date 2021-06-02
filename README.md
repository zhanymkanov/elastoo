## How to build?
1. Setup a virtual environment
```
python3 -m venv venv
```
2. Activate venv (Linux, Mac OS)
```
source venv/bin/activate
```
3. Install Packages
```
pip install -r requirements.txt
```

## How to Start?
1. Run the server
```
uvicorn src.main:app --reload
```
2. Go to Swagger UI at http://127.0.0.1:8000/docs
