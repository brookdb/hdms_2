import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import MainNav from './components/MainNav';
import Account from './routes/Account/Account';

const Home = () => {
  return <div>Home component</div>;
};

const Dashboard = () => {
  return <div>Dashboard component</div>;
};

const App = () => {
  return (
    <Router>
      <MainNav />
      <Routes>
        <Route path="/account/*" element={<Account />} />
        <Route path="/dashboard" component={Dashboard} />
        <Route exact path="/" element={<Home />} />
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;
