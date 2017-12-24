from flask import Flask,render_template, send_from_directory, request
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'milan'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dbms12345'
app.config['MYSQL_DATABASE_DB'] = 'akcsc'
app.config['MYSQL_DATABASE_HOST'] = 'dbms.cqxf1eojtngf.us-west-2.rds.amazonaws.com'
mysql.init_app(app)

@app.route('/')
@app.route('/index.html/')
def index():
	return "Index page"

# @app.route('/leaderboard/')
# def leaderboard():
#   con = mysql.connect()
#   with con:
#       cur = con.cursor()
#       cur.execute("select teamnumber as t,level, timestampdiff(second, (select utime from leaderboard where level = 0 group by level), (select utime from leaderboard where teamnumber=t) ) as time from leaderboard where level>0 order by level desc,time;")
#       data=cur.fetchall()
#   cur.close()
#   con.close()
#   return render_template('leaderboard.html',data=data)

# @app.route('/download/')
# def download():
#   try:
#     return send_file("/var/www/funtastic.ml/static/funtastic.apk", attachment_filename='funtastic.apk')
#   except Exception as e:
#     return str(e)
    
  
  
  

# @app.route('/<hash>/<teamnum>/<level>/')
# def test(hash,teamnum,level):
# 	if hash=="827ccb0eea8a706c4c34a16891f84e7b":
# 		con=mysql.connect()
# 		with con:
# 			cur = con.cursor()
# 			cur.execute("UPDATE leaderboard set level="+str(level)+" WHERE teamnumber= "+str(teamnum)+" ;"+ "UPDATE leaderboard set utime=now() WHERE teamnumber= "+str(teamnum)+" ;")
#       # cur.execute("UPDATE leaderboard set utime=now() WHERE teamnumber= "+str(teamnum)+" ;")
#    		cur.close() 
#    		con.close()
#    		return "Updated"
#    	else: return "DB error"

    


# @app.route('/finit/')
# def finit():
#     con=mysql.connect()

    

#     with con:
#         cur = con.cursor()
#         cur.execute("DROP TABLE IF EXISTS leaderboard")
#         cur.execute("CREATE TABLE leaderboard (teamnumber INTEGER PRIMARY KEY, level INTEGER, utime timestamp)")

#         for x in range(1,51):
#             cur.execute("INSERT INTO leaderboard (teamnumber, level, utime) VALUES ("+str(x)+", 0, now())")

#     cur.close()
#     con.close()

#     return "Funtastic Database Initialized"


@app.route('/contact/', methods = ['POST'])
def contact():
  name=request.form["name"]
  email=request.form["email"]
  message=request.form["message"]
  con = mysql.connect()
  cur = con.cursor()
  cur.execute("insert into contact_form values('"+name+"','"+email+"','"+message+"');commit")
  cur.close()
  con.close()
  return "Submited Sucessfully"

if __name__ == '__main__':
    app.run(debug=True)
