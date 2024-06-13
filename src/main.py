from src.services.user_service import UserService

def main():
    user_service = UserService()
    user = user_service.get_user("John Doe")
    print(user)

if __name__ == "__main__":
    main()