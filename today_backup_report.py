# !/usr/bin/env python3 
# Author: zuoguocai@126.com

from datetime import datetime
import  zmail


def  mail_push(content_html):
    server = zmail.server('myemail', 'pass', smtp_host='host', smtp_port=25,smtp_tls=True, smtp_ssl=False)
    mail = {
        'subject': '今日备份报告',
        'content_html': content_html,
    }
    server.send_mail('myemail',mail)
    

content='''<style type="text/css" media="screen">
body {
    font-family: PingFang SC, Verdana, Helvetica Neue, Microsoft Yahei, Hiragino Sans GB, Microsoft Sans Serif, WenQuanYi Micro Hei, sans-serif;
    font-size: 14px;
}
h1 {
    font-size: 16pt;
    color: gray
}
.heading {
    margin-top: 0;
    margin-bottom: 1ex
}
.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0
}
.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex
}
#result_table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #777
}

#header_row {
    color: #fff;
    background-color: #777
}

#result_table td {
    border: 1px solid #777;
    padding: 2px;
}



#result_table td:first-of-type {
    text-align: center;
    min-width: 60px;
}

#total_row {
    font-weight: bold
}

.passClass,
.failClass,
.errorClass,
.skipClass {
    font-weight: bold
}

.passCase {
    background-color: #97cc64
}

.failCase {
    background-color: #fd5a3e
}

.errorCase {
    background-color: #ffd050
}

.skipCase {
    background-color: #aaa
}



.testcase {
    margin-left: 2em
}




</style>
 
</head>

<body>

    <div class='heading'>
  <h1 align='center'>今日备份报告</h1>
  <p class='attribute'>
    <strong>
      <span class="lang-cn">启动时间：</span>
      <span class="lang-en">Start Time:</span>
    </strong> 2020-11-11 10:18:18
  </p>
  <p class='attribute'>
    <strong>
      <span class="lang-cn">结束时间：</span>
      <span class="lang-en">End Time:</span>
    </strong> 2020-11-11 10:20:39
  </p>
  <p class='attribute'>
    <strong>
      <span class="lang-cn">运行时长：</span>
      <span class="lang-en">Duration:</span>
    </strong> 0:02:21.045219
  </p>
  <p class='attribute'>
    <strong>
      <span class="lang-cn">结果：</span>
      <span class="lang-en">Status:</span>
    </strong>
    <span class="lang-cn">合计：</span>
    <span class="lang-en">Total:</span>74&nbsp;&nbsp;&nbsp;&nbsp;
    <span class="lang-cn">成功：</span>
    <span class="lang-en">Passed:</span>35&nbsp;&nbsp;&nbsp;&nbsp;
    <span class="lang-cn">失败：</span>
    <span class="lang-en">Failed:</span>5&nbsp;&nbsp;&nbsp;&nbsp;

  </p>
  
  
  <br>
  <br>
  <br>
  <br>
  
  
<table id='result_table'>

<tr id='header_row'>
        <th>
            <span class="lang-cn">序号</span>         
        </th>
        <th>
            <span class="lang-cn">备份名称</span>        
        </th>
        <th>
            <span class="lang-cn">备份方式</span>   
        </th>
        <th>
            <span class="lang-cn">备份IP</span>   
        </th>
        <th>
            <span class="lang-cn">备份路径</span>   
        </th>
        <th>
            <span class="lang-cn">备份状态</span>      
        </th>
        <th>
            <span class="lang-cn">备份时间</span>          
        </th>     
    </tr>
      
<tr id='pt1.1'>
   <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">1</div>
    </td>
   <td class='errorCase' align='center'>
        <div class='testcase' style="margin-left: auto;">zabbix</div>
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">mysqldump</div>
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">172.24.126.4</div>
    </td>
    <td class='skipCase' align='center'>
        <div class='testcase' style="margin-left: auto;">/tmp/1.sql</div>
    </td>
    <td class='passCase' align='center'>     
            <span class="lang-cn">成功</span>    
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">2020年11月11日16:48:35</div>
    </td>   
</tr> 
<tr id='pt1.2'>
   <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">2</div>
    </td>
   <td class='errorCase' align='center'>
        <div class='testcase' style="margin-left: auto;">DNS</div>
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">email</div>
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">172.24.126.4</div>
    </td>
    <td class='skipCase' align='center'>
        <div class='testcase' style="margin-left: auto;">/tmp/1.zone</div>
    </td>
    <td class='passCase' align='center'>     
            <span class="lang-cn">成功</span>    
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">2020年11月11日16:48:35</div>
    </td>   
</tr> 

     
<tr id='pt1.3'>
   <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">3</div>
    </td>
   <td class='errorCase' align='center'>
        <div class='testcase' style="margin-left: auto;">elasticsearch templates</div>
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">elasticdump</div>
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">172.24.126.4</div>
    </td>
    <td class='skipCase' align='center'>
        <div class='testcase' style="margin-left: auto;">/tmp/1.json</div>
    </td>
    <td class='failCase' align='center'>     
            <span class="lang-cn">失败</span>    
    </td>
    <td class='passCase' align='center'>
        <div class='testcase' style="margin-left: auto;">2020年11月11日16:48:35</div>
    </td>   
</tr>
</table></body> '''

mail_push(content)
