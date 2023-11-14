/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "themes/aalmazan/**/*.html",
    "content/**/*.md",
    "output/**/*.html",
  ],
  darkMode: false,
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("daisyui")
  ],
  daisyui: {
    styled: true,
    themes: ["lofi", "dracula"],
    base: true,
    utils: true,
    logs: true,
    rtl: false,
    // prefix: "",
    darkTheme: false,
  },
};
