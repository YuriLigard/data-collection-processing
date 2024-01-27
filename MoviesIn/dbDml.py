from interfaces.Idbbml import Idbml


class DbDml(Idbml):

    def __init__(self, conn: object):
        self.conn = conn
        self.expiration = 1800 #30min


    def add(self, key: str, value: str) -> str:
        
        return self.conn.set(name=key, value=value, ex=self.expiration)
    
    def get(self, key):
        return self.conn.get(key)
    


#test
if __name__ == '__main__':
    from conndb import Conndb

    a = Conndb("127.0.0.1", 6379)
    conn = a.connect()

    dbdml = DbDml(conn)

    print(dbdml.set("www","1203mek"))

