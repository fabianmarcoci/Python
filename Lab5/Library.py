class LibraryItem:
    def __init__(self, title, identifier):
        self.title = title
        self.identifier = identifier
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def display_info(self):
        return f"Title: {self.title}, ID: {self.identifier}"


class Book(LibraryItem):
    def __init__(self, title, identifier, author, pages):
        super().__init__(title, identifier)
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"{super().display_info()}, Author: {self.author}, Pages: {self.pages}"


class DVD(LibraryItem):
    def __init__(self, title, identifier, duration, rating):
        super().__init__(title, identifier)
        self.duration = duration
        self.rating = rating

    def display_info(self):
        return f"{super().display_info()}, Duration: {self.duration}, Rating: {self.rating}"


class Magazine(LibraryItem):
    def __init__(self, title, identifier, issue_number):
        super().__init__(title, identifier)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}, Issue: {self.issue_number}"
