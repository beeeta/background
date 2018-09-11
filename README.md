# Background2 : run stuff in the backround  
--- 
this is a fork from [kennethreitz/background](https://github.com/kennethreitz/background.git)   

The main purpose is add multi instance to background   

```
import background2
import time

bg1 = background2.Background()

bg2 = background2.Background()

@bg1.task
def work1(param1,param2):
    print('task1:work1')
    time.sleep(3)
    return 'task1:work1:{}-{}'.format(param1,param2)

@bg2.task
def work2():
    print('task2:work2')
    time.sleep(3)
    return 'task2:work2'

@bg1.callback
def back1(future):
    print('back1 for task1')


@bg2.callback
def back2(future):
    print('back2 for task2')

def test_background():
    work1('1','2')
    work2()

def common():
    print('common function')

if __name__ == '__main__':
    test_background()
    common()
```   
### install  
```pip install background2```   
or  
clone the project and ``` python setup.py install ```

--- 
suggestion and pull request are welcome   




LICENSE:MIT

