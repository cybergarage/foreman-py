![foreman_logo](doc/img/icon.png)

`foreman-py` is a client package for Foreman, and it has a command line tool, [`fqlsh`](./doc/fql.md), which can execute the domain specific language of Foreman, [Foremqn Query Language](https://github.com/cybergarage/foreman-doc/blob/master/dsl.md), easily.

## Install

```bash
pip install foreman_client
```

## Executing FQL

### Interactive Mode

To run the command utility, `fql`, interactive, type the following command.

```bash
fqlsh [-h] [-H HOST] [-P PORT] [-E EXECUTE]
```

Example:

```bash
fqlsh -H foreman.ynwm.cybergarage.org -E 'SELECT * FROM ACTION'
```

`fqlsh` tries to connect the `localhost` with the default port (8188) when the arguments is not specified.

Using the interactive mode, you can send FQL commands to the connected host.

### Pipeline Mode

`fql` has two execution mode, the above interactive and pipeline mode.
Using the pipeline mode, you can send massive FQL commands at once.
To use the pipeline mode, send your FQL commands using Unix pipeline as the following.

```bash
fqlsh [-H HOST] [-P PORT] < <your FQL command file>
```
