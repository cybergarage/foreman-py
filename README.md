![foreman_logo](doc/img/icon.png)

`foreman-py` is a client package for Foreman, and it has a command line tool, [`fql`](./doc/fql.md), which can execute the domain specific language of Foreman, [Foremqn Query Language](https://ghe.corp.yahoo.co.jp/nosql/foreman-doc/blob/master/dsl.md), easily.

## Setup

`foreman-py` is not packeged yet, and so get the package from the following git directly.
```
git clone https://ghe.corp.yahoo.co.jp/nosql/foreman-py.git
```

To run `foreman-py`, you have to the following modules on your Pyhton environment.

- requests

#### MacOSX

On MacOSX, type the following commands if you use the default Python package.

```
xcode-select --install
sudo easy_install requests
```

## Executing FQL

`foreman-py` is not packeged yet, and so use the following command to run it before running `foreman-py`.

```
cd foreman-py
source ./setenv
```

### Interactive Mode

To run the command utility, `fql`, interactive, type the following command.

```
./foreman/fql <host> <port>
```

`fql` tries to connect the local host with the default port when the arguments is not specified.

Using the interactive mode, you can send FQL commands to the connected host.

### Pipeline Mode

`fql` has two execution mode, the above interactive and pipeline mode.
Using the pipeline mode, you can send massive FQL commands at once.
To use the pipeline mode, send your FQL commands using Unix pipeline as the following.

```
cat <your FQL command file> | ./foreman/fql <host> <port>
```
