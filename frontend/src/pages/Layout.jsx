import React from 'react'; 
import { useAuth } from '../contexts/AuthContext'; 
import { Toaster } from 'react-hot-toast'; 
 
const Layout = ({ children }) =
  const { logout } = useAuth(); 
 
  return ( 
      {/* Sidebar */} 
            {/* Adicione mais links de navega��o aqui */} 
 
      {/* Main Content */} 
        {/* Header */} 
          {/* Adicione informa��es do usu�rio ou outras a��es aqui */} 
 
        {/* Page Content */} 
          {children} 
  ); 
}; 
 
export default Layout; 
