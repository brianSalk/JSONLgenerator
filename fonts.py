def tangerine(text):
    return    """<!DOCTYPE html>
<html>
<head>
    <title>Webfont Example</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tangerine:wght@700&display=swap">
    <style>
        .finetune_stuff {
            font-family: 'Tangerine', cursive;
            font-size: 70px !important;
        }
    </style>
</head>
<body>""" + f' <h1 class="finetune_stuff">{text}</h1> ' + """
</body>
</html>"""

