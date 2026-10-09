# PowerShell script to set up venv (if not already) and run the FastAPI server

# create virtual environment if missing
if (-not (Test-Path -Path .\.venv)) {
    C:/Python314/python.exe -m venv .venv
}

# activate venv
.\.venv\Scripts\Activate

# upgrade pip
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt

# run server
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
