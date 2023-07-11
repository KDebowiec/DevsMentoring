# Poniższy kod realizuje funkcjonalność prostego notatnika 'T[ODO'. Możemy do niego dodawać dowolne notatki,
# usuwać niektóre oraz czyścić całą listę. Umieść go w pliku src.py i otestuj każdą z funkcji.
# Zapewnij sprawdzenie przypadków, w których zostanie rzucony wyjątek.

todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]


def check_pos(pos, todos):
    if len(todos) == 0:
        raise Exception("No more todos!")
    elif pos >= len(todos) or pos < 0:
        raise Exception("No such item number!")


def add_todo(content):
    todos.append(content)


def remove_todo(pos):
    check_pos(pos, todos)

    todos.pop(pos)


def edit_todo(pos, content):
    check_pos(pos, todos)

    todos[pos] = content


def remove_all():
    todos.clear()


# add_todo("Go to bed")
# remove_todo(0)
# edit_todo(0, "Get up from bed")
# remove_all()