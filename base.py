import gevent
def test():
    print('hello world 123 from eclipse')
    
def use_gevent():
    g = gevent.spawn(test)
    g.join()