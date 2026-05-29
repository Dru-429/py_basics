import asyncio

async def main():
  print("start")
  await asyncio.sleep(3)
  print("Done")

asyncio.run(main())


# import time

# print("Start")
# time.sleep(3)
# print("Done")