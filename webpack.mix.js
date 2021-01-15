
const mix = require('laravel-mix'); 

mix.js('resources/js/app.js', 'assets/js/vue-app.js')
    .sass('resources/sass/app.scss', 'assets/css/vue-app.css');




    