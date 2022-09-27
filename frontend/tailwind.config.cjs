/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        django: {
          100: '#fff',
          600: '#44B78B',
          700: '#25c488',
          900: '#0C3C26',
        }
      },
    }
  },
  plugins: [],
}
