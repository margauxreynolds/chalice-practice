from chalice import Chalice

app = Chalice(app_name='run-on-schedule')

instance_id = "id-1234123412341234123"
ec2 = boto3.client('ec2')


@app.schedule('cron(0 0 * * *')')
def daily task():
    print("Running daily task at midnight")
    response = ec2.start_instances(instance_id)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
