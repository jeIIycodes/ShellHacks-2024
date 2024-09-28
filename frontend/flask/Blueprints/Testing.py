from flask import Blueprint,jsonify

test_bp=Blueprint("lp", __name__, url_prefix="/testing")


@test_bp.route('/TestRoute')
def helloWorld():
    return jsonify({"Hello": "World"})

@test_bp.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1,num2):
    return f"{num1 * num2}"