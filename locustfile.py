from locust import HttpUser, task

class GetDataAPI(HttpUser):
    # jwt_token = "YOUR_JWT_TOKEN_HERE"
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtYSI6IlJJU0tBIEFVTElBIE5BWkFSSU5BIiwicm9sZSI6ImMybHpkMkU9IiwiaWF0IjoxNzI1ODU1NzQ3LCJleHAiOjE3MjY0NjA1NDd9.kEvHdtP7QhbNsEkX6OBpsP2ZXjyNC-TCP57_wfWC3fI"
    @task
    def send_answer(self):
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "kode_soal": "65b898b5390d668bfb7322df",
            "index_soal": 0,
            "kode_jawaban": "ed45251f-ba81-440a-b479-3ddbcaa6f1a4"
        }
        self.client.post("/api/v1/client_siswa/ujiankhusus/paketsoal/detail/65a44ab921be5acd2d3da797/jawab", json=payload, headers=headers)
    # @task
    # def hello_world(self):
    #     headers = {
    #         "Authorization": f"Bearer {self.jwt_token}"
    #     }
        # !getall soal kn
        #self.client.get("/api/v1/client_siswa/ujiankhusus/paketsoal/detail/65a44ab921be5acd2d3da797", headers=headers)
        # !skrip do jawab simpan
    #     self.client.get("/api/v1/client_siswa/ujiankhusus/paketsoal/detail/65a44ab921be5acd2d3da797/jawab", headers=headers)
        
       



        # self.client.get("/api/v1/admin/sekolah/index", headers=headers)
        # self.client.get("/redis/UJIANKHUSUS_V3_PROSES_SISWAID_B_1", headers=headers)
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