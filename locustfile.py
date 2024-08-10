from locust import HttpUser, task

class GetDataAPI(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        # self.client.get("/profile")
        # self.client.get("/redis/UJIANKHUSUS_PROSES_SISWA_ID_18593")
        # self.client.get("/sekolah/68/kelas/989")
        # self.client.get("/api/v1/ujiankhusus/proses/siswa/17874")
        # self.client.get("/api/v1/ujiankhusus/proses")
        # self.client.get("/hello")
        # self.client.get("/world")