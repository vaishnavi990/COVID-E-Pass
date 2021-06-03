import requests
from flask import Flask, render_template,request
from twilio.rest import Client
import requests_cache

account_sid = ''
auth_token = ''

client = Client(account_sid,auth_token)
app = Flask(__name__,static_url_path='/static')
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        source_st = request.form['source_state']
        source_dt = request.form['source']
        destination_st = request.form['dest_state']
        destination_dt = request.form['destination']
        phoneNumber = request.form['phoneNumber']
        id_proof = request.form['idcard']
        date = request.form['trip']
        full_name = fname+" "+lname
        r = requests.get('https://api.covid19india.org/v4/data.json')
        json_data = r.json()
        cnt = json_data[destination_st]['districts'][destination_dt]['total']['confirmed']
        pop = json_data[destination_st]['districts'][destination_dt]['meta']['population']
        travel_pass = ((cnt/pop)*100)
        if travel_pass < 30 and request.method =='POST':
            status = 'CONFIRMED'
            client.messages.create(from_='whatsapp:+14155238886',to='whatsapp:+919705515409',
                                  body="Hello "+" "+full_name+" "+'Your Travel From'+" "+source_dt+" "+"To"+" "+destination_dt+" "+
                                  "Has"+" "+status+" "+"On"+" "+date+" ")
            return render_template('user_registration_details.html',var=full_name,var1=email,var2=id_proof,
                                   var3=source_st,var4=source_dt,var5=destination_st,var6=destination_dt,
                                   var7=phoneNumber,var8=date,var9=status)
        else:
            status = 'NOT CONFIRMED'
            client.messages.create(from_='whatsapp:+14155238886',to='whatsapp:+919705515409',
                                  body="Hello" + " " + full_name + " " + 'Your Travel From' + " " + source_dt + " " + "To" + " " + destination_dt + " " +
                                       "Has" + " " + status +"  "+"On" + " " + date + " "+", Apply later")
            return render_template('user_registration_details.html', var=full_name, var1=email, var2=id_proof,
                                   var3=source_st, var4=source_dt, var5=destination_st, var6=destination_dt,
                                   var7=phoneNumber, var8=date, var9=status)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
