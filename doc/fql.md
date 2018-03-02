# fql - The Foreman Command Line Tool

To run the command line tool as an interactive interpreter, type the command, `fql` without any parameter.

```
fql
```

To execute many FQL queries, run 'fql' as the following using UNIX pipeline.

```
echo "EXPORT CONFIG" | fql
```