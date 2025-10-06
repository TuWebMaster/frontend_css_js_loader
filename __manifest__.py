# -*- coding: utf-8 -*-
{
    "name": "Frontend CSS/JS Loader",
    "summary": "CSS & JS personalizados para el Website",
    "description": """
Módulo para inyectar y mantener código CSS/JS en el frontend del Website.
Incluye assets versionados vía manifest para cambios persistentes.
Desarrollado por: Tu Web Master — https://www.tuwebmaster.com.ar
    """,
    "version": "18.0.1.0.0",
    "author": "Tu Web Master",
    "website": "https://www.tuwebmaster.com.ar",
    "license": "LGPL-3",
    "category": "Website",
    "depends": ["base", "web", "website", "website_sale"],

    # Data files (add here your QWeb/OWL views if needed)
    "data": [
        "views/views.xml",
        "views/move_sections.xml",
        # "views/templates.xml",  # enable only if you actually have QWeb templates
    ],

    # Demo data (optional)
    "demo": [
        # "demo/demo.xml",
    ],

    # Web assets for frontend
    "assets": {
        "web.assets_frontend": [
            "frontend_css_js_loader/static/src/js/website.js",
            "frontend_css_js_loader/static/src/css/style.css",
        ],
    },

    # Optional: images shown in the Apps page (if present)
    # "images": [
    #     "static/description/icon.png",
    #     "static/description/screenshot-1.png",
    # ],

    "installable": True,
    "application": False,
    "auto_install": False,
}
