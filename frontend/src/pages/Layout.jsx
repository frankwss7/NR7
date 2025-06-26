import React from 'react';
import { useAuth } from '../contexts/AuthContext';
import { Toaster } from 'react-hot-toast';

const Layout = ({ children }) => {
  const { logout } = useAuth();

  return (
    <div className="layout">
      {/* Sidebar */}
      {/* Adicione mais links de navegação aqui */}

      {/* Main Content */}
      <header>
        {/* Adicione informações do usuário ou outras ações aqui */}
      </header>

      <main>
        {children}
      </main>

      <Toaster />
    </div>
  );
};

export default Layout;

