// Gruntfile.js
module.exports = function(grunt) {
    grunt.initConfig({
        // Watch task config
        watch: {
            sass: {
                files: "sass/*.scss",
                files: "sass/*.sass",
                tasks: ['sass']
            }
        },
        // SASS task config
        sass: {
            dev: {
                files: {
                    // destination        // source file
                    "public/css/styles.css": "sass/material_styles.scss",
                    "public/css/materialize.css": "bower_components/materialize/sass/materialize.scss"
                }
            }
        },
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
};