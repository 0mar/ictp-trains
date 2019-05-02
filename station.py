from train import Train
from parcel import Parcel


class Station:

    def __init__(self):
        """
        Create a new station that loads the parcels on the train.
        :param:
        """
        self.list_of_parcels = []
        self.list_of_trains = []
        self.get_train_schedule()
        self.get_data_from_parcel_file()

    def process_trains(self):
        """
        Accept each train on the schedule and load them with the parcels
        :return:
        """
        for train in self.list_of_trains:
            self.load_train(train)

    def load_train(self, train):
        """
        Loads a train by taking parcels from the list and seeing if they fit.
        If a parcel is found to exceed the capacity of the train, the train is cleared from loading.
        If a parcel is loaded, it is removed from the packing list by replacing it with None
        :param train: the train that is being loaded
        :return: None
        """
        for index, parcel in enumerate(self.list_of_parcels):
            if parcel:
                if parcel.destination == train.destination:
                    if train.has_capacity_for(parcel):
                        train.add_parcel(parcel)
                        self.list_of_parcels[index] = None
                    else:
                        break

    def get_train_schedule(self):
        """
        Load the train schedule from the file.
        Provides capacities and destinations for each train arriving to the station

        :return: None
        """
        filename = 'trains.txt'
        cities = []
        capacities = []
        with open(filename, 'r') as train_file:
            for line in train_file.readlines():
                if line.startswith('#'):
                    continue
                data = line.split()
                cities.append(data[0])
                capacities.append(float(data[1]) * 1000)
        for city, capacity in zip(cities, capacities):
            self.list_of_trains.append(Train(city, capacity))

    def get_data_from_parcel_file(self):
        """
        Loads information and retrieves parcel weights and destinations.
        :return:None
        """
        filename = 'parcels.txt'
        cities = []
        weights = []
        with open(filename, 'r') as parcel_file:
            for line in parcel_file.readlines():
                if line.startswith('#'):
                    continue
                data = line.split()
                cities.append(data[0])
                weights.append(float(data[1]))
        for city, weight in zip(cities, weights):
            self.list_of_parcels.append(Parcel(city, weight))

    def write_train_data(self):
        """
        Write up the train/parcel distribution.
        Loads a format string from file and uses that to format the output data
        to write out the train properties per train file.
        :return:
        """
        with open('format.str', 'r') as format_file:
            format_str = format_file.read()
        for train_number, train in enumerate(self.list_of_trains):
            train_output_filename = "trains_%03d.txt" % train_number
            with open(train_output_filename, 'w') as train_output_file:
                data_str = format_str % (
                train_number, train.destination, train.capacity, train.current_weight, train.get_number_of_parcels())
                parcels = '\n'.join(
                    ["  %s %.2f" % (parcel.destination, parcel.weight) for parcel in train.get_parcel_list()])
                train_output_file.write(data_str + parcels)


if __name__ == '__main__':
    station = Station()
    station.process_trains()
    station.write_train_data()
