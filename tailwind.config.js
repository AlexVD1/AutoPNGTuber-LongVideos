/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          yellow: "#FFE600",
          blue: "#38BDF8",
          dark: "#0F172A",
          accent: "#F43F5E",
        },
      },
    },
  },
  plugins: [],
};
