"""practice importing from other modules."""

from lessons.my_functions import addition

if __name__ == "__main__":
    print("Howdy!")

print(addition(100,2))