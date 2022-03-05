# pip install connexion[swagger-ui]
# pip install markupsafe==2.0.1

import connexion
from flask_cors import CORS

app = connexion.App(__name__, specification_dir='openapi/')

app.add_api('api-config.yaml')

print("Running?..")
if __name__ == '__main__':
    app.run(port=8081, debug=True)

'''
-> API (dockerfile for api engine)
-> model (config) -> node
-> model-dev (dockerfile for model training)
'''