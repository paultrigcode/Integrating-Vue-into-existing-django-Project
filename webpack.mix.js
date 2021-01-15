const mix = require('laravel-mix');
const tailwindcss = require('tailwindcss')

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('resources/js/app.js', 'static/js/vue-app.js')
   .sass('resources/sass/app.scss', 'static/css/vue-app.css')
   // .combine(['node_modules/@fortawesome/fontawesome-free/css/all.css', 'static/css/vue-app.css'], 'static/css/vue-app.css')
   // .copyDirectory('node_modules/@fortawesome/fontawesome-free/webfonts', 'static/webfonts')
   .options({
      // processCssUrls: false,
      postCss: [ tailwindcss('tailwind.config.js') ],
   });
