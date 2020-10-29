from flask import Flask, request,jsonify
import json
import requests
import time




def post_data(data):
  eshost = "http://172.24.126.15:9200/"
  auth = auth=requests.auth.HTTPBasicAuth('elastic', 'elastic')
  headers = {'Content-Type':'application/json'}
  date = time.strftime("%Y.%m.%d", time.localtime())
  url = eshost + "backup-monitor-" + date + "/_doc"
  r = requests.post(url, headers=headers,auth=auth,data=data)
  return r.text




app = Flask(__name__)
@app.route("/api/backupinfo",methods=["POST"])
def get_post():
  if request.method == 'POST':
    #data = {
    #      "backup_project" :request.json['backup_project'],
    #      "backup_method" :request.json['backup_method'],
    #      "ip_addr" :request.json['ip_addr'],
    #      "backup_path" :request.json['backup_path'],
    #      "backup_status" :request.json['backup_status'],
    #      "backup_time" :request.json['backup_time']
    #}
    #post_data(json.dumps(data))
    post_data(json.dumps(request.json))
    return jsonify({'status': "ok"})




if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
