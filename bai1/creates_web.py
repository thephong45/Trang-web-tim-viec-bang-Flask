from flask import Flask
import sqlite3


conn = sqlite3.connect("data.db", check_same_thread=False)
conn.commit()
data = conn.execute('SELECT * FROM jobs;')
app = Flask(__name__)


@app.route("/")
def begin():
    result = """<hr><center><h1 style="color:#FF0000;">TRANG TUYỂN DỤNG IT </h1></center><hr><br><center><table border='2'> 
    				<tr>
        		  		<th >TÊN TRANG TUYỂN DỤNG </th>
        		  		<th >LIÊN KẾT WEB TRÊN GITHUB </th>
        		  	</tr> """
    lines = []
    for name, link in data.fetchall():
        line = ''' 
        		  <h3><tr>
        		  	<td>{}</td>
        		  	<td><a href={}>{}</a></td>
        		  </tr>
        		  </h3>
        	   '''.format(name, link, link)
        lines.append(line)
    result += "".join(lines) + "</table><center>"
    return result


if __name__ == "__main__":
    app.run(debug=True)

