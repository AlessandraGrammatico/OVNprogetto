class Lightpath(object):
    def __init__(self, power, path, channel):
        self._sig_power = power #float
        self._path = path #list[string]
        self._channel = channel #integer 
        self._noise_power = 0 #float
        self._latency = 0 #float total time delay due to propagation
        self.Rs = 32.0e9
        self.df = 50.0e9

    @property
    def signal_power(self):
        return self._sig_power

    def set_signal_power(self, value):
        self._sig_power = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def channel(self):
        return self._channel

    @property
    def noise_power(self):
        return self._noise_power

    @noise_power.setter
    def noise_power(self, value):
        self._noise_power = value

    @property
    def latency(self):
        return self._latency

    @latency.setter
    def latency(self, value):
        self._latency = value

    def add_noise(self, value):
        self.noise_power += value

    def add_latency(self, value):
        self.latency += value

    def next(self):
        self.path = self.path[1:]


class SignalInformation(Lightpath):

    def __init__(self, signal_power, path):
        super().__init__(signal_power, path, 0)
        self._signal_power = signal_power
        self._noise_power = 0
        self._latency = 0
        self._path = path
        self.Rs = 32.0e9
        self.df = 50.0e9

    def increase_noise(self, value):
        self._noise_power += value

    def increase_latency(self, value):
        self._latency += value

    def next(self):
        self._path = self._path[1:]

    @property
    def path(self):
        return self._path

    def getLatency(self):
        return self._latency

    def getNoisePower(self):
        return self._noise_power

    def getSignalPower(self):
        return self._signal_power
