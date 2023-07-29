def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
safe_print_division(12, 2)