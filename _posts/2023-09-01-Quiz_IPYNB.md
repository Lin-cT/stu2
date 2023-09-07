---
comments: True
layout: post
title: Quiz
description: A quiz on coding terminology as well as my blog
type: tangibles
courses: {'compsci': {'week': 2}}
---

```python
name = input("What's your name?");
#Input will ask for the user's input, so they will have to type.
print("Hello " + name);

questions = 5;
correct = 0;
#There are a total of 5 questions and as the user gets more of them right, theyr score will go up

ready = input("You will be asked " + str(questions) + " questions. Please answer 'Yes' if ready.");
if ready == "Yes":
    print("Good luck.");
else:
    print("Too bad.");

rsp = input("What command is used to include other functions that were previously developed?");
#If they answer impor, they will get the question right and their score increases by one, otherwise they will not get to increase their score.
if rsp == "import":
    print("That's right!");
    correct += 1;
else:
    print("That's not right! Import is the correct answer.");

rsp = input("What command is used to evaluate correct or incorrect response in this example?");
if rsp == "if":
    print("Good job!");
    correct += 1;
else:
    print("That's not right! If is the correct answer.");

rsp = input("Each 'if' command contains an '_________' to determine a true or false condition?");
if rsp == "expression":
    print("Amazing!");
    correct =+ 1;
else:
    print("That's not right! Expression is the right answer.");

rsp = input("Now here are some questions about my blog! First one: How many siblings do I have?");
if rsp == "2":
    print("That's right!");
    correct += 1;
else:
    print("That's not right! I have two older siblings");

rsp = input("Next one. What is my cats name?");
if rsp == "Maomao":
    print("That's right!");
    correct += 1;
else:
    print("That's not right! My cat's name is Maomao");

print("Thank you for playing! Your score is " + str(correct) + "/5.");
percentage = correct / 5 * 100
#This takes the amount they scored correctly and turns it into a percentage.
print("You scored a " + str(percentage) + "%.")
```

    Hello Lindsay
    Good luck.
    That's not right! Import is the correct answer.
    Good job!
    That's not right! Expression is the right answer.
    That's right!
    That's right!
    Thank you for playing! Your score is 3/5.
    You scored a 60.0%.

