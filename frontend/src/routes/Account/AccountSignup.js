import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Typography, TextField, Button, FormControlLabel, Checkbox } from '@mui/material';

const AccountSignup = () => {
    // State variables to store form input values
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [dob, setDob] = useState('');
    const [isStaff, setIsStaff] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const navigate = useNavigate();
    // Add other fields as needed

  // Add any additional form fields as needed

  // Event handler for form submission
     const handleSignup = async (e) => {
      e.preventDefault();

      try {
        const username = email;
        // Make a POST request to your Django backend endpoint for signup
        const response = await axios.post('http://localhost:8000/api-auth/register', {
          first_name: firstName,
          last_name: lastName,
          email,
          password,
          dob,
          is_staff: isStaff,
          username,
          // Include other required fields and any additional form data needed for signup
        });

        // Handle the response from the backend as needed
        if (response.status === 201) {
            // Signup successful, redirect to login page
            setSuccessMessage('Signup successful. Redirecting to login page...');
            setTimeout(() => {
              // Redirect logic here
              navigate('/account/login');
            }, 3000);
          } else {
            // Unexpected response status, show error message
            setErrorMessage('Cannot complete this action at the moment. Please try again later.');
          }
      } catch (error) {
        // Handle any errors from the backend
        if (error.response && error.response.status === 400) {
            setErrorMessage('A user with the provided email already exists.');
          } else {
            setErrorMessage('Cannot complete this action at the moment. Please try again later.');
          }
      }
    };
      return (
      <div>
        <Typography variant="h4">Sign Up</Typography>
        <form onSubmit={handleSignup}>
          <TextField
            label="First Name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Last Name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            fullWidth
            margin="normal"
            required
          />
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
          <TextField
            label="Date of Birth"
            type="date"
            value={dob}
            onChange={(e) => setDob(e.target.value)}
            fullWidth
            margin="normal"
            required
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={isStaff}
                onChange={(e) => setIsStaff(e.target.checked)}
              />
            }
            label="Is Staff"
          />
          {/* Add other form fields as needed */}
          {/* Show error message if there is one */}
          {errorMessage && <div>{errorMessage}</div>}
          {/* Show success message if there is one */}
          {successMessage && <div>{successMessage}</div>}
          <Button type="submit" variant="contained" color="primary">
            Sign Up
          </Button>
        </form>
      </div>
    );
};

export default AccountSignup;
