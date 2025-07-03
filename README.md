# hello-world-project-template-python

This is the Hello World project which has all the basic files explained in our [Hello World Tutorial](https://learn.temporal.io/getting_started/python/hello_world_in_python//).

## Instructions

Ensure you have Python 3.7 or later installed locally, and that you have Docker installed to run the Temporal Cluster.

Clone this repository:

```bash
git clone https://github.com/temporalio/hello-world-project-template-python
```

Switch to the cloned directory:

```bash
hello-world-project-template-python
```

Create a virtual environment for your project and install the Temporal SDK:

```bash
python3 -m venv env
source env/bin/activate
python -m pip install temporalio pytest pytest-asyncio
```

The fastest way to get a development cluster running on your local machine is to use [Temporal CLI](https://docs.temporal.io/cli).

Temporal CLI is a tool for interacting with a Temporal Cluster from the command-line interface, but it includes a self-contained distribution of the Temporal Server and [Web UI](https://docs.temporal.io/web-ui) as well.

Install Temporal CLI on your local machine using the following instructions for your platform.

###  MacOS:

You can install the latest stable version with [Homebrew](https://brew.sh/) using the following command:

```brew install temporal```

You can also install Temporal CLI using the [installation script](https://temporal.download/cli.sh). Review the script and then download and install Temporal CLI with the following command:

```curl -sSf https://temporal.download/cli.sh | sh```

To manually install Temporal CLI, download the version for your architecture:

*  [Download Temporal CLI for Intel Macs](https://temporal.download/cli/archive/latest?platform=darwin&arch=amd64)
*  [Download Temporal CLI for Apple Silicon Macs](https://temporal.download/cli/archive/latest?platform=darwin&arch=arm64)

Once you've downloaded the file, extract the downloaded archive and add the ```temporal``` binary to your ```PATH``` by copying it to a directory like ```/usr/local/bin```.

### Windows

To install Temporal CLI on Windows, download the version for your architecture:

* [Download Temporal CLI for Windows amd64](https://temporal.download/cli/archive/latest?platform=windows&arch=amd64)
* [Download Temporal CLI for Windows arm64](https://temporal.download/cli/archive/latest?platform=windows&arch=arm64)

Once you've downloaded the file, extract the downloaded archive and add the ```temporal.exe``` binary to your ```PATH```.

### Linux

Install Temporal CLI using the [installation script](https://temporal.download/cli.sh). Review the script and then download and install Temporal CLI with the following command:

```curl -sSf https://temporal.download/cli.sh | sh```

To manually install Temporal CLI, download the version for your architecture

*  [Download Temporal CLI for Linux amd64](https://temporal.download/cli/archive/latest?platform=linux&arch=amd64)
*  [Download Temporal CLI for Linux arm64](https://temporal.download/cli/archive/latest?platform=linux&arch=arm64)

Once you've downloaded the file, extract the downloaded archive and add the ```temporal``` binary to your ```PATH``` by copying it to a directory like ```/usr/local/bin```.

### Start the Temporal Cluster

Once you've installed Temporal CLI on your platform of choice and added it to your ```PATH```, open a new Terminal window and run the following command:

```temporal server start-dev```

This command starts a local Temporal Cluster. It starts the Web UI, creates the default [Namespace](https://docs.temporal.io/namespaces), and uses an in-memory database.

*  The Temporal Server will be available on ```localhost:7233```.
*  The Temporal Web UI will be available at ```http://localhost:8233```.

Leave the local Temporal Cluster running as you work through tutorials and other projects. You can stop the Temporal Cluster at any time by pressing ```CTRL+C```.

### To change the Web UI port
The Temporal Web UI may be on a different port in some examples or tutorials. To change the port for the Web UI, use the ```--ui-port``` option when starting the server::

```temporal server start-dev --ui-port 8080```

The Temporal Web UI will now be available at http://localhost:8080.

The ```temporal server start-dev``` command uses an in-memory database, so stopping the server will erase all your Workflows and all your Task Queues. If you want to retain those between runs, start the server and specify a database filename using the ```--db-filename``` option, like this:

```temporal server start-dev --db-filename your_temporal.db```

When you stop and restart the Temporal Cluster and specify the same filename again, your Workflows and other information will be available.


