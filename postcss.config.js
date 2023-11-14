const purgecss = require('@fullhuman/postcss-purgecss')
const cssnano = require("cssnano");

module.exports = {
  plugins: [
    require("postcss-import"),
    require("tailwindcss"),
    require("autoprefixer"),
    purgecss({
      content: [
        './themes/aalmazan/**/*.html',
        './content/**/*.md',
        './output/**/*.html',
      ]
    }),
    cssnano({preset: require("cssnano-preset-advanced")})
  ],
  variants: {
    extend: {},
  },
};