user = input("File name: ").lower().strip()
if user.endswith(".gif"):
    print("image/gif")
elif user.endswith(".jpg"):
    print("image/jpg")
elif user.endswith(".jpeg"):
    print("image/jpeg")
elif user.endswith(".pdf"):
    print("application/pdf")
else :
    print("application/octet-stream")   