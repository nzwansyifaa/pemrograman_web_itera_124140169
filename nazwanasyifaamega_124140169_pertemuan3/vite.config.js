import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

// Konfigurasi Vite + Vitest (environment jsdom agar bisa menguji komponen React)
export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: "./src/setupTests.js",
  },
});
