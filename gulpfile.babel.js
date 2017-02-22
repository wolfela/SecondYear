'use strict';

import gulp from 'gulp';
import babelify from 'babelify';
import browserify from 'browserify';
import foreach from 'gulp-foreach';
import gulpif from 'gulp-if';
import merge from 'gulp-merge';
import sass from 'gulp-sass';
import source from 'vinyl-source-stream';
import sourcemaps from 'gulp-sourcemaps';
import util from 'gulp-util';

const dirs = {
    scssSrc: 'scss',
    jsSrc: 'js',
    dest: 'static'
};

const scssPaths = {
    srcs: [
        `${dirs.scssSrc}/student-app.scss`,
        `${dirs.scssSrc}/teacher-app.scss`,
        `${dirs.scssSrc}/app.scss`,
		`${dirs.scssSrc}/mcq.scss`
    ],
    dest: `${dirs.dest}/css`
};

const jsPaths = {
    srcs: [
        `${dirs.jsSrc}/student-app.js`,
        `${dirs.jsSrc}/teacher-app.js`
    ],
    dest: `${dirs.dest}` // For some reason vinyl-source-stream will prepend /js to the final output path
};

gulp.task('scss', () => {
    return gulp.src(scssPaths.srcs)
        .pipe(foreach(function(stream, file) {
            return stream
                .pipe(gulpif(!util.env.production, sourcemaps.init()))
                .pipe(sass.sync({
                    outputStyle: (util.env.production) ? 'compressed' : 'nested',
                    includePaths: ['./node_modules/foundation-sites/scss','./node_modules/motion-ui/src']
                }).on('error', sass.logError))
                .pipe(gulpif(!util.env.production, sourcemaps.write('.')))
                .pipe(gulp.dest(scssPaths.dest))
        }))
        .pipe(gulp.dest(scssPaths.dest));
});

gulp.task('js', () => {
    let seq = merge();
    for (let file of jsPaths.srcs) {
        let bundleStream = browserify(file).transform(babelify).bundle();

        bundleStream
            .pipe(source(file))
            .pipe(gulp.dest(jsPaths.dest));
        seq.add(bundleStream)
    }

    return seq
});
gulp.task('watch', () => {
    gulp.watch(`${dirs.scssSrc}/**/*.scss`, ['scss']);
    gulp.watch(`${dirs.jsSrc}/**/*.js`, ['js']);
});

gulp.task('default', () => {
    gulp.start('scss', 'js');
});
