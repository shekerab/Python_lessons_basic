class Task:
    params = {}

    def __init__(self, params):
        self.params = params

    def __str__(self):
        return str(self._resolve())

    def _resolve(self):
        raise NotImplementedError("Should have implemented this")
