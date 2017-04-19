from tests import get_model, oauth2, storage
from flask import Blueprint, current_app, redirect, render_template, request, \
    session, url_for

crud = Blueprint('crud', __name__)

@crud.route("/")
def default():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    tests, next_page_token = get_model().list(cursor=token)

    return render_template(
        "home.html",
        tests=tests,
        next_page_token=next_page_token)


@crud.route("/all")
@oauth2.required
def listAllTest():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    tests, next_page_token = get_model().list_by_user(
        user_id=session['profile']['id'],
        cursor=token)

    return render_template(
        "list.html",
        tests=tests,
        next_page_token=next_page_token)


@crud.route('/<id>')
def viewTest(id):
    test = get_model().read(id)
    return render_template("view.html", test=test)

@crud.route('/add', methods=['GET','POST'])
def addTest():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        if 'profile' in session:
            data['owner'] = session['profile']['displayName']
            data['owner_id'] = session['profile']['id']

        test = get_model().create(data)

        return redirect(url_for('.view', id=test['id']))

    return render_template("form.html",action="Adding", test={})

@crud.route('/edit/<id>', methods=['GET','POST'])
def editTest(id):
    test = get_model().read(id)

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        test = get_model().update(data, id)

        return redirect(url_for('.view', id=test['id']))

    return render_template("form.html", action="Editing", test=test)


@crud.route('/delete/<id>')
def deleteTest(id):
    get_model().delete(id)
    return redirect(url_for('.list'))
