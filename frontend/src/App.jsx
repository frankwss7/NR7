import React from 'react'; 
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; 
import { AuthProvider } from './contexts/AuthContext'; 
import ProtectedRoute from './components/ProtectedRoute'; 
import Login from './pages/Login'; 
import Dashboard from './pages/Dashboard'; 
import Layout from './components/Layout'; 
import './App.css'; 
 
function App() { 
  return ( 
            path="/dashboard" 
            element={ 
            } 
          {/* Adicione outras rotas protegidas aqui */} 
  ); 
} 
 
export default App; 
