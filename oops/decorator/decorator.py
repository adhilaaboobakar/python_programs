def greeting(fn):
    def wrapper(user):
        data=fn(user)
        return f"Hello!, {data}"
        # return fn(user)
    return wrapper


@greeting
def morning_greeting(user):
    return f"good morning {user}"
@greeting
def afternoon_greeting(user):
    return f"good afternoon {user}"
@greeting
def evening_greeting(user):
    return f"good evening {user}"


print(morning_greeting("alan"))
print(afternoon_greeting("max"))