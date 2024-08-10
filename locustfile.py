from locust import HttpUser, task

class GetDataAPI(HttpUser):
    @task
    def hello_world(self):
        # self.client.get("/")
        # self.client.get("/profile")
        # self.client.get("/redis/UJIANKHUSUS_PROSES_SISWA_ID_21597")
        # self.client.get("/redis/UJIANKHUSUS_PROSES_SISWA_ID_21597/aspek/1")
        # self.client.get("/redis/UJIANKHUSUS_V3_PROSES_SISWAID_A_21597/aspek/2")
        self.client.get("/redis/UJIANKHUSUS_V3_PROSES_SISWAID_A_21597/full_soal/5")
        # self.client.get("/sekolah/68/kelas/989")
        # self.client.get("/api/v1/ujiankhusus/proses/siswa/21597")
        # self.client.get("/api/v1/ujiankhusus/proses")
        # self.client.get("/hello")
        # self.client.get("/world")