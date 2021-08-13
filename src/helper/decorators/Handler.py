#!python3

# from functools import wraps

# # class Retry:
# #     def __init__(self, operation):
# #         wraps(operation)(self)
# #         self.operation = operation

# #     def __call__(self, *args, **kwargs):
# #         last_raised = None
# #         RETRIES_LIMIT = 3
# #         for _ in range(RETRIES_LIMIT):
# #             try:
# #                 return self.operation(*args, **kwargs)
# #             except ControlledException as e:
# #                 logger.info("retrying %s", self.operation.__qualname__)
# #                 last_raised = e
# #         raise last_raised


# # @Retry
# # def run_operation(task):
# #     """Run the operation in the task"""
# #     return task.run()


# class Handler:

#     def __init__(self, operation) -> None:
#         wraps(operation)(self)
#         self.operation = operation


#     def __call__(self, cursor):
        
#         result = self.operation(cursor)
#         if result > 0:
#             return { "output": 1 }
#         else:
#             return { "output": 0 }


# @Handler
# def func_set(cursor):
#     return cursor


# out = func_set(2)
# print(out.get("output"))