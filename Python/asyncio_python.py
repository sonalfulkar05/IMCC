import asyncio

async def task1():
    print("task1 started")
    await asyncio.sleep(2)
    print("tassk 1 completed")
    return ("task1")

async def task2():
    print("task 2 started")
    await asyncio.sleep(1)
    print("task 2 completed")
    return ("task2")

    
async def main():
    results = await asyncio.gather( # gather will always return a tuple of the function names
        task1(),
        task2()
    )
    print(results)
    #if we want to use gather then in above functions we should use return 
    
    #otherwise we can use below code
    #either one is correct
    
    # t1= asyncio.create_task(task1())
    # t2= asyncio.create_task(task2())
    # await t1
    # await t2

    
asyncio.run(main())
    