from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, AnyDict
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.json import JsonDocument
import json
import os

class CarList(ServiceBase):
	@rpc(_returns=AnyDict)
	def getAllCars(ctx):
		return { 
				"electricCars": 
					[
						{
							"brand" : "Renault",
							"model" : "Zoé",
							"autonomy" : 300,
							"chargeTime" : 70
						},
						{
							"brand" : "Citroen",
							"model" : "Pe-casso",
							"autonomy" : 410,
							"chargeTime" : 80
						},
						{
							"brand" : "Nissan",
							"model" : "GTHix",
							"autonomy" : 500,
							"chargeTime" : 90
						},
						{
							"brand" : "Renault",
							"model" : "Twizzy",
							"autonomy" : 240,
							"chargeTime" : 45
						},
						{
							"brand" : "BMW",
							"model" : "E1",
							"autonomy" : 400,
							"chargeTime" : 35
						}
					]
				}

application = Application([CarList], 'spyne.examples.hello.soap',
	in_protocol=Soap11(validator='lxml'),
	out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

port = int(os.environ.get('PORT',8000))

server = make_server('0.0.0.0', port, wsgi_application)
server.serve_forever()