#!/usr/bin/env python3
##author: zuoguocai@126.com
## html report
import zmail

def genHtmltable(color,jsonList):

  table_begin = '''<table align="center" border="1" cellpadding="1" cellspacing="1" width="100%" style="border-collapse: collapse;border:1px #9cf solid;">'''
  table_end = '''</table>'''
  if color == "blue":
    begin_head = '''<td style="border:1px #fff solid;background:#9cf;padding: 1px 0 1px 0; color: #fff; font-size: 14px; font-weight: bold; font-family: Arial, sans-serif;height:28px;text-align:center">'''
  elif color == "orange":
    begin_head = '''<td style="border:1px #fff solid;background:#f85415;padding: 1px 0 1px 0; color: #fff; font-size: 14px; font-weight: bold; font-family: Arial, sans-serif;height:28px;text-align:center">'''
  begin_content = '''<td style="border:1px #9cf solid;background:#fff;padding: 1px 0 1px 0; color: #153643; font-size: 12px; font-family: Arial, sans-serif;height:28px;text-align:center">'''
  end_content = '''</td>'''
  html2 = ""

  for i in range(len(jsonList)):
    line_html = ""
    for key in jsonList[0].keys():
      if i != 0:
        line = "".join((begin_content,str(jsonList[i][key]),end_content))
      else:
        line = "".join((begin_head,str(jsonList[i][key]),end_content))
      line_html += line
    lineplus = "".join(('<tr>',line_html,'</tr>'))
    html2 += lineplus

  return "".join((table_begin,html2,table_end))



def  mail_push(to,subject,content_html):
  server = zmail.server('user', 'passwd', smtp_host='url', smtp_port=25,smtp_tls=True, smtp_ssl=False)
  mail = {
    'subject': subject,
    'content_html': content_html,
  }
  #server.send_mail(['zuoguocai@126.com','zuoguocai@outlook.com'],mail)
  server.send_mail(to,mail)





  ## 查询数据库组成数据结构
  ## elastisearch 查询
def get_data():
  eshost = "http://172.24.126.15:9200/"
  auth = auth=requests.auth.HTTPBasicAuth('elastic', 'elastic')
  headers = {'Content-Type':'application/json'}
  url = eshost + "backup-monitor.2020.10.28/_search?pretty=true&q=*:*"
  r = requests.get(url, headers=headers,auth=auth)
  result = r.json()
  output = result['hits']['hits']
  Allitem = [{"backup_id":"backup_id","backup_project":"backup_project","backup_method":"backup_method","ip_addr":"ip_addr","backup_path":"backup_path","backup_status":"backup_status","backup_time":"backup_time"}]
  for i in output:
    item = {"backup_id":i['_id'],"backup_project":i['_source']['backup_project'],"backup_method":i['_source']['backup_method'],"ip_addr":i['_source']['ip_addr'],"backup_path":i['_source']['backup_path'],"backup_status":i['_source']['status'],"backup_time":i['_source']['backup_time']}
    Allitem.append(item)
  return Allitem


  
def trigger_http():

  ## 数据结构
  #jsonList=[
    #{"backup_project":"backup_project","backup_method":"backup_method","ip_addr":"ip_addr","backup_path":"backup_path","backup_status":"backup_status","backup_time":"backup_time"},
    #{"backup_project":"Zabbix数据库","backup_method":"mysqldump","ip_addr":"172.20.250.217","backup_path":"//data","backup_status":"ok","backup_time":"2020年10月16日15:38:10"},
    #{"backup_project":"Jumpserver数据库","backup_method":"mysqldump","ip_addr":"172.20.250.218","backup_path":"//data","backup_status":"ok","backup_time":"2020年10月16日15:38:10"},
    #{"backup_project":"DNS Record","backup_method":"email","ip_addr":"172.20.250.219","backup_path":"//data","backup_status":"ok","backup_time":"2020年10月16日15:38:10"},
    #{"backup_project":"Grafana Template","backup_method":"shell","ip_addr":"172.20.250.220","backup_path":"//data","backup_status":"ok","backup_time":"2020年10月16日15:38:10"},
    #{"backup_project":"OpenStack Config","backup_method":"shell","ip_addr":"172.20.250.221","backup_path":"//data","backup_status":"ok","backup_time":"2020年10月16日15:38:10"}
  #]
  
  jsonList = get_data()
  ## 颜色定义 支持blue,orange 
  send_body = genHtmltable("orange",jsonList)
  send_title = '''<h2 style="color:black ;display:inline;text-align: center; ">今日备份CheckList</h2>'''
  content_html = "".join((send_title,send_body))
  mail_push("zuoguocai","今日备份CheckList一览",content_html)


trigger_http()
