from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, AnyDict
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.json import JsonDocument
import json

class CarList(ServiceBase):
	@rpc(_returns=AnyDict)
	def getAllCars(ctx):
		return { 
				"electricCars": 
					[
						{
							"brand" : "Renault",
							"model" : "Zoé",
							"batteryTank" : 300,
							"consumption" : 1.2
						},
						{
							"brand" : "Citroen",
							"model" : "Pe-casso",
							"batteryTank" : 410,
							"consumption" : 1.8
						},
						{
							"brand" : "Nissan",
							"model" : "GTHix",
							"batteryTank" : 500,
							"consumption" : 2.3
						},
						{
							"brand" : "Renault",
							"model" : "Twizzy",
							"batteryTank" : 240,
							"consumption" : 1.0
						},
						{
							"brand" : "BMW",
							"model" : "E1",
							"batteryTank" : 400,
							"consumption" : 2.0
						}
					]
				}

application = Application([CarList], 'spyne.examples.hello.soap',
	in_protocol=Soap11(validator='lxml'),
	out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

server = make_server('127.0.0.1', 8000, wsgi_application)
server.serve_forever()