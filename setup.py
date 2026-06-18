import os

folders = [
    "database",
    "models",
    "routes",
    "utils",
    "templates",
    "reports",
    "static/css",
    "static/js",
    "static/images"
]

files = [
    "app.py",
    "config.py",
    "requirements.txt",
    "README.md",

    "database/pharmacy.db",
    "database/schema.sql",

    "models/__init__.py",
    "models/user.py",
    "models/medicine.py",
    "models/category.py",
    "models/supplier.py",
    "models/customer.py",
    "models/employee.py",
    "models/sale.py",
    "models/purchase.py",
    "models/inventory.py",
    "models/billing.py",

    "routes/auth_routes.py",
    "routes/medicine_routes.py",
    "routes/supplier_routes.py",
    "routes/customer_routes.py",
    "routes/sales_routes.py",
    "routes/purchase_routes.py",
    "routes/dashboard_routes.py",
    "routes/report_routes.py",

    "utils/auth.py",
    "utils/barcode.py",
    "utils/invoice.py",
    "utils/backup.py",
    "utils/validators.py",

    "templates/login.html",
    "templates/dashboard.html",
    "templates/medicines.html",
    "templates/sales.html",
    "templates/invoice.html"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Project structure created successfully!")