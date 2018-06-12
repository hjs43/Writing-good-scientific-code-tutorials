git-bisect-sample
=================

Sample code to demo 'git bisect'

Use it if you want illustrate how `git bisect` works.

The code contains five different commits.
The third commit introduces a bug that breaks the unit tests.
The purpose of the demo is to identify this commit as the buggy thanks to `git-bisect`.


The code is made of a function to compute Fibonacci numbers and corresponding unit tests.


Howto run the demo
==================

- `git bisect start`
- `git bisect bad`: the unit tests fail on the last commit
- `git bisect good HEAD~4` : the unit tests pass on the first commit
- `python test_fibo.py`: unit tests fail on the commit proposed by `git bisect`
- `git bisect bad`: mark current commit as bad
- `python test_fibo.py`: unit tests pass on the commit proposed by `git bisect`
- now git bisect has identified the last commit as the first buggy one.
- `git bisect reset`: stop bisection


Resources
=========
- http://git-scm.com/book/en/Git-Tools-Debugging-with-Git
- http://git-scm.com/docs/git-bisect



