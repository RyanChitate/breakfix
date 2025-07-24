# FastAPI Backend

## Installation

Install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Starting the Server

Run the FastAPI development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Documentation

FastAPI provides interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

## Testing

Run tests using:
```bash
pytest
```
