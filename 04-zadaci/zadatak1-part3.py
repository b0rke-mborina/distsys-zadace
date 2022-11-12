import aiohttp
import asyncio
from aiohttp import web
import requests

routes = web.RouteTableDef()

temp = []

@routes.get("/otherActivities")
async def get_fact(request):
	try:
		json_data = await request.json()
		#print(json_data)
		result = dict((k, json_data[k]) for k in ('activity', 'type'))
		response = requests.get("https://randomuser.me/api/")
		responseData = response.json()
		#print(responseData)
		result["firstName"] = responseData["results"][0]["name"]["first"]
		result["lastName"] = responseData["results"][0]["name"]["last"]
		result["dateOfBirth"] = responseData["results"][0]["dob"]["date"]
		print("RESULT: ", result)
		temp.append(result)
		return web.json_response({"status":"success"}, status = 200)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

@routes.get("/charityAndRecreational")
async def get_fact(request):
	try:
		json_data = await request.json()
		#print(json_data)
		result = dict((k, json_data[k]) for k in ('activity', 'type'))
		response1 = requests.get("https://randomuser.me/api/")
		responseData1 = response1.json()
		#print(responseData)
		result["firstName"] = responseData1["results"][0]["name"]["first"]
		result["lastName"] = responseData1["results"][0]["name"]["last"]
		result["dateOfBirth"] = responseData1["results"][0]["dob"]["date"]
		response2 = requests.get("https://randomuser.me/api/")
		responseData2 = response2.json()
		result["latitude"] = responseData2["results"][0]["location"]["coordinates"]["latitude"]
		result["longitude"] = responseData2["results"][0]["location"]["coordinates"]["longitude"]
		print("RESULT: ", result)
		temp.append(result)
		return web.json_response({"status":"success"}, status = 200)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8082)
