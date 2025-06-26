import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react( )],
  esbuild: {
    target: 'esnext', // Suporte completo para ES6+
  },
  build: {
    target: 'esnext', // Target também para o build
  }
})
