import abc
import typing

class DataProcessor(abc.ABC):
    def __init__(self):
        self.data = []
        self.rank = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise Exception("No data")

        value = self.data.pop(0)
        rank = self.rank
        self.rank += 1
        return (rank, value)



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
                self.data.append(str(x))
        else:
            self.data.append(str(data))



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
            self.data.extend(data)
        else:
            self.data.append(data)



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
                self.data.append(format_log(d))
        else:
            self.data.append(format_log(data))



print("=== Code Nexus - Data Processor ===")


print("Testing Numeric Processor...")
num = NumericProcessor()

print("Trying to validate input'42':", num.validate(42))
print("Trying to validate input'Hello':", num.validate("Hello"))

print("Test invalid ingestion of string'foo' without prior validation:")
try:
    num.ingest("foo")
except Exception as e:
    print("Got exception:", e)

print("Processing data:", [1, 2, 3, 4, 5])
num.ingest([1, 2, 3, 4, 5])

print("Extracting 3 values...")
for i in range(3):
    r, v = num.output()
    print(f"Numeric value {r}: {v}")



print("Testing Text Processor...")
txt = TextProcessor()

print("Trying to validate input'42':", txt.validate(42))

data = ["Hello", "Nexus", "World"]
print("Processing data:", data)
txt.ingest(data)

print("Extracting 1 value...")
r, v = txt.output()
print(f"Text value {r}: {v}")



print("Testing Log Processor...")
log = LogProcessor()

print("Trying to validate input'Hello':", log.validate("Hello"))

logs = [
    {"log_level": "NOTICE", "log_message": "Connection to server"},
    {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
]

print("Processing data:", logs)
log.ingest(logs)

print("Extracting 2 values...")
for i in range(2):
    r, v = log.output()
    print(f"Log entry {r}: {v}")