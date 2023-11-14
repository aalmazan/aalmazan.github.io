/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "themes/aalmazan-tw/**/*.html",
    "content/**/*.md",
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
