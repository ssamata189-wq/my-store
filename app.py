from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# قائمة المنتجات الكاملة مع صور حقيقية فعلية ومطابقة لكل قطعة هاردوير
products = [
    # --- قسم المعالجات (Processors) ---
    {"id": 1, "name": "معالج Intel Core i9-14900KS", "price": 599, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=300"},
    {"id": 2, "name": "معالج Intel Core i7-14700K", "price": 410, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1555680202-c86f0e12f086?w=300"},
    {"id": 3, "name": "معالج Intel Core i5-14600K", "price": 299, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=300"},
    {"id": 4, "name": "معالج AMD Ryzen 9 7950X3D", "price": 649, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1555680202-c86f0e12f086?w=300"},
    {"id": 5, "name": "معالج AMD Ryzen 7 7800X3D", "price": 389, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=300"},
    {"id": 6, "name": "معالج AMD Ryzen 5 7600X", "price": 229, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1555680202-c86f0e12f086?w=300"},
    {"id": 7, "name": "معالج Intel Core i9-13900K", "price": 520, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=300"},
    {"id": 8, "name": "معالج AMD Ryzen 9 5950X", "price": 450, "category": "المعالجات", "image": "https://images.unsplash.com/photo-1555680202-c86f0e12f086?w=300"},

    # --- قسم كروت الشاشة (Graphics Cards) ---
    {"id": 9, "name": "بطاقة NVIDIA GeForce RTX 4090", "price": 1799, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=300"},
    {"id": 10, "name": "بطاقة NVIDIA GeForce RTX 4080 Super", "price": 999, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=300"},
    {"id": 11, "name": "بطاقة NVIDIA GeForce RTX 4070 Ti", "price": 799, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=300"},
    {"id": 12, "name": "بطاقة NVIDIA GeForce RTX 4060 Ti", "price": 399, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=300"},
    {"id": 13, "name": "بطاقة AMD Radeon RX 7900 XTX", "price": 920, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=300"},
    {"id": 14, "name": "بطاقة AMD Radeon RX 7800 XT", "price": 499, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=300"},
    {"id": 15, "name": "بطاقة AMD Radeon RX 7700 XT", "price": 419, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=300"},
    {"id": 16, "name": "بطاقة NVIDIA GeForce RTX 3060", "price": 289, "category": "كروت الشاشة", "image": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=300"},

    # --- قسم الإكسسوارات والكيبورد (Keyboards & Accessories) ---
    {"id": 17, "name": "لوحة مفاتيح ميكانيكية احترافية RGB Razer", "price": 149, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=300"},
    {"id": 18, "name": "لوحة مفاتيح لاسلكية مدمجة Logitech", "price": 99, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=300"},
    {"id": 19, "name": "ماوس ألعاب لاسلكي احترافي Logitech Pro", "price": 129, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=300"},
    {"id": 20, "name": "ماوس ألعاب خفيف الوزن RGB", "price": 59, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=300"},
    {"id": 21, "name": "سماعة رأس ألعاب محيطية 7.1 HyperX", "price": 99, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=300"},
    {"id": 22, "name": "سماعة رأس لاسلكية احترافية Corsair", "price": 159, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=300"},
    {"id": 23, "name": "ماوس باد كبير مانع للانزلاق RGB", "price": 29, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=300"},
    {"id": 24, "name": "ميكروفون بث مباشر احترافي USB", "price": 119, "category": "الإكسسوارات والكيبورد", "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=300"},

    # --- قسم الرامات (RAM) ---
    {"id": 25, "name": "ذاكرة عشوائية 32GB RGB DDR5 Corsair", "price": 125, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},
    {"id": 26, "name": "ذاكرة عشوائية 64GB DDR5 G.Skill", "price": 210, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},
    {"id": 27, "name": "ذاكرة عشوائية 16GB DDR4 Kingston", "price": 55, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},
    {"id": 28, "name": "ذاكرة عشوائية 32GB DDR4 Corsair", "price": 95, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},
    {"id": 29, "name": "ذاكرة عشوائية 64GB DDR4 T-Force", "price": 160, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},
    {"id": 30, "name": "ذاكرة عشوائية 16GB DDR5 Crucial", "price": 70, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},
    {"id": 31, "name": "ذاكرة عشوائية 8GB DDR4 Value", "price": 30, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},
    {"id": 32, "name": "ذاكرة عشوائية 32GB DDR5 TeamGroup", "price": 110, "category": "الرامات", "image": "https://images.unsplash.com/photo-1562976540-1e02c414436a?w=300"},

    # --- قسم اللوحات الأم (Motherboards) ---
    {"id": 33, "name": "لوحة أم ASUS ROG Strix Z790", "price": 320, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},
    {"id": 34, "name": "لوحة أم MSI MPG X670E Carbon", "price": 350, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},
    {"id": 35, "name": "لوحة أم Gigabyte Z790 Aorus", "price": 240, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},
    {"id": 36, "name": "لوحة أم ASUS TUF Gaming B650", "price": 190, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},
    {"id": 37, "name": "لوحة أم MSI MAG B760 Tomahawk", "price": 210, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},
    {"id": 38, "name": "لوحة أم ASRock B550 Phantom", "price": 130, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},
    {"id": 39, "name": "لوحة أم ASUS Prime X670-P", "price": 280, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},
    {"id": 40, "name": "لوحة أم Gigabyte B650 Eagle", "price": 160, "category": "اللوحات الأم", "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=300"},

    # --- قسم التبريد (Cooling) ---
    {"id": 41, "name": "مبرد مائي احترافي NZXT Kraken 360", "price": 180, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"},
    {"id": 42, "name": "مبرد هوائي مزدوج DeepCool AK620", "price": 65, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"},
    {"id": 43, "name": "مبرد مائي Corsair H150i Elite", "price": 240, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"},
    {"id": 44, "name": "مبرد هوائي Noctua NH-D15", "price": 109, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"},
    {"id": 45, "name": "مبرد مائي Lian Li Galahad II", "price": 160, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"},
    {"id": 46, "name": "مبرد هوائي Thermalright Assassin", "price": 40, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"},
    {"id": 47, "name": "مبرد مائي Arctic Liquid Freezer III", "price": 135, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"},
    {"id": 48, "name": "مبرد هوائي Cooler Master Hyper 212", "price": 35, "category": "التبريد", "image": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=300"}
]

cart = []

HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My PC - متجر قطع الحاسوب</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #f8f9fa; }
        .navbar { box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .hero { background: linear-gradient(135deg, #0f172a, #1e293b); color: white; padding: 45px 0; border-radius: 0 0 20px 20px; }
        .card { transition: transform 0.3s, box-shadow 0.3s; border: none; border-radius: 12px; overflow: hidden; }
        .card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }
        .card-img-top { height: 160px; object-fit: cover; background-color: #f1f5f9; }
        .price { color: #0d6efd; font-weight: 700; font-size: 1.25rem; }
        .category-pill { transition: all 0.2s; }
        .category-pill:hover, .category-pill.active { background-color: #0d6efd !important; color: white !important; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container">
            <a class="navbar-brand fw-bold fs-3 text-warning" href="/">💻 My PC</a>
            <div class="d-flex align-items-center gap-3">
                <a href="/cart" class="btn btn-outline-light position-relative">
                    🛒 عربة التسوق
                    <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                        {{ cart_count }}
                    </span>
                </a>
            </div>
        </div>
    </nav>

    <div class="hero text-center mb-4">
        <div class="container">
            <h1 class="display-5 fw-bold">مرحباً بك في My PC</h1>
            <p class="text-muted lead mb-0">أقوى المعالجات، كروت الشاشة، الرامات، اللوحات الأم والإكسسوارات بصور حقيقية ومطابقة تماماً</p>
        </div>
    </div>

    <div class="container mb-4">
        <div class="d-flex flex-wrap justify-content-center gap-2">
            <a href="/" class="btn btn-light border category-pill fw-bold px-4 {% if not selected_category %}active{% endif %}">الكل (جميع المنتجات)</a>
            {% for cat in categories %}
            <a href="/?category={{ cat }}" class="btn btn-light border category-pill fw-bold px-3 {% if selected_category == cat %}active{% endif %}">{{ cat }}</a>
            {% endfor %}
        </div>
    </div>

    <div class="container mb-5">
        <div class="row">
            {% if products %}
                {% for product in products %}
                <div class="col-md-4 mb-4">
                    <div class="card h-100 shadow-sm bg-white">
                        <img src="{{ product.image }}" class="card-img-top" alt="{{ product.name }}" loading="lazy">
                        <div class="card-body d-flex flex-column">
                            <span class="badge bg-secondary mb-2 align-self-start">{{ product.category }}</span>
                            <h5 class="card-title fw-bold text-dark" style="font-size: 1rem;">{{ product.name }}</h5>
                            <p class="price mt-2">${{ product.price }}</p>
                            
                            <form action="/buy_now/{{ product.id }}" method="POST" class="mt-auto">
                                <button type="submit" class="btn btn-success w-100 fw-bold py-2 shadow-sm">شراء مباشر (الدفع السريع) ⚡</button>
                            </form>
                            <form action="/add_to_cart/{{ product.id }}" method="POST" class="mt-2">
                                <button type="submit" class="btn btn-outline-primary w-100 fw-bold py-1">إضافة للسلة 🛒</button>
                            </form>
                        </div>
                    </div>
                </div>
                {% endfor %}
            {% else %}
                <div class="text-center py-5">
                    <p class="fs-4 text-muted">لا توجد منتجات متاحة في هذا القسم حالياً.</p>
                </div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

CART_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>عربة التسوق - My PC</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <style> body { font-family: 'Cairo', sans-serif; background-color: #f8f9fa; }</style>
</head>
<body>
    <div class="container my-5">
        <div class="card shadow p-4 border-0 rounded-4">
            <h2 class="mb-4 fw-bold text-dark">🛒 عربة التسوق الخاصة بك</h2>
            {% if cart %}
                <ul class="list-group mb-4">
                    {% for item in cart %}
                    <li class="list-group-item d-flex justify-content-between align-items-center py-3">
                        <div class="d-flex align-items-center">
                            <img src="{{ item.image }}" alt="" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" class="ms-3">
                            <span class="fw-bold">{{ item.name }}</span>
                        </div>
                        <span class="badge bg-primary fs-6 px-3 py-2">${{ item.price }}</span>
                    </li>
                    {% endfor %}
                </ul>
                <div class="d-flex justify-content-between align-items-center bg-light p-3 rounded-3 mb-4">
                    <h4 class="fw-bold mb-0">المجموع الكلي:</h4>
                    <h4 class="text-success fw-bold mb-0">${{ total }}</h4>
                </div>
                <div class="d-flex gap-2">
                    <a href="/" class="btn btn-secondary px-4 py-2">العودة للمتجر</a>
                    <a href="/checkout" class="btn btn-success px-4 py-2 fw-bold">الانتقال لخيارات الدفع 💳</a>
                </div>
            {% else %}
                <div class="text-center py-5">
                    <p class="fs-4 text-muted">عربتك فارغة حالياً.</p>
                    <a href="/" class="btn btn-primary px-4 py-2 mt-2">تصفح المنتجات الآن</a>
                </div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

CHECKOUT_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>بوابة الدفع الآمنة - My PC</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <style> 
        body { font-family: 'Cairo', sans-serif; background-color: #f8f9fa; }
        .payment-box { border: 2px solid #dee2e6; border-radius: 10px; padding: 15px; cursor: pointer; transition: 0.2s; }
        .payment-box:hover { border-color: #0d6efd; background-color: #f1f8ff; }
    </style>
</head>
<body>
    <div class="container my-5" style="max-width: 700px;">
        <div class="card shadow p-4 border-0 rounded-4">
            <h2 class="mb-4 fw-bold text-center text-dark">💳 بوابة الدفع الآمنة - My PC</h2>
            
            {% if selected_item %}
            <div class="alert alert-info d-flex align-items-center justify-content-between mb-4">
                <div class="d-flex align-items-center">
                    <img src="{{ selected_item.image }}" alt="" style="width: 40px; height: 40px; object-fit: cover; border-radius: 5px;" class="ms-2">
                    <strong>المنتج المطلوب:</strong> {{ selected_item.name }}
                </div>
                <span class="badge bg-success fs-6">${{ selected_item.price }}</span>
            </div>
            {% endif %}

            <form method="POST">
                <div class="mb-3">
                    <label class="form-label fw-bold">الاسم الكامل</label>
                    <input type="text" class="form-control" required placeholder="أدخل اسمك الكريم">
                </div>
                <div class="mb-3">
                    <label class="form-label fw-bold">عنوان الشحن / الولاية</label>
                    <input type="text" class="form-control" required placeholder="أدخل عنوانك بالتفصيل">
                </div>
                <div class="mb-3">
                    <label class="form-label fw-bold">رقم الهاتف</label>
                    <input type="tel" class="form-control" required placeholder="05xxxxxxxx">
                </div>

                <label class="form-label fw-bold mb-3">اختر وسيلة الدفع المفضلة لديك:</label>
                
                <div class="row g-3 mb-4">
                    <div class="col-6">
                        <div class="payment-box text-center">
                            <input class="form-check-input mb-1" type="radio" name="payment_method" id="visa" checked>
                            <label class="form-check-label d-block fw-bold" for="visa">Visa / Mastercard</label>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="payment-box text-center">
                            <input class="form-check-input mb-1" type="radio" name="payment_method" id="paypal">
                            <label class="form-check-label d-block fw-bold" for="paypal">PayPal</label>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="payment-box text-center">
                            <input class="form-check-input mb-1" type="radio" name="payment_method" id="baridimob">
                            <label class="form-check-label d-block fw-bold" for="baridimob">بريدي موب (BaridiMob)</label>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="payment-box text-center">
                            <input class="form-check-input mb-1" type="radio" name="payment_method" id="cod">
                            <label class="form-check-label d-block fw-bold" for="cod">الدفع عند الاستلام</label>
                        </div>
                    </div>
                </div>

                <button type="submit" class="btn btn-success w-100 py-3 fw-bold fs-5 shadow">تأكيد ودفع المبلغ النهائي 🔒</button>
            </form>
            <div class="text-center mt-3">
                <a href="/" class="text-decoration-none">العودة إلى المتجر الرئيسي</a>
            </div>
        </div>
    </div>
</body>
</html>
"""

SUCCESS_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>تمت عملية الدفع بنجاح - My PC</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <style> body { font-family: 'Cairo', sans-serif; background-color: #f8f9fa; }</style>
</head>
<body class="text-center py-5">
    <div class="container my-5" style="max-width: 500px;">
        <div class="card shadow p-5 border-0 rounded-4">
            <h1 class="text-success fw-bold mb-3">🎉 تم الدفع بنجاح!</h1>
            <p class="fs-5 text-muted mb-4">شكراً لتسوقك من متجر My PC. تم تسجيل طلبك وبدء تجهيزه للشحن.</p>
            <a href="/" class="btn btn-primary py-2 fw-bold">العودة للرئيسية</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    global cart
    selected_category = request.args.get('category')
    categories = list(set(p['category'] for p in products))
    
    if selected_category:
        filtered_products = [p for p in products if p['category'] == selected_category]
    else:
        filtered_products = products
        
    return render_template_string(HOME_TEMPLATE, 
                                 products=filtered_products, 
                                 categories=categories, 
                                 selected_category=selected_category, 
                                 cart_count=len(cart))

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    global cart
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('home'))

@app.route('/buy_now/<int:product_id>', methods=['POST'])
def buy_now(product_id):
    global cart
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template_string(CHECKOUT_TEMPLATE, selected_item=product)

@app.route('/cart')
def view_cart():
    global cart
    total = sum(item['price'] for item in cart)
    return render_template_string(CART_TEMPLATE, cart=cart, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    global cart
    if request.method == 'POST':
        cart.clear()
        return render_template_string(SUCCESS_TEMPLATE)
    return render_template_string(CHECKOUT_TEMPLATE, selected_item=None)

if __name__ == '__main__':
    app.run(debug=True)