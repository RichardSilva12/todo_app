#
# A SIMPLE TODO APP
#
# Author: Richard F Silva
# Email: richarfsilva@pm.me
#


class Todo:
    def __init__(self, todos):
        self.todos = todos


class Inteface:

    _todos = []

    def add_todo(self):
        todo = input("Add TODO:\n")
        self._todos.append(Todo(todo))
        print("\nTODO added!")

    def show_todos(self):
        for i, e in enumerate(self._todos):
            print(i, e.todos)

    def remove_todo(self):
        try:
            index_todo = int(input("Enter index of TODO:\n"))
            index = self._todos[index_todo]
            self._todos.remove(index)
        except IndexError as e:
            print(e, "\nTry again.")

    def update_todo(self):
        try:
            todo_update = int(input("Enter with the index:\n"))
            for x, _ in enumerate(self._todos):
                if todo_update == x:
                    todo = input("Update todo:\n")
                    self._todos[todo_update] = Todo(todo)
        except:
            print("ERROR! Try again.")
                    
    def loop(self):
        bi = True

        while bi:
            print("\n****TODO****\n")
            opt = int(input("1-Add  2-Show  3-Delete  4-Update  5-Quit --> "))
            print("")
            if opt == 1:
                self.add_todo()
            elif opt == 2:
                self.show_todos()
            elif opt == 3:
                self.remove_todo()
            elif opt == 4:
                self.update_todo()
            elif opt == 5:
                print("QUITING...")
                bi = False


if __name__ == "__main__":
    interface = Inteface()
    interface.loop()
