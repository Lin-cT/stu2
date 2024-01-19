---
toc: True
comments: True
layout: post
title: Binary to Colors
description: This is a program that allows you to convert any binary code into colors.
courses: {'compsci': {'week': 17}}
type: tangibles
permalink: "btc"
---

<head>
  <meta charset="UTF-8"> <!-- Declares the character set as UTF-8 -->
</head>
<body>
  <div id="userInputs">
    <h1 id="title">Converting Binary Into Colors</h1> <!-- Represents the title -->
    <p id="description">Binary code, consisting of 0s and 1s, serves as the fundamental language of computers. In the RGB color model, colors like red are represented by values ranging from 0 to 255, with each component expressed in binary. For example, if the red component is 255, its binary representation is 11111111, while 0 is represented as 00000000. The combination of binary values for red, green, and blue components forms the binary representation of a color, illustrating the essential link between binary code and the digital representation of colors in computing.</p>
  </div>

  <div id="converterContainer">
    <input type="text" id="binaryInput" placeholder="Enter binary code"> <!-- Input field for entering binary code -->
    <button id="convertButton">Convert</button> <!-- Button to trigger the conversion -->
  </div>

  <script>
    // JavaScript code for handling the binary input and changing the background color
    function convertBinaryToColor() {
      const binaryInput = document.getElementById('binaryInput').value;

      // Check if the input is a valid binary number
      if (/^[01]+$/.test(binaryInput)) {
        const decimalValue = parseInt(binaryInput, 2);
        const hexColor = decimalValue.toString(16).padStart(6, '0'); // Convert to hexadecimal

        document.body.style.backgroundColor = `#${hexColor}`; // Changes the background color of the body
      } else {
        alert('Please enter a valid binary number (0s and 1s only).'); // Alert for invalid input
      }
    }

    const convertButton = document.getElementById('convertButton');
    convertButton.addEventListener('click', convertBinaryToColor); // Adds event listener for the "Convert" button
  </script>
</body>