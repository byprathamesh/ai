import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    const res = await fetch("/api/extract", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 500, margin: "auto", padding: 32 }}>
      <h1>Health Insurance Premium Checker</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".pdf,.jpg,.jpeg,.png" onChange={handleFileChange} />
        <button type="submit" disabled={loading || !file} style={{ marginLeft: 8 }}>
          {loading ? "Checking..." : "Check Premium"}
        </button>
      </form>
      {result && (
        <div style={{ marginTop: 32 }}>
          <h2>Extracted Metrics</h2>
          <pre>{JSON.stringify(result.metrics, null, 2)}</pre>
          <h2>Result</h2>
          {result.result.eligible ? (
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
            <p style={{ color: "red" }}>Ineligible: {result.result.reason}</p>
          )}
        </div>
      )}
    </div>
  );
} 