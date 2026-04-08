class std_result:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #DECORATOR   #STATIC METHOD (WITHOUT----S E L F)
    def salam():
        print("AsSalamu-Alaikum")

    def avg(self):
        sum = 0
        cnt = 0
        for i in self.marks:
            sum += i
            cnt += 1
        print("The Average is",sum/cnt,"of Student",self.name)
st1 = std_result("Khalid", [89,23,43])
st1.salam()
st1.avg()
st1.name = "Tony Stark"
st1.avg()