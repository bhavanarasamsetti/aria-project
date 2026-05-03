# Quick Setup for IBM watsonx.ai Integration

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 2. Configure API
```bash
cp .env.example .env
```

Edit `.env`:
```
WATSONX_API_KEY=your_actual_api_key
WATSONX_PROJECT_ID=your_actual_project_id
USE_WATSONX_API=true
```

## 3. Run
```bash
# Test analyzer
python src/analyzer.py

# Start backend
cd backend
uvicorn main:app --reload
```

## Mock Mode (No API)
Set in `.env`:
```
USE_WATSONX_API=false