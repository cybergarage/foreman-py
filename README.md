# foreman-py

`foreman-py` is a client package for Foreman is a time series failure analysis utility.

## Installation

```
pip install foreman-py
```

### fql - The Foreman Command Line Tool

To run the command line tool as an interactive interpreter, type the command, `fql` without any parameter.

```
fql
```

To execute many FQL queries, run 'fql' as the following using UNIX pipeline.

```
echo "EXPORT CONFIG" | fql
```