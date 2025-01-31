import React, { useEffect, useState } from "react";

function App() {
  const [family, setFamily] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/family")
      .then((response) => response.json())
      .then((data) => setFamily(data));
  }, []);

  return (
    <div>
      <h1>Family Tree</h1>
      <ul>
        {family.map((member) => (
          <li key={member.id}>{member.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
