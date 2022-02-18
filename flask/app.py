from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Base de datos en memoria
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
    ],
    "product-details": [
        {
            "id": 1,
            "name": "Meyoji Robast Drone",
            "image": "img/product/tranding-1.jpg",
            "price": "$100.00",
            "category": "Dron",
            "rate": 5,
            "color": ['red', 'blue'],
            'stock': 0,
            'description': """ eget velit. Donec ac tempus ante. Fusce ultricies massa massa. 
                            Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in """,
            'review': {
                'client': {
                    'name': 'Juan',
                    'message': 'roadthemes',
                    "datetime": 'September 12, 2018',
                    'rate': 2
                }
            },
            'images': [
                'img/product/details-1.jpg',
                'img/product/details-2.jpg',
                'img/product/details-3.jpg',
                'img/product/details-4.jpg',
            ]
        },
        {
            "id": 2,
            "name": "Ut praesentium earum",
            "image": "img/product/tranding-2.jpg",
            "price": "$80.00",
            "category": "Dron",
            "rate": 4,
            "color": ['red', 'blue'],
            'stock': 500,
            'description': """ eget velit. Donec ac tempus ante. Fusce ultricies massa massa. 
                            Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in """,
            'review': {
                'client': {
                    'name': 'Juan',
                    'message': 'roadthemes',
                    "datetime": 'September 12, 2018',
                    'rate': 5
                }
            },
            'images': [
                'img/product/details-1.jpg',
                'img/product/details-2.jpg',
                'img/product/details-3.jpg',
                'img/product/details-4.jpg',
            ]
        },
        {
            "id": 3,
            "name": "Consectetur adipisicing",
            "image": "img/product/tranding-3.jpg",
            "price": "$50.00",
            "category": "Dron",
            "rate": 5,
            "color": ['red', 'blue'],
            'stock': 200,
            'description': """ eget velit. Donec ac tempus ante. Fusce ultricies massa massa. 
                            Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in """,
            'review': {
                'client': {
                    'name': 'Juan',
                    'message': 'roadthemes',
                    "datetime": 'September 12, 2018',
                    'rate': 3
                }
            }
        },
        {
            "id": 4,
            "name": "  adipisicing",
            "image": "img/product/tranding-1.jpg",
            "price": "$50.00",
            "category": "Dron",
            "rate": 3,
            "color": ['red', 'blue'],
            'stock': 40,
            'description': """ eget velit. Donec ac tempus ante. Fusce ultricies massa massa. 
                            Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in """,
            'review': {
                'client': {
                    'name': 'Juan',
                    'message': 'roadthemes',
                    "datetime": 'September 12, 2018',
                    'rate': 4
                }
            },
            'images': [
                'img/product/details-1.jpg',
                'img/product/details-2.jpg',
                'img/product/details-3.jpg',
                'img/product/details-4.jpg',
            ]
        }, {
            "id": 5,
            "name": "Consectetur  ",
            "image": "img/product/tranding-3.jpg",
            "price": "$50.00",
            "category": "Dron",
            "rate": 2,
            "color": ['red', 'blue'],
            'stock': 55,
            'description': """ eget velit. Donec ac tempus ante. Fusce ultricies massa massa. 
                            Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in """,
            'review': {
                'client': {
                    'name': 'Juan',
                    'message': 'roadthemes',
                    "datetime": 'September 12, 2018',
                    'rate': 2
                }
            },
            'images': [
                'img/product/details-1.jpg',
                'img/product/details-2.jpg',
                'img/product/details-3.jpg',
                'img/product/details-4.jpg',
            ]
        }, {
            "id": 6,
            "name": "Peruvian Drone",
            "image": "img/product/tranding-2.jpg",
            "price": "$50.00",
            "category": "Dron",
            "rate": 1,
            "color": ['red', 'blue'],
            'stock': 150,
            'description': """ eget velit. Donec ac tempus ante. Fusce ultricies massa massa. 
                            Fusce aliquam, purus eget sagittis vulputate, sapien libero hendrerit est, sed commodo augue nisi non neque. 
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor, lorem et placerat vestibulum, metus nisi posuere nisl, in """,
            'review': {
                'client': {
                    'name': 'Juan',
                    'message': 'roadthemes',
                    "datetime": 'September 12, 2018',
                    'rate': 1
                }
            },
            'images': [
                'img/product/details-1.jpg',
                'img/product/details-2.jpg',
                'img/product/details-3.jpg',
                'img/product/details-4.jpg',
            ]
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


# Maestro detalle
# Pasar parametros por URL
@app.route('/productos/<int:id>')
def productos(id):
    productos = db.get('product-details')
    producto = {}
    for p in productos:
        if p.get('id') == id:
            producto = p

    data = {
        'producto': producto
    }

    return render_template('productos.html', data=data)


@app.route('/tienda')  # Rutas
def tienda():  # Controllador
    # db
    tienda = db.get('shop')
    data = {'tienda': tienda}
    return render_template('tienda.html', data=data)


# VERBOS
# GET - POST - PUT - DELETE
API_V1 = '/api/v1/'


@app.route(API_V1 + 'productos')  # GET => S
def api_products():
    productos = db.get('products')
    return jsonify(productos)
    # return { "nombre": "Yahyr", "apellido": "Paredes" } # Diccionario "cadena"
    # return jsonify(
    #     nombre='Jhon Doe',
    #     apellido='Paredes',
    #     edad=24
    # ) # Formateror de json (ordena)


@app.route(API_V1 + 'producto/<int:id>')  # GET => /ID
def api_product_detail(id):
    productos = db.get('product-details')
    producto = {}
    for p in productos:
        if p.get('id') == id:
            producto = p

    return jsonify(producto)


@app.route(API_V1 + 'producto', methods=['POST']) # POST
def api_product_create():
    if request.method == 'POST':

        print(request.method)
        print(request.json) # formateando en json
        print(request.data) # diccionario
        print(request.files) # archivos - multipart

        return {}

    # if request.method == 'GET':
    #     return 'Method not implement'






if __name__ == '__main__':
    app.run(debug=True, port=5000)
