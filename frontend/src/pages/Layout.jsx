import React from 'react'; 
import { useAuth } from '../contexts/AuthContext'; 
import { Toaster } from 'react-hot-toast'; 
 
const Layout = ({ children }) => 
  const { logout } = useAuth(); 
 
  return ( 
      {/* Sidebar */} 
            {/* Adicione mais links de navega‡Æo aqui */} 
 
      {/* Main Content */} 
        {/* Header */} 
          {/* Adicione informa‡äes do usu rio ou outras a‡äes aqui */} 
 
        {/* Page Content */} 
          {children} 
  ); 
}; 
 
export default Layout; 
