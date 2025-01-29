from flask import Flask, request, render_template_string

app = Flask(__name__)

# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 0:
        return "Введите положительное число"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Главная страница с формой ввода
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            number = int(request.form.get('number', 0))
            result = fibonacci(number)
        except ValueError:
            result = "Введите целое число"

    html_content = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Fibonacci Calculator</title>
      </head>
      <body>
        <div style="max-width: 400px; margin: auto; padding: 20px;">
          <h1>Фибоначчи Калькулятор</h1>
          <form method="post">
            <label for="number">Введите номер позиции:</label><br>
            <input type="number" id="number" name="number" required><br><br>
            <input type="submit" value="Рассчитать">
          </form>
          {% if result is not none %}
            <h2>Результат: {{ result }}</h2>
          {% endif %}
        </div>
      </body>
    </html>
    '''
    return render_template_string(html_content, result=result)

if __name__ == '__main__':
    app.run(debug=True)