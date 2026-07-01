import React, { useEffect, useState } from "react";

function User() {
  const [user, setUser] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://api.example.com/user")
      .then((res) => res.json())
      .then((data) => {
        setUser(data.name);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return <h2>{user}</h2>;
}

export default User;
