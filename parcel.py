class Parcel:

    def __init__(self, destination, weight):
        """
        Creates a parcel with a fixed address and a weight.
        :param destination: City the particle needs to go to
        :param weight: The mass capacity needed on the train
        """
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return "Parcel: {weight} kg to {destination}".format(weight=self.weight, destination=self.destination)
