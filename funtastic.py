from flask import Flask,render_template, send_from_directory
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'milan'
app.config['MYSQL_DATABASE_PASSWORD'] = 'nightfury'
app.config['MYSQL_DATABASE_DB'] = 'milan'
app.config['MYSQL_DATABASE_HOST'] = 'milan.cqxf1eojtngf.us-west-2.rds.amazonaws.com'
mysql.init_app(app)

@app.route('/')
@app.route('/index.html/')
def index():
	return "Index page"

@app.route('/leaderboard/')
def leaderboard():
  con = mysql.connect()
  with con:
      cur = con.cursor()
      cur.execute("select * from (select * from leaderboard where level>0 order by level desc) a order by utime;")
      data=cur.fetchall()
  cur.close()
  con.close()
  return render_template('leaderboard.html',data=data)

@app.route('/download/')
def download():
  try:
    return send_file("/var/www/funtastic.ml/static/funtastic.apk", attachment_filename='funtastic.apk')
  except Exception as e:
    return str(e)
    
  
  
  

@app.route('/<hash>/<teamnum>/<level>/')
def test(hash,teamnum,level):
	if hash=="827ccb0eea8a706c4c34a16891f84e7b":
		con=mysql.connect()
		with con:
			cur = con.cursor()
			cur.execute("UPDATE leaderboard set level="+str(level)+" WHERE teamnumber= "+str(teamnum)+" ;"+ "UPDATE leaderboard set utime=now() WHERE teamnumber= "+str(teamnum)+" ;")
      # cur.execute("UPDATE leaderboard set utime=now() WHERE teamnumber= "+str(teamnum)+" ;")
   		cur.close() 
   		con.close()
   		return "Updated"
   	else: return "DB error"

    


@app.route('/finit/')
def finit():
    con=mysql.connect()

    

    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS leaderboard")
        cur.execute("CREATE TABLE leaderboard (teamnumber INTEGER PRIMARY KEY, level INTEGER, utime timestamp)")

        for x in range(1,51):
            cur.execute("INSERT INTO leaderboard (teamnumber, level, utime) VALUES ("+str(x)+", 0, now())")

    cur.close()
    con.close()

    return "Funtastic Database Initialized"


if __name__ == '__main__':
    app.run()
