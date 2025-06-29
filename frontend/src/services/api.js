import axios from 'axios';

const api = axios.create({
  baseURL: 'https://nr7-backend-production.up.railway.app', // substitua pela sua URL real
});

// Interceptor para incluir o token automaticamente em cada requisição
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
