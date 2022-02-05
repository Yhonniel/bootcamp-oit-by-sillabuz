from flask import Flask, render_template

app = Flask(__name__)

db = {
    "shop": [
        {
            "id": 1,
            "address": "Calle Juan Martín",
            "type": "frutería",
            "nombre": "Lola Castro Frutas",
            "latitude": 37.880273,
            "longitude": -4.792098
        },
        {
            "id": 2,
            "address": "Calle Pepe Cruz",
            "type": "supermercado",
            "nombre": "Ultramarinos Lolo Castro",
            "latitude": 37.862323,
            "longitude": -4.77812
        },
        {
            "id": 3,
            "address": "Avenida de la Cruz",
            "type": "pescadería",
            "nombre": "Pescados El Boquerón",
            "latitude": 37.856273,
            "longitude": -4.776992
        }
    ],
    "products": [
        {
            "id": 1,
            "name": "manzanas",
            "shopId": 1
        },
        {
            "id": 2,
            "name": "peras",
            "shopId": 1
        },
        {
            "id": 3,
            "name": "escoba",
            "shopId": 2
        },
        {
            "id": 4,
            "name": "detergente",
            "shopId": 2
        }
    ]
}

@app.route('/')
def index():
    data = {
        'nombre': 'Yahyr',
        'edad': 24
    }
    return render_template('index.html')


@app.route('/productos')
def productos():
    # DB
    productos = db.get('products')
    data = {
        'productos': productos
    }
    return render_template('productos.html', data=data)


@app.route('/tienda')  # Rutas
def tienda():  # Controllador
    # db
    tienda = db.get('shop')
    data = {'tienda': tienda}
    return render_template('tienda.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
