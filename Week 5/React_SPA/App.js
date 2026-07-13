import React, { useState, useEffect } from "react";
import { Routes, Route, Link } from "react-router-dom";

function Home() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Home</h2>
      <p>Counter: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </div>
  );
}

function About() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    setMessage("Welcome to React!");
  }, []);

  return (
    <div>
      <h2>About</h2>
      <p>{message}</p>
    </div>
  );
}

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>React SPA Demo</h1>

      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/about">About</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  );
}

export default App;
