# AI Healthcare Chatbot

A production-grade full-stack AI chatbot that predicts diseases from symptom descriptions. Built with FastAPI, React, TypeScript, and Tailwind CSS.

> **Disclaimer:** This tool is for educational purposes only and does NOT provide medical advice. Always consult a qualified healthcare professional.

## Architecture

```
├── backend/          # FastAPI Python backend
│   ├── app/
│   │   ├── main.py              # FastAPI app + lifespan
│   │   ├── api/routes.py        # API endpoints
│   │   ├── core/config.py       # Settings via env vars
│   │   ├── services/
│   │   │   ├── predictor.py     # ML model loading + prediction
│   │   │   ├── symptoms.py      # Symptom extraction from text
│   │   │   └── knowledge_base.py # Disease descriptions + precautions
│   │   ├── schemas.py           # Pydantic request/response models
│   │   └── utils/logging.py     # Structured logging
│   ├── data/                    # CSV data files + model.pkl
│   ├── tests/                   # Pytest test suite
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/         # React + TypeScript + Tailwind
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat.tsx         # Chat interface
│   │   │   ├── MessageBubble.tsx # Message display
│   │   │   └── ResultCard.tsx   # Disease result card
│   │   ├── lib/api.ts           # API client
│   │   └── pages/Home.tsx       # Main page
│   ├── Dockerfile
│   └── nginx.conf
└── docker-compose.yml
```

## Quick Start (Local)

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Backend runs at http://localhost:8000. API docs at http://localhost:8000/docs.

### Frontend

```bash
cd frontend
npm install   # or bun install
npm run dev   # or bun run dev
```

Frontend runs at http://localhost:3000.

## Quick Start (Docker)

```bash
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## API Reference

### Health Check

```bash
curl http://localhost:8000/health
```

Response:
```json
{ "status": "ok", "version": "1.0.0" }
```

### Predict Disease

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I have itching and skin rash"}'
```

Response:
```json
{
  "disease": "Fungal infection",
  "description": "...",
  "precautions": ["bath twice", "use detol or neem in bathing water", "keep infected area dry", "use clean cloths"],
  "matched_symptoms": ["itching", "skin rash"],
  "disclaimer": "This tool is for educational purposes only..."
}
```

### Error (no symptoms detected)

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'
```

Response (422):
```json
{
  "detail": "No recognizable symptoms found in your input. Try describing specific symptoms like: headache, fever, cough, fatigue, nausea, skin rash, etc."
}
```

## Running Tests

```bash
cd backend
python -m pytest tests/ -v
```

## Tech Stack

- **Backend:** Python 3.11, FastAPI, scikit-learn (DecisionTree), Pandas
- **Frontend:** React 19, TypeScript, Tailwind CSS 4, Vite
- **Deployment:** Docker, docker-compose, Nginx

## Screenshots

<!-- Add screenshots here -->
