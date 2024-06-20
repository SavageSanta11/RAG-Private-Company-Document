import re
import numpy as np
from tqdm import tqdm

from statistics import mean
import pandas as pd
from statistics import mean

import evaluate

def calculate_metric_score(metric_name,references, predictions):
    if metric_name != "bleurt":
        metric = evaluate.load(metric_name)
    else:
        metric = evaluate.load(metric_name, module_type='metric')

    if metric_name != "bertscore":
        if metric_name == 'bleu':
            results = metric.compute(predictions=predictions, references=references, smooth = True)
        else:
            results = metric.compute(predictions=predictions, references=references)
    else:
        results = metric.compute(predictions=predictions, references=references, lang='en')
                
    return results


def generate_metrics_summary(references, prediction_dict):

    results = {}

    # #ROUGE
    rouge_results = {}
    print("Calculating ROUGE Score...")
    for prediction_label, predictions in prediction_dict.items():
        metric_result = calculate_metric_score('rouge', references, predictions)
        rouge_results[prediction_label] = metric_result
    
    rouge_df = pd.DataFrame(rouge_results).T.reset_index().rename(columns={"index": "System"})
    results["rouge"] = rouge_df

    # # BLEU
    bleu_results = {}
    print("Calculating BLEU Score...")
    for prediction_label, predictions in prediction_dict.items():
        metric_result = calculate_metric_score('bleu', references, predictions)
        metric_result.pop("precisions")
        metric_result.pop("brevity_penalty")
        metric_result.pop("length_ratio")
        metric_result.pop("translation_length")
        metric_result.pop("reference_length")
        bleu_results[prediction_label] = metric_result
    bleu_df = pd.DataFrame(bleu_results).T.reset_index().rename(columns={"index": "System"})
    results["bleu"] = bleu_df

    # # # BERT
    bert_results = {}
    print("Calculating BERT Score...")
    for prediction_label, predictions in prediction_dict.items():
        metric_result = calculate_metric_score('bertscore', references, predictions)
        metric_result["average_bertscore_precision"] = mean(metric_result["precision"])
        metric_result["average_bertscore_recall"] = mean(metric_result["recall"])
        metric_result["average_bertscore_f1"] = mean(metric_result["f1"])
        metric_result.pop("precision")
        metric_result.pop("recall")
        metric_result.pop("f1")
        metric_result.pop("hashcode")
        bert_results[prediction_label] = metric_result
    bert_df = pd.DataFrame(bert_results).T.reset_index().rename(columns={"index": "System"})
    results["bert_score"] = bert_df

    bleurt_results = {}
    print("Calculating BLEURT Score...")
    for prediction_label, predictions in prediction_dict.items():
        metric_result = calculate_metric_score('bleurt', references, predictions)
        metric_result["average_bleurt_score"] = mean(metric_result["scores"])
        metric_result.pop("scores")
        bleurt_results[prediction_label] = metric_result
    bleurt_df = pd.DataFrame(bleurt_results).T.reset_index().rename(columns={"index": "System"})
    results["bleurt_score"] = bleurt_df


    # METEOR
    meteor_results = {}
    print("Calculating METEOR Score...")
    for prediction_label, predictions in prediction_dict.items():
        metric_result = calculate_metric_score('meteor', references, predictions)
        meteor_results[prediction_label] = metric_result
    meteor_df = pd.DataFrame(meteor_results).T.reset_index().rename(columns={"index": "System"})
    results["meteor"] = meteor_df

    return results


def generate_human_eval_summary(references_dict, predictions, system_name):

    results = {}
    rouge_results = {}
    print("Calculating ROUGE Score...")
    for reference_label, references in references_dict.items():
        metric_result = calculate_metric_score('rouge', references, predictions)
        rouge_results[reference_label] = metric_result
    
    # Convert ROUGE scores to DataFrame
    rouge_df = pd.DataFrame(rouge_results).T.reset_index().rename(columns={"index": system_name})
    
    # Add ROUGE DataFrame to results
    results["rouge"] = rouge_df

    bleu_results = {}
    print("Calculating BLEU Score...")
    for reference_label, reference in references_dict.items():
        metric_result = calculate_metric_score('bleu', references, predictions)
        metric_result.pop("precisions")
        metric_result.pop("brevity_penalty")
        metric_result.pop("length_ratio")
        metric_result.pop("translation_length")
        metric_result.pop("reference_length")
        bleu_results[reference_label] = metric_result
    
    # Convert BLEU scores to DataFrame
    bleu_df = pd.DataFrame(bleu_results).T.reset_index().rename(columns={"index": system_name})
    
    # Add BLEU DataFrame to results
    results["bleu"] = bleu_df

    bert_results = {}
    print("Calculating BERT Score...")
    for reference_label, reference in references_dict.items():
        metric_result = calculate_metric_score('bertscore', references, predictions)
        metric_result["average_bertscore_precision"] = mean(metric_result["precision"])
        metric_result["average_bertscore_recall"] = mean(metric_result["recall"])
        metric_result["average_bertscore_f1"] = mean(metric_result["f1"])
        metric_result.pop("precision")
        metric_result.pop("recall")
        metric_result.pop("f1")
        metric_result.pop("hashcode")
        bert_results[reference_label] = metric_result
    
    # Convert BERTScore scores to DataFrame
    bert_df = pd.DataFrame(bert_results).T.reset_index().rename(columns={"index": system_name})
    
    # Add BERTScore DataFrame to results
    results["bert"] = bert_df

    meteor_results = {}
    print("Calculating METEOR Score...")
    for reference_label, reference in references_dict.items():
        metric_result = calculate_metric_score('meteor', references, predictions)
        meteor_results[reference_label] = metric_result
    
    # Convert METEOR scores to DataFrame
    meteor_df = pd.DataFrame(meteor_results).T.reset_index().rename(columns={"index": system_name})
    
    # Add METEOR DataFrame to results
    results["meteor"] = meteor_df

    return results