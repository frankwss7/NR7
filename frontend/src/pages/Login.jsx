import { useState } from 'react';
import logo from '...frontend/src/assets/logo_app_psicossocial.png';


export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Login:', email, senha);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 to-blue-200 px-4">
      <div className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-md">
        <div className="flex flex-col items-center mb-6">
          <img src={logo} alt="Logo" className="w-24 h-24 mb-4 rounded-full shadow-md" />
          <h1 className="text-2xl font-bold text-gray-800">Acesse sua conta</h1>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          {/* inputs */}
        </form>
      </div>
    </div>
  );
}

