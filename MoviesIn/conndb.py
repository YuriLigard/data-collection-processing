import redis


class Conndb:

    __statusBase = False

    def __init__(self):

        self.host     = "127.0.0.1"
        self.port     = 6379
        self.decode   = True


    def connect(self):

        try:
            conn = redis.Redis(host=self.host, port=self.port, decode_responses=self.decode)
            __class__.__statusBase = conn.ping() 
        except redis.exceptions.ConnectionError as err:
            print('\n Conn Redis: {0} \n'.format(err))

        return conn

    def close(self, conn):

        if __class__.__statusBase == True:
            conn.execute_command('CLIENT KILL laddr {0}:{1}'.format(self.host, self.port))
        
        return __class__.__statusBase
            


## Test
if __name__ == '__main__':
    a = Conndb()
    conn = a.connect()
    conn = a.close(conn)
    print(conn)
