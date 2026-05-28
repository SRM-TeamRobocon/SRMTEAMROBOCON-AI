import { useEffect, useMemo, useRef, useState } from 'react'
import './App.css'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const THEME_KEY = 'rag-ui-theme'

const seedMessages = [
  {
    id: 1,
    role: 'assistant',
    content: 'Hi, I’m your RAG assistant. Ask me something from the uploaded documents.',
  },
]

function App() {
  const [messages, setMessages] = useState(seedMessages)
  const [query, setQuery] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [theme, setTheme] = useState(() => localStorage.getItem(THEME_KEY) || 'dark')
  const endOfMessagesRef = useRef(null)

  useEffect(() => {
    document.documentElement.dataset.theme = theme
    localStorage.setItem(THEME_KEY, theme)
  }, [theme])

  useEffect(() => {
    endOfMessagesRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading])

  const canSend = useMemo(() => query.trim().length > 0 && !isLoading, [query, isLoading])

  async function handleSubmit(event) {
    event?.preventDefault()
    if (!query.trim() || isLoading) return

    const userMessage = { id: Date.now(), role: 'user', content: query.trim() }
    const nextMessages = [...messages, userMessage]
    setMessages(nextMessages)
    setQuery('')
    setIsLoading(true)

    try {
      const res = await fetch(`${API_BASE_URL}/api/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userMessage.content }),
      })

      const data = await res.json()
      setMessages((current) => [
        ...current,
        {
          id: Date.now() + 1,
          role: 'assistant',
          content: data.answer ?? 'No answer returned.',
        },
      ])
    } catch (error) {
      console.error('Error:', error)
      setMessages((current) => [
        ...current,
        {
          id: Date.now() + 1,
          role: 'assistant',
          content: 'Something went wrong while contacting the backend.',
        },
      ])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="app-shell">
      <section className="chat-card">
        <header className="chat-header">
          <div>
            <p className="eyebrow">RAG Chat</p>
            <h1>Document assistant</h1>
          </div>
          <button
            type="button"
            className="theme-toggle"
            onClick={() => setTheme((current) => (current === 'dark' ? 'light' : 'dark'))}
            aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
          >
            {theme === 'dark' ? 'Light mode' : 'Dark mode'}
          </button>
        </header>

        <div className="chat-body">
          <div className="messages" aria-live="polite">
            {messages.map((message) => (
              <article key={message.id} className={`message ${message.role}`}>
                <div className="message-label">{message.role === 'user' ? 'You' : 'Assistant'}</div>
                <p>{message.content}</p>
              </article>
            ))}
            {isLoading && (
              <article className="message assistant">
                <div className="message-label">Assistant</div>
                <p>Thinking...</p>
              </article>
            )}
            <div ref={endOfMessagesRef} />
          </div>

          <form className="composer" onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Ask a question about your documents..."
              className="query-input"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              aria-label="Message input"
            />
            <button className="submit-button" type="submit" disabled={!canSend}>
              {isLoading ? 'Sending...' : 'Send'}
            </button>
          </form>
        </div>
      </section>
    </main>
  )
}

export default App
