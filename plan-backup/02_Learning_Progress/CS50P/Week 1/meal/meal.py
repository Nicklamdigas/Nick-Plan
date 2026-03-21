def main():
    time = input("What is the time? ")
    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("Lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("Dinner time")

def convert(time):
    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)

    return hours + (minutes/60)


if __name__ == "__main__":
    main()