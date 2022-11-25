import time
import random
import heapq
from threading import Thread
from enum import Enum, auto


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f'{i + 1}...')
        time.sleep(1)
    print('Rocket launched!')


# С ипользованием потоков
def run_threads(rockets):
    threads = [
        Thread(target=launch_rocket, args=(d, c))
        for d, c in rockets()
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


class State(Enum):
    WAITING = auto()
    COUNTING = auto()
    LAUNCHING = auto()


class Op(Enum):
    WAIT = auto()
    STOP = auto()


# конечные автоматы
class Launch:
    def __init__(self, delay, countdown):
        self._state = State.WAITING
        self._delay = delay
        self._countdown = countdown

    def step(self):
        if self._state is State.WAITING:
            self._state = State.COUNTING
            return Op.WAIT, self._delay
        if self._state is State.COUNTING:
            if self._countdown == 0:
                self._state = State.LAUNCHING
            else:
                print(f'{self._countdown}...')
                self._countdown -= 1
                return Op.WAIT, 1
        if self._state is State.LAUNCHING:
            print('Rocket launched!')
            return Op.STOP, None
        assert False, self._state


def now():
    return time.time()


# finit state machine
def run_fsm(rockets):
    start = now()
    work = [(start, i, Launch(d, c)) for i, (d, c) in enumerate(rockets)]
    while work:
        step_at, id, launch = heapq.heappop(work)
        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)
        op, arg = launch.step()
        if op is Op.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, id, launch))
        else:
            assert op is Op.STOP


def rockets():
    N = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(N)
    ]


if __name__ == '__main__':
    # Запуск отдельно каждой ракеты
    # for d, c in rockets():
    #     launch_rocket(d, c)

    # run_threads()

    run_fsm(rockets())
