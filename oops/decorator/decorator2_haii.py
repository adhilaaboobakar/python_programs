def tag_dec(fn):
    def wrapper():
        data=fn()
        return f"<b> {fn()} <b>"
    return wrapper


@tag_dec
def get_hello():
    return "hello"

@tag_dec
def get_hai():
    return "hai"

print(get_hai())
print(get_hello())
# <b>hello<b>
# <b>hai<b>