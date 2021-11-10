import time
from contextlib import contextmanager

class cm_timer_1:

    def __init__(self):
        pass
        
    def __enter__(self):
        self.before = time.perf_counter()

        
    def __exit__(self, exp_type, exp_value, traceback):
        self.after = time.perf_counter()
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print("time: {}".format(self.after - self.before))



@contextmanager
def cm_timer_2():
    before = time.perf_counter()
    yield
    after = time.perf_counter()
    print("time: {}".format(after - before))


def sleep(num):
    return num

if __name__ == "__main__":
    with cm_timer_1():
        sleep(5.5)
        
    with cm_timer_2():
        sleep(5.5)
