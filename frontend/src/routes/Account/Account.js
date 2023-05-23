import React from 'react';
import { Route, Routes } from 'react-router-dom';
import AccountLogin from './AccountLogin';
import AccountSignup from './AccountSignup';
import AccountProfile from './AccountProfile';

const Account = () => {
  return (
    <div>
      <h2>Account Management</h2>
      <Routes>
        <Route path="/login" element={<AccountLogin />} />
        <Route path="/signup" element={<AccountSignup />} />
        <Route path="/profile" element={<AccountProfile />} />
      </Routes>
    </div>
  );
};

export default Account;