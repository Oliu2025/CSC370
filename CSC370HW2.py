def access_control(rights, min_permission):
    result = ""

    for user_permission in rights:
        if user_permission >= min_permission:
            result += 'A'
        else:
            result += 'D'

    return result


def main():
    while True:
        try:
            passcodes_input = input("Enter passcodes separated by spaces: ")
            rights = [int(code) for code in passcodes_input.split()]
            min_permission = int(input("Enter the minimum permission level: "))

            access_result = access_control(rights, min_permission)

            print("Access Control Result:", access_result)

            continue_or_exit = input("Do you want to continue (Y/N)? ").upper()
            if continue_or_exit != 'Y' or continue_or_exit == 'N' or 'n':
                break

        except ValueError:
            print("Invalid Entry, please enter valid integers for passcodes and permission level. Try again.")


if __name__ == "__main__":
    main()
