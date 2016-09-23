from digExtractor.extractor import Extractor
from digCrfTokenizer.crf_tokenizer import CrfTokenizer
import copy

class TokenizerExtractor(Extractor):

    def __init__(self):
        tokenizer = CrfTokenizer()
        tokenizer.setRecognizePunctuation(True)
        tokenizer.setRecognizeHtmlTags(True)
        tokenizer.setSkipHtmlEntities(True)
        tokenizer.setRecognizeHtmlEntities(True)
        tokenizer.setSkipHtmlTags(True)
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
        return self.tokenizer.tokenize(doc['text'].lower())

    def get_renamed_input_fields(self):
        return self.renamed_input_fields;