import json
import csv
from transformers import BertTokenizer
from simple_gnn.utils.build_mpnn_graph import build_mpnn_graph

# Initialize Bert tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Build graph dataset
input_csv_file = 'train_data_43590.csv'
output_jsonl_file = 'mpnn_dataset.jsonl'

# Build graph dataset
with open(input_csv_file, 'r') as file, open(output_jsonl_file, 'w') as outfile:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        _, _, message, label, _ = row

        # Skip empty messages
        if len(message) < 1:
            continue

        # Build graph
        x, edge_index, batch = build_mpnn_graph(message, tokenizer)

        # Skip empty graphs
        if len(edge_index) < 1:
            continue

        # Write graph to file
        graph_data = {
            'x': x,
            'edge_index': edge_index,
            'batch': batch,
            'y': [int(label == 'spam')],
        }
        json.dump(graph_data, outfile)
        outfile.write('\n')
