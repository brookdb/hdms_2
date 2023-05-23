import React, { useState } from 'react';
import axios from 'axios';
import { Typography, TextField, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const AccountLogin = () => {
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api-auth/login', {
        email,
        password,
      });

      if (response.status === 200) {
        const token = response.data.token;
        // Save the token to local storage
        localStorage.setItem('token', token);

        // Redirect to the desired page
        navigate('/dashboard');
      } else {
        // Handle other response statuses as needed

      }
    } catch (error) {
      setErrorMessage('Invalid email or password. Please try again.');
    }
  };

  return (
    <div>
      <Typography variant="h4">Log In</Typography>
      {errorMessage && <p>{errorMessage}</p>}
      <form onSubmit={handleLogin}>
        <TextField
          label="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          fullWidth
          margin="normal"
          required
        />
        <TextField
          label="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          fullWidth
          margin="normal"
          required
        />
        <Button type="submit" variant="contained" color="primary">
          Log In
        </Button>
      </form>
    </div>
  );
};

export default AccountLogin;