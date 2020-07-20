import asyncio

async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x * x

# Create event loop
loop = asyncio.get_event_loop()

# # Run async function and wait for completion
# results = loop.run_until_complete(square(1))
# print(results)

# # Close the loop
# loop.close()
results = loop.run_until_complete(asyncio.gather(
    square(1),
    square(2),
    square(3)
))
print(results)

# Close the loop
loop.close()