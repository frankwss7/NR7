import React from 'react'; 
import { useAuth } from '../contexts/AuthContext'; 
 
const Dashboard = () => {
  const { user } = useAuth(); 
 
  return ( 
      {/* Adicione mais conte£do do dashboard aqui */} 
  ); 
}; 
 
export default Dashboard; 
