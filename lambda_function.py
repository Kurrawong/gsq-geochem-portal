from mangum import Mangum

from geochem_portal.app import create_app

app = create_app()
lambda_handler = Mangum(app)
