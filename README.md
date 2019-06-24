# SpellCheck

I used the spell checker written by [Peter Norvig](https://norvig.com/spell-correct.html). It is based on occurances of words(word counts) in large corpus of English text. 

### What did I add to the existing SpellChecker?

Most of the features in this Flask app are already implemented in the source. I tried to tackle the word segmentation that is segment the word which is a concatenation of two words. To do this, I did segmentation and calculated the occurance of the resultant word as suggested by the author and added some sanity checks to make segmentation more meaningful in `app.py` using `c_flag` and `flag`.

#### Drawbacks

This program fails when there is concatenation of two badly spelled words. Example, `clus-room` is not corrected to `classroom` or `class-room`. The two segments of the word should be correctly spelled.

### Improvements

There are many more improvements that can be done to this basic spell checker. If we want to incorporate Deep Learning into this we can calculate the word occurance probabilities using character level RNNs(similar to language model). We can use context aware models to correct the spelling according to the context of word appearance.

### Running the Flask App

Install the required libraries:
```
pip install -r requirements.txt
```

Run the command:
```
python app.py
```

Go the app URL: 
`http:0.0.0.0:5000/spellCorrect`
