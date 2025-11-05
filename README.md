# hello-world-project-template-python

This is the Hello World project which has all the basic files explained in our [Hello World Tutorial](https://learn.temporal.io/getting_started/python/hello_world_in_python//).

## Instructions

To complete this tutorial, you will need Python 3.9 or later. If you 
have not already installed the `temporal` command-line interface (CLI), 
[follow these instructions](https://docs.temporal.io/cli#install) to do
so now.


Next, clone this repository:

```bash
git clone https://github.com/temporalio/hello-world-project-template-python
```

Switch to the cloned directory:

```bash
cd hello-world-project-template-python
```

Create a virtual environment for your project and install the Temporal SDK:

```bash
python3 -m venv env
source env/bin/activate
python -m pip install temporalio pytest pytest-asyncio
```

Use the Temporal CLI to start a Temporal Service for local development:

```bash
temporal server start-dev
```


Run the Worker for this project:

```bash
python run_worker.py
```

Open an other terminal window to the same directory, activate the 
virtual environment in that session, and then start the Workflow:

```bash
source env/bin/activate
python run_workflow.py
```

You can access the Temporal Web UI at <http://localhost:8233> and use
it to see the details for this Workflow Execution.
