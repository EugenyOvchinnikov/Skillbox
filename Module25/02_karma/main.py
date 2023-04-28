from random import random, randint, choice


class Error(Exception):
    pass


class KillError(Error):
    pass


class DrunkError(Error):
    pass


class CarCrashError(Error):
    pass


class GluttonyError(Error):
    pass


class DepressionError(Error):
    pass


def one_day():
    daily_karma = randint(1, 7)

    if random() < 1 / 10:
        raise choice(errors_list)

    return daily_karma


if __name__ == '__main__':
    karma = 0
    file_path = 'karma.log'
    errors_list = (KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError)

    with open(file_path, 'w') as file_out:
        while karma < 500:
            try:
                karma += one_day()
            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
                file_out.write(type(exc).__name__ + '\n')

    print('Карма набрана!')
