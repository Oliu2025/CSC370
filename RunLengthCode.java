package csc370;

import java.util.Scanner;

public class RunLengthCode {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String user = input.nextLine();

        System.out.println(encode(user));
    }

    public static String encode(String input) {
        StringBuilder output = new StringBuilder();

        if (input.length() > 0) {
            char repeat = input.charAt(0);
            int count = 1;
            
            for (int i = 1; i < input.length(); i++) {
                if (repeat == input.charAt(i) && i != input.length() - 1) {
                    count++;
                } else {
                    if (count > 3) {
                        output.append("/").append(String.format("%02d", count)).append(repeat);
                    } else {
                        output.append(String.valueOf(repeat).repeat(count));
                    }
                    repeat = input.charAt(i);
                    count = 1;
                }
            }
            
            if (count > 3) {
                output.append("/").append(String.format("%02d", count)).append(repeat);
            } else {
                output.append(String.valueOf(repeat).repeat(count));
            }
        }
        return output.toString();
    }
}