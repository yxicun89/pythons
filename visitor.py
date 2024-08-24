# Visitorクラス
class AnimalVisitor:
    def visit_lion(self, lion):
        # print("ライオンが来た！")
        pass

    def visit_elephant(self, elephant):
        # print("ゾウが来た！")
        pass

    def visit_giraffe(self, giraffe):
        # print("キリンが来た！")
        pass

# 訪れる要素のクラス
class Animal:
    def accept(self, visitor):
        # print("動物園に来た！")
        pass

class Lion(Animal):
    def accept(self, visitor):
        visitor.visit_lion(self)

class Elephant(Animal):
    def accept(self, visitor):
        visitor.visit_elephant(self)

class Giraffe(Animal):
    def accept(self, visitor):
        visitor.visit_giraffe(self)

# Visitorの具象サブクラス
class AnimalSoundVisitor(AnimalVisitor):
    def visit_lion(self, lion):
        print("The lion roars.")

    def visit_elephant(self, elephant):
        print("The elephant trumpets.")

    def visit_giraffe(self, giraffe):
        print("The giraffe makes no sound.")

# オブジェクトの構造を表すクラス
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def accept(self, visitor):
        for animal in self.animals:
            animal.accept(visitor)

# 実行例
if __name__ == "__main__":
    # 動物のインスタンスを作成
    lion = Lion()
    elephant = Elephant()
    giraffe = Giraffe()

    # 動物を動物園に追加
    zoo = Zoo()
    zoo.add_animal(lion)
    zoo.add_animal(elephant)
    zoo.add_animal(giraffe)

    # 音を出すVisitorを作成し、動物園を訪れる
    sound_visitor = AnimalSoundVisitor()
    zoo.accept(sound_visitor)