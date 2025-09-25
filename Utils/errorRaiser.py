class LazyError():
    errors_to_handle = list()

    def __init__(self, exception_type: str):
        self.errors_to_handle.append(
            exception_type) if exception_type not in self.errors_to_handle else None

    def show_errors(self):
        return self.errors_to_handle


# loop = True

# while loop:
#     try:
#         int('a')
#     except Exception as e:
#         error = (type(e).__name__)
#         err = LazyError(error)
#         loop = False

# print(err.show_errors())
