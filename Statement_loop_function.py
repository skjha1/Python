# bill_amount = float(input("Enter your total bill amount rs: "))

# if bill_amount > 5000:
#     discount = bill_amount * 0.20
#     print(f"Congrats! You get a 20% of discount of rs{discount: .2f}")
# elif 3000 <= bill_amount <= 5000:
#     discount = bill_amount * 0.10
#     print(f"Congrats! You get a 20% of discount of rs{discount: .2f}")
# else:
#      print("No discount avaiable. Thankyou for shopping with us!")


# bill_amount = float(input("Enter your total bill amount rs: "))
# is_loyalty_member = input("Are you a loyality member? (yes/no) ").lower()

# print(is_loyalty_member)

# if bill_amount > 5000:
#     discount = bill_amount * 0.20
#     print(f"Base Discount: {discount: .2f}")

#     if is_loyalty_member == "yes":
#         additional_discout = bill_amount * 0.05 # Extra 5% discount
#         print(f"Loyality Discount: rs {additional_discout:.2f}")
#         total_discount = discount + additional_discout
#     else:
#         total_discount = discount
    
#     print(f"Total Discount: rs {total_discount:.2f}")
#     print(f"Final Bill Amount: rs {bill_amount - total_discount}")

# else:
#     print("No Discount avaiable.  Thankyou for shopping with us!")

##### For LOOP ########


# posts = [
#     { "post_id": 1, "likes": 120},
#     { "post_id": 2, "likes": 540},
#     { "post_id": 3, "likes": 320},
# ]



# print("Displaying Instagram post likes: ")
# for post in posts:
#     print(f"Post Id: {post['post_id']}, Likes: {post['likes']}")


##### While LOOP ########


# watch_queue = ["Video 1: Learn Python", "Video 2: Learn DSA", "Video 3: Learn ML" ]

# print("Youtube Watch Queue: ")
# while watch_queue:
#     print(f"Now Playing: {watch_queue.pop(0)}")
#     choice = input("Do you want to watch the next video? (yes/no)").lower()
#     if choice == 'no':
#         print("Exiting watch queue..")
#         break


# Defining a function 
# def calculate_total_price(prices):
#     total = sum(prices)
#     #print("before returning printing total : ",total)
#     return total

# cart = [100, 200, 50, 150]
# total_price = calculate_total_price(cart)
# print(f"Totl Price rs : {total_price}")


# Global varible 
# app_name = "MyAwesomeApp"

# def display_app_name():
#     global app_name # refactoring the global variable
#     app_name = "MySuperApp" # modifying the global variable
#     print(f"Inside Function: {app_name}")

# display_app_name()
# print(f"Outside Function: {app_name}")


# lambda arguments: expression

# square = lambda x: x ** 2
# print(square(5)) # Output: 25 







# videos = [
#     {"title": "Python Basics", "Views": 1500},
#    {"title": "Data structure and algorithms", "Views": 2000},
#     {"title": "Machine Learning", "Views": 1800},
# ]

# videos_sorted = sorted(videos, key=lambda video: video["Views"], reverse=True)

# print("Videos sorted by views: ")
# for video in videos_sorted:
#     print(f"{video['title']}: {video['Views']} views")
