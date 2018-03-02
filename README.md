# foreman-py

`foreman-py` is a client package for Foreman, and it has a command line tool, `fql`, which can execute the domain specific language of Foreman, [Foremqn Query Language](https://ghe.corp.yahoo.co.jp/nosql/foreman-doc/blob/master/dsl.md), easily.

### fql - The Foreman Command Line Tool

To run the command line tool as an interactive interpreter, type the command, `fql` without any parameter.

```
$ fql
Foreman v0.5.5 (localhost:8080)
shell> 
```

To execute many FQL queries, run 'fql' as the following using UNIX pipeline.

```
$ echo "EXPORT CONFIG" | fql

or

$ cat foo.fql | fql
```
