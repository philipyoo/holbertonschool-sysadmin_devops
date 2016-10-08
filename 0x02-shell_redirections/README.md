#Shell I/O Redirection Exercises

NOTE: Why does the following happen?

### list all files/directories in current working directory and all sub-directories

vagrant@vagrant-ubuntu-trusty-64:~/philip$ ls -laR
.:
total 16
drwxrwxr-x 4 vagrant vagrant 4096 Oct  8 00:00 .
drwxr-xr-x 7 vagrant vagrant 4096 Oct  6 19:34 ..
-rw-rw-r-- 1 vagrant vagrant    0 Oct  7 23:07 10-no_more_js
-rw-rw-r-- 1 vagrant vagrant    0 Oct  8 00:00 a.js
drwxrwxr-x 3 vagrant vagrant 4096 Oct  8 00:00 dir1
drwxrwxr-x 2 vagrant vagrant 4096 Oct  8 00:00 dir.js
-rw-rw-r-- 1 vagrant vagrant    0 Oct  6 21:21 .gitignore
-rw-rw-r-- 1 vagrant vagrant    0 Oct  7 23:07 hello
-rw-rw-r-- 1 vagrant vagrant    0 Oct  7 23:07 iacta
-rw-rw-r-- 1 vagrant vagrant    0 Oct  7 23:07 ls_cwd_content

./dir1:
total 12
drwxrwxr-x 3 vagrant vagrant 4096 Oct  8 00:00 .
drwxrwxr-x 4 vagrant vagrant 4096 Oct  8 00:00 ..
drwxrwxr-x 3 vagrant vagrant 4096 Oct  8 00:00 acedir
-rw-rw-r-- 1 vagrant vagrant    0 Oct  8 00:00 b.js
-rw-rw-r-- 1 vagrant vagrant    0 Oct  7 23:39 hello

./dir1/acedir:
total 12
drwxrwxr-x 3 vagrant vagrant 4096 Oct  8 00:00 .
drwxrwxr-x 3 vagrant vagrant 4096 Oct  8 00:00 ..
-rw-rw-r-- 1 vagrant vagrant    0 Oct  8 00:00 c.js
drwxrwxr-x 2 vagrant vagrant 4096 Oct  7 23:58 hi

./dir1/acedir/hi:
total 8
drwxrwxr-x 2 vagrant vagrant 4096 Oct  7 23:58 .
drwxrwxr-x 3 vagrant vagrant 4096 Oct  8 00:00 ..

./dir.js:
total 8
drwxrwxr-x 2 vagrant vagrant 4096 Oct  8 00:00 .
drwxrwxr-x 4 vagrant vagrant 4096 Oct  8 00:00 ..
-rw-rw-r-- 1 vagrant vagrant    0 Oct  8 00:00 d.js


### Attempt 1 - When piping commands, I need to explicitly add quotations around `*.js` and I get the output I want.
vagrant@vagrant-ubuntu-trusty-64:~/philip$ ls -laR . | find -name '*.js' -type 'f' | wc -l
4

### Attempt 2 - Without the quotations...
vagrant@vagrant-ubuntu-trusty-64:~/philip$ ls -laR | find -name *.js -type f | wc -l
find: paths must precede expression: dir.js
Usage: find [-H] [-L] [-P] [-Olevel] [-D help|tree|search|stat|rates|opt|exec] [path...] [expression]
0

### However, if I just did:
$ find -name *.js -type f | wc -l
This works and returns the output I look for. I guess the extra `ls` command is unneccessary, but am curious why the quotations matter only in certain cases.


----

### For exercise 12, `wc -l` returns 10 results, but when running the script, I can only count 9. Need to double check this.