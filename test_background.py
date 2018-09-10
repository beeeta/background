import background2
import time

bg1 = background2.Background()

bg2 = background2.Background()

@bg1.task
def work1(param1,param2):
    print('task1:work1')
    time.sleep(3)
    return 'task1:work1:{}-{}'.format(param1,param2)

@bg1.task
def work11(param1,param2):
    print('task1:work11')
    time.sleep(3)
    return 'task1:work11:{}-{}'.format(param1,param2)

@bg2.task
def work2():
    print('task2:work2')
    time.sleep(3)
    return 'task2:work2'

@bg1.callback
def back1(future):
    print('back1 for task1')

@bg1.callback
def back11(future):
    print('back11 for task1')

@bg2.callback
def back2(future):
    print('back2 for task2')

def test_background():
    work1('1','2')
    work11('11','22')
    work2()

def common():
    print('common function')

if __name__ == '__main__':
    test_background()
    common()