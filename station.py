from train import Train
from parcel import Parcel


class Station:

    def __init__(self, list_of_parcels):
        self.list_of_parcels = list_of_parcels
        self.current_train = None

    def load_train(self, train):
        """
        Loads a train by taking parcels from the list and seeing if they fit.
        If a parcel is found to exceed the capacity of the train, the train is cleared from loading.

        :param train: the train that is being loaded
        :return: None
        """
        for parcel in self.list_of_parcels:
            if parcel.destination == train.destination:
                if train.has_capacity_for(parcel):
                    train.add_parcel(parcel)
                else:
                    self.dispatch(train)
                    break

    def dispatch(self, train):
        """
        Indicates a train is full and ready to leave the station
        :param train: Train that is filled as much as possible.
        :return: None
        """
        train.loaded = True


def get_data_from_train_file():
    filename = 'trains.txt'
    cities = []
    capacities = []
    with open(filename, 'r') as train_file:
        for line in train_file.readlines():
            if line.startswith('#'):
                continue
            data = line.split()
            cities.append(data[0])
            capacities.append(int(data[1]))
    trains = []
    for city, capacity in zip(cities, capacities):
        trains.append(Train(city, capacity))
    return trains


def get_data_from_parcel_file():
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
    parcels = []
    for city, weight in zip(cities, weights):
        parcels.append(Parcel(city, weight))
    return parcels


def write_train_data(trains):
    for train_number, train in enumerate(trains):
        train_output_filename = "trains_%03d.txt" % train_number
        with open(train_output_filename, 'w') as train_output_file:
            train_output_file.write("Train: %03d\n" % train_number)
            train_output_file.write("Destination: %s\n" % train.destination)
            train_output_file.write("Capacity: %05d\n" % train.capacity)
            train_output_file.write("Actual load: %.2f\n" % train.current_weight)
            train_output_file.write("Number of parcels: %03d\n" % train.get_number_of_particles())
            train_output_file.write("Parcels:\n")

            for parcel in train.get_parcel_list():
                train_output_file.write("  %s %.2f\n" % (parcel.destination, parcel.weight))


if __name__ == '__main__':
    trains = get_data_from_train_file()
    parcels = get_data_from_parcel_file()

    station = Station(parcels)
    for train in trains:
        station.load_train(train)
    write_train_data(trains)
