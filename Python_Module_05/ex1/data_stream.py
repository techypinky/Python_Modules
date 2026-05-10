import abc
import typing

class DataProcessor(abc.ABC):
    def __init__(self):
        self._data: list[str] = []
        self._total: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data")
        value = self._data.pop(0)
        return (0, value)

    def get_total(self) -> int:
        return self._total

    def get_remaining(self) -> int:
        return len(self._data)



class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            for x in data:
                self._data.append(str(x))
                self._total += 1
        else:
            self._data.append(str(data))
            self._total += 1



class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            for x in data:
                self._data.append(x)
                self._total += 1
        else:
            self._data.append(data)
            self._total += 1



class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        def valid_dict(d):
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

        if valid_dict(data):
            return True
        if isinstance(data, list):
            return all(valid_dict(x) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def format_log(d):
            return d["log_level"] + ": " + d["log_message"]

        if isinstance(data, list):
            for d in data:
                self._data.append(format_log(d))
                self._total += 1
        else:
            self._data.append(format_log(data))
            self._total += 1



class DataStream:
    def __init__(self):
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            handled = False

            for p in self._processors:
                if p.validate(item):
                    p.ingest(item)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for p in self._processors:
            name = p.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {p.get_total()} items processed, "
                f"remaining {p.get_remaining()} on processor"
            )



print("=== Code Nexus - Data Stream ===")

print("Initialize Data Stream...")
ds = DataStream()
ds.print_processors_stats()

print("Registering Numeric Processor")
num = NumericProcessor()
ds.register_processor(num)

stream = [
    "Hello world",
    [3.14, -1, 2.71],
    [
        {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
        {"log_level": "INFO", "log_message": "User wil is connected"},
    ],
    42,
    ["Hi", "five"],
]

print("Send first batch of data on stream:", stream)
ds.process_stream(stream)
ds.print_processors_stats()

print("Registering other data processors")
txt = TextProcessor()
log = LogProcessor()

ds.register_processor(txt)
ds.register_processor(log)

print("Send the same batch again")
ds.process_stream(stream)
ds.print_processors_stats()

print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")

for _ in range(3):
    num.output()

for _ in range(2):
    txt.output()

for _ in range(1):
    log.output()

ds.print_processors_stats()