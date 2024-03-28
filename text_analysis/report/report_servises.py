import math

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


class Report:
    """
    Class contains the results of analyzing a corpus of documents
    """

    def __init__(self, data):
        self.data = data

    def show_report(self) -> dict:
        """
        Returns a dictionary containing the analysis results, sorted by IDF value
        """
        return dict(sorted(self.data.items(), key=lambda item: item[1]["idf"], reverse=True)[:50])


class CreateReport:
    """
    Class analyzes the document corpus and returns the Report class with the analysis results
    """

    def __init__(self, file_object):
        self.documents = self.get_documents(file_object)
        self.word_reports = {}

    def get_documents(self, file_object) -> list[str]:
        """
        Retuns a corpus of documents
        """
        decoded_file = file_object.read().decode()
        documents = [document for document in decoded_file.split("\n") if document]
        return documents

    @staticmethod
    def get_document_key(document: str, words: int = 4) -> str:
        """
        Returns a string with the specified number of first words in the document.
        """
        return " ".join(document.split()[:words]) + " ..."

    def get_words_in_documents(self) -> list[list[str]]:
        """
        Returns a list of lists of words from documents
        """
        words_in_documents = []
        for i in range(len(self.documents)):
            words_in_documents.append([self.words[j] for j in self.word_presence_matrix[i].indices])
        return words_in_documents

    def get_count_of_words_in_documents(self) -> dict:
        """
        Returns the dict with number of words in the documents that were parsed.
        """
        count_of_words = {}

        for i in range(len(self.documents)):
            word_indices = self.word_presence_matrix[i].nonzero()[1]
            count_of_words[i] = {}
            for index in word_indices:
                word = self.words[index]
                freq = self.word_presence_matrix[i, index]
                count_of_words[i][word] = freq

        return count_of_words

    def get_word_info_per_document(self, word) -> dict[str, str | int | float]:
        """
        Returns the dict with word information for each document
        """
        word_info = {}

        for document_index, words in self.count_of_words_in_documents.items():
            word_info[document_index] = {}
            word_info[document_index]["word"] = word
            word_info[document_index]["document_key"] = self.get_document_key(self.documents[document_index])
            word_info[document_index]["count"] = 0
            word_info[document_index]["word_count"] = len(self.words_in_documents[document_index])
            if word in words:
                word_info[document_index]["count"] += words[word]
            word_info[document_index]["tf"] = (
                word_info[document_index]["count"] / word_info[document_index]["word_count"]
            )

        return word_info

    def analyze(self):
        """
        Creates collections with analysis results

        Perhaps he is doing black magic...
        """
        count_vectorizer = CountVectorizer()
        self.word_presence_matrix = count_vectorizer.fit_transform(self.documents)
        self.words = count_vectorizer.get_feature_names_out()
        self.word_count_per_document = np.asarray(self.word_presence_matrix.sum(axis=0)).flatten()
        self.words_in_documents = self.get_words_in_documents()
        self.count_of_words_in_documents = self.get_count_of_words_in_documents()

    def get_report_data(self) -> dict:
        """
        Collects information about documents into a dictionary.
        """
        self.analyze()

        word_data = {}
        for word, count in zip(self.words, self.word_count_per_document):
            document_counter = sum(document_words.count(word) for document_words in self.words_in_documents)
            word_info = self.get_word_info_per_document(word)
            word_data[word] = {
                "count": count,
                "documents_count": len(self.documents),
                "documents_with_word": document_counter,
                "idf": math.log10(len(self.documents) / document_counter),
                "word_info": word_info,
            }

        return word_data

    def create_report(self) -> Report:
        """
        Returns Report class containing the analysis results
        """
        data = self.get_report_data()
        return Report(data)
