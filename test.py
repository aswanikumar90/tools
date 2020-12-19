import gevent
def test():
    print('hello world 123 from eclipse')
g = gevent.spawn(test)
g.join()