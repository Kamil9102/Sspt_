from flask import Flask, render_template, request
import os


app = Flask(__name__)

@app.route('/')
def index():
    title = "Планер"
    activity = "время"
    if activity:
        activity_current = f"Самое дорогое в жизни - {activity}!"
        print(activity_current)
    else:
        activity_current = "Сервис недоступен"

    return render_template('index.html', page_title=title, activity=activity_current)
    
#Это из-за изменения в форме бутстрапа, теперь при нажатии на кнопку запрос отправится сюда
@app.route('/test', methods=["GET"])
def index2():
    plans = request.args.get('Какие планы?')
    time = request.args.get('Рекомендуемое время')
    print(plans)
    print(time)
    return index()

if __name__ == "__main__":
    app.run()
