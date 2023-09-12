from celery import Celery, signature

app = Celery(broker="redis://redis:6379/0", backend="redis://redis:6379/1")


def my_dummy_task(arg1: int, arg2: str) -> str:
    # Define a signature for the task - this must be the same as what the worker expects
    task_signature = signature("tasks.my_dummy_task", args=(arg1, arg2))

    # Send the task using the signature
    result = task_signature.delay()
    return result.get()


def inspect_pid_and_thread():
    # Define a signature for the task - this must be the same as what the worker expects
    task_signature = signature("tasks.inspect_pid_and_thread")

    # Send the task using the signature
    result = task_signature.delay()
    return result.get()


print(my_dummy_task(22, "string arg"))
print(inspect_pid_and_thread())
