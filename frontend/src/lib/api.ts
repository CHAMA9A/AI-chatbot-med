const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export interface PredictResponse {
  disease: string;
  description: string;
  precautions: string[];
  matched_symptoms: string[];
  disclaimer: string;
}

export interface ApiError {
  detail: string;
}

export async function predictDisease(text: string): Promise<PredictResponse> {
  const res = await fetch(`${API_BASE}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  if (!res.ok) {
    const err: ApiError = await res.json().catch(() => ({
      detail: "An unexpected error occurred. Please try again.",
    }));
    throw new Error(err.detail);
  }

  return res.json();
}
