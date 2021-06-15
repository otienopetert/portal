
import nexmo

client = nexmo.Client(key='d362a680', secret='7Al18gG0lnAeH4Fl')

client.send_message({
    'from': 'Vonage APIs',
    'to': '255769490287',
    'text': 'Hello from Vonage SMS API',
})
