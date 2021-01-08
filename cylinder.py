#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program calculates the volume of a cylinder

import math


def calculate_volume(radius, height):
    # calculates the volume of a cylinder

    number = math.pi * radius ** 2 * height
    cylinder_volume = "{:.2f}".format(number)

    return cylinder_volume


def main():
    # input the radius and height
    while True:
        try:
            radius_from_user = float(input("Enter the radius of a cylinder "
                                           "(cm): "))
            height_from_user = float(input("Enter the height of a cylinder "
                                           "(cm): "))
            print("")

            # calls function
            float_volume = calculate_volume(radius_from_user,
                                            height_from_user)

            if radius_from_user <= 0 or height_from_user <= 0:
                print("Invalid input\n")
            else:
                # output
                print("The volume is: {0} cm³".format(float_volume))
                break

        except ValueError:
            print("\nYou entered an invalid key.\nTry again.\n")


if __name__ == "__main__":
    main()
