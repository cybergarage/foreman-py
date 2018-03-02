# fql - The Foreman Command Line Tool

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
