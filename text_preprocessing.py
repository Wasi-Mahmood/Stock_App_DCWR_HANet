import pandas as pd
import spacy
import en_core_web_lg
import time
from FunctionProgress1 import Progress
nlp = en_core_web_lg.load()



def artical_to_sentence(text):
    sentence_list =[]
    doc = nlp(text)
    
    for sents in doc.sents:
        sentence_list.append(str(sents))
    return sentence_list



def text_normalization_for_sentiment_analysis(text_list):
    sentence_list =[]
    for text in text_list:
        doc = nlp(text)
        norm_text =[]
        for token in doc:
            if not token.is_punct and not token.is_space:
                norm_text.append(token.lemma_)
        sentence_list.append(' '.join(norm_text))
        
    return sentence_list


def preprocessing(text):
    return text_normalization_for_sentiment_analysis(artical_to_sentence(text))

def dataset_preprocessing(dataframe,column_name):
    artical_list =[]
    total_indexes =len(dataframe)
    progress = Progress()
    for count in range(len(dataframe)):
        start_time = time.time()
        artical = dataframe[column_name][count]
        artical_list.append(text_normalization_for_sentiment_analysis(artical_to_sentence(artical)))
        time_taken = time.time() - start_time
        progress.print_progress(count,total_indexes,time_taken)
        
    return artical_list
        
        
        
# class Progress:
#     time_taken_list =[]
#     def print_progress(self,current_index:int, total_indexes:int, time_taken: time):
#         self.time_taken_list.append(time_taken)
#         average_time = sum(self.time_taken_list)/len(self.time_taken_list)
#         estd_time_to_complt = average_time * total_indexes
#         print(f"{current_index}/{total_indexes} completed in {time_taken: .2f} seconds. Estimated Time to Complete: {estd_time_to_complt}", end='\r')

        
        
