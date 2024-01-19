---
toc: True
comments: True
layout: post
title: Letters to Binary
courses: {'compsci': {'week': 17}}
type: tangibles
permalink: "ltb"
---
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div style="text-align:center">
        <p>
            Binary is used by a computer and is made up of various sequences of zeros and ones.
        </p>
    </div>
    <div style="text-align:center">
        <p>
            Different sequences of binary can represent letters. ASCII converts the letters into binary.
        </p>
    </div>
    <div style="text-align:center">
        <p>
            ASCII assigns a unique binary code to each character, allowing computers to process and store text. For example, the letter 'A' corresponds to the binary representation 01000001. This binary conversion enables computers to manipulate and convey textual information through a standardized digital language, showcasing the integral role of binary code in handling letters and text in the digital world.
        </p>
    </div>
    <div id="converterContainer">
        <input type="text" id="binaryInput" placeholder="Enter a letter" maxlength="1">
        <button id="convertButton" onclick="convertToBinary()">Convert</button>
        <font size="6"> <p id="binaryOutput"></p> </font>
    </div>
    <script>
        function convertToBinary() {
            var letter = document.getElementById('binaryInput').value;
            if (letter.length === 1) {
                var binary = letter.charCodeAt(0).toString(2);
                document.getElementById('binaryOutput').innerText = 'Binary: ' + binary;
            } else {
                document.getElementById('binaryOutput').innerText = 'Please enter a single letter.';
            }
        }
    </script>
</body>