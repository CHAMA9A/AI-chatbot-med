import type { PredictResponse } from "../lib/api";

interface ResultCardProps {
  result: PredictResponse;
}

export default function ResultCard({ result }: ResultCardProps) {
  return (
    <div className="bg-white border border-blue-100 rounded-xl shadow-sm overflow-hidden">
      {/* Disease header */}
      <div className="bg-gradient-to-r from-blue-500 to-blue-600 px-5 py-3">
        <h3 className="text-white font-semibold text-lg">{result.disease}</h3>
      </div>

      <div className="p-5 space-y-4">
        {/* Description */}
        <div>
          <h4 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-1">
            Description
          </h4>
          <p className="text-gray-700 text-sm leading-relaxed">
            {result.description}
          </p>
        </div>

        {/* Precautions */}
        {result.precautions.length > 0 && (
          <div>
            <h4 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-2">
              Recommended Precautions
            </h4>
            <ul className="space-y-1">
              {result.precautions.map((p, i) => (
                <li key={i} className="flex items-start gap-2 text-sm text-gray-700">
                  <span className="text-blue-500 mt-0.5">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </span>
                  <span className="capitalize">{p}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Matched symptoms */}
        <div>
          <h4 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-2">
            Detected Symptoms
          </h4>
          <div className="flex flex-wrap gap-2">
            {result.matched_symptoms.map((s, i) => (
              <span
                key={i}
                className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-blue-50 text-blue-700 border border-blue-200"
              >
                {s}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
