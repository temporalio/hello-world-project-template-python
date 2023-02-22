# @@@SNIPSTART python-project-template-workflows
from datetime import timedelta
from temporalio import workflow
from activities import say_hello

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, start_to_close_timeout=timedelta(seconds=5)
        )
# @@@SNIPEND
