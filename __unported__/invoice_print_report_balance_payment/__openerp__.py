# -*- encoding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "Print invoices with balance payments",
    'version': '1.0',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    "category": "Accounting & Finance",
    'summary': "Prints invoices with balance payments (and other things)",
    'description': """
Print invoices with balance payments
====================================
Changes the default invoice layout to add a few things, the main of which is the balance payment
fields. Under the Total field, 3 new lines appear:

* Previous balance: The previous balance of the customer at the date of the previous invoice.
* Payments: The amount of payments that have been made between the date of the last invoice and \
the date of the printed invoice.
* To Pay: The total amount owed by the customer at the date of this invoice.

Also, it changes two minor and unrelated aspects:

* Replaces "Source" by "Contract Number".
* Removes the Tax column in the invoice line table.

Contributors:
-------------
* Virgil Dupras (virgil.dupras@savoirfairelinux.com)
""",
    "depends": ['account'],
    'external_dependencies': {
        'python': [],
    },
    'data': [],
    'update_xml': [
        'reports.xml',
    ],
    'demo': [],
    'test': [],
    'installable': False,
    'active': False,
}
