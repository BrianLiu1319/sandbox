
# Lesson overview

This section contains a general overview of topics that you will learn in this lesson.

Explain the “Single Responsibility Principle”.
Briefly explain the additional SOLID principles.
Explain what “tightly coupled” objects are and why we want to avoid them.
Understand why composition is generally preferred to inheritance.


# Single responsibility principle:

a class should only have one responsibility

Most of our code has functions to update and write things to DOM
good idea to seperate DOM stuff from application logic



  function isGameOver() {

    // game over logic goes here!

    if (gameOver) {
      const gameOverDiv = document.createElement('div');
      gameOverDiv.classList.add('game-over');
      gameOverDiv.textContent = `${this.winner} won the game!`;
      document.body.appendChild(gameOverDiv);
    }
  }
  
  should be 

    function isGameOver() {

    // game over logic goes here!

    if (gameOver){
      DOMStuff.gameOver(this.winner);
    }
  }

The first issue is that the function should not directly be the one to manipulate the DOM. We should extract all the DOM manipulation into its own module

isGameOver function should only be responsible if the gameOver condition is met. th function that handles the gameloop should be responsible for deciding whether to call DOMstuff.gameOver(this.winner)

a given method / class should have a single reason to change. if an object has mutliple responsibilities - changing one aspect might affect another.


# Loosely Coupled Objects

all objects are intended to work together to form final application. But we should make sure individual objects can stand alone as much as possible. Tightly coupled objects are objects that rely so heavily on each other that changing one module will mean completely changing another.

ex: If we were writing a game but wanted to change UI - we should be able to work on the UI without completely working the game logic.



# SOLID

  ## S : single responsiblity:
  a class or module should only have a single purpose. Wallet class should only implement wallet functionality. Car class has 



# Coupling

coupling between modules occur when one module directly references another module. I.E on module knows about another module. A modular approach to implement an app is to create a module that handles orders and another that handles deliveries. One modular approach is to

# Knowledge Check

## What is the “Single Responsibility Principle”?
  SRP is making sure a class or module of the class has a single purpose
## What are the additional SOLID principles?

## What are “tightly coupled” objects and why do we want to avoid them?
  Objects that are reliant to another. We want to avoid them because if we change something
  we want to avoid changing everything just to make it work again

## Why is favoring composition over inheritance suggested?
  


