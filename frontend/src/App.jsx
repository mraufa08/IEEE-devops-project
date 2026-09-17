import { useEffect, useState } from "react";

function App() {
  const [backendStatus, setBackendStatus] = useState("Checking...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((response) => response.json())
      .then((data) => {
        setBackendStatus(data.status);
      })
      .catch(() => {
        setBackendStatus("error");
      });
  }, []);

  return (
    <body bgcolor="darkblue">
    <div>
      <h1>IEEE DevOps Project</h1>

      <p>Frontend is running.</p>

      <p>
        Backend status: <strong>{backendStatus}</strong>
      </p>
    </div>
    </body>
  );
}

export default App;