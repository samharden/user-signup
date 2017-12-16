form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="POST">
            <label for="rot_input">Rotate by:</label>
            <input id="rot_input" type="text" name="rot" value="0"/>
            <br>
            <textarea name="text">{0}</textarea>
            <br>
            <br>
            <input type="submit" value="GO" />
        </form>
    </body>
</html>
"""
