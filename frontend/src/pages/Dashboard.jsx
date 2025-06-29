import React from 'react';
import { useAuth } from '../contexts/AuthContext';

const Dashboard = () => {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-indigo-100 to-blue-200 px-4">
      <div className="w-full max-w-xl bg-white p-8 rounded-2xl shadow-xl text-center">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">
          Bem-vindo, {user?.name || 'Usuário'}!
        </h1>
        <p className="text-gray-600 mb-8">
          Você está logado com sucesso na plataforma NR7.
        </p>
        <button
          onClick={logout}
          className="bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-6 rounded-md transition duration-200"
        >
          Sair
        </button>
      </div>
    </div>
  );
};

export default Dashboard;
