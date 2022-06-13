from locust import HttpUser, task


class IdempotentStressTest(HttpUser):
    @task
    def read_idempotent_task(self):
        self.client.get("/read/1/69420")

class NonIdempotentStressTest(HttpUser):
    @task
    def read_non_idempotent_task(self):
        self.client.get("/read/1/")