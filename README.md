# RAG Practice

Frontend chat UI for a Retrieval-Augmented Generation demo.

## What it does

- Full-screen chat interface built with React + Vite
- Sends user questions to a backend at `POST /api/query`
- Displays assistant responses in a simple message thread
- Uses a black, high-contrast visual theme with sharp corners

## Project Layout

- `frontend/rag` - React/Vite app
- `frontend/rag/src/App.jsx` - main chat UI
- `frontend/rag/src/App.css` - chat layout and styling
- `frontend/rag/src/index.css` - global theme and font setup

## Run It

```bash
cd frontend/rag
npm install
npm run dev
```

## Backend

The frontend expects a backend at `http://localhost:8000` by default.

Set a different API URL with:

```bash
VITE_API_BASE_URL=http://your-backend-host:8000
```

## Notes

- The chat input is sent to `/api/query`
- The UI is intentionally minimal and full-screen
- Corners are sharp, not rounded
