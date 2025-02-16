from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty list to store items
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if 0 <= index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
