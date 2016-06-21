# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, url_for, redirect


bp_module_one = Blueprint('module_one', __name__,
                          template_folder='templates')


@bp_module_one.route('/')
def module_one_index():
    return render_template('login.html', error=None)


@bp_module_one.route('/sub')
def module_one_sub():
    return redirect(url_for('.module_one_index'))
