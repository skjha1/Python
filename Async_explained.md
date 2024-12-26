```python
import asyncio
import random
# Function that return a corouting simulatig a food order 

async def order_food():
    print("Order placed....")
    print("Waiting for food to be prepared...")
    await asyncio.sleep(2) # Simulate food preparation time

    deciding_no = random.random()
    print(deciding_no)
    food_is_ready = deciding_no > 0.7
    if food_is_ready:
        print("Food is ready to be served")
        return "Food is served"
    else:
        print("Food can not be prepared")
        raise Exception("Soory, we're out of that dish")
    

async def poll_for_food(max_attempt, interval):
    attempt = 0

    while attempt < max_attempt:
        attempt +=1
        print(f"Polling attempt {attempt}...")
        try:
            message = await order_food()
            print(message)
            print("Customer starts eating") 
            return
        except Exception as error:
            print(error)
            if attempt < max_attempt:
                print(f"Food not ready yet, retrying in {interval} seconds")
                await asyncio.sleep(interval)
            else:
                print("Maximum pooling attempts reached. customer decided to leave the restaurant")


# Function to start the polling function
                
async def process_order():
    print("Customer arrives at the restaurant ")
    print("Customer places an order ")

    await poll_for_food(max_attempt=20, interval=3)

    print("Customer's experience at the restaurant is complete")

asyncio.run(process_order())

print("Customer is waiting for the food to be served...")



```
