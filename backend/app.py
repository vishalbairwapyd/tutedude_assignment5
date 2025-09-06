from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo

app = Flask(__name__)


# start database configure
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
# client.admin.command('ping')  # Quick and safe connection test
# print(" MongoDB Atlas connection successful.")
collection = db['student_records']
# end database configure

@app.route('/')
def home():
    return "Backend Running Successfully!"

@app.route('/receive', methods=['POST'])
def receive_data():
    try:
        # Get form data from Express
        data = request.get_json()
        print("✅ Received Student Data:", data)

        if data is None:
            print("You dont send data.")
            return jsonify({
                "status": "Failed",
                "message": "Please submit data.",
                "data": data
            })


        if data.get('email'):
            record = collection.find_one({'email': data['email']})
            print("redord==> ", record)

            if record is None:
                result = collection.insert_one(data)
                print("result==> ", result)
                return jsonify({
                    "status": "success",
                    "message": "Student data received successfully",
                    "inserted_id": str(result.inserted_id)
                }) 
            else:
                return jsonify({
                    "status": "Failed",
                    "message": f"{data.get('email')} is already found."
                })
             
    except Exception as e:
        return jsonify({
            "status": "Server Error",
            "message": "An Error occured while submiting.Please retry after some time."
        })
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


