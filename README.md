# foreman-py

`foreman-py` is a client package for Foreman, and it has a command line tool, `fql`, which can executed the domain specific language, [Foremqn Query Language](https://github.com/cybergarage/foreman-doc/blob/master/dsl.md), easily.

### fql - The Foreman Command Line Tool

To run the command line tool as an interactive interpreter, type the command, `fql` without any parameter.

```
fql
```

To execute many FQL queries, run 'fql' as the following using UNIX pipeline.

```
echo "EXPORT CONFIG" | fql
```
