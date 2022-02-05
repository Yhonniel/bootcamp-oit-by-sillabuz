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
            "name": "Meyoji Robast Drone",
            "image": "img/product/tranding-1.jpg",
            "price": "$100.00",
            "category": "Dron"
        },
        {
            "id": 2,
            "name": "Ut praesentium earum",
            "image": "img/product/tranding-2.jpg",
            "price": "$80.00",
            "category": "Dron"
        },
        {
            "id": 3,
            "name": "Consectetur adipisicing",
            "image": "img/product/tranding-3.jpg",
            "price": "$50.00",
            "category": "Dron"
        },
        {
            "id": 4,
            "name": "  adipisicing",
            "image": "img/product/tranding-1.jpg",
            "price": "$50.00",
            "category": "Dron"
        }, {
            "id": 5,
            "name": "Consectetur  ",
            "image": "img/product/tranding-3.jpg",
            "price": "$50.00",
            "category": "Dron"
        }, {
            "id": 6,
            "name": "Peruvian Drone",
            "image": "img/product/tranding-2.jpg",
            "price": "$50.00",
            "category": "Dron"
        }
    ],
    "testimonials": [
        {
            "id": 1,
            'image': 'img/about/team-1.jpg',
            'message': """There are many variations of passages of Lorem Ipsum available, but the majority
                                        have suffered alteration in some form, by injected humour, or randomised words
                                        which don't look even""",
            'fullname': 'John Sullivan',
            'role': 'Customer'
        },
        {
            "id": 2,
            'image': 'img/about/team-2.jpg',
            'message': """College in Virginia, looked up one of the more obscure Latin words, consectetur,
                                        from a Lorem Ipsum passage, and going through the cites""",
            'fullname': 'Jenifer Brown',
            'role': ' Manager of AZ'
        },
        {
            "id": 3,
            'image': 'img/about/team-3.jpg',
            'message': """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots
                                        in a piece of classical Latin literature from 45""",
            'fullname': 'Kathy Young',
            'role': 'CEO of SunPark'
        },
        {
            "id": 4,
            'image': 'img/about/team-4.jpg',
            'message': """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots
                                       in a piece of classical Latin literature from 45""",
            'fullname': 'Baby Drash',
            'role': 'CTO OF PERUVIAN'
        }
    ]
}


@app.route('/')
def index():
    productos = db.get('products')
    testimonials = db.get('testimonials')
    data = {
        'productos': productos,
        'testimonials': testimonials
    }
    return render_template('index.html', data=data)


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
