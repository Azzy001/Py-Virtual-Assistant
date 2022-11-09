import wolframalpha
import wikipedia

while True:
    user = input("Question: ")

    try:
        # wolframalpha
        api_id = "******-**********"
        client = wolframalpha.Client(api_id)
        result = client.query(user)
        answer = next(result.results).text
        print(answer)
    except:
        # wikipedia
        print(wikipedia.summary(user))