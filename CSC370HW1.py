class RunLengthCode:
    def encode(self, input_string):
        if not input_string:
            return ""
        elif len(input_string) < 4:
            return input_string

        encoded_string = ""
        count = 1

        for i in range(1, len(input_string)):
            if input_string[i] == input_string[i-1]:
                count += 1
            else:
                if any(char in input_string for char in "{}:;'+=.,"):
                    if count > 4:
                        encoded_string += f"/{count:02d}{input_string[-1]}"
                        return encoded_string
                if count > 4:
                    encoded_string += f"/{count:02d}{input_string[i-1]}"
                else:
                    encoded_string += input_string[i-1] * count
                count = 1

        if count > 4:
            encoded_string += f"/{count:02d}{input_string[-1]}"
        else:
            encoded_string += input_string[-1] * count

        return encoded_string


def main():
    run_length_encoder = RunLengthCode()
    user_input = input("Input: ")
    encoded_message = run_length_encoder.encode(user_input)
    print(encoded_message)


if __name__ == "__main__":
    main()
