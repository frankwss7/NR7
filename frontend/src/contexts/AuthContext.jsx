import React, { createContext, useState, useEffect, useContext } from 'react'; 
import { useNavigate } from 'react-router-dom'; 
import api from '../services/api'; 
 
const AuthContext = createContext(); 
 
export const AuthProvider = ({ children }) =
  const [user, setUser] = useState(null); 
  const [loading, setLoading] = useState(true); 
  const navigate = useNavigate(); 
 
  useEffect(() =
    const token = localStorage.getItem('token'); 
    if (token) { 
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`; 
      // Aqui vocˆ faria uma chamada para validar o token e buscar os dados do usu rio 
      // Por simplicidade, vamos apenas definir um usu rio mock 
      setUser({ email: 'user@example.com' }); 
    } 
    setLoading(false); 
  }, []); 
 
  const login = async (email, password) =
    try { 
      const response = await api.post('/auth/login', { email, password }); 
      const { access_token } = response.data; 
      localStorage.setItem('token', access_token); 
      api.defaults.headers.common['Authorization'] = `Bearer ${access_token}`; 
      setUser({ email }); // Definir usu rio ap¢s login bem-sucedido 
      navigate('/dashboard'); 
    } catch (error) { 
      console.error('Login failed:', error); 
      throw error; 
    } 
  }; 
 
  const logout = () =
    localStorage.removeItem('token'); 
    delete api.defaults.headers.common['Authorization']; 
    setUser(null); 
    navigate('/login'); 
  }; 
 
  return ( 
      {children} 
  ); 
}; 
 
export const useAuth = () =
