from website import create_app

app = create_app()

if(__name__ == "__main__"):
    app.run(debug=True)
    #when running in production, set debug to false