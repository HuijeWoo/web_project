from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

win01_page = Blueprint('win01_page', __name__, 
                       template_folder='templates',
                       url_prefix='/win01')

# win01_page.add_url_rule("/", methods=['GET','POST'], view_func=)