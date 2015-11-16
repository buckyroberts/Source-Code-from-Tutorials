module.exports = function(grunt) {

    grunt.initConfig({

        pkg: grunt.file.readJSON('package.json'),
        cssmin: {
            combine: {
                files: {
                    'html/css/main.css': ['html/css/content.css', 'html/css/sidebar.css']
                }
            }
        },
        uglify: {
            dist: {
                files: {
                    'html/js/toggle.min.js': ['html/js/toggle.js']
                }
            }
        }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    // Do the tasks
    grunt.registerTask('default', ['cssmin', 'uglify']);

};