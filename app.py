from flask import Flask, render_template
from histogram import histogram
from sample import sample, words_list
from markov import MarkovChain


app = Flask(__name__)

@app.route('/')
def markov():
    word_list = words_list()
    markov_chain = MarkovChain(word_list)
    sentence = markov_chain.walk(10)

    return render_template('index.html', tweet=sentence)
 


@app.route('/histogram')
def generate_words():
    #build a histogram
    filename = open("./adamsmith.txt", "r")
    lines = filename.readlines()
    my_histogram = histogram(lines)
    print(my_histogram)

    sentence = ""
    num_words = 10
    for i in range(num_words):
        word = sample(my_histogram)
        sentence += " " + word

    return render_template('index.html', tweet=sentence)



if __name__ == '__main__':
    app.run()