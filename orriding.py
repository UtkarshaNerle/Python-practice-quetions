class father:
    def work(self):
        print("i am a doctor")
        
class son(father):
    def work(self):
        super().work()
        print("i am a software eng")
        
son1 = son()
son1.work()