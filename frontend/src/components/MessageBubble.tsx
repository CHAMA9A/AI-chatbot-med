import type { PredictResponse } from "../lib/api";
import ResultCard from "./ResultCard";

export type Message =
  | { role: "user"; text: string }
  | { role: "assistant"; result: PredictResponse }
  | { role: "error"; text: string };

interface MessageBubbleProps {
  message: Message;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  if (message.role === "user") {
    return (
      <div className="flex justify-end">
        <div className="max-w-[80%] bg-blue-500 text-white px-4 py-3 rounded-2xl rounded-br-md shadow-sm">
          <p className="text-sm">{message.text}</p>
        </div>
      </div>
    );
  }

  if (message.role === "error") {
    return (
      <div className="flex justify-start">
        <div className="max-w-[80%] bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-2xl rounded-bl-md shadow-sm">
          <p className="text-sm">{message.text}</p>
        </div>
      </div>
    );
  }

  // Assistant result
  return (
    <div className="flex justify-start">
      <div className="max-w-[85%]">
        <ResultCard result={message.result} />
      </div>
    </div>
  );
}
