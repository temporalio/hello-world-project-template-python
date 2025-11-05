# Introduction

This tests the functionality of the `SayHello` Workflow and `say_hello` Activity with the two tests: `test_execute_workflow` and `test_mock_activity`.

- `test_execute_workflow` tests the execution of a Workflow using the `execute_workflow` method of the Client class. The Workflow being tested is `SayHello`, and the test asserts that the expected output of the Workflow is returned when it is executed.

- `test_mock_activity` tests the ability to mock an activity in the `temporalio` library. It does this by defining a new activity, `say_hello_mocked`, which will be used in place of the original `say_hello` activity. The test then executes the `SayHello` workflow using the mocked activity and asserts that the expected output is returned.

The test suite also includes a `conftest.py` file which defines several fixtures that are used in both tests.

## Test Details

### `test_execute_workflow`

This test does the following:

1. Generates a unique Task Queue name using the `uuid` module.
2. Creates a Worker instance with the following parameters:
   - `client`: an instance of the Client class, passed as a fixture
   - `task_queue`: the unique Task Queue name generated in step 1
   - `workflows`: a list containing the `SayHello` workflow
   - `activities`: a list containing the `say_hello` activity
3. Within the context of the Worker instance, the test executes the `SayHello` Workflow using the `execute_workflow` method of the Client class, passing in the following parameters:
   - `SayHello.run`: the entry point of the `SayHello` Workflow
   - `"World"`: an argument to be passed to the Workflow
   - `id`: a unique ID generated using the `uuid` module
   - `task_queue`: the unique Task Queue name generated in step 1
4. The test then asserts that the expected output of the workflow `"Hello, World!"` is returned.

### `test_mock_activity`

This test does the following:

1. Defines a new activity, `say_hello_mocked`, using the `@activity.defn` decorator. This activity returns a modified version of the original output.
2. Generates a unique Task Queue name using the `uuid` module.
3. Creates a Worker instance with the following parameters:
   - `client`: an instance of the Client class, passed as a fixture
   - `task_queue`: the unique Task Queue name generated in step 2
   - `workflows`: a list containing the `SayHello` workflow
   - `activities`: a list containing the `say_hello_mocked` activity
4. Within the context of the Worker instance, the test executes the `SayHello` Workflow using the `execute_workflow` method of the `Client` class, passing in the following parameters:
   - `SayHello.run`: the entry point of the `SayHello` workflow
   - `"World"`: an argument to be passed to the workflow
   - `id`: a unique ID generated using the `uuid` module
   - `task_queue`: the unique Task Queue name generated in step 2
5. The test then asserts that the expected output of the workflow `Hello, World from mocked activity!` is returned.

## Fixtures

### `event_loop`

This fixture provides an event loop for use in the tests. It creates a new event loop using the `new_event_loop` method of the event loop policy, and yields it to the test. After the test is finished, the fixture closes the event loop.

### `env`

This fixture provides a `WorkflowEnvironment` instance for use in the tests. The type of environment to create is determined by the `--workflow-environment` command line option. If the option is set to `local`, the fixture will start a local environment using the `start_local` method of the `WorkflowEnvironment` class. If the option is set to `time-skipping`, the fixture will start a time-skipping environment using the `start_time_skipping` method. If the option is set to any other value, the fixture will create a `WorkflowEnvironment` instance using the `from_client` method and passing in a Client instance connected to the specified server. The fixture yields the `WorkflowEnvironment` instance to the test, and then shuts it down after the test is finished using the shutdown method.

### `client`

This fixture provides a `Client` instance for use in the tests. It creates the instance by calling the `client` property of the `env` fixture.

## How to write this test

1. Import the necessary modules. You will need to import `uuid`, `pytest`, and several classes and functions from the temporalio library.
2. Define the `test_execute_workflow` test function. This function should take a client argument of type Client.
3. Generate a unique Task Queue name using the `uuid` module.
4. Create a Worker instance using the Worker constructor, and pass in the following arguments:
   - `client`: the client argument passed to the test function
   - `task_queue`: the unique Task Queue name generated in step 3
   - `workflows`: a list containing the `SayHello` workflow
   - `activities`: a list containing the `say_hello` activity
5. Within the context of the Worker instance, execute the `SayHello` workflow using the `execute_workflow` method of the Client class, and pass in the following arguments:
   - `SayHello.run`: the entry point of the `SayHello` workflow
   - `"World"`: an argument to be passed to the workflow
   - `id`: a unique ID generated using the `uuid` module
   - `task_queue`: the unique Task Queue name generated in step 3
6. Assert that the expected output of the workflow `("Hello, World!")` is returned.
7. Define the `test_mock_activity` test function. This function should take a client argument of type Client.
8. Define a new activity, `say_hello_mocked`, using the `activity.defn` decorator. This activity should take a name argument of type `str` and return a modified version of the original output.
9. Generate a unique Task Queue name using the `uuid` module.
10. Create a Worker instance using the Worker constructor, and pass in the following arguments:
    - `client`: the client argument passed to the test function
    - `task_queue`: the unique Task Queue name generated in step 9
    - `workflows`: a list containing the `SayHello` workflow
    - `activities`: a list containing the `say_hello_mocked` activity
11. Within the context of the Worker instance, execute the `SayHello` workflow using the `execute_workflow` method of the Client class, and pass in the following arguments:
    - `SayHello.run`: the entry point of the `SayHello` workflow
    - `"World"`: an argument to be passed to the workflow
    - `id`: a unique ID generated using the `uuid` module
    - `task_queue`: the unique Task Queue name generated in step 9
12. Assert that the expected output of the workflow `("Hello, World from mocked activity!")` is returned.

Note: The `test_run_worker.py` file should also include the necessary import statements for the `SayHello` workflow and `say_hello` activity. These should be imported from the `run_worker` module.
