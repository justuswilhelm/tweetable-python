from wsgiref.simple_server import *;make_server('',8000,lambda e,s:s('200 ',[])and b'Hello, World!').serve_forever()
