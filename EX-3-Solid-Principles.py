from abc import ABC, abstractmethod


# S — Single Responsibility Principle
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# D — Dependency Inversion Principle
# I — Interface Segregation Principle
class UserRepository(ABC):

    @abstractmethod
    def save_user(self, user):
        pass


class NotificationService(ABC):

    @abstractmethod
    def send_notification(self, user):
        pass


# O — Open/Closed Principle
class DatabaseRepository(UserRepository):

    def save_user(self, user):
        print(
            f"User {user.name} "
            f"saved to database"
        )


class FileRepository(UserRepository):

    def save_user(self, user):
        print(
            f"User {user.name} "
            f"saved to file"
        )


# L — Liskov Substitution Principle
class EmailNotification(NotificationService):

    def send_notification(self, user):
        print(
            f"Email sent to "
            f"{user.email}"
        )


class SMSNotification(NotificationService):

    def send_notification(self, user):
        print(
            f"SMS sent to "
            f"{user.name}"
        )


class UserService:

    def __init__(
        self,
        repository,
        notification
    ):
        self.repository = repository
        self.notification = notification

    def register_user(self, user):
        self.repository.save_user(user)
        self.notification.send_notification(user)

        print(
            "User registration completed"
        )


def main():

    user = User(
        "Jothika",
        "jothika@gmail.com"
    )

    repository = DatabaseRepository()

    notification = EmailNotification()

    service = UserService(
        repository,
        notification
    )

    service.register_user(user)


if __name__ == "__main__":
    main()

Output:
User Jothika saved to database
Email sent to jothika@gmail.com
User registration completed

