"""
Account Service

This microservice handles the lifecycle of Accounts
"""
# pylint: disable=unused-import
from flask import jsonify, request, make_response, abort, url_for   # noqa; F401
from service.models import Account
from service.common import status  # HTTP Status Codes
from . import app  # Import Flask application


############################################################
# Health Endpoint
############################################################
@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), status.HTTP_200_OK


######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
    """Root URL response"""
    return (
        jsonify(
            name="Account REST API Service",
            version="1.0",
            # paths=url_for("list_accounts", _external=True),
        ),
        status.HTTP_200_OK,
    )


######################################################################
# CREATE A NEW ACCOUNT
######################################################################
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """
    Creates an Account
    This endpoint will create an Account based the data in the body that is posted
    """
    app.logger.info("Request to create an Account")
    check_content_type("application/json")
    account = Account()
    account.deserialize(request.get_json())
    account.create()
    message = account.serialize()
    # Uncomment once get_accounts has been implemented
    # location_url = url_for("get_accounts", account_id=account.id, _external=True)
    location_url = "/"  # Remove once get_accounts has been implemented
    return make_response(
        jsonify(message), status.HTTP_201_CREATED, {"Location": location_url}
    )

######################################################################
# LIST ALL ACCOUNTS
######################################################################

# ... place you code here to LIST accounts ...
def test_get_account_list(self):
    """It should Get a list of Accounts"""
    self._create_accounts(5)
    resp = self.client.get(BASE_URL)
    self.assertEqual(resp.status_code, status.HTTP_200_OK)
    data = resp.get_json()
    self.assertEqual(len(data), 5)

def test_list_empty_accounts(self):
    # Ensure there are no accounts in the database
    db.session.query(Account).delete()
    db.session.commit()

    # Make a GET request to the endpoint
    response = self.client.get(BASE_URL)

    # Check if the response status code is HTTP_200_OK
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Check if the response data is an empty list
    data = response.get_json()
    self.assertEqual(data, [])


######################################################################
# READ AN ACCOUNT
######################################################################

# ... place you code here to READ an account ...
def test_get_account(self):
    """It should Read a single Account"""
    account = self._create_accounts(1)[0]
    resp = self.client.get(f"{BASE_URL}/{account.id}", content_type="application/json"
    )
    self.assertEqual(resp.status_code, status.HTTP_200_OK)
    data = resp.get_json()
    self.assertEqual(data["name"], account.name)

def test_get_account_not_found(self):
    """It should not Read an Account that is not found"""
    resp = self.client.get(f"{BASE_URL}/0")
    self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)


######################################################################
# UPDATE AN EXISTING ACCOUNT
######################################################################

# ... place you code here to UPDATE an account ...


######################################################################
# DELETE AN ACCOUNT
######################################################################

# ... place you code here to DELETE an account ...


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################


def check_content_type(media_type):
    """Checks that the media type is correct"""
    content_type = request.headers.get("Content-Type")
    if content_type and content_type == media_type:
        return
    app.logger.error("Invalid Content-Type: %s", content_type)
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}",
    )
