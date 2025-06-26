import React from 'react'; 
import { Navigate } from 'react-router-dom'; 
import { useAuth } from '../contexts/AuthContext'; 
import LoadingSpinner from './LoadingSpinner'; 
 
const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth(); 
 
  if (loading) { 
  } 
 
  if (!user) { 
  } 
 
  return children; 
}; 
 
export default ProtectedRoute; 
