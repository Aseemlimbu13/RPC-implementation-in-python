from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    print("Listening on port 8000")

    def facto(x):
        temp=1
        if(x==0):
            return 1
        elif(x<0):
            return('invlaid no.')
        else:
            while(x!=1):
                temp*=x
                x-=1
            return temp

    server.register_function(facto, 'fact')

    server.serve_forever()