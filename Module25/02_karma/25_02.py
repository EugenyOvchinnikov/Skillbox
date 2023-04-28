from random import randint, choice


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


if __name__ == '__main__':
    errors_list = (KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError)

    try:
        raise choice(errors_list)
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
        print(type(exc).__name__)
