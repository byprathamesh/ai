import { useState } from "react";

// Use environment variable for backend API URL, fallback to relative path for local dev
const API_URL = process.env.NEXT_PUBLIC_API_URL || "";
const MAX_FILE_SIZE_MB = 5;
const ALLOWED_TYPES = ["application/pdf", "image/jpeg", "image/png"];

export default function Home() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    setResult(null);
    setError("");
    if (!selected) return;
    if (!ALLOWED_TYPES.includes(selected.type)) {
      setError("Invalid file type. Please upload a PDF or image file.");
      setFile(null);
      return;
    }
    if (selected.size > MAX_FILE_SIZE_MB * 1024 * 1024) {
      setError(`File is too large. Max size is ${MAX_FILE_SIZE_MB}MB.`);
      setFile(null);
      return;
    }
    setFile(selected);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError("");
    if (!file) {
      setError("Please select a file to upload.");
      return;
    }
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await fetch(`${API_URL}/extract`, {
        method: "POST",
        body: formData,
      });
      if (!res.ok) {
        throw new Error("Failed to get a valid response from the backend.");
      }
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message || "An unexpected error occurred.");
    }
    setLoading(false);
  };

  return (
    <main style={{ maxWidth: 500, margin: "auto", padding: 32 }}>
      <h1>Health Insurance Premium Checker</h1>
      {process.env.NODE_ENV === "production" && !process.env.NEXT_PUBLIC_API_URL && (
        <div style={{ color: "orange", marginBottom: 16 }}>
          Warning: Backend API URL is not set. Please configure NEXT_PUBLIC_API_URL.
        </div>
      )}
      <form onSubmit={handleSubmit} aria-label="Upload form">
        <input
          type="file"
          accept=".pdf,.jpg,.jpeg,.png"
          onChange={handleFileChange}
          aria-label="Select a PDF or image file"
        />
        <button type="submit" disabled={loading || !file} style={{ marginLeft: 8 }}>
          {loading ? "Checking..." : "Check Premium"}
        </button>
      </form>
      {loading && (
        <div role="status" aria-live="polite" style={{ marginTop: 16 }}>
          <span>Loading...</span>
        </div>
      )}
      {error && (
        <div style={{ color: "red", marginTop: 16 }} role="alert">
          Error: {error}
        </div>
      )}
      {result && !error && (
        <section style={{ marginTop: 32 }} aria-label="Results">
          <h2>Extracted Metrics</h2>
          <pre>{JSON.stringify(result.metrics, null, 2)}</pre>
          <h2>Result</h2>
          {result.result && result.result.eligible ? (
            <div>
              <p style={{ color: "green" }}>
                Eligible! Premium: ₹{result.result.premium.toFixed(2)}
              </p>
              <p>
                Market premium: ₹{result.result.market_premium.toFixed(2)}
                <br />
                You save: ₹{result.result.savings.toFixed(2)} compared to market rate.
              </p>
            </div>
          ) : (
            <p style={{ color: "red" }}>
              Ineligible: {result.result ? result.result.reason : "Unknown reason"}
            </p>
          )}
        </section>
      )}
    </main>
  );
} 