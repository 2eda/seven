print('Hello,World')
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Id:
    counter = 0  # 何番までの識別番号を与えたか
    def __init__(self):
        Id.counter += 1
        self.id = Id.counter
    # 識別番号を取得
    def get_id(self):
        return self.id
    # 最後の識別番号を返す
    @staticmethod
    def get_max_id(): return Id.counter

# mainメソッドを含むIdTesterクラスを書く
class IdTester:
    @staticmethod
    def main():
        a = Id()  # 識別番号1
        b = Id()  # 識別番号2
        print(f"aの識別番号: {a.get_id()}")
        print(f"bの識別番号: {b.get_id()}")
        print(f"Id.counter = {Id.counter}")
        print(f"a.counter = {a.counter}")
        print(f"b.counter = {b.counter}")
        print(f"MaxId = {Id.get_max_id()}")

if __name__ == "__main__":
    IdTester.main()
