import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState("");
  const [error, setError] = useState();
  const [counter, setCounter] = useState(0);

  useEffect(() => {
    // Function to fetch data
    const fetchData = async () => {
      try {
        const response = await fetch(import.meta.env.VITE_URL);
        const data = await response.json();
        setData(data.message);
      } catch (error) {
        setError('Error fetching dataa');
      }
    };

    // Fetch data initially
    fetchData();

    // Set up interval to fetch data every 5 seconds
    const intervalId = setInterval(() => {
      fetchData();
      setCounter(counter +1 )
    }, 5000);

    // Cleanup on component unmount
    return () => {
      clearInterval(intervalId);
    };
  }, [counter]);

  console.log("here")

  return (
    <>
      <h1>hello world</h1>
      <h4>{data}</h4>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p>{counter}</p>
      <button onClick={() => setCounter(counter + 1)}>+</button>
    </>
  );
}

export default App;
