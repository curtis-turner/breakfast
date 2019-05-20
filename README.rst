=============
Build Status
=============
.. image:: https://travis-ci.com/curtis-turner/breakfast.svg?branch=master
    :target: https://travis-ci.com/curtis-turner/breakfast

==========
Breakfast
==========

The most important meal of the day

========
Purpose
========

A complete and balanced meal to start the day. That is why it makes a perfect example of developing using the best practices for Python development.
I will be using this repo as a playground to building a small module called breakfast that will be released to PyPi so others can make use of breakfast.
Primarily targetted as a learning experience for myself others encouraged to helpout if they too like the idea of building a small healthy breakfast to 
start the day and to learn the basics of Python development with the best practices in mind.

=======
Usage
=======

Example usage can be seen in this simple be seen in the example below.

import breakfast

first_breakfast = breakfast.Breakfast() # this creates an instances of the Breakfast class

bacon = breakfast.Food() #this initializes a default instances of a Food class
bacon.name = "Bacon"
bacon.cals = 42

first_breakfast.add_item(_bacon) #adds and item to our breakfast
first_breakfast.count_cals() #this will return the sum of the calories for the items in your breakfast
first_breakfast.complete_breakfast() #this displays all the items in your breakfast and their calories

banana = breakfast.Food(32, "Banana")

my_food = [banana, bacon]

second_breakfast = breakfast.Breakfast(my_food) #you can also initialize your breakfast with a list of food items