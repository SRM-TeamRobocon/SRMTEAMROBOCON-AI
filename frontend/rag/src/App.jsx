import { useState } from 'react'
import './App.css'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

function App() {
  const [query, setQuery] = useState('')
  const [response, setResponse] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  async function handleSubmit() {
    if (!query.trim()) {
      setResponse('Please enter a question.')
      return
    }

    setIsLoading(true)
    try {
      const res = await fetch(`${API_BASE_URL}/api/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      })

      const data = await res.json()

      setResponse(data.answer ?? 'No answer returned.')
    } catch (error) {
      console.error('Error:', error)
      setResponse('Something went wrong.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="app-container">
      <h1>RAG Chatbot</h1>

      <input
        type="text"
        placeholder="Ask something..."
        className="query-input"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button className="submit-button" onClick={handleSubmit} disabled={isLoading}>
        {isLoading ? 'Thinking...' : 'Submit'}
      </button>

      <div className="response-container">
        <p className="response-text">{response}</p>
      </div>
    </div>
  )
}

export default App
