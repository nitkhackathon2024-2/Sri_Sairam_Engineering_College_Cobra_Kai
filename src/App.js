import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setResult(response.data.extracted_text);
    } catch (error) {
      console.error('Error uploading file:', error);
      setResult('Error uploading file');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Document Processing App</h1>
        <form onSubmit={handleSubmit}>
          <input className="button1" type="file" onChange={handleFileChange} />
          <button type="submit">Upload</button>
        </form>
        {result && (
          <div className="Result">
            <h2>Extracted Text</h2>
            <pre>{result}</pre>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;