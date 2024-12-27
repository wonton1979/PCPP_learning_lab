import abc

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def __init__(self):
        self.scanner_resolution = "800x600"
        self.printer_resolution = "800x600"

    def __str__(self):
        return "Cheap Multifunction Device"

    def scan_document(self):
        print("Document has been scanned")

    def get_scanner_status(self):
        print(f"The resolution of Scanner is {self.scanner_resolution}")

    def get_printer_status(self):
        print(f"The resolution of Printer is {self.printer_resolution}")

    def print_document(self):
        print("Document has been printed")



class MFD2(Scanner, Printer):
    def __init__(self):
        self.scanner_resolution = "1024x768"
        self.printer_resolution = "1024x768"

    def __str__(self):
        return "Medium Priced Multifunction Device"

    def scan_document(self):
        print("Document has been scanned")

    def get_scanner_status(self):
        print(f"The resolution of Scanner is {self.scanner_resolution}")

    def get_printer_status(self):
        print(f"The resolution of Printer is {self.printer_resolution}")

    def print_document(self):
        print("Document has been printed")


class MFD3(Scanner, Printer):
    def __init__(self):
        self.scanner_resolution = "1920x1080"
        self.printer_resolution = "1920x1080"

    def __str__(self):
        return "Premium Multifunction Device"

    def scan_document(self):
        print("Document has been scanned")

    def get_scanner_status(self):
        print(f"The resolution of Scanner is {self.scanner_resolution}")

    def get_printer_status(self):
        print(f"The resolution of Printer is {self.printer_resolution}")

    def print_document(self):
        print("Document has been printed")

print("*"*40)
cheap_device = MFD1()
print(cheap_device)
print("*"*40)
cheap_device.scan_document()
cheap_device.get_scanner_status()
cheap_device.get_printer_status()
cheap_device.print_document()
print("*"*40)

medium_priced_device = MFD2()
print(medium_priced_device)
print("*"*40)
medium_priced_device.scan_document()
medium_priced_device.get_scanner_status()
medium_priced_device.get_printer_status()
medium_priced_device.print_document()
print("*"*40)

premium_device = MFD3()
print(premium_device)
print("*"*40)
premium_device.scan_document()
premium_device.get_scanner_status()
premium_device.get_printer_status()
premium_device.print_document()
print("*"*40)
