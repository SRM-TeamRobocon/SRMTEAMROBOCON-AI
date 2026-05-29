# RAG Chat Frontend

React + Vite chat UI for the RAG demo.

## Setup

```bash
npm install
npm run dev
```

## Environment

By default the app talks to:

```text
http://localhost:8000
```

Override it with:

```bash
VITE_API_BASE_URL=http://your-backend-host:8000
```

## Build

```bash
npm run build
npm run lint
```

## Behavior

- Full-screen chat interface
- Sharp corners
- Minimal black theme
- Messages are sent to `POST /api/query`
