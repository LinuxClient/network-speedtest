import speedtest
from tabulate import tabulate


class Speedtest(object):
    def __init__(self):
        self.parser = speedtest.Speedtest()

    def data(self):
        download = str(f"{round(self.parser.download() / 1_000_000, 2)} Mbps")
        upload = str(f"{round(self.parser.upload() / 1_000_000, 2)} Mbps")
        return [
            ["Download", "Upload"],
            [download, upload]
        ]

    def __repr__(self):
        result = self.data()
        return tabulate(result, headers="firstrow", tablefmt="fancy_grid")
