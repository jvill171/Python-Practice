"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        '''Creates a Serial number from the starting number'''
        self.start = start
        self.tag_counter = 0
    
    def __repr__(self):
        '''Show representation of SerialGenerator'''
        return f'<SerialGenerator start={self.start} tag_counter={self.tag_counter}>'
    
    def generate(self):
        '''Generates a new serial number, increasing the tag_counter before doing so'''
        self.tag_counter += 1
        return self.start + self.tag_counter -1
    
    def reset(self):
        '''Resets tag_counter for serial generation'''
        self.tag_counter = 0
    

    

