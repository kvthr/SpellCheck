#######################################################################
# Flask app to correct the spelling of the input word
# #######################################################################
from flask import Flask, request, render_template
from wordProcess import *
from segmentation import *

app = Flask(__name__)

@app.route('/spellCorrect')
def render_form():
    return render_template('index.html')

@app.route('/spellCorrect', methods=['POST'])
def get_word_post():
    text = request.form['text']
    text = text.lower()

    # words separated by " " or "-"
    text = text.replace(' ', '')
    text = text.replace('-', '')
    
    # get top word corrections from probability model
    top_words, top_probs = corrections_topK(text)
    # if the length of top_words in 1 then there is no correction for the text
    # then we try segmentation
    c_flag = False
    if(text in top_words):
        c_flag = True
    # check for possible segmentation
    segmentations = segment(text)
    seg_prob = Pwords(segmentations)

    flag = True
    for w in segmentations:
        if (w not in WORDS) or (len(w)<2):
            flag = False

    if(flag):
        return render_template('index.html', correct=None, segments=segmentations)
    else:
        if(c_flag):
            segmentations = [correction(w) for w in segmentations]
            return render_template('index.html', correct=None, segments=segmentations)
        else:
            return render_template('index.html', correct=top_words, segments=None)

if __name__=="__main__":
    app.run()