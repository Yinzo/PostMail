from flask import Flask, request, jsonify
from postmail import MailSender

app = Flask(__name__)
mail_sender = MailSender()


@app.route('/')
def homepage():
    return "MailSender is online!"

@app.route('/mail', methods=['POST'])
def mail():
    mail_sender.send(**request.form.to_dict())
    try:
        return jsonify({'status': 'succeed', 'msg': ""})
    except Exception as ex:
        return jsonify({'status': 'failed', 'msg': str(ex)})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
