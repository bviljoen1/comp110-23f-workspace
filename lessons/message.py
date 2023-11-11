"""Class to store a message (operator overload, union types, default parameters)."""

class Email:

    to: str | int
    message: str
    important: bool


    # Default parameters = if no input is given, it will default to this shit. 
    def __init__(self, recipient: str | int = "Finn", message_text: str = "", importance_flag: bool = False):
        """Constructor of an email."""
        self.to = recipient
        self.message = message_text
        self.important = importance_flag

    def __str__(self) -> str:
        """Makes the message."""
        m_string: str = f"To {self.to}: \n"
        m_string += f"Important? {self.important}\n"
        m_string += f'"{self.message}"'
        return m_string
    
    # Function to overload
    def __mul__(self, factor: int):
        self.message = self.message * factor

email_to_kiara: Email = Email("kiara", "You're a great TA! ", False)
# email_to_kiara * 100
print(email_to_kiara)

# recipient can be a name or an int (PID etc). 
email_to_enis: Email = Email(730579443)
email_to_enis.message = "Hello "
print(email_to_enis)

# email_to_finn: Email = Email()
# print(email_to_finn)