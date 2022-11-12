import aiohttp
import asyncio
from aiohttp import web
import requests

routes = web.RouteTableDef()

@routes.get("/parseActivities")
async def save_fact(request):
	try:
		json_data = await request.json()
		#print(json_data)
		#print(json_data.get("type"))
		if json_data.get("type") == "charity" or json_data.get("type") == "recreational":
			link = "http://127.0.0.1:8082/charityAndRecreational"
		else:
			link = "http://127.0.0.1:8082/otherActivities"
		#print(link)
		result = requests.get(link, json = json_data)
		resultData = result.json()
		print(resultData)
		return web.json_response(resultData, status = 200)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8081)

