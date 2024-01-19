# Menage Cache 

keycache = self.baseUrl+"_".join([str(self.params[key]) for key in self.params if key != "api_key"])

        incache = self.dbcache.seach(keycache)

        if incache == None:
        


        value = resp.text
                self.dbcache.add(keycache, value)