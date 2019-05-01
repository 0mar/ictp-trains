class Train:

    def __init__(self, destination, capacity):
        """
        Create new train with a
        :param destination: City the train goes to
        :param capacity: Mass capacity that fits in the train
        """
        self.destination = destination
        self.capacity = capacity
        self.current_weight = 0
        self._list_of_parcels = []

    def add_parcel(self, parcel):
        """
        Load the parcel onto the train. If the parcel fits, return true, otherwise, return false.
        :param parcel: parcel with weight and destination
        :return: True if parcel fits on train, False otherwise
        """
        self._list_of_parcels.append(parcel)
        self.current_weight += parcel.weight
        if self.current_weight > self.capacity:
            raise ValueError("Overweight: {}/{}".format(self.current_weight, self.capacity))

    def get_number_of_parcels(self):
        """
        Get the number of parcels on the train
        :return:
        """
        return len(self._list_of_parcels)

    def get_parcel_list(self):
        """
        View the current list of parcels loaded on the train.
        Any changes made to this list will not impact the train.
        :return: List of parcels
        """
        return self._list_of_parcels.copy()

    def has_capacity_for(self, parcel):
        """
        Check if the train has capacity left for the given parcel.

        :param parcel: parcel which is not yet on the train
        :return: True if there is place for the parcel, False otherwise
        """
        return parcel.weight + self.current_weight < self.capacity

    def __str__(self):
        return "Train to {city}: Loaded with {num} parcels, {weight}/{cap}".format(city=self.destination,
                                                                                   weight=self.current_weight,
                                                                                   cap=self.capacity,
                                                                                   num=len(self._list_of_parcels))
