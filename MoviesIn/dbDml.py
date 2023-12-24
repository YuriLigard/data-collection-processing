class DbDml:

    def __init__(self, conn: object):
        self.conn = conn
        self.expiration = 1800 #30min


    def add(self, keyUrl: str, value: str) -> str:
        
        return self.conn.set(name=keyUrl, value=value, ex=self.expiration)
    
    def seach(self, keycahe):
        return self.conn.get(keycahe)
    
    ## Exluir cache 
    ## Mudar tmp
    


#test
if __name__ == '__main__':
    from conndb import Conndb

    a = Conndb("127.0.0.1", 6379)
    conn = a.connect()

    dbdml = DbDml(conn)

    print(dbdml.set("www","1203mek"))

