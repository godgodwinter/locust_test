from locust import HttpUser, task

class GetDataAPI(HttpUser):
    # jwt_token = "YOUR_JWT_TOKEN_HERE"
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtYSI6IlJJU0tBIEFVTElBIE5BWkFSSU5BIiwicm9sZSI6ImMybHpkMkU9IiwiaWF0IjoxNzI1ODU1NzQ3LCJleHAiOjE3MjY0NjA1NDd9.kEvHdtP7QhbNsEkX6OBpsP2ZXjyNC-TCP57_wfWC3fI"
    @task
    def hello_world(self):
        headers = {
            "Authorization": f"Bearer {self.jwt_token}"
        }
        # self.client.get("/api/v1/admin/sekolah/index", headers=headers)
        self.client.get("/redis/UJIANKHUSUS_V3_PROSES_SISWAID_B_1", headers=headers)
        # self.client.get("/redis/UJIANKHUSUS_V3_PROSES_SISWAID_A_1", headers=headers)
        # self.client.get("/api/v2/master/sekolah")
        # self.client.get("/")
        # self.client.get("/profile")
        # self.client.get("/redis/UJIANKHUSUS_PROSES_SISWA_ID_18593")
        # self.client.get("/sekolah/68/kelas/989")
        # self.client.get("/api/v1/ujiankhusus/proses/siswa/17874")
        # self.client.get("/api/v1/ujiankhusus/proses")
        # self.client.get("/hello")
        # self.client.get("/world")