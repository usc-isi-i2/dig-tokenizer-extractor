from digExtractor.extractor import Extractor
from digCrfTokenizer.crf_tokenizer import CrfTokenizer
import copy

class TokenizerExtractor(Extractor):

    def __init__(self, setRecognizePunctuation=True, setRecognizeHtmlTags=True, setSkipHtmlEntities=True,
        setRecognizeHtmlEntities=True, setSkipHtmlTags=True, recognize_linebreaks=False,
                 create_structured_tokens=False):
        tokenizer = CrfTokenizer(recognize_linebreaks=recognize_linebreaks,
                                 create_structured_tokens=create_structured_tokens)
        tokenizer.setRecognizePunctuation(setRecognizePunctuation)
        tokenizer.setRecognizeHtmlTags(setRecognizeHtmlTags)
        tokenizer.setSkipHtmlEntities(setSkipHtmlEntities)
        tokenizer.setRecognizeHtmlEntities(setRecognizeHtmlEntities)
        tokenizer.setSkipHtmlTags(setSkipHtmlTags)
        self.tokenizer = tokenizer
        self.metadata = {'extractor': 'tokenizer'}
        self.renamed_input_fields = 'text'

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def set_tokenizer(self, tokenizer):
        self.tokenizer = tokenizer
        return self

    def extract(self, doc):
        results = list()
        results.append(self.tokenizer.tokenize(doc['text'].lower()))
        return results

    def get_renamed_input_fields(self):
        return self.renamed_input_fields;