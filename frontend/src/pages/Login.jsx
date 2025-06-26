import React, { useState } from 'react'; 
import { useAuth } from '../contexts/AuthContext'; 
import { useNavigate } from 'react-router-dom'; 
import { toast } from 'react-hot-toast'; 
 
const Login = () =
  const [email, setEmail] = useState(''); 
  const [password, setPassword] = useState(''); 
  const { login } = useAuth(); 
  const navigate = useNavigate(); 
 
  const handleSubmit = async (e) =
    e.preventDefault(); 
    try { 
      await login(email, password); 
      toast.success('Login bem-sucedido!'); 
      navigate('/dashboard'); 
    } catch (error) { 
      toast.error('Erro ao fazer login. Verifique suas credenciais.'); 
      console.error('Login error:', error); 
    } 
  }; 
 
  return ( 
              Email: 
              type="email" 
              id="email" 
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
              value={email} 
              onChange={(e) =
              required 
              Senha: 
              type="password" 
              id="password" 
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" 
              value={password} 
              onChange={(e) =
              required 
              type="submit" 
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" 
              Entrar 
  ); 
}; 
 
export default Login; 
