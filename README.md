# htmlreport

```
curl -u elastic:elastic -X PUT \
 http://127.0.0.1:9200/_template/backup-monitor_template \
 -H 'content-type:application/json' \
 -d '{
   "template": "backup-monitor*",
   "index_patterns": ["backup-monitor*"],
   "settings" : {
      "index" : {
         "number_of_replicas" : 1,
         "number_of_shards" : 3
      }
   },
   "mappings" : {
            "properties": { 
               "backup_project":{"type":"text"},
               "backup_method":{"type":"text"},
               "ip_addr":{"type":"ip"},
               "backup_path":{"type":"text"},
               "backup_status":{"type":"text"},
               "backup_time":{"type":"date"}
            }
   }
}'



```
