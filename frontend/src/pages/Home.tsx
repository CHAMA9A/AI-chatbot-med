import Chat from "../components/Chat";

export default function Home() {
  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-3xl mx-auto px-4 py-3 flex items-center gap-3">
          <div className="w-9 h-9 bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
            <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.26 10.147a60.438 60.438 0 0 0-.491 6.347A48.62 48.62 0 0 1 12 20.904a48.62 48.62 0 0 1 8.232-4.41 60.46 60.46 0 0 0-.491-6.347m-15.482 0a50.636 50.636 0 0 0-2.658-.813A59.906 59.906 0 0 1 12 3.493a59.903 59.903 0 0 1 10.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0 1 12 13.489a50.702 50.702 0 0 1 7.74-3.342" />
            </svg>
          </div>
          <div>
            <h1 className="text-lg font-semibold text-gray-900">HealthAI</h1>
            <p className="text-xs text-gray-500">Symptom Analysis Assistant</p>
          </div>
        </div>
      </header>

      {/* Disclaimer banner */}
      <div className="bg-amber-50 border-b border-amber-200 px-4 py-2">
        <p className="text-xs text-amber-700 text-center max-w-3xl mx-auto">
          <strong>Disclaimer:</strong> Educational only — not medical advice. Always consult a qualified healthcare professional.
        </p>
      </div>

      {/* Chat area */}
      <main className="flex-1 overflow-hidden max-w-3xl mx-auto w-full">
        <Chat />
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 py-2 px-4">
        <p className="text-xs text-gray-400 text-center">
          HealthAI v1.0 — For educational purposes only
        </p>
      </footer>
    </div>
  );
}
