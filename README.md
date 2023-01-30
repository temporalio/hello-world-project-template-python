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
python -m pip install temporalio
```

[Install and run the Temporal Server](https://docs.temporal.io/docs/server/quick-install) using `docker compose`.

```bash
git clone https://github.com/temporalio/docker-compose.git
cd docker-compose
docker compose up
```

You can now view Temporal Web at <http://localhost:8080>.

Run the worker and starter included in the project.

```bash
python run_worker.py
python run_workflow.py
```
