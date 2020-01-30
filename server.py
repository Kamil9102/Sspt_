from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Календарь"
    activity = "время"
    if activity:
        activity_current = f"Самое дорогое в жизни - {activity}!"
        print(activity_current)
    else:
        activity_current = "Сервис недоступен"
    return render_template('index.html', page_title=title, activity=activity_current)

@app.route('/', methods=["GET"])
def index2():
    plans = request.args.get('Какие планы?')
    time = request.args.get('Рекомендуемое время')
    print(plans)
    print(time)

if __name__ == "__main__":
    app.run()