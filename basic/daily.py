toDo={
    "monday":"Play Football",
    "tuesday":"code ",
    "wendesday":"Go To The Gym",
    "thursday":"Bake a cake",
    "friday":"Attend a dance class",
    "saturday":"Go To church",
    "sunday":"Movie Time"
}
def get_all_to_do():
    return f"<ul>{toDo.keys()}</ul>"

def to_to_do():
    li=""
    # for key in toDo:
    #     li=li+f"<li><h1>On:<b>{key}</b> we {toDo[key]}</h1></li>"
    for key in toDo:
        href=f"http://127.0.0.1:5000/day/{key}"
        li=li+f"<a href={href}><li><h1 >On:<b>{key}</b> we {toDo[key]}</h1></li></a>"
    return li

def get_the_to_do(key):
    return f"<h1>On This Day {key}</h1><h2>{toDo[key]}</h2>"

# print(to_to_do())



