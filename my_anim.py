import turtle
import hashlib
import unittest
import secrets

def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

class TestPasswordLocker(unittest.TestCase):
    def test_password_hiding(self):
        password = generate_password()
        hashed_password = hash_password(password)
        self.assertNotEqual(password, hashed_password)

def draw_locker():
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(150)
    turtle.penup()
    turtle.goto(-100, 30)
    turtle.pendown()
    turtle.forward(200)
    turtle.penup()
    turtle.goto(-100, -30)
    turtle.pendown()
    turtle.forward(200)

def draw_asterisks(password):
    turtle.penup()
    turtle.goto(-80, -10)
    turtle.pendown()
    for _ in range(len(password)):
        turtle.write("*", font=("Arial", 24, "normal"))
        turtle.forward(20)

def draw_safe():
    turtle.penup()
    turtle.goto(-90, -60)
    turtle.pendown()
    turtle.write("Safe", font=("Arial", 18, "normal"))

def animate_locker(password):
    turtle.speed(1)
    draw_locker()
    draw_asterisks(password)
    draw_safe()
    turtle.done()

# Example usage:
password = generate_password()
hashed_password = hash_password(password)
print("Generated password:", password)
print("Hashed password:", hashed_password)

# Running the unittest
unittest.main(argv=[''], exit=False)

# Animating the locker
animate_locker(hashed_password)
