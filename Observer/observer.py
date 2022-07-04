class Subject:

    def registerObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyObserver(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def registerObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except:
            pass

    def notifyObservers(self):
        for i in self._observers:
            i.update(self._temperature, self._humidity, self._pressure)

    def setMeasurements(self, temp, humid, pres):
        self._temperature = temp
        self._humidity = humid
        self._pressure = pres
        self.notifyObservers()


class Observer:

    def update(self, temp, humid, press):
        pass


class DisplayElement:

    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._current_temperature = 70.0
        self._last_temperature = 0.0
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humid, press):
        self._last_temperature = self._current_temperature
        self._current_temperature = temp
        self._temperature = temp
        self._humidity = humid
        self.display()

    def display(self):
        print("Current conditions are: " + str(self._current_temperature) +
              "F and " + str(self._humidity) + "%")
        if self._current_temperature > self._last_temperature:
            print("It got hotter")
        elif self._current_temperature < self._last_temperature:
            print("It got colder")
        else:
            print("Same temperature folks")


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._max_temp = 0.0
        self._min_temp = 200.0
        self._sum_temp = 0.0
        self._num_readings = 0
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humid, press):
        self._sum_temp = self._sum_temp + temp
        self._num_readings = self._num_readings + 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self):
        avg_temp = self._sum_temp/self._num_readings
        print("Statistics Avg/Min/Max temp: {0}/{1}/{2}"
              .format(avg_temp, self._min_temp, self._max_temp))


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._current_pressure = 29.92
        self._last_pressure = 0.0
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humid, press):
        self._last_pressure = self._current_pressure
        self._current_pressure = press
        self.display()

    def display(self):
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")

        elif self._current_pressure < self._last_pressure:
            print("Watch out for cooler, rainy weather!")
        else:
            print("More of the same")


if __name__ == '__main__':

    # TODO: instantiate an object of WeatherData
    weather_data = WeatherData()
# TODO: instantiate an object of CurrentConditionsDisplay
    current_display = CurrentConditionsDisplay(weather_data)
# TODO: instantiate an object of CurrentConditionsDisplay
    stats_display = StatisticsDisplay(weather_data)
# TODO: instantiate an object of CurrentConditionsDisplay
    forecast_display = ForecastDisplay(weather_data)
# TODO: create multiple events

weather_data.setMeasurements(76, 65, 30.4)
print("***** New event *****")
weather_data.setMeasurements(74, 68, 30.1)
print("***** New event *****")
