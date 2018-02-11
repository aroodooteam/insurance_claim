# -*- coding: utf-8 -*-

{
    "name": "Insurance Claim",
    "version": "0.1",
    "author": "Haritiana Rakotomalala <haryoran04@gmail.com>",
    "category": "Insurance",
    "complexity": "normal",
    "data": [
        # "data/templates.xml", # un comment to enable js, css code
        # "security/security.xml",
        # "security/ir.model.access.csv",
        # "views/view.xml",
        # "actions/act_window.xml",
        # "menu.xml",
        # "data/data.xml",
    ],
    "depends": [
        "base",
        "insurance_setup",
        "insurance_management",
    ],
    "qweb": [
        # "static/src/xml/*.xml",
    ],
    "test": [
    ],
    "installable": True,
    "auto_install": False,
}
