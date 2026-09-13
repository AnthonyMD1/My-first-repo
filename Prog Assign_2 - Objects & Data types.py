class Car:
    """Represents a car traveling at a constant speed."""

    def __init__(self, speed):
        """Constructor that takes speed (mph) and stores it as an attribute."""
        self.speed = speed  # float, miles per hour

    def calculate_distance(self, time):
        """Returns the distance traveled given a time (in hours)."""
        distance = self.speed * time
        return distance


def main():
    # Create a Car object with a speed of 70 mph
    my_car = Car(70.0)

    # Times to calculate distance for
    times = [6, 10, 15]

    # Calculate and display distance traveled for each time
    for t in times:
        distance = my_car.calculate_distance(t)
        print(f"In {t} hours, the car will travel {distance:.0f} miles.")


if __name__ == "__main__":
    main()