import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './componets/Login';
import SignUp from './componets/SignUp';
import Layout from './componets/Layout';
import ImageGenerator from './componets/ImageGenerator';


const App = () => {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/imagegenerator" element={<ImageGenerator />} />
        </Routes>
      </Layout>
    </Router>
  );
};

export default App;
