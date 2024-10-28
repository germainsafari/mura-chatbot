// frontend/src/components/Chatbox.js
import React, { useState } from 'react';
import axios from 'axios';

function Chatbox() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  
  const handleSendMessage = async () => {
    const token = localStorage.getItem('token');
    const result = await axios.post('http://localhost:5000/api/chat/send', { message }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setResponse(result.data.response);
    setMessage('');  // Clear input field
  };

  return (
    <div>
      <h2>Chat with AI</h2>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message here"
      />
      <button onClick={handleSendMessage}>Send</button>
      <div>
        <h3>Response:</h3>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default Chatbox;
