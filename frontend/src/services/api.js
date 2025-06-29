import axios from 'axios';

const api = axios.create({
  baseURL: baseURL: 'https://nr7-production.up.railway.app'
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
