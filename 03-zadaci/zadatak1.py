import asyncio
import os

async def afun1(listOfFileNames):
	await asyncio.sleep(0.1)
	return [{"naziv": fileName, "velicina": os.path.getsize(os.path.dirname(os.path.realpath(__file__)) + "\\" + fileName)} for fileName in listOfFileNames]

def fun2(listOfFileNames):
	for fileName in listOfFileNames:
		file = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + fileName, 'a')
		for i in range(1, 10001):
			file.write(str(i) + " ")
		file.close()

async def main():
	dirPath = os.path.dirname(os.path.realpath(__file__))
	fileNames = ["datoteka1.txt", "datoteka2.txt", "datoteka3.txt"]
	for fileName in fileNames:
		open(dirPath + "\\" + fileName, 'a').close()
	res = asyncio.create_task(afun1(fileNames))
	fun2(fileNames)
	print(await asyncio.gather(res))

if __name__ == "__main__":
	asyncio.run(main())
